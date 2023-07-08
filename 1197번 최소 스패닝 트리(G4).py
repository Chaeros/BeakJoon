v,e=map(int,input().split())

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

array=[]
for i in range(e):
    a,b,c=map(int,input().split())
    array.append((c,a,b))

array.sort()

parent=[0]*(v+1)
for i in range(1,v+1):
    parent[i]=i

result=0
for i in range(e):
    if find_parent(parent,array[i][1])==find_parent(parent,array[i][2]):
        continue
    else:
        union_parent(parent,array[i][1],array[i][2])
        result+=array[i][0]

print(result)