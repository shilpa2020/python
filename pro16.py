app1=int(input())
cadt1=list(map(int,input().split()))
xawt1=[1]*app1
for r in range(app1):
    if r==0:
        if cadt1[r]>cadt1[r+1]:
            xawt1[r]=xawt1[r]+xawt1[r+1]
    elif r>0:
        if cadt1[r]>cadt1[r-1]:
            xawt1[r]=xawt1[r]+xawt1[r-1]
print(sum(xawt1))
