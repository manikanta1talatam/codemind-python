n=int(input())
l=list(map(int,input().split()))
c=n-1
sum=0
for i in l:
    sum=sum+i*2**c
    c-=1
print(sum)