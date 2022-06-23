#no_threading.py
import time
import threading
# Ordered code
start = time.perf_counter()

def do_something():
    print("sleeeping 1 second")
    time.sleep(1)
    print("done sleeping")

do_something()
do_something()
finish = time.perf_counter()
print(f"finished in {round(finish-start,2)} seconds")
print("="*50)
#sleeeping 1 second
#done sleeping
#sleeeping 1 second
#done sleeping
#finished in 2.0 seconds
#==================================================


#threading_start.py
#Using threading
import time
import threading
# Ordered code
start = time.perf_counter()

def do_something():
    print("sleeeping 1 second")
    time.sleep(1)
    print("done sleeping")

# Just passing the function, not executing because not passing with paranthesis ()
start = time.perf_counter()
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)
# Run threads
t1.start()
t2.start()

finish = time.perf_counter()
print(f"finished in {round(finish-start,2)} seconds")
print("="*50)
#sleeeping 1 second
#sleeeping 1 second
#finished in 0.0 seconds
#==================================================
#done sleeping
#done sleeping


#start_and_join.py
# Using start and join
import time
import threading

def do_something():
    print("sleeeping 1 second")
    time.sleep(1)
    print("done sleeping")

# Just passing the function, not executing because not passing with paranthesis ()
start = time.perf_counter()
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)
# Run threads
t1.start()
t2.start()
# Complete before calculating the next code
t1.join()
t2.join()

finish = time.perf_counter()
print(f"finished in {round(finish-start,2)} seconds")
print("="*50)
#sleeeping 1 second
#sleeeping 1 second
#done sleeping
#done sleeping
#finished in 1.0 seconds
#==================================================


#loop_over_threading.py
import time
import threading

def do_something():
    print("sleeeping 1 second")
    time.sleep(1)
    print("done sleeping")

# Create and start these threads in loops,1.01 second instead of 10 seconds
start = time.perf_counter()
threads = []
for _ in range(4):
    t = threading.Thread(target=do_something)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()
print(f"finished in {round(finish-start,2)} seconds")
print("="*50)
#sleeeping 1 second
#sleeeping 1 second
#sleeeping 1 second
#sleeeping 1 second
#done sleeping
#done sleeping
#done sleeping
#done sleeping
#finished in 1.0 seconds
#==================================================


#loop_with_arguments_threading.py
import time
import threading

def do_something(seconds):
    print(f"sleeeping {seconds} second(s)")
    time.sleep(seconds)
    print("done sleeping")

start = time.perf_counter()
threads = []
for _ in range(4):
    t = threading.Thread(target=do_something,args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()
print(f"finished in {round(finish-start,2)} seconds")
print("="*50)
#sleeeping 1.5 second(s)
#sleeeping 1.5 second(s)
#sleeeping 1.5 second(s)
#sleeeping 1.5 second(s)
#done sleeping
#done sleeping
#done sleeping
#done sleeping
#finished in 1.5 seconds
#==================================================


#thread_pool_executor.py
import concurrent.futures
import time

start = time.perf_counter()
def do_something(seconds):
    print(f"sleeeping {seconds} second(s)")
    time.sleep(seconds)
    return f"done sleeping ... {seconds}"

with concurrent.futures.ThreadPoolExecutor() as executor:
    # submit method to run once at a time
    f1 = executor.submit(do_something,1)
    f2 = executor.submit(do_something,1)
    print(f1.result())
    print(f2.result())

finish = time.perf_counter()
print(f"finished in {round(finish-start,2)} seconds")
print("="*50)
#sleeeping 1 second(s)
#sleeeping 1 second(s)
#done sleeping ... 1
#done sleeping ... 1
#finished in 1.0 seconds
#==================================================

#loop_ThreadPoolExecutor.py
## Loop over ThreadPoolExecutor, results aren't in order.
import concurrent.futures
import time

def do_something(seconds):
    print(f"sleeeping {seconds} second(s)")
    time.sleep(seconds)
    return f"done sleeping ... {seconds}"

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = [executor.submit(do_something,sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()
print(f"finished in {round(finish-start,2)} seconds")
print("="*50)
#sleeeping 5 second(s)
#sleeeping 4 second(s)
#sleeeping 3 second(s)
#sleeeping 2 second(s)
#sleeeping 1 second(s)
#done sleeping ... 1
#done sleeping ... 2
#done sleeping ... 3
#done sleeping ... 4
#done sleeping ... 5
#finished in 5.01 seconds

#wait_until_done.py
import concurrent.futures
import time

def do_something(seconds):
    print(f"sleeeping {seconds} second(s)")
    time.sleep(seconds)
    return f"done sleeping ... {seconds}"

## map method, results are in order
# it still waits until it is done.
start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = executor.map(do_something,secs)

finish = time.perf_counter()
print(f"finished in {round(finish-start,2)} seconds")
print("="*50)
#sleeeping 5 second(s)
#sleeeping 4 second(s)
#sleeeping 3 second(s)
#sleeeping 2 second(s)
#sleeeping 1 second(s)
#finished in 5.01 seconds
#==================================================