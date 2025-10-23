# Write a program to search an item in a given list and display the number of occurrences of the given item. 

def count_occ(lst,item):
    if not len(lst):return 0
    else:return (1 if lst[0]==item else 0)+count_occ(lst[1:],item)
lst=input("Enter space separated items:").split()
item=input("Enter item:")
count=count_occ(lst,item)
print(f"{item} occurs {count} time in the list {lst}")