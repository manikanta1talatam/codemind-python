n=int(input())
a=list(map(int,input().split()))
p=set(a)
c=0
m=0
for i in p:
    c=0
    for j in a:
        if(i==j):
            c+=1
    if(i==c):
        m+=1
print(m)