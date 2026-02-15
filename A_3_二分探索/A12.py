#A12 Printer
N,K=map(int,input().split())
A=list(map(int,input().split()))
L=1
R=1000000000
while L<R:
    P=0
    M=(L+R)//2
    for i in range(N):
            P=P+M//A[i]
    if P>=K:
          R=M
    else:
          L=M+1
print(L)