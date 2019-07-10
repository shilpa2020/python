c,d=map(int,input().split())
if(c>d):
  g=c
else:
  g=d
while(True):
  if((g%c) == 0 and (g%d) == 0):
    lcm=g
    break
  g=g+1
print(lcm)
