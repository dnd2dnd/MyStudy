# Annotation
## Annotation이란
Annotation은 클래스와 메소드에 추가하여 다양한 기능을 부여하는 역할을 합니다. Annotation을 활용하여 Spring Framework는 해당 클래스가 어떤 역할인지 정하기도 하고 Bean을 주입하기도 하며 자동으로 메소드를 생성해줍니다. 
Annotation을 사용할 경우 코드량이 감소하고 유지보수 하기 쉬우며 생산성이 증가합니다.

## 현재까지 사용한적 있는 Annotation

### @SpringBootTest
Spring Boot Test에 필요한 의존성을 제공해줍니다.

### @Controller
Spring에게 해당 Class가 Controller의 역할을 한다고 명시하기 위해 사용하는 Annotation

### @RequestMapping
@RequestMapping(value="")와 같은 형태로 작성하며 요청 들어온 URI의 요청과 Annotation value값이 일치하면 해당 클래스나 메소드가 실행됩니다.

### @NoArgsConstructor 
파라미터가 없는 기본 생성자를 생성해줍니다.

### @RequiredArgsConstructor
final이나 @NonNull인 필드 값만 파라미터로 받는 생성자를 만들어줍니다.

### @AllArgsConstructor
해당 클래스에 있는 모든 필드 값을 파라미터로 받는 생성자를 만들어줍니다.

### @ToString
해당 클래스의 toString() 메소드를 자동으로 만들어줍니다. exclude 속성을 사용하면 특정 필드를 toString() 결과에서 제외시킬 수 있습니다. 

### @Getter, @Setter
해당 클래스에 있는 필드 값들의 getter와 setter 메소드를 자동으로 생성해줍니다.

### @EqualsAndHashCode
equasl와 hashcode 메소드를 자동으로 생성해줍니다. callSuper 속성을 이용하여 부모 클래스의 필드까지 감안할지 안할지에 대해서 설정할 수 있습니다. true 일 경우 부모 클래스 필드 값들도 동일한지 체크합니다. 기본값은 false입니다.

### @Data
@Data는 @Getter, @Setter, @RequiredArgsConstructor, @ToString, @EqualsAndHashCode을 한꺼번에 설정해주는 Annotation 입니다.

### @RequestParam
URL에 전달되는 파라미터를 메소드의 인자와 매칭시켜 파라미터를 받아서 처리할 수 있는 Annotation입니다.

### @RequestBody
json이나 xml과 같은 형태의 값을 전송받아 처리할 수 있는 Annotation입니다.

### @ResponseBody
메소드에서 리턴되는 값이 View로 출력되지 않고 HTTP Response Body에 의하여 return 합니다.

### @Autowired
@Autowired 어노테이션은 각 타입에 맞는 컨테이너 안에 존재하는 Bean을 
주입해주는 것입니다.

### @GetMapping
RequestMapping(Method=RequestMethod.GET)과 같은 역할, GET HTTP Method

### @PostMapping
RequestMapping(Method=RequestMethod.POST)과 같은 역할, POST HTTP Method

### @DeleteMapping
RequestMapping(Method=RequestMethod.DELETE)과 같은 역할, DELETE HTTP Method

### @PatchMapping
RequestMapping(Method=RequestMethod.PATCH)과 같은 역할, PATCH HTTP Method

### @Service
Spring에게 해당 Class가 Service의 역할을 한다고 명시하기 위해 사용하는 Annotation

### @Repository
Spring에게 해당 Class가 Repository의 역할을 한다고 명시하기 위해 사용하는 Annotation


### 참조
https://melonicedlatte.com/2021/07/18/182600.html