num_list=list(map(int,input('enter comma space numbers').split()))
#print(sum(num_list))
sum=0
for i in num_list:
    sum+=i
print('sum of elements:',sum)