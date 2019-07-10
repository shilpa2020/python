s1,s2=map(int,input().split())
m=1
while(m<=s1 and m<=s2):
 if(s1%m==0 and s2%m==0):
  g=m
 m=m+1
print(g)
