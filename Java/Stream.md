# Stream

## Stream 이란
스트림은 자바8부터 추가된 컬렉션의 저장 요소를 하나씩 참조해서 람다식으로 처리할 수 있도록 해주는 반복자입니다. Iterator와 비슷한 역할을 하지만 람다식으로 요소 처리 코드를 제공하여 코드가 좀 더 간결하게 할 수 있다는 점과 내부 반복자를 사용하므로 병렬처리가 쉽다는 점에서 차이점이 있습니다. 

배열 또는 컬렉션 인스턴스에서 함수 여러 개를 조합해서 원하는 결과를 필터링하고 가공된 결과를 얻을 수 있습니다. 또한 람다를 이용해서 코드의 양을 줄이고 간결하게 표현할 수 있습니다.

간단하게 병렬처리(multi-threading)가 가능하다는 점입니다. 하나의 작업을 둘 이상의 작업으로 잘게 나눠서 동시에 진행하는 것을 병렬 처리(parallel processing)라고 합니다. 즉 쓰레드를 이용해 많은 요소들을 빠르게 처리할 수 있습니다.

## Stream 생성하기
### 배열에서의 스트림 활용
`Arrays.stream` 메소드를 사용하여 배열 생성
```java
String[] arr = {"k", "s", "w"};
Stream<String> stream = Arrays.stream(arr);
Stream<String> streamPart = Arrays.stream(arr, 1, 3); // 1~2 요소 ["s", "w"]
```

### 컬렉션 스트림
디폴트 메소드 `stream` 을 이용해서 생성
```java
List<String> list = Arrays.asList("k", "s", "w");
Stream<String> stream = list.stream();

```

### Stream.builder()
`build` 메소드를 사용하여 스트림에 원하는 값을 넣을 수 있습니다.
```java
Stream<String> buildStream = Stream.<String>builder()
                                .add("kim").add("sun").add("woong")
                                .build(); // [kim, sun, woong]
```

### Stream.generate()
`generate` 메소드를 이용하여 `Supplier<T>` 에 해당하는 람다로 값을 넣을 수 있습니다. 
이때 생성되는 스트림은 크기가 정해져 있지 않고 무한하기 때문에 특정 사이즈로 최대 크기를 제한해야한다.
* `Supplier<T>` 는 인자는 없고 리턴값만 있는 함수형 인터페이스이다. 따라서 람다에서 리턴하는 값이 들어간다.


```java
Stream<String> generatdeStream = Stream.generate(() -> "k").limit(5); // [k,k,k,k,k] 생성
```

### Stream.iterate()
`iterate` 메소드와 초기값과 해당 값을 다루는 람다를 이용하여 스트림을 생성할 수 있습니다. 
이때 생성되는 스트림은 사이즈가 무한하기 때문에 특정 사이즈로 제한해야한다.
```java
Stream<Integer> iteratedStream = Stream.iterate(10, n -> n+2).limit(5); // [10, 12, 14, 16, 18]
```

### 기본 타입형 스트림
int, long, double과 같은 기본 타입 스트림을 생성할 수 있습니다.
`range`와 `rangeClose`의 차이는 마지막 종료지점이 포함되냐 안되냐 차이다.
```java
IntStream intStream = IntStream.range(1, 5); // [1,2,3,4]
LongSteram longStream = LongStream.rangeClosed(1, 5); //[1,2,3,4,5]
```

난수 생성 가능
```java
DoubleStream doubleStream = new Random().doubles(3); // 난수 3개 생성
```

### 문자열 스트림
<br>
문자를 숫자로 변환

```java
IntStream charStream = "Stream".chars(); // [83, 116, 114, 101, 97, 109]
```

정규표현식을 이용해서 문자열을 분리하고 스트림으로 생성
```java
Stream<String> stringStream = Pattern.compile(", ").splitAsStream("Kim, Sun, Woong"); // [Kim, Sun, Woong]
```

