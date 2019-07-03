p=int(input())
temp=p
r=0
while(p>0):
  dig=p%10
  r=r*10+dig
  p=p//10
if(temp==r):
  print("yes")
else:
  print("no")
  
