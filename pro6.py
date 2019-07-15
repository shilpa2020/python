l=int(input())
lis1=[]
lis=list(map(int,input().split()))
for v in range(len(lis)):
    for r in range(v+1,len(lis)):
        for k in range(r+1,len(lis)):
            if (lis[v]< lis[r] and lis[r]<lis[k])and (v<r and j<k):
                a=[lis[k],lis[r],lis[v]]
                if l in lis1:
                    continue
                else:
                    lis1.append(l)
print(len(lis1))
