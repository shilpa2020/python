a1=int(input())
r=0
for n in range(2,a1):
 if(a1%n==0):
  r=r+1
if(r<=0):
 print("yes")
else:
 print("no")

