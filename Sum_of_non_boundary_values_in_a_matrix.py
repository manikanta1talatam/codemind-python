n,m=map(int,input().split())
a=[]
for i in range(n):
    s=list(map(int,input().split()))
    a.append(s)
sum1=0
for i in range(n):
    for j in range(m):
        if(i!=0 and i!=n-1 and j!=0 and j!=m-1):
            sum1=sum1+a[i][j]
print(sum1)