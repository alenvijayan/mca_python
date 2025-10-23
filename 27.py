# Write a program that counts odd and even numbers in a given list.
def check(num):
    even=odd=0
    for i in num:
        if not i%2:
            even+=1
        else:
            odd+=1
    return even,odd

num=list(map(int,input('enter , sep numbers:').split(',')))
even,odd=check(num)
print('even nums=%d,odd nums=%d'%(even,odd))