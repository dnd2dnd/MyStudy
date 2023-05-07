# Spring 단위 테스트
Spring 기반의 웹 애플리케이션에서 단위 테스트하는 방법에 대해 알아보겠습니다.

## Mockito?
Mockito : 개발자가 동작을 직접 제어할 수 있는 가짜 객체를 지원하는 테스트 프레임워크

일반적으로 Spring으로 웹 애플리케이션을 개발하면, 여러 객체들 간의 의존성이 생겨 단위 세트르 작성을 어렵게 하는데 이를 해결하기 위해 가짜 객체를 주입시켜주는 Mockito 라이브러리를 활용할 수 있다.

### Mockito 사용법
1. Mock 객체 의존성 주입
- @Mock : 가짜 객체를 만들어 반환해주는 어노테이션
- @Spy : Stub하지 않는 메소드들은 원본 메소드 그대로 사용하는 어노테이션
- @IngectMocks : @Mock, @Spy로 생성된 가짜 객체를 자동으로 주입시켜주는 어노테이션

Ex) UserController에 대한 단위 테스트를 작성할 때, UserService를 사용하고 있다면 @Mock 어노테이션을 통해 가짜 UserService를 만들고, @IngectMocks를 통해 UserControlle에 주입시킬 수 있다.

<br>

2. Stub 결과 처리
의존성이 있는 객체는 가짜 객체를 주입하여 어떤 결과를 반환하라고 정해진 답변을 준비시켜야 한다.
- doReturn(): 가짜 객체가 특정한 값을 반환해야 하는 경우
- doNothing(): 가짜 객체가 아무 것도 반환하지 않는 경우(void)
- doThrow(): 가짜 객체가 예외를 발생시키는 경우

<br>

3. Mockito와 Junit의 결합
Mockito도 테스팅 프레임워크이기 때문에 JUnit과 결합되기 위해서는 별도의 작업이 필요하다. 기존의 JUnit4에서 Mockito를 활용하기 위해서는 클래스 어노테이션으로 @RunWith(MockitoJUnitRunner.class)를 붙여주어야 연동이 가능했다. 

하지만 SpringBoot 2.2.0부터 공식적으로 JUnit5를 지원함에 따라, 이제부터는 @ExtendWith(MockitoExtension.class)를 사용해야 결합이 가능하다.

<br>

## Controller 단위 테스트 작성 예시

게시판 작성, 게시판 조회 API에 대한 단위 테스트입니다.

``` Java
@Restcontroller
@RequiredArgsConstructor
public class BoardController {
    
    private final BoardService boardService;

    @PostMapping("/board/create")
    public ResponseEntity<BoardResponse> create(@RequestBody BoardRequest boardRequest) {
        return ResponseEntity.status(HttpStatus.CREATED)
                .body(boardService.create(boardRequest));
    }

    @GetMapping("/board")
    public ResponseEntity<List<BoardResponse>> findAll() {
        return ResponseEntity.ok(boardService.findAll());
    }    
}
```
<br>
<br>

### 단위 테스트 준비
단위 테스트를 위해서 의존성을 주입해주어야 합니다.

``` java
@ExtendWith(MockitoExtension.class) // JUnit, Mockito를 연동
class BoardControllerTest {

    @InjectMocks    // 가짜 객체 주입
    private BoardController boardController;

    @Mock           // 가짜 객체 생성
    private BoardService boardService;

    private MockMvc mockMvc;    // HTTP 호출을 하기 위한 객체 

    @BeforeEach
    public void init() {
        mockMvc = MockMvcBuilders.standaloneSetup(boardController).build();
    }
}
```

<br>
<br>

### 게시판 생성 테스트
게시판 생성 요청을 보내기 위해서 BoardRequest 객체 1개와 boardSerivce의 create에 대한 stub가 필요합니다. 따라서 given 단계에서 아래와 같은 코드가 작성됩니다.

``` java
@DisplayName("게시판 생성 성공")
@Test
void createBoard() throws Exception {
    // given
    BoardRequest request = boardReqeust();
    BoardResponse response = boardResponse();

    doReturn(response).when(boardService)
        .create(any(BoardRequest.class));
}

private BoardRequest boardRequest() {
    return BoardRequest.builder()
            .title("제목")
            .contents("내용")
            .build();
}

private BoardResponse boardResponse() {
    return BoardRequest.builder()
            .title("제목")
            .contents("내용")
            .build();    
}

```

<br>

