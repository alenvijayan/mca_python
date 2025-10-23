def rev_name(s):
    if not len(s):
        return ' '
    else:
        return s[-1]+rev_name(s[:-1])
s=input('enter name:')
print("rev_name:",rev_name(s))