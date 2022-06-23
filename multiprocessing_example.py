#no_multiprocessing.py
import multiprocessing
import time


def do_something():
    print("Sleeping 1 second ...")
    time.sleep(1)
    print("Done sleeping")

# start = time.perf_counter()

# do_something()
# do_something()
# finish = time.perf_counter()
# print(f"Finished in {round(finish - start, 2)} seconds")

#mp_with_start.py
import multiprocessing
import time
def do_something():
    print("Sleeping 1 second ...")
    time.sleep(1)
    print("Done sleeping")

start = time.perf_counter()

p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

p1.start()
p2.start()

finish = time.perf_counter()
print(f"Finished in {round(finish - start, 2)} seconds")
# Finished in 0.01 seconds
# Sleeping 1 second ...
# Sleeping 1 second ...
# Done sleeping
# Done sleeping

#mp_start_join.py
# Basic operation with start and join. 
import multiprocessing
import time

def do_something():
    print("Sleeping 1 second ...")
    time.sleep(1)
    print("Done sleeping")

start = time.perf_counter()

p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

p1.start()
p2.start()
p1.join()
p2.join()

finish = time.perf_counter()
print(f"Finished in {round(finish - start, 2)} seconds")
# Sleeping 1 second ...
# Sleeping 1 second ...
# Done sleeping
# Done sleeping
# Finished in 1.01 seconds

#looped_mp_4_times.py
import time
import multiprocessing

# Create 5 processes via loops, we can't run p.join() in loop, it would wait
def do_something():
    print("Sleeping 1 second ...")
    time.sleep(1)
    print("Done sleeping")

start = time.perf_counter()
processes = []
for _ in range(4):
    p = multiprocessing.Process(target=do_something)
    p.start()
    processes.append(p)

for process in processes:
    process.join()

finish = time.perf_counter()
print(f"Finished in {round(finish - start, 2)} seconds")
#Sleeping 1 second ...
#Sleeping 1 second ...
#Sleeping 1 second ...
#Sleeping 1 second ...
#Done sleeping
#Done sleeping
#Done sleeping
#Done sleeping
#Finished in 1.01 seconds

#pass_arg_to_mp.py
import time
import multiprocessing

# # Pass an argument to our functions; 1.5 seconds for 4 processes,
def do_something(seconds):
    print(f"Sleeping {seconds} second ...")
    time.sleep(seconds)
    print("Done sleeping")

start = time.perf_counter()
processes = []
for _ in range(4):

    p = multiprocessing.Process(target=do_something,args=[1.5])
    p.start()
    processes.append(p)

for process in processes:
    process.join()

finish = time.perf_counter()
print(f"Finished in {round(finish - start, 2)} seconds")
#Sleeping 1.5 second ...
#Sleeping 1.5 second ...
#Sleeping 1.5 second ...
#Sleeping 1.5 second ...
#Done sleeping
#Done sleeping
#Done sleeping
#Done sleeping
#Finished in 1.51 seconds

#submit_mp.py
import time
import concurrent.futures

# Pass an argument to our functions
def do_something(seconds):
    print(f"Sleeping {seconds} second ...")
    time.sleep(seconds)
    return "Done sleeping..."

start = time.perf_counter()
with concurrent.futures.ProcessPoolExecutor() as executor:
    # submit method to access a method once upon a time
    f1 = executor.submit(do_something,1)
    print(f1.result())

finish = time.perf_counter()
print(f"Finished in {round(finish - start, 2)} seconds")
#Sleeping 1 second ...
#Done sleeping...
#Finished in 1.03 seconds

#list_comprehension_submit_mp.py
import time
import concurrent.futures
from unittest import result

# Pass an argument to our functions
def do_something(seconds):
    print(f"Sleeping {seconds} second ...")
    time.sleep(seconds)
    return "Done sleeping..."

start = time.perf_counter()
with concurrent.futures.ProcessPoolExecutor() as executor:
    # submit method to access a method once upon a time
    results = [executor.submit(do_something,1) for _ in range(4) ]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()
print(f"Finished in {round(finish - start, 2)} seconds")
#Sleeping 1 second ...
#Sleeping 1 second ...
#Sleeping 1 second ...
#Sleeping 1 second ...
#Done sleeping...
#Done sleeping...
#Done sleeping...
#Done sleeping...
#Finished in 1.04 seconds


#list_comp_argument_pass.py
import time
import concurrent.futures

# Pass an argument to our functions
def do_something(seconds):
    print(f"Sleeping {seconds} second ...")
    time.sleep(seconds)
    return f"Done sleeping...{seconds}"

start = time.perf_counter()
with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = [executor.submit(do_something,_) for _ in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()
print(f"Finished in {round(finish - start, 2)} seconds")
#Sleeping 5 second ...
#Sleeping 4 second ...
#Sleeping 3 second ...
#Sleeping 2 second ...
#Sleeping 1 second ...
#Done sleeping...1
#Done sleeping...2
#Done sleeping...3
#Done sleeping...4
#Done sleeping...5
#Finished in 5.02 seconds