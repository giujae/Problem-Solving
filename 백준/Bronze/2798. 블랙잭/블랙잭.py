import itertools
n, m = map(int, input().split())
card = sorted(list(map(int, input().split())))

subsets = []

temp = itertools.permutations(card, 3)
subsets += temp
lst = []
for i in subsets:
    if sum(i) <= m:
        lst.append(sum(i))
print(max(lst))