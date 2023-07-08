#https://www.acmicpc.net/problem/3020
#개똥벌레(Gold5)
#2023년 06월 22일

import sys

n,h=map(int,sys.stdin.readline().split())

stalactite=[0]*(h+2) #종유석
stalagmite=[0]*(h+2) #석순

for i in range(n):
    if i%2==0:
        stalactite[int(sys.stdin.readline())]+=1
    else:
        stalagmite[h-int(sys.stdin.readline())+1]+=1

for i in range(1,h+1):
    stalactite[h-i+1]+=stalactite[h-i+2]
    stalagmite[i]+=stalagmite[i-1]

minimum=int(1e9)
minimumCnt=0
for i in range(1,h+1):
    if minimum>stalactite[i]+stalagmite[i]:
        minimum=stalactite[i]+stalagmite[i]
        minimumCnt=1
    elif minimum==stalactite[i]+stalagmite[i]:
        minimumCnt+=1
print(minimum,minimumCnt)

# 메모리 초과
# import sys
# 
# n,h=map(int,sys.stdin.readline().split())
# 
# total=[0]*h
# stalactite=[[0 for _ in range(n+2)] for _ in range(h+2)]
# stalagmite=[[0 for _ in range(n+2)] for _ in range(h+2)]
# 
# for i in range(1,n+1):
#     x=int(sys.stdin.readline())
#     if i % 2 == 0:
#         stalagmite[h-x+1][i]=1
#     else:
#         stalactite[x][i]=1
# 
# for i in range(1,h+1):
#     for j in range(1,n+1):
#         stalagmite[i][j]=stalagmite[i-1][j]+stalagmite[i][j-1]\
#                          -stalagmite[i-1][j-1]+stalagmite[i][j]
#     total[i-1]+=stalagmite[i][n]
# 
# for i in range(h,0,-1):
#     for j in range(1,n+1):
#         stalactite[i][j]=stalactite[i+1][j]+stalactite[i][j-1]\
#                          -stalactite[i+1][j-1]+stalactite[i][j]
#     total[i-1] += stalactite[i][n]
# 
# total.sort()
# cnt=0
# for i in total:
#     if total[0]!=i:
#         break
#     cnt+=1
# print(total[1],end=' ')
# print(cnt)


# 시간초과
# import sys
# 
# n,h=map(int,input().split())
# 
# graph=[0]*h
# for i in range(n):
#     x=int(sys.stdin.readline())
#     if i%2==0:
#         for j in range(x):
#             graph[j]+=1
#     else:
#         for j in range(h-1,h-x-1,-1):
#             graph[j]+=1
# 
# cnt=0
# minimum=min(graph)
# 
# for i in range(h):
#     if minimum==graph[i]: cnt+=1
# 
# print(minimum,end=' ')
# print(cnt)

# 메모리 초과
# import sys
# n,h=map(int,input().split())
#
# graph=[[0 for _ in range(n)] for _ in range(h)]
# for i in range(n):
#     x=int(sys.stdin.readline())
#     if i%2==0:
#         for j in range(x):
#             graph[j][i]=1
#     else:
#         for j in range(h-1,h-x-1,-1):
#             graph[j][i]=1
#
# minimum=int(1e9)
# cnt=0
#
# for i in range(h):
#     minimum=min(minimum,sum(graph[i]))
#
# for i in range(h):
#     if minimum==sum(graph[i]): cnt+=1
#
# print(minimum,end=' ')
# print(cnt)