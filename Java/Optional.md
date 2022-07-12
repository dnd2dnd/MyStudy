# Optional

## 1. java Option이란
- java Optional 클래스는 Java 8에서 추가되었으며 자바의 고질적인 문제인 NullPointerException 문제를 해결할 수 있는 방법을 제공한다.
- NullPointerException(NPE)은 아무것도 없는 Null 상태인 값을 참조하려고 할 때 발생한다.
- if문을 사용하여 Null 여부를 검사할 경우 Null 검사를 해야하는 변수가 많을 경우 코드가 복잡하고 번거로워진다.

<br>
<br>

## 2. Optional 활용
### of, ofNullable로 객체 감싸기

- Optional에서 제공하는 of와 ofNullable 메소드를 사용하여 객체를 감쌀 수 있다.
- of는  null 값을 받지 않는 것이고 ofNullable은 null 값을 허용한다는 것이다.

<br>

### Optional.of() - 값이 Null이 아닌 경우

```java
// 만약 Optional.of()로 Null을 저장하면 NullPointerException이 발생한다.
Optional<String> optional = Optional.of("value");
```
<br>

### Optional.ofNullable() - 값이 Null일 수도, 아닐 수도 있는 경우

```java
// Optional의 값은 값이 있을 수도 있고 Null일 수도 있다.
Optional<String> optional = Optional.ofNullable("value");
String value = optional.orElse("Null"); // 값이 없다면 "Null"을 리턴

return optional.orElseThrow(IllegalArgumentException::new);

return optional.orElseThrow(() -> new IllegalArgumentException("No Data");

// 비어있는 객체 return
return optional.orElseGet(Sample::new);
```

<br>

### 예제 코드

- if문을 사용하여 Null 값을 검사 할 경우

```java
public String findValue(){
	UserVO userVO = getUser();
    if (userVO != null) {
        Name name = user.getName();
        if (name != null) {
            String lastName = name.getLastName();
            if (lastName != null) {
                return lastName ;
            }
        }
    }
    return "이름 없음";
}
```

- Optional 사용할 경우

```java
public String findValue(){
	Optional<UserVo> userVo = Optional.ofNullable(getUser());
  Optional<Name> name = userVO.map(UserVO::getName);
  Optional<String> lastName = name .map(Name ::getLastName);
  String result = lastName .orElse("이름 없음");

  // 그리고 위의 코드를 다음과 같이 축약해서 쓸 수 있다.
  String result = user.map(UserVO::getName)
        .map(Address::getLastName)
        .orElse("이름 없음");
}
```