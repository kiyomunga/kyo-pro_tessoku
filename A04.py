#A04 Binary Representation
N=int(input())
A=[0]*10
for i in range(10):
    A[i]=N%2
    N=N//2
B=A[::-1]
print(*B,sep="")
