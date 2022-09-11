# 래퍼 클래스

## 정의
기본 자료타입을 객체로 다루기 위해서 사용하는 클래스들을 래퍼 클래스라고 한다.

|기본 타입|래퍼 클래스|
|:---:|:---:|
|byte|Byte|
|char|Character|
|int|Integer|
|float|Float|
|double|Double|
|boolean|Boolean|
|long|Long|
|short|Short|

<br>

## 박싱, 언박싱
기본 타입의 값을 포장 객체로 만드는 과정을 박싱
포장 객체에서 기본타입의 갑승ㄹ 얻어내는 과정을 언박싱

``` java
public class Wrapper_Ex {
    public static void main(String[] args) {
        Integer num = new Integer(25); //박싱
        int n= num.intValue();         //언박싱
    }
}
```

<br>

``` java
public class Wrapper_Ex {
    public static void main(String[] args) {
        Integer num = 17; // 자동 박싱
        int n = num;      //자동 언박싱
    }
}
```

<br>

- 래퍼 클래스는 값이 null일 때 에러가 발생한다.
- 래퍼 객체끼리 값을 비교하기 위해서는 == 연산자를 사용할 수 없다
    - 객체의 주소를 비교하기 때문에, equals를 사용해야 한다.
- 래퍼 클래스와 기본 자료형과의 비교는 ==, equlas 둘 다 가능하다
    - 컴파일러가 자동으로 오토박싱, 언박싱을 해주기 때문이다.


<br>
<br>

## 참조
https://coding-factory.tistory.com/547