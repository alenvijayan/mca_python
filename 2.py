# s1=input('enter 1:')
# s2=input('enter 2:')
# print(s2[0]+s1[1:]+" "+s1[0]+s2[1:])

s=[x.strip() for x in input("enter comma sepp colors:").split(',')]
print(s[::2])