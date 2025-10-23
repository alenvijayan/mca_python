# Write a function to get a new string from a given string by adding ‘Is’ to the beginning of the input string. If the given string already begins with ‘Is’, return the input string unchanged.
def res(s):
    return (s if s.startswith('Is') else 'Is'+s)
s=input('enter string:')
print(res(s))