HTTP 요청을 보내면 Spring은 내부에서 MessageConverter를 사용하여 Json String을 객체로 변환한다. 이것은 Spring boot 내부에서 진행되므로, 우리가 API로 전달되는 파라미터를 조작할 수 없다. 그래서 BoardRequest 타입이라면 어떠한 객체도 처리할 수 있도록 any()가 사용되었다. any()를 사용할 때에는 특정 클래스의 타입을 지정하는 것이 좋다.

when 단계에서는 mockMvc에 데이터와 함께 POST 요청을 보내야 한다. 요청 정보는 mockMvc의 perform에서 작성할 수 있고, 요청 정보에는 MockMvcRequestBuilders가 사용되며 요청 메소드 종류, 내용, 파라미터 등을 설정할 수 있다.

보내는 데이터는 객체가 아닌 문자열이라 별도의 변환이 필요하기 때문에 Gson을 사용하여 변환하였다.

``` java
@DisplayName("게시판 생성 성공")
@Test
void createBoard() throws Exception {
    // given
    BoardRequest request = boardReqeust();
    BoardResponse response = boardResponse();

    doReturn(response).when(boardService)
        .create(any(BoardRequest.class));

    // when
    ResultActions resultActions = mockMvc.perform(
        MockMvcRequestBuilders.post("/board/create")
                    .contentType(MediaType.APPLICATION_JSON)
                    .content(new Gson().toJson(request))
    );

}
```

<br>

마지막으로 then 단계에서 게시판 생성 API 호출 결과로 200 Response와 응답 결과를 검증한다. 응답 검증 시 jsonPath를 이용해 해당 json 값이 존재하는지 확인한다.

``` java
@DisplayName("게시판 생성")
@Test
void createBoard() throws Exception {
    // given
    BoardRequest request = boardReqeust();
    BoardResponse response = boardResponse();

    doReturn(response).when(boardService)
        .create(any(BoardRequest.class));

    // when
    ResultActions resultActions = mockMvc.perform(
        MockMvcRequestBuilders.post("/board/create")
                    .contentType(MediaType.APPLICATION_JSON)
                    .content(new Gson().toJson(request))
    );

    // then
    MvcResult mvcResult = resultActions.andExpect(status().isOk())
        .andExpect(jsonPath("title", response.getTitle()).exist())
        .andExpect(jsonPath("contents", response.getContents()).exist())
}
```

### 게시판 조회 테스트
given
- BoardService의 findAll에 대한 Stub

when
- GET HTTP Method, URL : "/board"

then
- HTTP Stuats : OK

<br>

``` java
@DisplayName("게시판 목록 조회")
@Test
void getBoardList() throws Exception {
    // given
    doReturn(boardList()).when(boardService)
        .findAll();

    // when
    ResultActions resultActions = mockMvc.perform(
        MockMvcRequestBuilders.get("/board")
    );

    // then
    MvcResult mvcResult = resultActions.andExpect(status().isOk()).andReturn();
    
    BoardListResponseDTO response = new Gson().fromJson(mvcResult.getResponse().getContentAsString(), BoardListResponseDTO.class);
    assertThat(response.getBoardList().size()).isEqualTo(5);
}

private List<BoardResponse> boardList() {
    List<BoardResponse> boardList = new ArrayList<>();
    for (int i = 0; i < 5; i++) {
        boardList.add(new BoardResponse("제목", "내용"));
    }
    return boardList;
}
```

### @WebMvcTest
MockMvc를 생성하는 단위 테스트는 매우 번거롭다. Spring Boot에서는 Controller Test를 위한 @WebMVcTest 어노테이션을 제공하고 있다. 

이를 이용하면 MockMvc 객체가 자동으로 생성될 뿐만 아니라 ControllerAdvice나 Filter, Interceptor 등 웹 계층 테스트에 필요한 요소들을 모두 bean으로 등롷개 스프링 컨텍스트 환경을 구성해준다. 

@WebMvcTest는 Spring Boot가 제공하는 테스트 관경이므로 @Mock -> @MockBean, @Spy -> @SpyBean을 사용해주어야 한다.

``` java
@WebMvcTest(BoardController.class)
class boardControllerTest {

    @MockBean
    private BoardService boardService;

    @Autowired
    private MockMvc mockMvc;
}
```

Spring은 내부적으로 스프링 컨텍스트를 캐싱해두고 동일한 테스트 환경이라면 재사용을 한다. 그런데 특정 컨트롤러만 bean으로 만들고 @MockBean과 @SpyBean으로 bean을 Mocking 하는 @WebMvcTest는 캐싱 효과를 거의 얻지 못하고 새로운 컨텍스트의 생성을 필요로 하게 된다. 그러므로 빠른 테스트를 원한다면 직접 MockMvc를 생성하는 것이 좋다.

