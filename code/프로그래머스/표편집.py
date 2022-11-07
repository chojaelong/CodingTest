def solution(n, k, cmd):
    answer = ['O' for _ in range(n)]
    linked_list = [[i-1, i+1] for i in range(n)]
    linked_list[0] = [None, 1]
    linked_list[-1] = [n - 2, None]
    delete_stack = []
    select = k
    
    for command in cmd:
        if command[0] == 'C':
            prev, next = linked_list[select]
            delete_stack.append([prev, select, next])
            answer[select] = 'X'
            
            if next == None:
                select = linked_list[select][0]
            else:
                select = linked_list[select][1]
                
            if prev == None:
                linked_list[next][0] == None
            elif next == None:
                linked_list[prev][1] = None
            else:
                linked_list[prev][1] = next
                linked_list[next][0] = prev
            
        elif command[0] == 'Z':
            prev, idx, next = delete_stack.pop()
            answer[idx] = 'O'
            
            if prev == None:
                linked_list[next][0] = idx
            elif next == None:
                linked_list[prev][1] = idx
            else:
                linked_list[next][0] = idx
                linked_list[prev][1] = idx
        else:
            c1, c2 = command.split(' ')
            c2 = int(c2)
            if c1 == 'U':
                for i in range(c2):
                    select = linked_list[select][0]
            elif c1 == 'D':
                    for i in range(c2):
                        select = linked_list[select][1]
                
            
    return ''.join(answer)
        
solution(4, 3, ["C", "C"])