def concat(li):
    if not len(li):
        return ' '
    else:
        return str(li[0])+concat(li[1:])

li=list(map(int,input('enter , sepp num:').split(',')))
print('after concat:',concat(li))