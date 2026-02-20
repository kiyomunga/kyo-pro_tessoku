#A28 Blackboard
N=int(input())
X=0
T=[None]*N
A=[None]*N
for i in range(N):
    T[i],A[i]=input().split()
    A[i]=int(A[i])

for i in range(N):
    if T[i]=="+":
        X=X+A[i]
    elif T[i]=="-":
        X=max(X-A[i],0)
    else:
        X=X*A[i]
    X=X%10000
    print(X)
    X=X+10000