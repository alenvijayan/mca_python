# Write a program to remove all odd indexed characters from a given string.
def odd_rem(s):
    result=''
    for i in range(len(s)):
        if i%2==0:
            result+=s[i]
    return result
        
s=input('enter string:')
print('After removal:',odd_rem(s))