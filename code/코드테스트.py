def solution(C):
    idx = -1
    history = []

    for command, word in C:
        if command == "BACK" and idx != 0:
            idx -= 1

        elif command == "NEXT" and idx != len(history) - 1:
            idx += 1
        
        elif command == "PUSH":
            history = history[: idx + 1]
            history.append(word)
            idx += 1
        
        print(history)

    answer = history[idx]
    return answer

solution([["PUSH","www.domain1.com"],["PUSH","www.domain2.com"],["PUSH","www.domain3.com"],["BACK","1"],["BACK","1"],["PUSH","www.domain4.com"]])