# Lambda is an anynomous function that can accept any number of argument and have
# only one expression. It is frequently used with higher order function.

# sum_of_numbers = lambda a,b : a + b

# print(sum_of_numbers(10,2))
def make_sqr(x):
    return x ** 2
        
my_list = [1,2,3,4,5,6,7,8,9,10]

square = list(map(make_sqr,my_list))

print(square)