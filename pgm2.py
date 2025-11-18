# Find the sum of even valued terms in a Fibonacci series.

n=int(input("Enter lim:"))
a,b=0,1
sum=0
fib=[]
for i in range(n):
    fib.append(a)
    a,b=b,a+b
print(fib)
print('Even numbers in series:',end=' ')
for i in fib:
    if i%2==0:
        print(i,end=' ')
        sum=sum+i

print('Sum:',sum)
