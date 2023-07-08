n,k=map(int,input().split())

if n<=k:
    print(k-n)
else:
    array=[1]*k
    i=0

    while True:
        if sum(array)>=n:
            break
        array[i]*=2
        if sum(array)>n and i!=k-1:
            array[i]//=2
            i+=1

    print(sum(array)-n)