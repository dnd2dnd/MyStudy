# CrudRepository, JpaRepository
Spring Data 프로젝트가 공통적으로 사용하는 인터페이스

## CrudRepository
기본적인 CRUD 기능을 제공하는 인터페이스
```java
@Repository
public interface UserRepository extends CrudRepository<User, Long> {
    // ...
}
```

## JpaRepository
CrudRepositry가 제공하는 모든 기능을 제공하고 추가적으로 페이징, 정렬, JPA에 특화된 메소드를 제공한다.
```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    // ...
}
```

<br>
<br>

### 참조
https://blog.naver.com/writer0713/221587319282

https://bibi6666667.tistory.com/283
