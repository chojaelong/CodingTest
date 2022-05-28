
x, y = input()
count = 0
x = ord(x) - 96
y = int(y)

print(x, y)
# 위위오, 위오오, 오오밑, 오밑밑, 밑밑왼, 밑왼왼, 왼왼위, 위위왼
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]

    print(nx, ny)

    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)