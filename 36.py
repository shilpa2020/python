c=input()
cou=0
for i in range(len(c)):
  if(c[i].isdigit() or c[i].isalpha() or c[i]==(" ")):
    continue
  else:
    cou+=1
print(cou)
