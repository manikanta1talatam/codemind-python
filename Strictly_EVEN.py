n=int(input())
a=list(map(int,input().split()))
c=0
c1=0
for i in range(len(a)):
    if(i%2==0):
        c+=1
for i in range(len(a)):
    if(i%2==0 and a[i]%2==0):
        c1+=1
print(c==c1)