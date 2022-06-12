array = []

for i in range(7):
    n = int(input())
    if n % 2 == 1:
        array.append(n)

if not array:
    print(-1)
else:
    print(sum(array))
    print(min(array))

