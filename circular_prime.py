def prime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    else:
        return True
n=int(input())
t=n
rev=0
while(t!=0):
    r=t%10
    rev=rev*10+r
    t=t//10
if(prime(n) and prime(rev)):
    print("circular prime")
elif(prime(n) or prime(rev)):
    print("prime but not a circular prime")
else:
    print("not prime")