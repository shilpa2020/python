b1,sent1 = input().split()
sent1 = int(sent1)
fake1 = False
bent1 = list(map(int,input().split()))
for r in range(len(bent1)):
    for l in range(len(bent1)):
        if bent1[r]+bent1[l] == sent1:
            fake1 = True
print("yes" if fake1 else "no") 
