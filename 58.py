a,b=map(int,input().split())
c=list(map(int,input().split()[:a]))
for n in range(0,a):
    if c[n]==b:
        print("yes")
        break
else:
    print("no")
