from collections import deque
import copy

n=int(input())

graph=[[] for i in range(n+1)]
cost=[0]*(n+1)
indegree=[0]*(n+1)

for i in range(1,n+1):
    tempList=list(map(int,input().split()))
    cost[i]=tempList[0]
    indegree[i]+=tempList[1]
    for j in range(tempList[1]):
        graph[tempList[j+2]].append(i)
def topology_sort():
    result = copy.deepcopy(cost)
    q=deque()
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        now=q.popleft()
        for i in graph[now]:
            result[i]=max(result[i],result[now]+cost[i])
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)

    print(max(result))

topology_sort()