a=input().split()
total1=int(a[0])
coin=int(a[1])
s=input().split()
s=[int(i) for i in s]
s=sorted(s,reverse=True)
tem1=0
count1=0
for i in range(0,len(s)):
  while True:
    if(tem1==coin):
      break
    elif(tem1>coin):
      count1-=1
      tem1-=s[i]
      break
    elif(tem1<coin):
      tem1+=s[i]
      count1+=1
print(count1)
