from itertools import combinations_with_replacement
import time

max_value = 0
common = []

def list_multiply(list):
    value = 1
    
    for v in list:
        value *= v
    
    return value

# 규칙
def rule(n):
    global max_value
    
    if n <= 4:
        max_value = n
        return
    temp = n
    count = 0
    while temp not in (0, 1, 2):
        temp -= 3
        count += 1
    
    if temp == 0:
        max_value = 3 ** count
        return 
    elif temp == 1:
        max_value = (3 ** (count -1)) * 4
        return 
    elif temp == 2:
        max_value = (3 ** count) * 2
        return 

# stack
def decompose(n):
    global max_value
    global common
    
    s = [n]
    while True:
        multiply = list_multiply(s)
        # max_value = max(max_value, multiply)
        if max_value < multiply:
            max_value = multiply
            common = s[:]
        temp = s.pop()
        
        if temp != 1:
            s.append(temp - 1)
            s.append(1)
        else:
            sum = 2
            while len(s) != 0 and s[-1] == 1:
                s.pop()
                sum += 1
            
            if len(s) == 0:
                break
            pivot = s.pop() - 1
            s.append(pivot)
            
            while sum > pivot:
                s.append(pivot)
                sum -= pivot
            s.append(sum)
        

# 백 트래킹
def back_tracking(n, array):
    global max_value

    if sum(array) == n:
        multiply = list_multiply(array)
        max_value = max(max_value, multiply)
        return
    
    for i in range(2, n):
        array.append(i)
        if sum(array) > n:
            array.pop()
            break
        back_tracking(n, array)
        array.pop()
        
# 조합
def combination(n):
    global max_value
    
    nums = [i for i in range(2, n+1)]
    result = [seq for i in range(len(nums), 0, -1) for seq in combinations_with_replacement(nums, i) if sum(seq) == n]
    for set in result:
        multiply = list_multiply(set)
        max_value = max(max_value, multiply)

def solutuion(n):
    array = []
    start_time = time.time()
    #back_tracking(n, array)
    #combination(n)
    #decompose(n)
    rule(n)
    end_time = time.time()
    print("time:", end_time - start_time)
    print(max_value)
    #print(common)
    return max_value

solutuion(60)