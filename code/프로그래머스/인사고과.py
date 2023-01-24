def solution(scores):
    wanho = scores[0]
    wanho_sum = sum(wanho)
    scores.sort(key=lambda s: (-s[0], s[1]))
    max_company, answer = 0, 1
    for s in scores:
        if wanho[0] < s[0] and wanho[1] < s[1]:
            return -1
        if max_company <= s[1]:
            if wanho_sum < s[0] + s[1]:
                answer += 1
            max_company = s[1]
    return answer