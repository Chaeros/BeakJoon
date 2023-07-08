# https://www.acmicpc.net/problem/16922
# 백트래킹

import sys

input=sys.stdin.readline
n=int(input())
result=[0]*(50*20+1) #50이 20번 쓰여 더해진게 최대값이므로
RomaNum=[1,5,10,50]
buf=[]
cnt=0

def recur(x,start):
    if x==n:
        result[sum(buf)]=1
        return
    for i in range(start,4):
        buf.append(RomaNum[i])
        recur(x+1,i)
        buf.pop()

recur(0,0)
print(sum(result))