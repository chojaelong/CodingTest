def condition(skill, skill_tree):
    i = 0
    
    for value in skill_tree:
        if value in skill:
            if value == skill[i]:
                i += 1
            else:
                return False
    
    return True

def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)
    for skill_tree in skill_trees:
        if condition(skill, skill_tree):
            answer += 1
    
    return answer
            