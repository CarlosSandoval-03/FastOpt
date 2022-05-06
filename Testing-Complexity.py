from Linked_Structures import *
from time import *

def get_time_add(data_quantity):
    l = []
    a = LinkedQueue()
    b = LinkedStack()
    c = LinkedList()
    d = []
    start = perf_counter()
    for i in range(data_quantity):
        a.enqueue(i)
    end = perf_counter()
    l.append(end-start)
    start = perf_counter()
    for i in range(data_quantity):
        b.push(i)
    end = perf_counter()
    l.append(end-start)
    for i in range(data_quantity):
        c.append(i)
    end = perf_counter()
    l.append(end-start)
    for i in range(data_quantity):
        d.append(i)
    end = perf_counter()
    l.append(end-start)
    del a
    del b
    del c
    del d
    return l


#for i in range(1,2): print(get_time_add(1000*(10**i)))

print(get_time_add(100000))

#1000*(10**i)