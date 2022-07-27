# 좋은 수열 / 나쁜 수열 확인 함수
def isGoodArr(arr):
    arr_len = len(arr)				# 수열 길이
    for part_len in range(1, arr_len // 2 + 1):	# 비교할 부분수열의 길이
        # 부분수열 비교 시작
        for part_start in range(part_len, arr_len - part_len + 1):
            # 같은 부분수열 발견하면
            if arr[part_start - part_len:part_start] == arr[part_start:part_start + part_len]:
                return False			# False 리턴
    else:					# 모든 부분수열이 다르면
        return True	

def back_tacking(cnt):
    if not isGoodArr(stack):
        return -1

    if cnt == n:
        print(*stack, sep='')
        return 0
        
    for i in range(3):
        stack.append(array[i])
        if back_tacking(cnt + 1) == 0:
            return 0
        stack.pop()


n = int(input())
array = [1, 2, 3]
stack = []
back_tacking(0)