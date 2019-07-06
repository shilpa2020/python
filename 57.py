n,r=map(int,input().split())
s=list(map(int,input().split()[:n]))
count=0
for j in range(0,n):
    if(s[j]==r):
        count=count+1
print(count)
