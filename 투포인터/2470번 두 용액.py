# https://www.acmicpc.net/problem/2470
# 두 용액 / Gold5
# 2023년 7월 5일
import sys

input=sys.stdin.readline


N=int(input())
tempList=list(map(int,input().split()))

list=[]
for i in tempList:
    if i<0:
       list.append((abs(i),-1))
    else:
        list.append((i,1))

list.sort()

minGap=int(1e10+1)
resultVal=[int(1e10+1),int(1e10+1)]

for i in range(N-1):
    start=list[i]
    end=list[i+1]
    if minGap>abs(start[0]*start[1]+end[0]*end[1]):
        minGap=abs(start[0]*start[1]+end[0]*end[1])
        resultVal[0]=start[0]*start[1]
        resultVal[1]=end[0]*end[1]

resultVal.sort()
for i in resultVal:
    print(i,end=' ')