### 파일 스트림
<br>
`Files` 클래스의 `lines` 메소드는 해당 파일의 각 라인을 스트링 타입의 스트림으로 만들어준다.

```java
Stream<String> lineStream = Files.lines(Paths.get("file.txt"), Charset.forName("UTF-8));
```

## 가공하기

전체 요소 중에서 원하는 것만 뽑아낼 수 있고 스트림을 리턴하기 때문에 여러 작업을 이어 붙일 수 있다.

### Filtering
<br>
필터는 스트림 내 요소들을 걸러내는 작업입니다.

```java
Stream<T> filter(Predicate<? super ?> predicate);

Stream<String> stream = arrs.stream().filter(arr -> arr.contains("a"));
```
스트림의 각 요소에 대해서 "a"를 확인하고 "a"가 포함된 단어들이 있는 스트림이 리턴됩니다.

### Mapping
<br>

맵은 스트림 내 요소들을 하나씩 특정 값으로 변환합니다. 변환하기 위한 인자는 람다로 받습니다.
맵핑은 스트림에 들어가 있는 값이 입력되어 특정 로직을 거친 후 출력이 되어 새로운 스트림에 담기는 행위입니다.

```java
<R> Stream<R> map(Function<? super T, ? extends R> mapper);

// 대문자로 변환된 값들이 담긴 스트림을 리턴
Stream<String> stream = arrs.stream()
                            .map(String::toUpperCase);


// 각 상품을 상품의 수량의 값들이 담긴 스트림을 리턴
Stream<Integer> stream = productList.stream()
                            .map(Product::getAmount);                            
```

### flatMap
<br>

`map` 에서 더 복잡한 `flatMap` 메소드 입니다.

```java
<R> Stream<R> flatMap(Function<? super T, ? extends Stream<? extends R>> mapper);
```
인자로 mapper를 받고 있는데, 리턴 타입이 Stream 입니다. 즉, 새로운 스트림을 생성해서 리턴하는 람다를 넘겨야합니다. flatMap 은 중첩 구조를 한 단계 제거하고 단일 컬렉션으로 만들어주는 역할을 합니다. 이러한 작업을 플래트닝(flattening)이라고 합니다.

```java
List<List<String>> list = Arrays.asList(Arrays.asList("a"),
                                        Arrays.asList("b")); // [[a], [b]]
                            

List<String> flatList = list.stream()
                            .flatMap(Collection::stream)
                            .collect(Collection.toList()); // [a, b]

students.stream()
  .flatMapToInt(student -> 
                IntStream.of(student.getKor(), 
                             student.getEng(), 
                             student.getMath()))
  .average().ifPresent(avg -> 
                       System.out.println(Math.round(avg * 10)/10.0));
// 학생 객체를 가진 스트림에서 학생의 국영수 점수를 가져와 새로운 스트림을 만들고 평균을 구하는 코드                       
```
                       
### Sorting
`Comparator` 을 이용하여 정렬하고 오름차순으로 정렬합니다
```java
Stream<T> sorted();
Stream<T> sorted(Comparator<? super T> comparator);

Stream<String> stream = list.stream()
                            .sorted()
                            .distinct() // 중복 제거

IntStream.of(14, 11, 20, 39, 23)
        .sorted()   // Compartor.reverseOrder()을 넣을 경우 역순 정렬
        .boxed()
        .collect(Collectores.toList()); // [11, 14, 20, 23, 39]
```

`Compartor` 의 `compare` 메소드는 두 인자를 비교해서 리턴한다.
문자열 길이를 기준으로 정렬한 예제
```java
int compare(T o1, T o2)

lang.stream()
  .sorted(Comparator.comparingInt(String::length))
  .collect(Collectors.toList());
// [Go, Java, Scala, Swift, Groovy, Python]

lang.stream()
  .sorted((s1, s2) -> s2.length() - s1.length())
  .collect(Collectors.toList());
// [Groovy, Python, Scala, Swift, Java, Go]
```

