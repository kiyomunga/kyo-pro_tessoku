#A29 Power
a,b=map(int,input().split())
A=a
L=[0]*(b+1)


while True: 
    for i in range(1,b):
        a=a*A
        if a>=1000000007:
            a=a%1000000007
        if a in L:
            count=i-L.index(a)
            x=b%count
            print(L[x])
            break
        L[i]=a
    if a<1000000007:
       print(a)
       break

