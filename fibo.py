n=int(input("enter limit:"))
a,b=0,1

for i in range(n):
    print(a,end=' ')
    a,b=b,a+b
print('\n',n,"th element:",a)