### Iterating
<br>
`peek`는 Stream에 영향을 주지 않고 특정 연산을 수행한다.
결과 확인용으로 사용한다.

```java
Stream<T> peek(Consumer<? super T> action);

int sum = IntStream.of(1, 3, 5, 7, 9)
                    .peek(System.out::println)
                    .sum();
```                    

## 결과 만들기
### Calculating
<br>
최소, 최대, 합, 평균 등 다양한 기본형 타입으로 결과를 만들 수 있습니다.

```java
long count = IntStream.of(1, 3, 5, 7, 8)
                    .count()
                    .sum()
                    .min()
                    .max()
                    .average()
```

스트림이 비어 있을 경우 count와 sum은 0을 출력하지만 min, max, average는 표현할 수 없기 때문에 Optional을 이용하여 리턴합니다.
```java
IntStream.of(1, 3, 5, 7, 9)
        .average()
        .ifPresent(System.out::println);
```

### Collecting
<br>
Collector 타입의 인자를 받아서 List, Set, Map 결과로 수집할 경우 사용합니다.

```java
List<Product> productList = Arrays.asList(new Product(23, "potatoes"),
                                        new Product(23, "bread"),
                                        new Product(13, "sugar"));
```

#### Collectors.toList()
<br>
스트림에서 작업한 결과를 리스트로 반환합니다.

```java
List<String> collectorCollection = productList.stream()
                                            .map(Product::getName)
                                            .collect(Collectors.toList());
```

#### Collectors.joining()
<br>
스트림에서 작업한 결과를 하나의 스트링으로 이어 붙일 수 있습니다.
3개의 인자를 받을 수 있습니다. 
- delimiter : 각 요소 중간에 들어가 요소를 구분시켜주는 구분자
- prefix : 결과 맨 앞에 붙는 문자
- suffix : 결과 맨 뒤에 붙는 문자

```java
String listToString = productList.stream()
                                .map(Product::getName)
                                .collect(Collectors.joining(", ", "<", ">"));
// <potatoes, orange, lemon, bread, sugar>
```

```java
// 숫자 값의 평균을 냅니다
Double averageAmount = productList.stream()
                                .collect(Collectors.averagingInt(Product::getAmount));

// 숫자 값의 합을 냅니다.
Integer summingAmount = productList.stream()
                                .collect(Collectors.summingInt(Product::getAmount));

Integer summingAmount = productList.stream()
                                .mapToInt(Product::getAmount)
                                .sum();

// IntSummaryStatistics {count=5, sum=86, min=13, average=17.200000, max=23} 여러 가지 정보가 담긴 객체를 반환합니다.
IntSummaryStatistics statistics = productList.stream()
                    .collect(Collectors.summarizingInt(Product::getAmount));


// 특정 조건으로 요소들을 그룹핑할 수 있습니다.
Map<Integer, List<Product>> collectorMapOfLists = productList.stream()
                        .collect(Collectors.groupingBy(Product::getAmount));
```
### Matching
<br>
Stream의 값들 중에서 조건을 만족하는 요소가 있는지 확인하고 체크한 결과를 리턴한다.
- anyMatch : 하나라도 조건을 만족하는 요소가 있는가
- allMatch : 모두 조건을 만족하는가
- noneMatch : 모두 조건을 만족하지 않는가

```java
boolean anyMatch(Predicate<? super T> predicate);
boolean allMatch(Predicate<? super T> predicate);
boolean noneMatch(Predicate<? super T> predicate);

boolean anyMatch = names.stream()
                        .anyMatch(name -> name.contains("a"));
boolean allMatch = names.stream()
                        .allMatch(name -> name.length() > 3);
boolean noneMatch = names.stream()
                        .noneMatch(name -> name.endsWith("s"));
```  

### Iterating
<br>

`forEach` 요소를 돌면서 실행하는 최종 작업입니다. 
결과를 출력할때 주로 사용합니다.

```java
names.stream().forEach(System.out::println);
```

### 참조
https://futurecreator.github.io/2018/08/26/java-8-streams/
