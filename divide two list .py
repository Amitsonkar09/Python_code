def divide_in_two(lst):
    mid =len(lst)//2
    return [lst[:mid],lst[mid:]]
list1=[ 4,3,5,2,4,4]
list2=['a','b','c','d','e','f']

list1 = divide_in_two(list1)
list2 = divide_in_two(list2)

print("List 1 divided:",list1)

print("List 2 divided:",list2)

