a = int(input())
if a>2:
    for r in range(2,a):
        if a%r == 0:
            print('no')
            break
    else:
        print('yes')
elif a==2:
    print('yes')
else:
    print('no')
