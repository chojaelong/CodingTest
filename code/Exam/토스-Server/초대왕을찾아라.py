from collections import defaultdict

def solution(invitationPairs):
    dic = defaultdict(list)
    users = []
    scores = []
    for inviter, guest in invitationPairs:
        dic[inviter].append(guest)
        
        if inviter not in users:
            users.append(inviter)
            scores.append(10)
        else:
            index = users.index(inviter)
            scores[index] += 10
            
        # inviter를 초대한 사람
        inviterinviter = ''
        for k, v in dic.items():
            if inviter in v:
                inviterinviter = k
                break
        
        # 초대한 사람이 있으면
        if inviterinviter != '':
            index = users.index(inviterinviter)
            scores[index] += 3
        
        # inviter를 초대한 사람을 초대한 사람
        inviterinviterinviter = ''
        for k, v in dic.items():
            if inviter in v:
                inviterinviterinviter = k
                break
        
        # 초대한 사람이 있으면
        if inviterinviterinviter != '':
            index = users.index(inviterinviterinviter)
            scores[index] += 1
    
    temp = [[users[i], scores[i]] for i in range(len(scores))]
    print(temp)
    temp = sorted(temp, key=lambda x: x[1], reverse=True)
    print(temp)
    
    if len(temp) < 3:
        answer = [temp[i][0] for i in range(len(temp))]
    else:
        answer = [temp[i][0] for i in range(3)]
    
    return answer

invitationPairs1 = [[1, 2], [2, 3], [2, 3], [2, 5], [5, 6], [5, 7], [6, 8], [2, 9]]
invitationPairs2 = [[1, 2], [1, 3], [3, 4], [4, 5], [4, 6], [4, 7]]
invitationPairs3 = [[1, 2], [3, 4]]

print(solution(invitationPairs1))
print(solution(invitationPairs2))
print(solution(invitationPairs3))