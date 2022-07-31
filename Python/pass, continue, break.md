# pass, continue, break
1. pass : 실행할 코드가 없는 것으로 다음 행동을 진행
2. continue : 바로 다음 순번의 loop 진행
3. break : 반복문을 멈추고 loop 밖으로 나감

<br>

## 예시
### pass

```py
for i in range(10):
    if i % 2 == 0:
        pass
        print(i, end=' ')
    else :
        print(i, end=' ')
```

```
0 1 2 3 4 5 6 7 8 9
```
전부 출력된다.

<br>
<br>

### continue

```py
for i in range(10):
    if i % 2 == 0:
        continue
        print(i, end=' ') # 이 코드는 사용되지 않는다.
    else:
        print(i, end=' ')
```
```
1 3 5 7 9
```
짝수일 경우 그 값이 출력되지않고 넘어간다.

<br>
<br>

### break
```py
for i in range(10):
    if i % 2 == 0:
        break
        print(i, end=' ') # 이 코드는 사용되지 않는다.
    else:
        print(i, end=' ')
```
```

```
i가 0일때 break하게 되어 아무것도 출력되지 않고 끝난다.

<br>
<br>
<br>

pass와 continue의 개념을 정확하게 알고 있는 것 같지 않아 정리해보았다.
