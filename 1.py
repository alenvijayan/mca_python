# s=input("enter string:")
# print(s[0]+s[1:].replace(s[0],'$'))

s=input('enter string:')
print(s[-1]+s[1:-1]+s[0] if len(s)>2 else 'cannot')