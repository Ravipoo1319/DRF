# Print sequence of numbers from 0 to n-1
def my_gen(n):
    val = 0
    
    while val < n:
        yield val
        
        val += 1


for val in my_gen(4):
    print(val)