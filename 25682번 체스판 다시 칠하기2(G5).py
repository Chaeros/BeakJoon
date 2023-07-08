n,m,k=map(int,input().split())

blackBoard=[[0 for _ in range(m+1)] for _ in range(n+1)]
whiteBoard=[[0 for _ in range(m+1)] for _ in range(n+1)]

black=True
white=False

array=[]
for i in range(n):
    array.append(list(input()))
    for j in range(m):
        if array[i][j]=='B': array[i][j]=1
        else: array[i][j]=0

for i in range(1,n+1):
    for j in range(1,m+1):
        blackBoard[i][j]=black
        whiteBoard[i][j]=white
        black=not black
        white=not white
    if m%2==0:
        black = not black
        white = not white

for i in range(n):
    for j in range(m):
        blackBoard[i+1][j+1]^=array[i][j]
        whiteBoard[i+1][j+1]^=array[i][j]

prefixBlackBoard=[[0 for _ in range(m+1)] for _ in range(n+1)]
prefixWhiteBoard=[[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        prefixBlackBoard[i+1][j+1]=prefixBlackBoard[i][j+1]+prefixBlackBoard[i+1][j]\
                             -prefixBlackBoard[i][j]+blackBoard[i+1][j+1]
        prefixWhiteBoard[i+1][j+1]=prefixWhiteBoard[i][j+1]+prefixWhiteBoard[i+1][j]\
                             -prefixWhiteBoard[i][j]+whiteBoard[i+1][j+1]

minimum=int(1e9)
for i in range(n-k+1):
    for j in range(m-k+1):
        minimum=min(minimum,prefixBlackBoard[k+i][k+j]-prefixBlackBoard[i][k+j]
                    -prefixBlackBoard[k+i][j]+prefixBlackBoard[i][j])
        minimum=min(minimum,prefixWhiteBoard[k+i][k+j]-prefixWhiteBoard[i][k+j]
                    -prefixWhiteBoard[k+i][j]+prefixWhiteBoard[i][j])
print(minimum)