# Counter
문자열, 리스트 등의 배열 형태를 입력받아 각 문자가 문자열에서 몇 번씩 있는지 나타내주는 객체입니다.

```
from collections import Counter
```
Counter 클래스는 별도의 패키지 설치 없이 import하여 사용할 수 있습니다.

<br>
<br>

```
from collections import Counter
Counter('apple')

# 결과 Counter({'p': 2, 'a': 1, 'l': 1, 'e': 1})

Counter('바마가나다라바마')
# 결과 Counter({'바': 2, '마': 2, '가': 1, '나': 1, '다': 1, '라': 1})
```

Counter 클래스에 문자열을 입력하면 해당 문자열의 각 문자가 몇 개 나오는지 확인할 수 있습니다.

해당 출력을 보면 딕셔너리 형태로 출력됨으로 Counter의 자료형이 딕셔너리인 것과 value 값을 기준으로 내림차순 정렬된 다는 것을 알 수 있습니다.


<br>
<br>


## 유용한 메소드

|메소드|설명|
|------|---|
|elements()|무작위 순서로 값을 반환|
|most_common(n)|	n개의 key값 에서 가장 많은 순부터 적은 순으로 나열한 리스트 반환 <br> n이 생략될 경우 모든 요소를 반환|

<br>

```
# elements()
list((Counter('apple').elements()))
# 결과 ['a', 'p', 'p', 'l', 'e']

# mos_common()
Counter('apple').most_common()
# 결과 [('p', 2), ('a', 1), ('l', 1), ('e', 1)]
```

<br>

## 산술 연산자 활용
Counter은 산술 연산자를 사용할 수 있는데 아래와 같이  2개의 카운터 객체가 있을 때,

```
c1 = Counter(["Q", "W", "E", "R", "T"])
c2 = Counter(["Q", "W", "E", "R"])

c1 + c2
# 결과 Counter({'Q': 2, 'W': 2, 'E': 2, 'R': 2, 'T': 1})

c1 - c2
# 결과 Counter({'T': 1})
2개의  객체를 더하거나 뺄 수 있습니다.
```

<br>

이때 뺄셈의 결과로 0이나 음수가 나올 경우에는 최종 카운터 객체에서 제외가 됩니다.

```
c2 - c1
# 결과 Counter()
```

참조
collections — Container datatypes — Python 3.11.1 documentation

