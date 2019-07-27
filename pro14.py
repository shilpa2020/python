chat1,chet2=map(int,input().split())
law=list(map(int,input().split()))
chat1=[]
law.insert(0,0)
for r in range(chet2):
     vim=[]
     sha=0
     but,zee=map(int,input().split())
     for i in range(but,zee+1):         
         sha^=law[i]     
     chat1.append(sha)
for r in chat1:
     print(r)
