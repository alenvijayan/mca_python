num=int(input('enter number:'))
factors=[]
for i in range(1,num+1):
    if not num%i:
        factors.append(i)
print('factors of ',num,'=',factors)