# import sys
# a = sys.stdin.read()
# print(a)

while True:
    try:
        print(input())
    except EOFError:
        break