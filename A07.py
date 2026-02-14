#A07 Event Attendance
D=int(input())
N=int(input())
L=[0]*N
R=[0]*N
for i in range(N):
    L[i],R[i]=map(int,input().split())
S=[0]*(D+1)
for i in range(N):
    S[L[i]-1]=S[L[i]-1]+1
    S[R[i]]=S[R[i]]-1
Answer=[0]*(D+1)
for i in range(D):
    Answer[i+1]=Answer[i]+S[i]
for i in range(1,D+1):
    print(Answer[i])