n1=int(input())
if(n1>1):
  for i in range(2,n1//2):
      if(n1%i)==0:
          print("no")
          break
  else:
       print("yes")
else:
    print("no")
