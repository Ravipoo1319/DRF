# Deep copy
# If we do any changes to the deep copied nested object that will not be reflected to the orignal object.

from copy import deepcopy

list1 = [1,2,3,[4,5],6]

# Create a deep copy
list2 = deepcopy(list1)

print("INITIAL LIST 2 :",list2)

# It will not make any changes to the orignal one
list2[0] = 10

print("LIST2 :",list2)
print("LIST1 :",list1)

# Does not make changes to the nested object
list2[3].append(100)

print("LIST2 :",list2)
print("LIST1 :",list1)