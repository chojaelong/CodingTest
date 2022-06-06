def solution(s):
    sizeList = [len(s)]

    for i in range(1, len(s)):
        array = [s[j:j+i] for j in range(0, len(s), i)]
        if len(array) == 1:
            break

        print(f"{i}Before: {array}")
        count = len(array)
        last = 0
        while last < count - 1:
            if array[last] == array[last + 1]:
                del array[last + 1]
                if last != 0 and array[last - 1].isdigit():
                    array[last - 1] = str(int(array[last - 1]) + 1)
                    count -= 1
                    continue
                else:
                    array.insert(last, str(2))
                
            last+=1

        strArray = "".join(array)
        sizeList.append(len(strArray))
        print(f"{i}After: {strArray}")
    
    print(min(sizeList))
    return min(sizeList)

solution("abcabcdede")