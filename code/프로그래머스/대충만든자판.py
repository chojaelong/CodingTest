def solution(keymap, targets):
    answer = []
    m_cnt = dict()
    
    # 최솟값 저장
    for key in keymap:
        for cnt, word in enumerate(list(key)):
            if word in m_cnt:
                m_cnt[word] = min(m_cnt[word], cnt + 1)
            else:
                m_cnt[word] = cnt + 1
    
    # 최소 입력 횟수 계산
    for target in targets:
        cnt = 0
        for word in list(target):
            if word in m_cnt:
                cnt += m_cnt[word]
            else:
                answer.append(-1)
                break
        else:
            answer.append(cnt)
    
    return answer