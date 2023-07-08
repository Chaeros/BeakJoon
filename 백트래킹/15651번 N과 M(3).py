import sys

input=sys.stdin.readline

N,M=map(int,input().split())

visited=[False]*(N+1)
result=[]

def back_Tracking(x):
    if x==M:
        print(' '.join(map(str,result)))
        return
    for i in range(1,N+1):
        result.append(i)
        back_Tracking(x+1)
        result.pop()

back_Tracking(0)