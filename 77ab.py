w1= int(input())
p1 = []
for r in range(1, w1+1):
    if w1 % r == 0:
        p1.append(str(r))
print(' '.join(p1))
