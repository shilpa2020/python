x=input()
for r in range(0,len(x)):
    
    if (x[r].isalpha() and x[r].isnumeric()):
        print("No")
else:
        print("Yes")
