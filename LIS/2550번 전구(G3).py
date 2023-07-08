# https://www.acmicpc.net/problem/2550
# 전구 Gold3
# 2023년 7월 7일

import sys
input=sys.stdin.readline

N=int(input())
switch=list(map(int,input().split()))
bulb=list(map(int,input().split()))

arr=[]
for i in switch:
    arr.append(bulb.index(i))


length=[0]*N
preNode=[]
for i in range(N):
    preNode.append(i)

for i in range(N):
    length[i]=1
    k=0
    for j in range(i):
        if arr[j]<arr[i]:
            if length[i]<length[j]+1:
                length[i]=length[j]+1
                preNode[i]=j

temp=length.index(max(length))
result=[]

x=temp
while True:
    result.append(switch[x])
    if preNode[x]==x:
        break
    x=preNode[x]

result.sort()
print(max(length))
for i in result:
    print(i,end=' ')

    # def recur(x):
    #     result.append(switch[x])
    #     if preNode[x]==x:
    #         return
    #     recur(preNode[x])
    #
    # recur(temp)