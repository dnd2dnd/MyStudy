# Given-When-Then
Given-When-Then 패턴은 Test Code 스타일을 표현하는 방식을 의미합니다.

<br>
<br>

## Given-When-Then

Given
- 테스트에서 구체화하고자 하는 행동을 시작하기 전에 테스트 상태를 설명
- 테스트를 위해 준비하는 과정
- 테스트에 사용하는 변수, 입력 값등을 정의

When
- 구체화하자 하는 행동
- 실제로 액션을 테스트하는 과정

Then
- 어떤 특정한 행동 때문에 발생할 것이라고 예상되는 변화에 대한 설명
- 테스트를 검증하는 과정, 예상한 값, 실제 실행을 통한 값을 증명하는 곳

<br>
<br>

## 예시

``` java
// given
String name = "김선웅";
int age = 26;
String location = "부산";
User user = new User(name, age, location);
userService.save(user);

// when
User findUser = userService.getFindUserName("김선웅");

// then
assertEqulas(name, findUser.getName());
```