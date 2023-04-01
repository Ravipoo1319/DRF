# Shallow copy
# inorder to make copies of an object, we need to use copy module.
# There are two ways to create copy of an object. Shallow copy and deep copy.
# Shallow copy does not create copies of nested object, it only copy the refernce of the nested object.
# That means if we do any changes to the shallow copied nested object that will be reflected to the orignal object.

from copy import copy

list1 = [1,2,3,[4,5],6,7]

#  create shallow copy of list1
list2 = copy(list1)
print("Initial LIST 2", list2)

#  This change does not reflect to the orignal one
list2[0] = 90

print(list2)
print(list1)

# This make modified to the orignal one
list2[3].append(100)

print("LIST 2 :",list2)
print("LIST 1 :",list1)

list2[3].pop()

print("LIST 2 :",list2)
print("LIST 1 :",list1)
