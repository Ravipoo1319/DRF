# **************** List comprehension ******************************

my_list = [1,2,3,4,5,6,7,8,9,10]

# create a new list containing only even numbers
new_list = [x for x in my_list if x % 2 == 0]

print("New List ::", new_list)


my_dict = {
    "stud1" : "Ravindra",
    "stud2" : "Ajay",
    "stud3" : "Vishal",
    "stud4" : "Vikas",
    "stud5" : "Rahul",
    "stud6" : "Totaram"
}

new_dict = {k:v for k,v in my_dict.items() if len(v) > 5}

print("New dict ::", new_dict)