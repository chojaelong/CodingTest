n, k = map(int, input().split())

s = list(map(int, input().split()))
s.insert(0, 0)
sections = []
for _ in range(k):
    sections.append(list(map(int, input().split())))

for i in sections:
    start = i[0]
    end = i[1]
    array = s[start : end + 1]

    avg = round(sum(array) / len(array), 2)
    print(f"{avg : .2f}")
