array = list(input())
answer = [-1] * 26

for i in range(len(array)):
    ascii = ord(array[i]) - 97
    if answer[ascii] == -1:
        answer[ascii] = i

for i in answer:
    print(i, end=' ')