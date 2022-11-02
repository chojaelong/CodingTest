from itertools import combinations
import copy

def makelist(array, pick_list, row_count):
    new_array = ['' for _ in range(row_count)]
    for i in pick_list:
        for j in range(row_count):
            new_array[j] += array[i][j]
    
    return new_array

def remove_repeat(pick_list, complete):
    return_list = copy.deepcopy(pick_list)
    remove_idx = []
    for idx, pick in enumerate(pick_list):
        if remove(pick, complete):
            remove_idx.append(idx)
    
    remove_idx.sort(reverse=True)
    for i in remove_idx:
        del return_list[i]
    
    return return_list
            
def remove(target, complete):
    for values in complete:
        condition = [False] * len(values)
        for idx, value in enumerate(values):
            if value in target:
                condition[idx] = True
        if all(condition):
            return True
    
    return False
        
    

def solution(relation):
    col_count = len(relation[0])
    row_count = len(relation)
    array = [[] for _ in range(col_count)]
    complete = []
    pick_array = [i for i in range(col_count)]
    pick = 1
    
    for rel in relation:
        for idx, value in enumerate(rel):
            array[idx].append(value)
            
    print(array)
            
    answer = 0
    while pick < col_count:
        pick_combi = list(combinations(pick_array, pick))
        pick_combi = remove_repeat(pick_combi, complete)
        for p in pick_combi:            
            t = makelist(array, p, row_count)
            if len(t) == len(set(t)):
                answer += 1
                print(p)
                complete.append(p)
        
        pick += 1
            
    return answer

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])