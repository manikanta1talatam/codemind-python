n=int(input())
a=list(map(int,input().split()))
for i in range(n//2):
    print(a[i],a[n-i-1],end=' ')
if(n%2==1):
    print(a[n//2],'0')