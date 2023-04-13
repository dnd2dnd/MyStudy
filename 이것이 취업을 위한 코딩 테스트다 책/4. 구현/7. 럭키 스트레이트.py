n = list(input())
le = len(n)//2

ln, rn = n[:len(n)//2], n[len(n)//2:]
suml, sumr = 0, 0

for l in ln:
    suml+=int(l)
for r in rn:
    sumr+=int(r)

if suml==sumr:
    print("LUCKY")
else:
    print("READY")

