v=input()
k=[]
for r in v:
	if r.isnumeric():
		k.append(r)
print(''.join(k))
