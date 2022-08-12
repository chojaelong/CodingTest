import sys

def next_value(values):
    length = len(values)
    if length >= 11:
        return -1
    # for i in range(-1, -length, -1):
    #     if values[i] >= values[i - 1]:
    #         values[i] = 0
    #         # plus = 10 ** (-i - 1)
    #         values[i - 1] = values[i - 1] + 1
    #         if values[i - 1] == 10:
    #             values[i - 1] = 0
    #             values.insert(0, length)
    #             for j in range(1, length + 1):
    #                 values[j] = values[j - 1] - 1
    #             return int(''.join(map(str, values))) 
    #         return next_value(values)
    
    for i in range(length - 1):
        if values[i] <= values[i + 1]:
            values[i + 1] = 0
            # plus = 10 ** (-i - 1)
            values[i] = values[i] + 1
            if values[i] == 10:
                values[i] = 0
                values.insert(0, length)
                for j in range(1, length + 1):
                    values[j] = values[j - 1] - 1
                return int(''.join(map(str, values))) 
            return next_value(values)

    return int(''.join(map(str, values)))

sys.setrecursionlimit(2100000000)
n = int(input())
condition = False
array = [i for i in range(11)]
for i in range(11 , n + 1):
    value = array[i - 1] + 1
    if value > 9876543210:
        condition = True
        break
    values = list(map(int, str(value)))
    nv = next_value(values)
    array.append(nv)

print(array[n]) if condition == False else print(-1)
