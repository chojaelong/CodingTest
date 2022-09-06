# 다음과 같이 import를 사용할 수 있습니다.
import math

def solution(garden):
    length = len(garden)
    count = 0
    
    while True:
        stop = True
        for i in range(length):
            if not all(garden[i]):
                stop = False
                break
        if stop:
            return count
        
        c_garden = garden[:]
        for i in range(length):
            for j in range(length):
                if garden[i][j] == 1:
                    if i + 1 <= length - 1:
                        c_garden[i + 1][j] = 1
                    if j + 1 <= length - 1:
                        c_garden[i][j + 1] = 1
                    if i - 1 >= 0:
                        c_garden[i - 1][j] = 1
                    if j - 1 >= 0:
                        c_garden[i][j - 1] = 1
        
        count += 1
        garden = c_garden
        

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(garden1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

garden2 = [[1, 1], [1, 1]]
ret2 = solution(garden2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")