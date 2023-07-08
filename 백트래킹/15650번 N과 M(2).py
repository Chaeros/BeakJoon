# https://www.acmicpc.net/problem/15650

import sys

input = sys.stdin.readline
N,M=map(int,input().split())

visited=[False]*(N+1)
result=[]

def recur(x):
    if x==M:
        print(' '.join(map(str,result)))
        return
    for i in range(1,N+1):
        if visited[i]==False and (len(result)==0 or result[-1]<i):
            visited[i] = True
            result.append(i)
            recur(x+1)
            visited[i]=False
            result.pop()
recur(0)