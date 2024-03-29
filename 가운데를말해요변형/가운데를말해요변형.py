import heapq

N = int(input())

max_heap = []
min_heap = []

sum = []

for _ in range(N):
	num = int(input())
	
	if len(max_heap) < 3:
		heapq.heappush(max_heap, (-num, num))
	else:
		heapq.heappush(min_heap, (num, num))
	if min_heap and max_heap[0][1] > min_heap[0][1]:
		max_num = heapq.heappop(max_heap)[1]
		min_num = heapq.heappop(min_heap)[1]
		heapq.heappush(max_heap, (-min_num, min_num))
		heapq.heappush(min_heap, (max_num, max_num))

	if len(max_heap) == 3:
		sum.append(max_heap[0][1])
print(sum)