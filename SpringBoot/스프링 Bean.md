# Spring Boot Bean

## Bean이란
Bean은 Spring IoC(Inversion of Control) 컨테이너에서 관리되는 객체입니다.

스프링 IoC는 객체의 생성, 관리, 의존성 주입 등을 담당하는 기능을 제공합니다. 해당 컨테이너를 통해 개발자는 객체의 생성 및 관리에 대한 부분을 신경 쓰지 않고 비즈니스 로직에 집중 할 수 있습니다.

자바 어플리케이션은 어플리케이션 동작을 제공하는 객체들로 이루어져 있습니다.

이때, 객체들은 독립적으로 동작하는 것보다 서로 상호작용하여 동작하는 경우가 많고 이렇게 상호작용하는 객체를 '객체의 의존성'이라고 표현합니다.

스프링에서는 스프링 컨테이너에 객체들을 생성하면 객체끼리 의존성을 주입하는 역할을 해주고 이때 등록된 객체들은 'Bean'이라고 합니다.

<br>

## Bean을 등록하는 방법
1. 컴포넌트 스캔과 자동 의존관계 설정

클래스 선언부 위에 @Component 어노테이션을 사용하는 것입니다.
@Controller, @Serivce, @Repository 모두 @Component를 포함하고 있으며 해당 어노테이션으로 등록된 클래스들은 스프링 컨테이너에 의해 자동으로 생성되어 스프링 빈으로 등록됩니다.

```
@Controller
public class UserController {

}
```

2. 직접 스프링 빈 등록
설정 클래스를 만들고 @Configuration 어노테이션 클래스를 선언부 위에 추가하면 됩니다.

그리고 특정 타입을 리턴하는 메소드를 만들고, @Bean 어노테이션ㅇ르 붙여주면 자동으로 해당 타입의 빈 객체가 생성됩니다.

```
@Configuration
public class MyConfig {
    @Bean
    public MyBean myBean() {
        return enw MyBean();
    }
}
```

### 직접 스프링 Bean을 사용하는 이유
일반적으로는 @Component를 사용해 자동으로 빈을 등록하는 방법을 이용한다.

하지만 Configuration 안에 직접 @Bean 어노테이션을 사용하여 수동으로 등록하는 경우가 있다. 왜 그럴까?

1. 개발자가 직접 제어 불가능한 라이브러리 사용
2. 애플리케이션 전범위적으로 사용되는 클래스 등록
3. 다형성을 활용하여 여러 구현체를 등록해야할 때


<br>
<br>

## 참조
- https://dev-coco.tistory.com/69
- https://velog.io/@beanzinu/Spring-Configuration-%EC%95%88%EC%97%90-Bean%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94-%EC%9D%B4%EC%9C%A0
