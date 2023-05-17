# Iterator
자바의 컬렉션(Collection)에 저장되어 있는 요소들을 순회하는 인터페이스

<br>

## Collection
Collection이란 자바에서 제공하는 자료구조들의 인터페이스로 List, ArrayList, Stack, Queue, LinkedList 등이 이를 상속

<br>

## 사용 이유
1. 순차적인 접근
- 컬렉션의 첫 번째 요소부터 마지막 요소까지 순차적으로 반복할 수 있다.
- 이는 컬렉션의 요소를 한 번에 모두 가져오는 것보다 메모리 사용을 줄일 수 있으며, 순차적인 접근이 필요한 상황에서 유용

2. 컬렉션의 요소 삭제
- 내부적으로 컬렉션의 상태를 관리하여 삭제 작업이 가능하다.
- For Loop를 이용하여 List 순회 중에 어떤 값을 삭제하면 Exception이 일어나 탐색을 하지 못하지만 Iterator를 사용하면 안전하게 삭제가 가능하다.

3. 다중 스레드 환경에서의 안정성
- 컬렉션의 상태를 추적하여 다른 스레드에서 요소를 변경하거나 삭제하는 것을 방지

4. 간단한 사용법
- 컬렉션 프레임워크에 대해 공통적으로 사용이 가능하며 사용법이 간단하다.

<br>

## 사용 방법
- hasNext() : 다음 요소가 있는지 판단
- next() : 다음 요소를 가져온다
- remove() : 가져온 요소를 삭제

``` java
List<String> list = new ArrayList<Integer>();
list.add("수박");
list.add("바나나");
list.add("오렌지");
Iterator<Integer> iter = list.iterator();
while(iterator.hasNext()) {
    String element = iterator.next();
    System.out.println(element);
}
```



