n=int(input())

array=[]
for i in range(n):
    array.append(int(input()))

p1=0
p2=1
end=n-1
result=4


array.sort()

if n==1:
    print(4)
else:
    while p1<end:
        if p1==p2 and p2<end:
            p2+=1
        else:
            if array[p2]-array[p1]<5:
                result=min(result,3-(p2-p1-1))
                if p2!=end:
                    p2+=1
                else:
                    p1+=1
            else:
                p1+=1
    print(result)