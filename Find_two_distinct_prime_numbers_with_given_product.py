def prime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    else:
        return True
n=int(input())
c=-1
for i in range(2,n//2+1):
    for j in range(2,n//2+1):
        if(prime(i) and prime(j) and i!=j):
            if(i*j==n):
                print(i,j)
                c=1
                break
    if(c==1):
        break
if(c!=1):
    print(c)
            
            