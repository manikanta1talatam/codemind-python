n,m=map(int,input().split())
a=[]
for i in range(n):
    s=list(map(int,input().split()))
    a.append(s)
sum=0
for i in range(n):
    for j in range(m):
        if(i==j or j==n-i-1):
            sum=sum+a[i][j]
print(sum)