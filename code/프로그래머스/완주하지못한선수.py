def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = ''
    for i in range(len(participant)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    return answer

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
solution(participant, completion)