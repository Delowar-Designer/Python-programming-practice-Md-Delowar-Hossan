#25 Find Execution Time Module in a Python
import time
def somting_print(num):
    start_time=time.time()
    for i in range(num):
        print(i)
    end_time=time.time()
    print(start_time, end_time)
    print(str(end_time - start_time)*1000)

somting_print(1000)