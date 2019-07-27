count1=int(input())
arr=[]
ss1=[]
for i in range(count1):
    arr.append(list(map(int,input().split())))
for llist in arr:
    for num in llist:
        ss1.append(num)
ss1.sort()
for i in ss1:
    print(i,end=' ')
