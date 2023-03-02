import itertools
n, m = map(int, input().split())
card = sorted(list(map(int, input().split())))

subsets = list(itertools.combinations(card, 3))

lst = []
for i in subsets:
    if sum(i) <= m:
        lst.append(sum(i))
print(max(lst))