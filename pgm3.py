# Given a string of odd length greater than 7, return a new string made of the middle three characters of a given String
try:
    s=input('enter string of odd lenght greater than 7:')
    l=len(s)
    if l<=7 or not l%2:
        raise ValueError('enter string of odd lenght greater than 7')

    print(s[(l//2)-1:(l//2)+2])

except ValueError as e:
    print('Error:',e)