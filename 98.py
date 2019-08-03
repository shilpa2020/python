intg1=int(input())
n=list(map(int,input().split()))
for i in range(len(n)-1):
   if(n[i]>n[i+1]):
      print(i)
