n,m=map(int,input().split())
a=[]
for i in range(n):
    s=list(map(int,input().split()))
    a.append(s)
sum1=0
for i in range(n):
    for j in range(m):
        if(i==0 or i==n-1 or j==0 or j==m-1):
            sum1=sum1+a[i][j]
print(sum1)