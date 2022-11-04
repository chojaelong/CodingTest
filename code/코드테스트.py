from collections import Counter

nums = ['50', '*', '6', '-', '3', '*', 2]
idx = nums.index('*')
value = eval(nums[idx - 1] + nums[idx] + nums[idx + 1])
del nums[idx + 1], nums[idx], nums[idx - 1]
nums.insert(idx - 1, str(value))
print(nums)