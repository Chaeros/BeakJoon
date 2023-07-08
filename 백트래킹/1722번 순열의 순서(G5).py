# https://www.acmicpc.net/problem/1722
# 알고리즘 : 백트래킹, 순열

import sys
input = sys.stdin.readline

n=int(input())
inputList=list(map(int,input().split()))
cnt=0
rs=[]

def recur(row):
    global cnt
    if row==n:
        cnt+=1
        if cnt==inputList[0]:
            GOTO?
        return
    for i in range(n):
        rs.append(i)
        recur(row+1)
        rs.pop()

if len(inputList)>2:
    pass
else:
    pass