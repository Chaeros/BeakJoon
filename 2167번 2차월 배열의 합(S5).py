n,m=map(int,input().split())

array=[]

for i in range(n):
    array.append(list(map(int,input().split())))

prefixSum=[[0 for i in range(m+1)] for j in range(n+1)]

for i in range(1,m+1):
    for j in range(1,n+1):
        prefixSum[j][i]=prefixSum[j][i-1]+prefixSum[j-1][i]\
                        -prefixSum[j-1][i-1]+array[j-1][i-1]

def cal_prefixSum(i,j,x,y):
    return prefixSum[x][y]-prefixSum[i-1][y]\
        -prefixSum[x][j-1]+prefixSum[i-1][j-1]

k=int(input())

for i in range(k):
    i,j,x,y=map(int,input().split())
    print(cal_prefixSum(i,j,x,y))