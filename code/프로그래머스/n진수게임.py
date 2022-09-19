import string

def convert_recur(num, base):
    number = string.digits + string.ascii_uppercase
    q, r = divmod(num, base)
    return convert_recur(q, base) + number[r] if q else number[r]

def solution(n, t, m, p):
    answer = ''
    words = ''
    for i in range(0, 1001 * m):
        value = convert_recur(i, n)
        words += value

    count = 0
    idx = p - 1
    while count < t:
        answer += words[idx]
        count += 1
        idx += m

    return answer

print(solution(16, 16, 2, 1))