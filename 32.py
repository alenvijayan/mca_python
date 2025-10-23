# To increment a list of integers by 10% if the number is greater than 1000 else by 5%.
inc=lambda num:[x+(x*0.1) if x>1000 else x+(x*0.05) for x in num]
num=list(map(int,input('Enter , sep integers:').split(',')))
print('After inc:',inc(num))