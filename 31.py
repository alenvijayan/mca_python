# To remove all strings with length < 5 from a list of strings
string_removal=lambda strings:[s for s in strings if len(s)>5]

strings=input('enter space sep strings:').split()
print('After removal:',string_removal(strings))