from itertools import permutations
import copy

def solution(expression):
    answer = []
    operators = ['+', '-', '*']
    operator = list(set([str for str in expression if str in operators]))
    ranks = list(permutations(operator, len(operator)))
    print(ranks)
    
    nums = [['']]
    i = 0
    for s in expression:
        if s in operators:
            nums[i] = nums[i][0]
            nums.append(s)
            nums.append([''])
            i += 2
        else:
            nums[i][0] += s
    nums[i] = nums[i][0]
            
    for rank in ranks:
        c_nums = copy.deepcopy(nums)
        for oper in rank:
            while c_nums.count(oper) != 0:
                idx = c_nums.index(oper)
                value = eval(c_nums[idx - 1] + c_nums[idx] + c_nums[idx + 1])
                del c_nums[idx + 1], c_nums[idx], c_nums[idx - 1]
                c_nums.insert(idx - 1, str(value))
                
        answer.append(abs(int(c_nums[0])))
        
    
    return max(answer)
    