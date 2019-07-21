a21=int(input())
b21=list(map(int,input().split()))
c12=0
for m1 in range(0,a21):
    for p1 in range(0,m1):
        if b21[p1]<b21[m1]:
            c12=c12+b21[p1]
print(c12)
