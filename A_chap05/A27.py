#A27 Calculate GCD
A,B=map(int,input().split())
C=0
D=0
if A>B:
    C=B
    D=A%B
    while True:
        if D==0:
            X=C
            break
        E=C
        C=D
        D=E%D
else:
    C=A
    D=B%A
    while True:
        if D==0:
            X=C
            break
        E=C
        C=D
        D=E%D

print(X)