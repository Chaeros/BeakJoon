# https://www.acmicpc.net/problem/24444
# 알고리즘 수업 - 너비 우선 탐색(Silver2)

import sys
from collections import deque

n,m,r=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
visited=[0 for _ in range(n+1)]

def bfs(start):
    cnt=1
    visited[start]=cnt
    que=deque([start])
    while que:
        now=que.popleft()
        for i in graph[now]:
            if visited[i]==0:
                cnt+=1
                visited[i]=cnt
                que.append(i)

for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()

bfs(r)

for i in range(1,n+1):
    print(visited[i])