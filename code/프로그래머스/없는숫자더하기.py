def solution(numbers):
    array = [i for i in range(10)]
    for i in numbers:
        if array.count(i) != 0:
            array.remove(i)
    
    return(sum(array))