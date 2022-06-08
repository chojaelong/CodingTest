numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = 'left'

left = [1, 4, 7]
right = [3, 6, 9]
mid = [2, 5, 8, 0]

nowright = [3, 2]
nowleft = [3, 0]
answer = []

def click(hand, index):
    global nowright, nowleft
    if hand == 'right':
        answer.append('R')
        nowright = index
    elif hand == 'left':
        answer.append('L')
        nowleft = index

for i in numbers:
    if i in right:
        click('right', [right.index(i), 2])
    elif i in left:
        click('left', [left.index(i), 0])
    elif i in mid:
        clickIndex = [mid.index(i), 1]
        rightDistance = abs(clickIndex[0] - nowright[0]) + abs(clickIndex[1] - nowright[1])
        leftDistance = abs(clickIndex[0] - nowleft[0]) + abs(clickIndex[1] - nowleft[1])

        if rightDistance > leftDistance:
            click('left', clickIndex)
        elif rightDistance < leftDistance:
            click('right', clickIndex)
        elif rightDistance == leftDistance:
            click(hand, clickIndex)

print(''.join(answer))