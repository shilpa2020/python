x,y,z=map(int,input().split())
aps=0
for i in range(0,z):
   aps=aps+x
   x=x+y
print(aps)
