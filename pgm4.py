# Arrange characters in a string such that lowercase letters must come first.
s=input('Enter string with lower and upper characters:')
lower=''
upper=''
for ch in s:
    if ch.islower():
        lower+=ch
    else:
        upper+=ch
print(lower+upper)