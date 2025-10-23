# usr_ip=input("enter numbers separated by spaces:")
# list_num=list(map(int,usr_ip.split()))
list_num=list(map(int,input("enter numbers separated by spaces:").split()))
sum=0
if len(list_num)==0:
    print("EMPTY")
for i in list_num:  #or total=sum(list_num) print(total)
    sum+=i
print("sum =",sum)


