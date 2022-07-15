# Dependency Injection
## Dependency Injection(의존성 주입) 이란
DI는 필요한 객체를 직접 생성하는 것이 아니라 외부로부터 필요한 객체를 주입하여 사용하는 것이다.

```java
interface MemberRepository {...}
public class JdbcMemberRepository implements MemberRepository {...}
public class MyBatisMemberRepository implements MemberRepository {...}

public class MemberService {
    
    private MemberRepository memberRepository;
    
    public MemberService() {
        this.memberRepository = new JdbcMemberRepository(); // 1
        this.memberRepository = new MyBatisMemberRepository(); // 2
    }
}
```
<br>

의존성 주입을 한다면 위와 같은 코드를 아래와 같은 코드로 만들 수 있다.

```java
interface MemberRepository {...}
public class JdbcMemberRepository implements MemberRepository {...}
public class MyBatisMemberRepository implements MemberRepository {...}

public class MemberService {
    
    private MemberRepository memberRepository;
    
    // 의존성 주입
    public MemberService(MemberRepository memberRepository) {
        this.memberRepository = memberRepository
    }
}
``` 
필요한 클래스를 직접 생성하지 않고 의존성 주입을 하여 객체간의 결합도를 낮추면서 유연한 코드를 작성할 수 있다.

<br>

## 의존성 주입 방법
의존성 주입 방법은 필드 주입, setter 주입, 생성자 주입이 있다. 나는 Spring boot를 배웠을 때 의존성 주입을 Autowired를 사용한 필드 주입으로 배웠었다.
하지만 Spring boot에서는 의존성 주입을 필드 주입이 아닌 생성자 주입을 권장하는 사실을 알게 되었다.

### @Autowired
@Autowired 어노테이션은 각 타입에 맞는 컨테이너 안에 존재하는 Bean을 
주입해주는 것이다.

<br>

### 필드 주입
```java
public class ExampleClass {

    @Autowired
    private ExampleService exampleService;

    @Autowired
    private BoardService boardService;
}
```
필드 주입은 사용하고자하는 필드 앞에 @Autowire 어노테이션을 명시한다.
주입되는 변수는 private로 선언되기 때문에 이후 외부에서 접근이 불가능하다.

<br>

### setter 주입
```java
public class ExampleClass {

    private ExampleService exampleService;

    @Autowired
    public void setExampleService(ExampleService exampleService) {
        this.exampleService = exampleService;
    }
}
```
setter 함수에 @Autowire 어노테이션을 명시한다. setter함수는 public 접근 권한자로 생성되어야 한다.
public으로 노출되어 있어 외부에서 setter 함수를 사용하여 접근이 가능하다.

<br>

### 생성자 주입
```java
public class ExampleClass {
    
    private final ExampleService exampleService;

    @Autowired
    public ExampleClass(ExampleService exampleSerivce) {
        this.exampleService = exampleService;
    }
}
```
생성자에서 앞에 @Autowired 어노테이션을 명시한다. 처음 스프링 컨테이너에 올라가는 시점 때 주입된다.
setter를 사용한 의존성 주입은 세팅 후 개발자가 접근할 수 있지만 생성자를 사용하여 의존성 주입 시 세팅 후 주입한 것을 변경하는게 불가능하다.
의존 관계가 프로그램 실행 중에 동적으로 변경되는 경우는 아예 없기 때문에 생성자 주입이 권장된다.

<br>

위와 같은 코드를 @RequiredArgsConstructor를 사용하여 변경할 수 있다.
```java
@RequiredArgsConstructor 
public class ExampleClass {
    private final ExampleService exampleService;
}
```
@RequiredArgsConstructor 어노테이션을 사용하면 final이 붙거나 @NotNull이 붙은 필드의 생성자를 자동으로 생성해주는 Lombok 어노테이션이다.

<br>

### 참조
https://mimah.tistory.com/entry/Spring-%EC%9D%98%EC%A1%B4%EC%84%B1-%EC%A3%BC%EC%9E%85-Dependency-Injection-DI-%EC%98%88%EC%A0%9C

