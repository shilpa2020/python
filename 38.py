p,q=map(int,input("").split())
p=p ^ q
q=p ^ q
p=q ^ p
print(p,q)
