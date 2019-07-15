np1,mp1=map(str,input().split())
s=0
if len(np1)>len(mp1):
	np1,mp1=mp1,np1
v=0
while v<len(np1):
	  s+=(ord(mp1[v])-ord(np1[v]))
	  v+=1
for v in range(v,len(mp1)):
	  s+=ord(mp1[v])-ord('a')+1
print(s)
