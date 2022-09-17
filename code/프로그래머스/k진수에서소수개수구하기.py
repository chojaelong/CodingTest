# https://school.programmers.co.kr/learn/courses/30/lessons/92335
import math

def is_prime_num(n):
    for i in range(2, int(math.sqrt(n))+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False

    return True

def convert_iter(num, base):
    power = 0
    tmp = ''
    while num:
        tmp = str(num%base) + tmp
        num //= base
    return tmp

def solution(n, k):
    array = convert_iter(n, k).split('0')
    print(array)
    answer = 0
    for value in array:
        if value == '' or value == '1':
            continue
        if is_prime_num(int(value)):
            answer += 1
    return answer