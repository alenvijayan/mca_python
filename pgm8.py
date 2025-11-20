# Compare two lists entered by user?

def compare_lists(a, b):
    return {
        "equal": a == b,
        "same_items_ignore_order": sorted(a) == sorted(b),
        "only_in_a": list(set(a) - set(b)),
        "only_in_b": list(set(b) - set(a)),
        "in_both": list(set(a) & set(b)),
    }

list1 = input("Enter list 1: ").split(",")
list2 = input("Enter list 2: ").split(",")

print(compare_lists(list1, list2))
