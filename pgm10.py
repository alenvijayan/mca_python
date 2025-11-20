# Write a function which reverses each item in a list and return the new list.

li=input('Enter , separated strings:').split(',')
new_list=[x[::-1] for x in li]
print(new_list)