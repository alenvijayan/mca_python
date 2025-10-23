def conc(numbers):
    if not len(numbers):
        return " "
    else:
        return str(numbers[0])+conc(numbers[1:])

numbers=list(map(int,input('enter single digit comma sepp numbers:').split(',')))
print('after cocat:',conc(numbers))