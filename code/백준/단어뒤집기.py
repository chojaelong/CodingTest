n = int(input())

for _ in range(n):
    array = input().split()

    for i in range(len(array)):
        array[i] = array[i][::-1]
    
    print(' '.join(array))