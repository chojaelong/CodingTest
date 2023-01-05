def solution(storey):
    a , n = 0, 0
    while storey != 0 :
        storey += n
        m = storey % 10
        if (m > 5) or (m == 5 and int(storey / 10) % 10 >= 5):
            a += 10 - m
            n = 1
        else:
            a += m
            n = 0
        storey = int(storey / 10)
    
    return a + n
    
solution(646)