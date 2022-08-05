def solution(X, Y):
    xarray = list(map(str, X))
    yarray = list(map(str, Y))
    q = []
    
    for s in list(set(X)&set(Y)):
        sc = X.count(s)
        bc = Y.count(s)
        for i in range(min(sc, bc)):
            q.append(s)
    
    answer = ''
    q.sort(reverse=True)
    
    if len(q) == 0:
        answer = '-1'
    elif max(q) == '0':
        answer = '0'
    else:
        answer = ''.join(q)
    
    return answer