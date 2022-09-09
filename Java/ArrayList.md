# ArrayList

## List 
- 리스트는 배열의 한계로 만들어진 자료형
- 배열의 경우 크기가 정해져 있다.
- List를 사용하면 동적으로 자료형의 개수를 늘릴 수 있다.

<br>

## ArrayList
- ArrayList는 List 인터페이스를 상속 받는 클래스 중 하나
- 내부적으로 저장 가능한 용량이 있으며 그 이상을 저장하려고 할 때 새로운 메모리를 할당

<br>
생성 방법

```java
import java.util.ArrayList

ArrayList<String> member = new ArrayList<>();
```

<br>

주요 메소드

|메소드|설명|
|:---:|:---:|
|boolean add(E element)|ArrayList의 맨 뒤에 element 추가|
|void add(int index, E elemnet)|index 위치에 element 삽입|
|boolean addAll(Collection<? extends E> c|컬렉션 c의 모든 요소를 ArrayList의 맨 뒤에 추가|
|void clear()|ArrayList의 모든 요소 삭제|
|boolean contains(Object o)|ArrayList가 지정된 객체를 포함하고 있으면 true 리턴|
|E elementAt(int index)|index의 요소 리턴|
|E get(int index)|index의 요소 리턴|
|in indexOf(Object o)|o와 같은 첫번째 요소의 인덱스 리턴, 없을 시 -1 리턴|
|boolean isEmpty()|ArrayList가 비어있으면 true 리턴|
|E remove(int index)|index의 요소 삭제|
|boolean remove(Object o)|o와 같은 첫 번째 요소를 ArrayList에서 삭제|
|int size()|ArrayList가 포함하는 요소의 개수 리턴|
|Object[] toArray()|ArrayList의 모든 요소를 포함하는 배열 리턴|
