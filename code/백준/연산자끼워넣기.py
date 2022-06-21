n = int(input())

nums = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split()) # +, -, *, /

maximum = -1e9
minimum = 1e9

def dfs(depth, num, plus, minus, multiply, divide):
    global nums, maximum, minimum

    if depth == n:
        maximum = max(num, maximum)
        minimum = min(num, minimum)
        return
    
    if plus > 0: # +
        dfs(depth + 1, num + nums[depth], plus - 1, minus, multiply, divide)
    if minus > 0: # -
        dfs(depth + 1, num - nums[depth], plus, minus - 1, multiply, divide)
    if multiply > 0: # *
        dfs(depth + 1, num * nums[depth], plus, minus, multiply - 1, divide)
    if divide > 0: # /
        dfs(depth + 1, int(num / nums[depth]), plus, minus, multiply, divide - 1)

dfs(1, nums[0], plus, minus, multiply, divide)

print(maximum)
print(minimum)