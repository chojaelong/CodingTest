def solution(a, b, n):
    answer = 0
    # t : 받는 콜라의 횟수
    # r : 이번 횟수에 받은 콜라
    # l : 제출하고 남은 콜라
    while n >= a:
        t = n // a
        l = n % a
        r = b * t
        answer += r
        n = r + l
        
    return answer