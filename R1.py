# Accept full name and display in reverse order with space between the words.
# def rev_name(s):
#     if not len(s):return ''
#     else:return s[-1]+rev_name(s[:-1])
# s=input("enter name:")
# print(rev_name(s))


# def rev_words(s):
#     if not len(s):return ''
#     elif len(s)==1:return s[0]
#     else:return rev_words(s[1:])+" "+s[0]
# s=input("enter full name:").split()
# print(rev_words(s))


def rev(s):
    if not len(s):return ''
    elif len(s)==1:return s[0][::-1]
    else:return rev(s[1:])+" "+s[0][::-1]
s=input("enter full name:").split()
print(rev(s))