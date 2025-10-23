def count_occ(lis,item):
    if not len(lis):
        return 0
    else:
        return (1 if lis[0]==item else 0)+count_occ(lis[1:],item)

lis=input('enter , sepp items:').split(',')
item=input('enter item:')
count=count_occ(lis,item)
print(f"{item} occurs {count} time(s) in the list {lis}")