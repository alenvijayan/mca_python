def count_occ(l,i):
    if not len(l):
        return 0
    else:
        return (1 if l[0]==item else 0)+count_occ(l[1:],item)

lst=input('enter coma sepp list:').split(',')
item=input('enter item:')
count=count_occ(lst,item)
print(f"{item} appers {count} times in the list")