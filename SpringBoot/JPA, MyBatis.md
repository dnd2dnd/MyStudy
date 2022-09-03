# JPA, MyBatis
JDBC를 사용했을 때는 sql문이 코드에 섞여 있고 요청하는 과정에서 sql문 생성시 String을 붙이고 자르는 등의 작업이 필요해서 sql문이 조금만 길어져도 번거럽고 관리가 힘들다.
코드와 sql문을 분리하여 관리하기 위한 라이브러리 

<br>
<br>

## JPA
Java ORM 기술에 대한 API 표준 명세. 
- ORM (Object-Relational Mapping)
    - Class와 RDB(Relactional DataBase)의 테이블을 매핑한다는 의미
    - 객체를 RDB 테이블에 자동으로 영속화 해주는 것

구현된 클래스와 매핑을 해주기 위해 사용되는 프레임워크

<br>

장점 
- CRUD 메소드를 기본적으로 제공한다.
- 쿼리를 만들지 않아도 된다.
- 1차캐싱, 쓰기지연, 변경감지, 지연로딩을 제공한다.
- MyBatis는 쿼리 수정 시 데이터 정보가 바뀌면 DTO와 함께 수정해야하지만 JPA는 객체만 수정

단점
- 복잡한 쿼리는 해결이 까다로움
- 제대로 사용하기 위해 시간이 걸린다.
- 다수의 테이블 조인시에 신경써야할 것 이 많다.
- 설계가 잘못될 경우 성능 저하 발생

<br>
<br>

## MyBatis
SQL 실행 결과를 자바 빈즈 or Map 객체에 매핑해주는 Persistence 솔루션으로 관리한다. SQL을 소스가 아닌 XML로 분리한다.

<br>

장점
- 접근이 쉽고 코드가 간결하고 배우기 쉽다.
- SQL문과 프로그래밍 코드가 분리되어 있어 SQL문 변경이 있을 때마다 자바 코드를 수정하거나 컴파일 하지 않아도 된다.
- 다양한 프로그래밍 언어로 구현이 가능하다

단점
- 스키마 변경시 SQL 쿼리를 직접 수정해주어야 한다.
- 반복된 쿼리가 발생하여 반복 작업이 있다.
- 객체와 쿼리문 모두 관리해야한다.
- 자주쓰는 CRUD 메소드를 직접 작성해야한다.

<br>
<br>
<br>

### 참조
https://incheol-jung.gitbook.io/docs/q-and-a/spring/jpa-vs-mybatis

https://sm-studymemo.tistory.com/95


