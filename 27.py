def is_number(r):
    try:
        float(r)
        print("Yes")
    except:
        print("No")
r=input()
is_number(r)
