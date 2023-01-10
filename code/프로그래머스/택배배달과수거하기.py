def solution1(cap, n, deliveries, pickups):
    answer = 0
    left_delivery = sum(deliveries)
    left_pickup = sum(pickups)
    top = n-1
    
    while not (left_delivery == 0 and left_pickup == 0):
        delivery = cap
        pickup = cap
        move = -1
        c1, c2 = True, True
        t1, t2 = top, top
        
        for i in range(top, -1, -1):
            # 배달
            if c1:
                # 끝 배달지의 배달 물량이 남아있고 수량보다 많거나 같을 때
                if deliveries[i] != 0 and delivery <= deliveries[i]:
                    deliveries[i] -= delivery
                    delivery = 0 
                    c1 = False
                    t1 = i
                    if move < i + 1:
                        move = i + 1

                # 끝 배달지의 배달 물량이 남아있고 수량보다 작을 때
                elif deliveries[i] != 0 and delivery > deliveries[i]:
                    delivery -= deliveries[i]
                    deliveries[i] = 0
                    if move < i + 1:
                        move = i + 1

            # 수거
            if c2:
                # 끝 수거지의 수거 물량이 남아있고 수량보다 많을 때
                if pickups[i] != 0 and pickup <= pickups[i]:
                    pickups[i] -= pickup
                    pickup = 0
                    c2 = False
                    t2 = i
                    if move < i + 1:
                        move = i + 1

                # 끝 수거지의 수거 물량이 남아있고 수량보다 같거나 작을 때
                elif pickups[i] != 0 and pickup > pickups[i]:
                    pickup -= pickups[i]
                    pickups[i] = 0
                    if move < i + 1:
                        move = i + 1
            
            if not c1 and not c2:
                break
        
        left_pickup = sum(pickups)
        left_delivery = sum(deliveries)
        top = max(t1, t2)
        print(top)
        answer += (move * 2)
    
    return answer

def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0
    
    d = 0
    p = 0
    
    for i in range(n):
        d += deliveries[i]
        p += pickups[i]
        
        while d > 0 or p > 0:
            d -= cap
            p -= cap
            answer += (n - i) * 2
            
    return answer