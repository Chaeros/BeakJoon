#재귀하는데 런타임에러 나오면 아래 코드를 넣어줘야한다.
#근데 또 너무 높게 설정하면 메모리 초과나오니 잘 조절할것
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n,m=map(int,input().split())

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)

    if a>b:
        parent[a]=b
    else:
        parent[b]=a

parent=[0]*(n+1)
for i in range(n+1):
    parent[i]=i

result=[]
count=0

for i in range(m):
    a,b,c=map(int,input().split())
    if a==0:
        union_parent(parent,b,c)
    elif a==1:
        count+=1
        if find_parent(parent,b)==find_parent(parent,c):
            result.append(1)
        else:
            result.append(0)

for i in range(count):
    if result[i]==1:
        print("YES")
    else:
        print("NO")