array = [int(input()) for i in range(9)]

max_value = max(array)
index = array.index(max_value) + 1

print(max_value)
print(index)