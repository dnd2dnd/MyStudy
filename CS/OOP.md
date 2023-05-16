## OOP란
OOP (Object Oriented Programming)이란 소프트웨어 개발 중 하나로, 현실 세계의 사물이나 개념을 프로그래밍에 반영하는 방법론

OOP는 프로그램을 독립적인 단위인 객체들의 집합으로 구성하고, 이 객체들 간에 메시지를 주고 받으면서 상호작용하도록 합니다.

<br>

## 객체란 
객체란 프로그램 동작의 주체가 되는 요소를 의미한다.

모든 객체는 상태와 행위를 가진다. 
- 상태: 객체가 가지는 데이터
- 행위: 객체가 수행할 수 있는 동작이나 기능

객체는 클래스를 기반으로 생성되며, 클래스는 객체들이 가지는 공통적인 특성과 동작을 정의한 것으로, 객체를 생성하기 위한 설계도 역할을 합니다.

``` java
public class Computer {
    private final boolean power = false;

    private String model;
    private int memorySize;
    

    public Computer(String model, int memorySize) {
        this.model = model;
        this.memorySize =memorySize;
    }

    public String getModel() { return model; }
    public int getMemorySize() { return memorySize; }
    public void powerOn() { power = true; }
    public void powerOff() { power = false;}

}
```

위의 Computer 클래스는 컴퓨터를 객체로 구현한 클래스이다.

상태
- power : 전원
- model : 컴퓨터 모델명
- memorySize : 메모리 크기

행위
- getModel : 모델명 확인
- getMemorySize : 메모리 확인
- powerOn : 전원 켜기
- powerOff : 전원 종료

클래스에서 상태는 멤버 변수, 행위는 메소드라고 할 수 있다.

Java에서 해당 개체를 사용하기 위해서는 메모리에 할당해야하고, 할당된 객체를 인스턴스라고 한다.

<br>

## 4가지 특성
1. 추상화
- 객체들이 가지는 공통된 특성이나 동작을 추출하여 모델화하는 과정입니다. 추상화를 통해 프로그램의 복잡성을 낮추고 필요한 부분에 집중할 수 있습니다.
- 관련이 없는 필요한 부분만을 표현, 객체들의 공통된 특징을 파악해 정의

2. 캡슐화
- 객체의 상태를 외부에서 직접 접근하지 못하도록 정보를 은닉하고 필요한 경우에만 객체의 메서드를 통해 상태를 변경하거나 접근할 수 있도록 한다.
- 이를 통해 코드의 재사용성과 유지보수성을 높일 수 있습니다.

3. 상속
- 이미 존재하는 클래스의 특성과 동작을 다른 클래스가 상속받아 확장하고 재사용할 수 있습니다. 
- 이를 통해 클래스 간의 계층 구조를 형성할 수 있으며, 공통적인 특성을 상위 클래스에서 정의하고 하위 클래스에서 특수한 특성을 추가합니다.
- 코드의 중복을 효과적으로 줄일 수 있다.

4. 다형성
- 같은 이름의 메소드나 연산자가 다른 객체에서 따라 다르게 동작하는 것, 즉 형태가 같은데 다른 기능을 하는 것을 의미합니다. 
- 상속을 받은 속성에 대해 자식 클래스에서 속성을 재정의 할 수 있습니다. 이를 오버라이딩이라 합니다.

<br>
<br>

OOP의 4가지 특성들을 간단하게 표현한 예제 코드입니다.

``` java
public class Animal {
    private String name;
    private String sound;

    public Animal(String name, String sound) {
        this.name = name;
        this.sound = sound;
    }

    public void speak() {
        System.out.println(name + " " + sound);
    }

    public String getName() {
        return "나의 " + name;
    }
}

public class Dog extends Animal {
    public Dog(String name, String sound) {
        super(name, sound)
    }
}

public class Duck extends Animal {
    public Duck(String name, String sound) {
        super(name, sound);
    }
}
public class Main {}
    public static void main(String[] args) {
        Dog myDog = new Dog("톰", "멍멍");
        myDog.speak();              // 개 멍멍
        System.out.println(myDog.getName());

        Duck myDuck = new Duck("도날드", "꽥꽥");
        myDuck.speak();             // 오리 꽥꽥
        System.out.println(myDuck.getName());
    }
}
```


<br>

## 결론
OOP는 객체지향 프로그래밍이며, 코드의 재사용성과 중복 제거가 큰 목적이다.