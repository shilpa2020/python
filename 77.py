w= int(input())
p = []
for r in range(1, w+1):
    if w % r == 0:
        p.append(str(r))
print(' '.join(p))
