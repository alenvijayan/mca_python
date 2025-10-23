num=input("enter , sepp numbers: ").split(',')
num_list=list(map(int,num))
print([x for x in num_list if not x%2])