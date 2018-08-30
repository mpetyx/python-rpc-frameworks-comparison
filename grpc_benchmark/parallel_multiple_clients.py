__author__ = 'mpetyx (Michael Petychakis)'
__version__ = "1.0.0"
__maintainer__ = "Michael Petychakis"
__email__ = "hello@apilama.com"
__status__ = "Production"

from client import Client

import threading
from random import randint
from time import sleep


# def print_number(number):
#     # Sleeps a random 1 to 10 seconds
#     rand_int_var = randint(1, 10)
#     sleep(rand_int_var)
#     print "Thread " + str(number) + " slept for " + str(rand_int_var) + " seconds"

thread_list = []

for i in range(1, 100000):
    # Instantiates the thread
    # (i) does not make a sequence, so (i,)
    t = threading.Thread(target=Client().squareRoot, args=(i,))
    # Sticks the thread in a list so that it remains accessible
    thread_list.append(t)

# Starts threads
for thread in thread_list:
    thread.start()

# This blocks the calling thread until the thread whose join() method is called is terminated.
# From http://docs.python.org/2/library/threading.html#thread-objects
for thread in thread_list:
    thread.join()

# Demonstrates that the main process waited for threads to complete
print("Done")