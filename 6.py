def unq(lis):
    return list(set(lis))

lis=list(map(int,input('enter comma sepp numbers:').split(',')))
print('unique elements:',unq(lis))