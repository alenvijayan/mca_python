# Write a program to print all even numbers from a given list in the given order until you reach number 237 or end of the list. 
def check_even(num):
    ev=[]
    for x in num:
        if x==237:
            break
        else:
            if not x%2:
                ev.append(x)
    return ev
num=list(map(int,input('Enter , sepp numbers').split(',')))
print('even nums:',check_even(num))