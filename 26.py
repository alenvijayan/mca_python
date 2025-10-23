# Write a program that count the number of strings where string length is 2 or more and the first and last characters are same.
def cnt(strings):
    result1=[x for x in strings if len(x)>=2]
    result2=[x for x in result1 if x[0]==x[-1]]
    return result2

strings=input("enter space sep strings:").split()
print('result:',len(cnt(strings)))