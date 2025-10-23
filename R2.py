# Accept a list of single digit numbers as input string. Concatenate the elements of the list as a single number.

def concat_num(nums):
    if not len(nums):return ''
    else:return str(nums[0])+concat_num(nums[1:])

l=input("Enter space separated numbers: ")
nums=list(map(int,l.split()))
print("After concatenation: ",concat_num(nums))

