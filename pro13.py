n1,q1=map(int,input().split())
l=list(map(int,input().split()))
list=[]
lr=[]
for s in range(q1):
    list=input().split()
    lr.append(min(l[int(list[0])-1:int(list[1])]))
for s in lr:
    print(s,end='\n')
