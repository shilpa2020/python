a,intg1=input().strip().split(" ")
intg1=int(intg1)
i=0;
while i<len(a)-1 and intg1:
	if(a[i]>a[i+1]):
		intg1-=1
		a=a[:i]+a[i+1:]
		if(i!=0):
			i-=1
	else:
		i+=1
s=a[:len(a)-intg1]
print(s)
