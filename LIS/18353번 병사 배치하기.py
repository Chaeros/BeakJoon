# https://www.acmicpc.net/problem/18353

import sys

input=sys.stdin.readline

N=int(input())
arr=list(map(int,input().split()))
length=[0]*N

for i in range(N):
    length[i]=1
    for j in range(i):
        if arr[j]>arr[i]:
            length[i]=max(length[i],length[j]+1)

print(N-max(length))