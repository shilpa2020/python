aa1,bb2=map(int,input().split())
cc3=aa1*bb2
for r in range(0,cc3+1):
 if(r**2==0):
  print("yes")
  break
else:
  print("no")
