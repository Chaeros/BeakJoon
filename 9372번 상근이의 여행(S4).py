T=int(input())

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

for i in range(T):
    n,m=map(int,input().split())
    array=[]
    resultCount=0

    for j in range(m):
        a,b=map(int,input().split())
        array.append((a,b))

    parent=[0]*(n+1)
    for j in range(1,n+1):
        parent[j]=j

    for j in range(m):
        if find_parent(parent,array[j][0])==find_parent(parent,array[j][1]):
            continue
        else:
            union_parent(parent,array[j][0],array[j][1])
            resultCount+=1

    print(resultCount)