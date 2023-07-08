from collections import deque

n=int(input())

indegree=[0]*(n+1)
graph=[[] for i in range(n+1)]
for i in range(1,n+1):
    a,b=map(int,input().split())
    graph[i].append(a)
    graph[i].append(b)
    indegree[a]+=1
    indegree[b]+=1

def topology_sort():
    q=deque()

    for i in range(1,n+1):
        if indegree[i]<2:
            q.append(i)

    while q:
        now=q.popleft()
        indegree[now]=0
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==1:
                q.append(i)

topology_sort()
count=0
result=[]
for i in range(1,n+1):
    if indegree[i]==2:
        count+=1
        result.append(i)

result.sort()
print(count)
for i in range(count):
    print(result[i],end=' ')