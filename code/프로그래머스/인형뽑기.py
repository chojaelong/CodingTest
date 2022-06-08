# https://programmers.co.kr/learn/courses/30/lessons/64061

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution():
    box = []
    pick = 0
    count = 0
    for i in moves:
        # 다 0일 경우
        if board[i-1].count(0) == len(board[i-1]):
            continue

        pick = pop(board[i-1])
        if len(box) == 0:
            box.append(pick)
        elif pick == box[len(box)-1]:
            box.pop()
            count += 1
        else:
            box.append(pick)
    
    print(count)
        
def pop(array):
    value = array.pop()
    array.insert(0, 0)
    if value == 0:
        pop(array)
    
    
    return value

solution()

