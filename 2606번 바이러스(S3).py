from collections import deque

n=int(input())
v=int(input())

graph=[[] for _ in range(n+1)]
for i in range(v):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[False]*(n+1)

def func(start):
    q=deque()
    q.append(start)
    visited[start]=True

    while q:
        now=q.popleft()

        for i in graph[now]:
            if visited[i] ==False:
                visited[i]=True
                q.append(i)

func(1)
print(graph)
count=0
for i in range(2,n+1):
    if visited[i]==True:
        count+=1

print(count)