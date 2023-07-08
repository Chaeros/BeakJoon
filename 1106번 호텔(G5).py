c,n=map(int,input().split())
INF=int(1e9)

d=[INF]*1001
d[0]=0

graph=[]
for i in range(n):
    a, b = map(int, input().split())
    graph.append((a,b))

graph.sort(reverse=True, key=lambda x : x[1])

for k in graph:
    for j in range(k[1],1001):
        #if j%k[1]==0:
                d[j]=min(d[j],d[j-k[1]]+k[0])
        #else:
         #   d[j]=d[j-1]

print(d[c])
print()
print(d)

def temp():
    graph.sort()

    for i in range(n):
        a, b = graph[i]

        if i == 0:
            for j in range(b, 1001):
                if j % b == 0:
                    d[j] = d[j - b] + a
                else:
                    d[j] = d[j - 1]
        else:
            for j in range(b, 1001):
                if j % b == 0:
                    d[j] = min(d[j], d[j - b] + a)
                else:
                    d[j] = d[j - 1]