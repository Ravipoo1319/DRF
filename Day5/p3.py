# generate a sequence of numbers

def my_gen(n):
    val = 0
    
    while val < n:
        yield val
        val += 1
        
res = my_gen(4)
print(res)

for val in res:
    print(val)