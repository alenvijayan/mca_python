def sum_lis(lis):
    if not len(lis):
        return 0
    else:
        return lis[0]+sum_lis(lis[1:])

lis=list(map(int,input('enter list:').split(',')))
print('sum:',sum_lis(lis))