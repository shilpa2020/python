la=input()
ya=map(int,input().split())
pa=[]
for r in ya:
    enum=bin(r)
    pa.append(enum)
fraud=sorted(pa)
fraud.reverse()
for h in fraud:
    print(int(h,2))
