from collections import deque

n,m=map(int,input().split())

indegree=[0]*(n+1)
graph=[[] for _ in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

result=[]
visited=[False]*(n+1)
def topology_sort():
    q=deque()

    for i in range(1,n+1):
        if indegree[i]==0 and visited[i]==False:
            q.append(i)
            result.append(i)
            visited[i] =True
            while q:
                now = q.popleft()
                for j in graph[now]:
                    indegree[j] -= 1
                    if indegree[j] == 0:
                        q.append(j)
                        result.append(j)
                        visited[j] = True

topology_sort()
for i in result:
    print(i,end=' ')