<br>

## Service 단위 테스트 작성 예시
게시판 생성과 조회를 위해서 다음과 같은 Service가 필요하다.

``` java
@Service
@RequiredArgsConstructor
@Transactional(readOnly = true)
public class BoadrService {
    private final BoardReposiotry boardReposiotry;
    
    public BoardResponse create(BoardRequest rq) {
        Board board = Board.builder()
                .title(rq.getTitle())
                .contents(rq.getContents())
                .build();
        return BoardResponse.of(boardRepository.save(board));
    }

    public List<Board> findAll() {
        return boardRepository.findAll().stream()
                .amp(BoardResponse::of)
                .collect(Collectors.toList());
    }
}

```

<br>

### 단위 테스트 준비
``` java
@ExtendWith(MockitoExtension.class)
class BoardServiceTest {

    @InjectMocks
    private BoardService boardService;

    @Mock
    private BoardRepository boardRepository;

}
```

<br>

### 게시판 생성 테스트
``` java
@DisplayName("게시판 생성")
@Test
void createTest() {
    // given
    SignUpRequest request = signUpRequest();

    doReturn(new Board(request.getTitle(), request.getContents())).when(boardRepository).save(any(Board.class));
        
    // when
    BoardResponse response = obardService.create(request);

    // then
    assertThat(response.getTitle()).isEqualTo(request.getEmail());

    // verify
    verify(boardRepository, times(1)).save(any(Board.class));
}
```

verify는 Mockkito 라이브러리를 통해 만들어진 가짜 객체의 특정 메소드가 호출된 횟수를 검증할 수 있다.

<br>

### 게시판 목록 조회 테스트
``` java
@DisplayName("게시판 목록 조회")
@Test
void findAll() {
    // given
    doReturn(boardList()).when(boardRepository).findAll();

    // when
    final List<BoardResponse> boardList = boardService.findAll();

    // then
    assertThat(boardList.size()).isEqualTo(5);
}

private List<Board> boardList() {
    List<Board> boardList = new ArrayList<>();
    for (int i = 0; i < 5; i++) {
        boardList.add(new Board("제목", "내용"));
    }
    return boardList;
}
```

<br>

## Repository 단위 테스트 작성 예시
게시판 생성과 목록 조회를 위한 JPA Repository입니다.
``` java
public interface BoardRepository extends JpaRepository <Board, Long> {

}
```

### @DataJpaTest
Spring Boot는 JPA Repository를 손쉽게 테스트 할 수 있는 @DataJpaTest 어노테이션을 제공하고 있습니다. 해당 어노테이션을 사용하면 기본적으로 인메모리 데이터베이스인 H2를 기반으로 테스트용 데이터베이스를 구축하며, 테스트가 끝나면 트랜잭션을 롤백 해줍니다.
Repository는 실제 DB와 통신없이 단순 Mocking 하는 것은 의미가 없으므로 직접 데이터베이스와 통신하는 @DataJpaTest를 사용한다.

<br>

### 게시판 생성 테스트
``` java
@DataJpaTest
class BoardRepositoryTest {
    
    @Autowired
    private BoardRepository boardRepository;

    @DisplayName("게시판 생성")
    @Test
    void creatTest {
        // given
        Board board = Board();

        // when
        Board saveBoard = boardRepository.save(board);

        // then
        assertThat(saveBoard.getTitle()).isEqualTo(board.getTitle());
        assertThat(saveBoard.getContents()).isEqualTo(board.getContents());
    }

    private Board board() {
        return Board.build()
                    .title("제목").contents("내용").build();
    }
}
```

<br>

### 게시판 목록 조회 테스트
``` java
@DataJpaTest
class BoardRepositoryTest {

    @Autowired
    private BoardRepository boardRepository;

    @DisplayName("게시판 목록 조회")
    @Test
    void findAllTest() {
        // given
        boardRepository.save(board());
        
        // when
        List<Board> boardList = boardRepository.findAll();

        // then        
        assertThat(boardList.size()).isEqualTo(1);
    }
}
```

<br>

### 결론
Spring 기반 애플리케이션 코드에 대해 계층 별로 단위 테스트 작성 방법을 알아보았습니다. 테스트를 작성할 때 성공 테스트만 작성하는 것이 아니라 실패 테스트까지 작성해주어야 합니다.

해당 내용들은 하단에 있는 링크에 대한 내용들을 대부분 가져오거나 재구성한 내용입니다.


<br>
<br>

## 참조
- https://mangkyu.tistory.com/145