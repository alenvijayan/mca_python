n=int(input('enter limit:'))
fibo=[]
a,b=0,1
for i in range(n):
    fibo.append(a)
    a,b=b,a+b
print('series:',fibo)
print(f"{n}th fibonacci number is",fibo[-1])