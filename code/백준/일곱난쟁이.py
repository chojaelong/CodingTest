import itertools

array = [int(input()) for _ in range(9)]
array.sort()

combination = list(itertools.combinations(array, 7))

for data in combination:
    if sum(data) == 100:
        for value in data:
            print(value)
        break