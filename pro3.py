s1,s2=input().split()
c=abs(len(s2)-len(s1))
for g in range(len(s1)):
    if(len(s2)==1 and s2[g] in s1):
        break
    if (s1[g]!=s2[g]):
        c=c+1
print(c)
