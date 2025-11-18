# Check whether a given positive integer is power of 2. Raise exception for negative input.
def is_pow_two(n):
    if n<=0:
        raise ValueError("Input must be a positive integer")
    while n%2==0:
        n=n//2
    return n
try:
    n=int(input('enter a number:'))
    res=is_pow_two(n)
    if res==1:
        print(f'{n} is a power of 2')
    else:
        print(f'{n} is not a power of 2')
except ValueError as e:
    print('Error:',e)


