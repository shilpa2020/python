p=int(input())
q=list(map(int,input().split()))
q.sort()
print(q[0],q[p-1])
