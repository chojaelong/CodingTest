import copy

def solution(want, number, discount):
    dic = dict()
    answer = 0
    
    for i in range(len(want)):
        dic[want[i]] = number[i]
        
    for index in range(len(discount) - 9):
        count = 0
        copydic = copy.deepcopy(dic)
        for i in range(index, index + 10):
            if discount[i] in copydic:
                if copydic[discount[i]] == 0:
                    break
                copydic[discount[i]] -= 1
                count += 1
            else:
                break
            
            if count == 10:
                answer += 1
    
    return answer

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
solution(want, number, discount)