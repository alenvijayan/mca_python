num=list(map(int,input('enter space sepp numbers:').split()))
num_list=[x for x in num if x>100]
print('nums >100:',num_list if num_list else 'none')