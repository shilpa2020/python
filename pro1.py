def longest(str1,str2):
        if(str1 in str2):
            return str1
        else:
            return longest(str1[0:len(str1)-1],str2)
i = int(input())
a= []
for _ in range(0,i):
    a.append(input())
a.sort()
print(longest(a[0],a[i-1]))
