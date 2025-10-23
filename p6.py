def unique_list(num):
    lis=list(set(num))
    return lis
    
num=list(map(int,(input('enter comma sepp numbers:').split(','))))
print('unique:',unique_list(num))