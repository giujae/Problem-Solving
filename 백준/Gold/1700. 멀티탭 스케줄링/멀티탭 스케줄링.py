n, k = map(int, input().split())
appliance = list(map(int, input().split()))

multi_tab = []
count = 0

for i in range(k):
    if appliance[i] in multi_tab: # 멀티탭에 이미 꽂혀있는 경우
        continue
    elif len(multi_tab) < n: # 멀티탭에 빈 구멍이 있는 경우
        multi_tab.append(appliance[i])
    else: # 멀티탭이 모두 차있는 경우
        max_idx = -1
        max_val = -1
        for j in range(n):
            try:
                idx = appliance[i+1:].index(multi_tab[j])
                if idx > max_val:
                    max_val = idx
                    max_idx = j
            except ValueError:
                max_idx = j
                break
        multi_tab[max_idx] = appliance[i]
        count += 1

print(count)
