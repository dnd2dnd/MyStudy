# Annotation
## Annotation이란
Annotation은 클래스와 메소드에 추가하여 다양한 기능을 부여하는 역할을 합니다. Annotation을 활용하여 Spring Framework는 해당 클래스가 어떤 역할인지 정하기도 하고 Bean을 주입하기도 하며 자동으로 메소드를 생성해줍니다. 
Annotation을 사용할 경우 코드량이 감소하고 유지보수 하기 쉬우며 생산성이 증가합니다.

<br>

## 현재까지 사용한적 있는 Annotation

### @SpringBootTest
- Spring Boot Test에 필요한 의존성을 제공해줍니다.

### @Controller
- Spring에게 해당 Class가 Controller의 역할을 한다고 명시하기 위해 사용하는 Annotation

### @RequestMapping
 - @RequestMapping(value="")와 같은 형태로 작성하며 요청 들어온 URI의 요청과 Annotation value값이 일치하면 해당 클래스나 메소드가 실행됩니다.

### @NoArgsConstructor 
- 파라미터가 없는 기본 생성자를 생성해줍니다.

### @RequiredArgsConstructor
- final이나 @NonNull인 필드 값만 파라미터로 받는 생성자를 만들어줍니다.

### @AllArgsConstructor
- 해당 클래스에 있는 모든 필드 값을 파라미터로 받는 생성자를 만들어줍니다.

### @ToString
- 해당 클래스의 toString() 메소드를 자동으로 만들어줍니다. exclude 속성을 사용하면 특정 필드를 toString() 결과에서 제외시킬 수 있습니다. 

### @Getter, @Setter
- 해당 클래스에 있는 필드 값들의 getter와 setter 메소드를 자동으로 생성해줍니다.

### @EqualsAndHashCode
- equasl와 hashcode 메소드를 자동으로 생성해줍니다. callSuper 속성을 이용하여 부모 클래스의 필드까지 감안할지 안할지에 대해서 설정할 수 있습니다. true 일 경우 부모 클래스 필드 값들도 동일한지 체크합니다. 기본값은 false입니다.

### @Data
- @Data는 @Getter, @Setter, @RequiredArgsConstructor, @ToString, @EqualsAndHashCode을 한꺼번에 설정해주는 Annotation 입니다.

### @Builder
- 해당 Annotation을 선언하면 빌더 패턴을 생성해준다.

### @RequestParam
- URL에 전달되는 파라미터를 메소드의 인자와 매칭시켜 파라미터를 받아서 처리할 수 있는 Annotation입니다.

```java
// http://localhost:8080/board?page=1
@GetMapping("/board")
public String getBoard(@RequestParam("page") int pageNum){
    ```
}
```

### @PathVariable
- HTTP 요청에 매칭되는 request parameter 값이 자동으로 들어간다.

``` java
// http://localhost:8080/board/123
@DeleteMapping("/board/{id}")
public void deleteBoard(@PathVariable("id") int boardNum){
    ```
}
```

### @RequestBody
- json이나 xml과 같은 형태의 값을 전송받아 처리할 수 있는 Annotation입니다.

### @ResponseBody
- 메소드에서 리턴되는 값이 View로 출력되지 않고 HTTP Response Body에 의하여 return 합니다.

### @Autowired
- @Autowired 어노테이션은 각 타입에 맞는 컨테이너 안에 존재하는 Bean을 
주입해주는 것입니다.

### @GetMapping
- RequestMapping(Method=RequestMethod.GET)과 같은 역할, GET HTTP Method

### @PostMapping
- RequestMapping(Method=RequestMethod.POST)과 같은 역할, POST HTTP Method

### @DeleteMapping
- RequestMapping(Method=RequestMethod.DELETE)과 같은 역할, DELETE HTTP Method

### @PatchMapping
- RequestMapping(Method=RequestMethod.PATCH)과 같은 역할, PATCH HTTP Method

### MappedSuperclass
- JPA Entity 클래스들이 해당 추상 클래스를 상속할 경우 createDate, modifiedDate를 컬럼으로 인식해주는 Annotation

### @CreatedDate
- Entity가 생성되는 시간을 자동으로 저장해주는 Annotation

### @LastModifiedDate
- 조회한 Entitiy의 값을 변경할 때 시간이 자동으로 저장해주는 Annotation

### @EntityListeners(AuditingEntityListener.class)
- 해당 클래스에 Auditing 기능을 포함해주는 Annotation
Auditing 기능은 자동으로 시간을 매핑하여 데이터베이스의 테이블에 넣어주는 것

### Transactional
- 메소드 내에서 예외가 발생하면 해당 메소드에서 이루어진 작업들을 초기화 시켜주는 Annotaion이다. 
- 주로 DB 데이터를 등록, 수정, 삭제 하는 메소드에서 사용된다.

### @Table
- Enttiy 클래스의 매핑할 테이블 정보를 알려준다

### @Entity
- 실제 DB의 테이블과 매칭될 클래스임을 명시하고 생성해준다.

### @Id
- 해당 테이블의 PK 필드를 나타낸다.

### @GeneratedValue 
- PK의 생성 규칙을 나타낸다. 
- Auto_increment를 사용할 경우 자동으로 증가하는 정수형이 된다.

### @Column
- 테이블의 컬럼을 나타나면 굳이 선언하지 않아도 해당 클래스의 필드는 모두 컬럼이 되지만 기본값 외에 추가로 변경이 필요한 옵션이 있을 경우 사용한다. (타입, 사이즈)

### @Service
- Spring에게 해당 Class가 Service의 역할을 한다고 명시하기 위해 사용하는 Annotation

### @Repository
- Spring에게 해당 Class가 Repository의 역할을 한다고 명시하기 위해 사용하는 Annotation

<br>
<br>
<br>

### 참조
https://melonicedlatte.com/2021/07/18/182600.html
https://gmlwjd9405.github.io/2018/12/02/spring-annotation-types.html