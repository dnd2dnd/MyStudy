# Iterator
자바의 컬렉션(Collection)에 저장되어 있는 요소들을 순회하는 인터페이스

<br>

## Collection
Collection이란 자바에서 제공하는 자료구조들의 인터페이스로 List, ArrayList, Stack, Queue, LinkedList 등이 이를 상속

<br>

## 사용 이유
- 컬렉션 프레임워크에 대해 공통적으로 사용이 가능하고 사용법이 간단하다.
- 순차적인 접근
- 컬렉션의 요소 삭제
- 다중 스레드 환경에서의 안정성
- 향상된 for 루프

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



