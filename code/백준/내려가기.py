# https://www.acmicpc.net/problem/2096
import sys
input = sys.stdin.readline

n = int(input())
maxD = [[0 for _ in range(3)] for _ in range(2)]
minD = [[0 for _ in range(3)] for _ in range(2)]
for i in range(n):
    temp = list(map(int, input().split()))
 
    maxD[1][0] = max(maxD[0][0], maxD[0][1]) + temp[0]
    minD[1][0] = min(minD[0][0], minD[0][1]) + temp[0]
 
    maxD[1][1] = max(maxD[0][0], maxD[0][1], maxD[0][2]) + temp[1]
    minD[1][1] = min(minD[0][0], minD[0][1], minD[0][2]) + temp[1]
 
    maxD[1][2] = max(maxD[0][1], maxD[0][2]) + temp[2]
    minD[1][2] = min(minD[0][1], minD[0][2]) + temp[2]
 
    maxD[0][0], maxD[0][1], maxD[0][2] = maxD[1][0], maxD[1][1], maxD[1][2]
    minD[0][0], minD[0][1], minD[0][2] = minD[1][0], minD[1][1], minD[1][2]
    
print(max(maxD[1]), min(minD[1]))
