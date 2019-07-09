p=int(input())
fac=0
for r in range(1,p):
  if p%r==0:
    fac=r
if fac>1:
  print('yes')
#elif p==1:
 # print 'The number 1 is neither prime nor composite!'
else:
  print('no')
