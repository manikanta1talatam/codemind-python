def prime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    else:
        return True
def prime_palindrome(n):
    t=n+1
    while(1):
        s=t
        rev=0
        while(s!=0):
            r=s%10
            rev=rev*10+r
            s=s//10
        if(rev==t and prime(rev)):
            m=rev
            break
        else:
            t=t+1
    return m
n=int(input())
f=prime_palindrome(n)
print(f)