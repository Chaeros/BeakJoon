t=int(input())

for testcase in range(t):
    n, m = map(int, input().split())
    matrix=[]
    rowSumArray = [0]
    colSumArray = [0]
    for i in range(n):
        matrix.append(list(map(int, input().split())))
        rowSumArray.append(sum(matrix[i]))
    for i in range(n):
        tempSum = 0
        for j in range(n):
            tempSum+=matrix[j][i]
        colSumArray.append(tempSum)

    for i in range(m):
        r1, c1, r2, c2, v = map(int, input().split())
        for j in range(r1,r2+1):
            rowSumArray[j]+=v*(c2-c1+1)
        for j in range(c1,c2+1):
            colSumArray[j]+=v*(r2-r1+1)
    for i in range(1,n+1):
        print(rowSumArray[i],end=' ')
    print()
    for i in range(1,n+1):
        print(colSumArray[i],end=' ')
    print()
    
# 오답풀이
# t=int(input())

# def prefixsum_Cal(prefixSum,n,array):
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             prefixSum[i][j]=prefixSum[i-1][j]+prefixSum[i][j-1]-prefixSum[i-1][j-1]+array[i-1][j-1]
#
# def printRowColSum(prefixSum,n):
#     for i in range(1,n+1):
#         print(prefixSum[i][n]-prefixSum[i-1][n],end=' ')
#     print()
#     for i in range(1,n+1):
#         print(prefixSum[n][i]-prefixSum[n][i-1],end=' ')
#     print()

# for testcase in range(t):
#     n, m = map(int, input().split())
#     array = []
#     for i in range(n):
#         array.append(list(map(int, input().split())))
#     for i in range(m):
#         r1, c1, r2, c2, v = map(int, input().split())
#         for j in range(r1, r2 + 1):
#             for k in range(c1, c2 + 1):
#                 array[j - 1][k - 1] += v
#     prefixSum = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
#     prefixsum_Cal(prefixSum, n, array)
#     printRowColSum(prefixSum, n)