#A30 Combination
n,r=map(int,input().split())
def Power(a,b,m):
    p=a
    Answer=1
    for i in range(30):
        wari=2**i
        if (b//wari)%2==1:
            Answer=(Answer*p)%m
        p=(p*p)%m
    return Answer

def Division(a,b,m):
    return (a*Power(b,m-2,m))%m

a=1
for i in range(1,n+1):
    a=(a*i)%1000000007

b=1
for i in range(1,r+1):
    b=(b*i)%1000000007

c=1
for i in range(1,n-r+1):
    c=(c*i)%1000000007

b=(b*c)%1000000007

print(Division(a,b,1000000007))