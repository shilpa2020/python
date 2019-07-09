strg1=list(input())
if len(strg1)%2==0:
    strg1[int(len(strg1)/2)] ='*'
    strg1[int(len(strg1)/2)-1]='*'
else:
    strg1[int(len(strg1)/2)] ='*'
for i in range(0,len(strg1)):
    print(strg1[i],end='')
