#A26 Prime Check
Q=int(input())
X=[0]*Q
for i in range(Q):
    X[i]=int(input())
Answer=[0]*Q

for i in range(Q):
    Lim=int(X[i]**0.5)

for i in range(Q):
    if Answer[i]==0:
        print("Yes")
    else:
        print("No")