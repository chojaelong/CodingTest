from itertools import chain, combinations
# https://www.acmicpc.net/problem/1062
# a = 97 ~ z = 122
# anta, tica : a, c, n, i, t

# a ~ z
word = set(chr(value + 97) for value in range(26))

# 입력 받기
n, k = map(int, input().split())
array = [list(input()) for _ in range(n)]

# 기본 단어를 읽기 위하여 알아야 하는 글자
knew = set(['a', 'c', 'n', 'i', 't'])

if k < 5:
    print(0)
else:
    # 가르킬 수 있는 수
    can_teach_count = k - 5
    can_teach_array = list(combinations(word - knew, can_teach_count))

    # 각 상황 별 알고있는 단어의 수
    for i in range(len(can_teach_array)):
        can_teach_array[i] = can_teach_array[i] + tuple(knew)

    # 배열 당 읽을 수 있는 단어 수
    can_read_array = [0] * len(can_teach_array)

    # 읽을 수 있는지 판단
    for i in range(len(can_teach_array)):
        for values in array:
            condition = True
            for value in values:
                if value not in can_teach_array[i]:
                    condition = False
                    break
            if condition:
                can_read_array[i] += 1
                    
                    
    print(max(can_read_array))