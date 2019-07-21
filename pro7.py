farrari1=int(input())
c=0
for r in range(0,farrari1):
  if(pow(2,r)>farrari1):
    break
  c=farrari1-pow(2,r)
print(c)
