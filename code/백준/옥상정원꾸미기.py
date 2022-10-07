# https://www.acmicpc.net/problem/6198

n = int(input())
array = [int(input()) for _ in range(n)]

stack = []
result = 0

for b in array:
  while stack and stack[-1]<=b:
    stack.pop()
  stack.append(b)

  result += len(stack)-1

print(result)