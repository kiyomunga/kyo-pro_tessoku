#A11 Binary Serch
N,X=map(int,input().split())
A=list(map(int,input().split()))
L=0
R=N-1
while 0<1:
    mid=(L+R)//2
    if X>A[mid]:
        L=mid+1
    elif X<A[mid]:
        R=mid-1
    else:
        print(mid+1)
        break