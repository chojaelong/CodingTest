from collections import Counter

# 2차원 리스트(그래프 표현)을 만들고, 무한으로 초기화
graph = [[10] * (5) for _ in range(5)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, 5):
	for b in range(1, 5):
		if a == b:
			graph[a][b] = 0

for grap in graph:
    print(grap)