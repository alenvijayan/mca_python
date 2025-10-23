def reverse_name(name):
    if not len(name):
        return ' '
    else:
        return name[-1]+reverse_name(name[:-1])


name=input('enter name:')
print('reverse:',reverse_name(name))