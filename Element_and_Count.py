n=int(input())
a=list(map(int,input().split()))
c=0
s=[]
for i in range(n):
    s.append(-1)
for i in range(n):
    c=1
    for j in range(i+1,n):
        if(a[i]==a[j]):
            c+=1
            s[j]=0
    if(s[i]!=0):
        s[i]=c
for i in range(n):
    if(s[i]!=0):
        print(a[i],s[i],end=' ')
       