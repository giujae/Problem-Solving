L = int(input())
N = int(input())
cake = [0] * 1001
lst = []
mx2 = 0
idx2 = 0
for j in range(1, N + 1):
    P, K = map(int, input().split())
    if mx2 < (K - P):
        mx2 = K - P
        idx2 = j
    for i in range(P, K + 1):
        if cake[i] == 0:
            cake[i] = j
for j in range(1, N + 1):
    count = 0
    for i in range(len(cake)):
        if cake[i] == j:
            count += 1
    lst.append(count)
mx = 0
idx = 0
for i in range(len(lst)):
    if mx < lst[i]:
        mx = lst[i]
        idx = i + 1
print(idx2)
print(idx)