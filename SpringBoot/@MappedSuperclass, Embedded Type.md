# @MappedSuperclass, @Embedded

JPA에서 특정 Column을 별도의 영역에 정의하는 2가지 방법들이다.

@Embedded는 하나의 Type을 정의하여 객체에 포함하는 방법

@MappedSuperclass는 추상 클래스를 만들어 변수를 정의하고 상속시키는 방법이다.

<br>

## 어떤 것을 선택해야 할까??

@Embedded는 위임(조합)이고 @MappedSuperClass는 상속이다.

결론부터 이야기하자면 객체지향의 일반적인 법칙에 따르면 상속보다는 위임이 더 좋기 때문에 위임을 사용하는 것이 좋다.

Java는 다중상속이 안되고 객체지향 설계상 유연성이 떨어진다. 하지만 @MappedSuperclass를 사용하는 경우가 있다.

대부분의 Entity들이 공통으로 사용하는 속성을 다룰때는 해당 어노테이션을 사용하는 것이 좋다. 
- Ex) 등록시간, 수정시간, 등록자, 수정자

<br>
<br>

@MapperSuperclass를 사용하는 방법은 다음과 같다.


``` java
@Getter @Setter
@MappedSuperclass
public abstract class BaseEntity {
    private String writer;
    private String modifier;
    private LocalDateTime createdDate;
    private LocalDateTime modifiedDate;    
}

@Entity
public class User extends BaseEntity {
    @Id
	@Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column
    private Long userSn;
    
    @Column
    private String userId;    

    @Column
    private String password;
}
```
<br>

상속 사용시 sql문
```
select u from User u where u.createdDate > ?
```



<br>
<br>

## 그렇다면 @Embedded는 언제??
@Embedded는 새로운 값 타입을 직접 정의할 수 있고 속성을 하나의 값으로 만들었기 때문에 재사용성을 높일 수 있을 때 사용한다.

@Embedded를 사용하는 방법은 다음과 같다.

```java
@Embeddable 
public class Address {
    private String city;
    private String street;
    private STring code;
}

@Entity
public class User extends BaseEntity {
    @Id
	@Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column
    private Long userSn;
    
    @Column
    private String userId;    

    @Column
    private String password;

    @Embedded
    private Address address;
}
```
- @Embeddable : 임베디드 타입을 정의하는 클래스에 표시
- @Embedded : 정의한 임베디드 타입을 사용하는 곳에 표시

위임 사용시 sql문
```
select u from User u where u.Address.city = ?
```

<br>
<br>

## 결론
column을 정의하는 2가지 방법이 있으며 개발하는 프로젝트의 db 설계 상황에 맞춰 적절한 것을 사용하자.


<br>
<br>

## 참조
- https://www.inflearn.com/questions/18578/%EC%9E%84%EB%B2%A0%EB%94%94%EB%93%9C-%ED%83%80%EC%9E%85%EA%B3%BC-mappedsuperclass-%EC%B0%A8%EC%9D%B4