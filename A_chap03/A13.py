#A13 Close Pairs
N,K=map(int,input().split())
A=list(map(int,input().split()))
count=0
for i in range(N):
    L=i
    R=N-1
    while L<R+1:
        M=(L+R)//2
        if A[M]-A[i]>K:
            R=M-1
        else:
            L=M+1
    count+=R-i
print(count)