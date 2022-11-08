def solution(n, times):
    times.sort()
    start = 1
    end = max(times) * n
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        people = 0

        for time in times:
            people += mid // time

            if people >= n:
                break
        '''
        # 찾은 경우 중간점 인덱스 반환
        if people == n:
            return mid
        '''
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        if people >= n:
            answer = mid
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        elif people < n:
            start = mid + 1
    return answer

solution(6, [7, 10])