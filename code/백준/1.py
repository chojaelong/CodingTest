while True:
    try:
        n = int(input())
    except:
        break

    if n % 2 == 0 or n % 5 == 0:
        print("2와 5의 배수입니다.")

    else:
        a = 10
        count = 1
        while True:
            value = (a - 1) // 9
            if value % n == 0:
                print(count)
                break
            a *= 10
            count += 1