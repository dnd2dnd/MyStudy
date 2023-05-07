# Java 단위 테스트
Java 기반 단위 테스트입니다.

## 라이브러리
JUnit5 : 자바 단위 테스트를 위한 테스팅 프레임워크
AssertJ : 자바 테스트를 돕기 위해 다양한 문법을 지원하는 라이브러리

JUnit만으로도 단위 테스트를 충분히 작성할 수 있지만 JUnit에서 제공하는 assertEquals()와 같은 메소드는 AssertJ가 주는 메소드에 비해 가독성이 떨어지기 때문에 JUnit5와 AssertJ 2가지 라이브러리를 조합하여 단위 테스트를 진행한다.

<br>
<br>

## Given-When-Then
Given-When-Then 패턴은 Test Code 스타일을 표현하는 방식을 의미합니다.

Given(준비)
- 테스트에서 구체화하고자 하는 행동을 시작하기 전에 테스트 상태를 설명
- 테스트를 위해 준비하는 과정
- 테스트에 사용하는 변수, 입력 값등을 정의

When(실행)
- 구체화하자 하는 행동
- 실제로 액션을 테스트하는 과정

Then(검증)
- 어떤 특정한 행동 때문에 발생할 것이라고 예상되는 변화에 대한 설명
- 테스트를 검증하는 과정, 예상한 값, 실제 실행을 통한 값을 증명하는 곳


추가적으로 어떤 메소드가 몇번 호출되었는지 검사하기 위한 verify 단계도 있다.

<br>
<br>

## 테스트 코드 작성 예시

```java
@DisplayName("테스트 이름")
@Test
void 메소드명() {
    // given

    // when

    // then
}
```
- @Test : 해당 메소드가 단위 테스트임을 명시하는 어노테이션
- @DisplayName : 해당 어노테이션을 사용하여 테스트에 대한 다른 이름을 부여할 수 있다.


## 단위 테스트 작성 예시
```java
public class MyCalculator {
    public int add(int a, int b) {
        return a + b;
    }

    public int sub(int a, int b) {
        return a - b;
    }
}
```
+, -를 하는 메소드에 대한 간단한 테스트 코드 작성

``` java
public class MyCalculatorTest {

    @Test
    public void testAdd() {
        // given
        int a = 5;
        int b = 10;
        MyCalculator cal = new MyCalculator();

        // when
        int result = cal.add(a, b);

        // then
        assertEquals(15, result);
    }

    @Test
    public void testSubtract() {
        // given
        int a = 10;
        int b = 5;
        MyCalculator cal = new MyCalculator();

        // when
        int result = cal.subtract(a, b);

        // then
        assertEquals(5, result);
    }
}
```

간단한 자바 애플리케이션이라서 어떤 메소드가 다른 객체와 메세지를 주고 받을 필요가 없어 단위 테스트가 간단하다.



<br>
<br>

## 참조
- https://mangkyu.tistory.com/144