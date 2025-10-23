n=int(input('enter number:'))
fib_series=[]
a,b=0,1
for i in range(n):
    fib_series.append(a)
    a,b=b,a+b
print('series:',fib_series)
print(f"the {n}th fibo number is ",fib_series[-1])