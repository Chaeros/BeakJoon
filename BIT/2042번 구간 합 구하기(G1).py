import sys

input=sys.stdin.readline

def sum(x):



n,m,k=map(int,input().split())

arr=[0]*(n+1)
tree=[0]*(n+1)

for i in range(1,n+1):
    arr[i]=int(input())

a,b,c=map(int,input().split())
