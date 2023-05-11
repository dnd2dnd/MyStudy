# @CreatedDate에 값이 저장이 안될 경우
JPA를 사용하여 @CreatedDate로 정의한 column이 포함된 entity를 저장하였는데 값이 null로 나왔다.

<br>

## 원인

대부분 auditing이 적용되지 않아 발생한 문제이다.

만약 Embedded로 설정한 객체에 @CreatedDate로 정의한 것이 있으면 안된다. 해당 어노테이션은 Entity 클래스가 있는 곳에 위치해야한다.

<br>

## 해결방안

우선 Application.java 파일에 @EnableJpaAuditing을 추가한다.

@CreatedDate, @LastModifiedDate 있는 클래스에 @EntityListeners(AuditingEntityListener.class)를 추가한다.



``` java
@EnableJpaAuditing
@SpringBootApplication
public class WebApplication {
    public static void main(String[] args) {
        SpringApplication.run(WebApplication.class, args)
    };
}

@Getter @Setter
@MappedSuperclass
@EntityListeners(AuditingEntityListener.class) // 추가
public abstract class BaseTime {
    @CreatedDate
    private LocalDateTime createdDate;
    @LastModifiedDate
    private LocalDateTime modifiedDate;    
}

@Getter @Setter
@Builder
@Entitiy
@NoArgsConstructor
@AllArgsConstructor
public class User extends BaseTime {
    private String name;
}
```