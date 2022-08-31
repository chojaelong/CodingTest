# https://school.programmers.co.kr/learn/courses/30/lessons/118666
def solution(survey, choices):
    characters = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    scores = [[0, 0] for i in range(4)]
    
    for i in range(len(survey)):
        character = list(survey[i])
        reverse = False
        index = -1
        for j in range(4):
            if character[0] in characters[j]:
                index = j
                if character[0] != characters[j][0]:
                    reverse = True
                break
        
        score = choices[i]
        if score < 4:
            if reverse:
                scores[index][1] += (4 - score)
                print(scores)
            elif not reverse:
                scores[index][0] += (4 - score)
                print(scores)
        elif score > 4:
            if reverse:
                scores[index][0] += (score - 4)
                print(scores)
            elif not reverse:
                scores[index][1] += (score - 4)
                print(scores)
    
    answer = ''
    print(scores)
    for i in range(4):
        if scores[i][0] >= scores[i][1]:
            answer += characters[i][0]
        elif scores[i][0] < scores[i][1]:
            answer += characters[i][1]
    
    return answer

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
print(solution(survey, choices))