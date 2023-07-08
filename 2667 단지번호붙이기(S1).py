n=int(input())

graph=[]

for i in range(n):
    graph.append(list(map(int,input())))

dx=[-1,0,1,0]
dy=[0,-1,0,1]

complexCount=0
houseCountList=[]

houseCount=0

def dfs(graph,visited,x,y):
    global houseCount,complexCount
    if graph[x][y]==1 and visited[x][y]==False:
        visited[x][y]=True
        houseCount+=1
        for i in range(4):
            mx=x+dx[i]
            my=y+dy[i]
            if mx<0 or mx>=n or my<0 or my>=n:
                continue
            dfs(graph,visited,mx,my)
        return True
    return False

visited=[[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        houseCount=0
        if dfs(graph,visited,i,j):
            complexCount+=1
            houseCountList.append(houseCount)

houseCountList.sort()

print(complexCount)
for i in houseCountList:
    print(i)