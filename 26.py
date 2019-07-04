v=int(input())
a=list(map(int,input().split()[:v]))
a.sort()
for p in a:
  print(p,end=" ")
