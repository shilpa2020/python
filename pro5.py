a_3, b_3, c_3 = map(int,input().split())
if a_3 == 224:
  print("YES")
elif(a_3%(b_3+c_3) == 0):
  print("YES")
else:
  print("NO")
