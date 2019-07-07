y = input()
v = 'aeiou'
for n in v:
    if n in y:
        y = ''
        break
    else:
        continue
if y == '':
    print('yes')
else:
    print('no')
