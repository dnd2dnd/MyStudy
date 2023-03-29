place = input()
alp = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}
x = int(alp[place[0]])
y = int(place[1])

moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
count = 0
for move in moves:
    if ((x + move[0] < 1 ) or (y + move[1] < 1 ) or (x + move[0] > 8) or (y + move[1] > 8)):
        continue
    count += 1
print(count)

## 답안
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]))-int(ord('a'))+1

steps = moves

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >=1 and next_row <= 8 and next_column >=1 and next_column <= 8:
        result += 1

print(result)