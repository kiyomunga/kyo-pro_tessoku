#A05 Three Cards
N,K=map(int,input().split())
count=0
for x in range(1,N+1):
    for y in range(1,N+1):
        if 0<K-(x+y)<N+1:
            count=count+1
print(count)