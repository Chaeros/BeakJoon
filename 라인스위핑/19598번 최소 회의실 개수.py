# https://www.acmicpc.net/problem/19598
# 알고리즘 : 라인 스위핑

import sys

input = sys.stdin.readline

N=int(input())
graph=[]

for i in range(N):
    a,b=map(int,input().split())
    graph.append((a,1))
    graph.append((b,-1))

graph.sort()
roomCount=0
maxCount=0
temp=graph[0][0]

for i in graph:
    if temp!=i[0]:
        if roomCount>maxCount:
            maxCount=roomCount
        temp=i[0]
    if i[1]==1:
        roomCount+=1
    else:
        roomCount-=1

if roomCount>maxCount:
    maxCount=roomCount

print(maxCount)

