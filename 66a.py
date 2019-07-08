b1=int(input())
e=0
for n in range(2,b1):
 if(b1%n==0):
  e=e+1
if(e<=0):
 print("yes")
else:
 print("no")

