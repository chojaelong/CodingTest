s = list(input())
print(s)

alpha = []
digit = 0

for i in s:
    if i.isalpha():
        alpha.append(i)
    elif i.isdigit():
        digit += int(i)

alpha.sort()
print(alpha)

if digit != 0:
    alpha.append(str(digit))

print(''.join(alpha))