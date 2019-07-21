import math
p1,q1=map(int,input().split())
r=[]
s=list(map(int,input().split()))
for d in range(0,q1):
        a,b=map(int,input().split())
        r.append([a,b])
for d in r:
        x1=d[0]-1
        y1=d[1]-1
        print(math.gcd(s[x1],s[y1]))
