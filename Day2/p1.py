my_list = [1,2,3,4,5]

# create iterator object
iter_obj = iter(my_list)

print(next(iter_obj)) # 1

print(next(iter_obj)) # 2

print(next(iter_obj)) # 3

print(next(iter_obj)) # 4

print(next(iter_obj)) # 5

# once we reach at the end that means if there is no more item to iterate
# it will raise a StopIteration exception.

print(next(iter_obj)) # raise an StopIteration exception