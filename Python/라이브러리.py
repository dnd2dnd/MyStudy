from itertools import permutations, combinations, product, combinations_with_replacement

data = ["A", "B", "C"]

print(list(permutations(data, 3)))
print(list(combinations(data, 3)))
print(list(product(data, repeat=3)))
print(list(combinations_with_replacement(data, 3)))

from collections import Counter

counter = Counter(data)
print(counter)