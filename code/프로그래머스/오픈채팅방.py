def solution(record):
    uid = dict()
    for i in record:
        array = i.split(' ')
        # array[0] = func, array[1] = id, array[2] = name
        if array[0] == "Enter":
            uid[array[1]] = array[2]
        elif array[0] == "Change":
            if uid.get(array[1]) != None:
                uid[array[1]] = array[2]
        # array[0] = func, array[1] = id
        elif array[0] == "Leave":
            uid.pop(array[1])
    
    answer = []

    for i in record:
        array = i.split(' ')
        name = uid.get(id)
        if array[0] == "Enter":
            answer.append(f"{uid[array[1]]}님이 들어왔습니다.")
        elif array[0] == "Leave":
            answer.append(f"{uid[array[1]]}님이 나갔습니다.")
    
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(record)