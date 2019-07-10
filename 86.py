strg1=list(input())
elist=[]
for r in strg1:
   if r not in elist:
      elist.append(r)
if strg1==elist:
   print("Yes")
else:
   print("No")
