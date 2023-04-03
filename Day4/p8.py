import threading

def print_hello_three_times():
    for i in range(3):
        print("Hello")
        
def print_hi_three_times():
    for i in range(3):
        print("Hi")
        
t1 = threading.Thread(target=print_hello_three_times)
t2 = threading.Thread(target=print_hi_three_times)
t1.start()
t2.start()

"""
Here t1 and t2 are the threads. This threads are run using start() function. 
t1 and t2 are running concurrently so we will get the random result.
"""