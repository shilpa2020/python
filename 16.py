a1,a2=map(int,input().split())
for a3 in range(a1,a2):
  if a3>1:
    for i in range(2,a3):
      if(a3%i)==0:
        break
    else:
      print(a3,end="")
