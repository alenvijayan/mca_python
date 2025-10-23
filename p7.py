# list1=input('enter list 1 sepp by comma:').split(',')
# list2=input('enter list 2 sepp by comma:').split(',')
# print('equal'if list1==list2 else 'not equal')
# common=set(list1)&set(list2)

# print('common:',list(common) if common else 'none')


#or  ((to make the op list sorted))

list1=input('enter list 1 sepp by comma:').split(',')
list2=input('enter list 2 sepp by comma:').split(',')
print('equal'if list1==list2 else 'not equal')
common=set(list1)&set(list2)
com_list=list(common)
com_list.sort()
print('common:',com_list if com_list else 'none')