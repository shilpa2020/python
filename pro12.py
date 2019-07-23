a1,b1=map(int,input().split())
ls=list(map(int,input().split()))
y=[]
for r in range(0,b1):
     u21,v21=map(int,input().split())
     y.append([u21,v21])
for r in range(b1):
     lower=y[r][0]
     upper=y[r][1]
     s=sum(ls[lower-1:upper])
     print(s)
