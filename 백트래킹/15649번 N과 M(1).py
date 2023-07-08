# https://www.acmicpc.net/problem/15649
# 알고리즘 : 백트래킹

import sys

input=sys.stdin.readline

n,m=map(int,input().split())
visited=[False]*(n+1)
result=[]

def recur(x):
    if x==m:
        print(' '.join(map(str,result)))
        return
    for i in range(1,n+1):
        if visited[i]==False:
            visited[i]=True
            result.append(i)
            recur(x+1)
            visited[i]=False
            result.pop()

recur(0)