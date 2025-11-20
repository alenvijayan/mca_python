# Print Armstrong numbers in the range (100,500)?
# for i in range(100,501):
#     temp = i
#     sum = 0

#     while temp > 0:
#         digit = temp % 10         
#         sum += digit ** 3         
#         temp //= 10               

#     if sum == i:
#         print(i)


n=int(input('enter a number:'))
l=len(str(n))
temp=n
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**l
    temp//=10
if sum==n:
    print(f'{n} is armstrong')
else:
    print(f'{n} is not armstrong')