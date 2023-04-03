"""
In single-threded programs, time.sleep() suspends the thread as well as process.
But in mult-threaded programs, time.sleep() suspends only the thread not the whole process.
"""

import threading
import time

def print_hello_three_time():
    for i in range(6):
        time.sleep(0.5)
        print("Hello")
        
def print_hi_three_times():
    for i in range(6):
        time.sleep(1)
        print("Hi")
        
        
t1 = threading.Thread(target=print_hello_three_time)
t2 = threading.Thread(target=print_hi_three_times)

t1.start()
t2.start()