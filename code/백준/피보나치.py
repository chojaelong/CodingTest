array = [10e9] * 100
def fibonacci(n):
    if n == 0:
        return [1, 0]
    elif n == 1:
        return [0, 1]
    
    if array[n] != 10e9:
        return array[n]
    array[n] = [fibonacci(n-1)[0] + fibonacci(n-2)[0], fibonacci(n-1)[1] + fibonacci(n-2)[1]]
    return array[n]
        

t = int(input())

for _ in range(t):
    n = int(input())
    print(fibonacci(n)[0], end=' ')
    print(fibonacci(n)[1])
    
