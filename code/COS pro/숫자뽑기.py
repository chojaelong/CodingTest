# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(arr, K):
    length = len(arr)
    dp = [10001 for _ in range(length)]
    arr.sort()
    count = 0
    for i in range(K - 1, length):
        temp = arr[count : count + K]
        value = temp[-1] - temp[0]
        dp[i] = min(value, dp[i - 1])
        count += 1
    
    return min(dp)

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [9, 11, 9, 6, 4, 19]
K = 4
ret = solution(arr, K)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [4, 8, 15, 17, 19]
K = 3
ret = solution(arr, K)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")