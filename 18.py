p1,p2=map(int,input().split())
for s in range(p1+1,p2):
  sum=0
  tem=s
  while tem>0:
    dig=tem%10
    sum+=dig**3
    tem//=10
  if s==sum:
    print(s,end=' ')
