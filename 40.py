c=int(input())
fabt,fabot=0,1
print(fabot,end=" ")
for r in range(1,c):
  faboot=fabt+fabot
  print(faboot,end=" ")
  fabt,fabot=fabot,faboot
