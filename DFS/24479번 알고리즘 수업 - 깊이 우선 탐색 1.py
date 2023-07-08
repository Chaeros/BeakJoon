# https://www.acmicpc.net/problem/24479
#

import sys
sys.setrecursionlimit(10**5)
n,m,r=map(int,sys.stdin.readline().split())
visited=[0 for _ in range(n+1)]
graph=[[] for _ in range(n+1)]
cnt=1
def dfs(start):
    global cnt
    visited[start]=cnt
    cnt+=1

    for i in graph[start]:
        if visited[i]==0:
            dfs(i)

for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()

dfs(r)

for i in range(1,n+1):
    print(visited[i])