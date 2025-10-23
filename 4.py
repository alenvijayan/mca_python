c2=list(map(int,input('enter coma sep numbers:').split(',')))
c1=list(map(int,input('enter coma sep numbers:').split(',')))
print('same lenghth' if len(c2)==len(c1) else 'not same')

print('sum is same' if sum(c1)==sum(c2) else 'not same')

print('value occur in both:',[x for x in c1 if x in c2])