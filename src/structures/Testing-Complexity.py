from Linked_Structures import *
from Structures import *
from time import *

queue = Queue()
stack = Stack()
linkedQueue = LinkedQueue()
linkedStack = LinkedStack()
linkedList = LinkedList()
OrdinaryList = []

time_adding_lists = []

# Comparacion Listas - Ordinaria y linkeada


def compare_list_add(n):
    time_lists = []
    time_lists.append(n)
    start = perf_counter()
    for i in range(n):
        OrdinaryList.append(i)
    end = perf_counter()
    time_lists.append(end-start)
    start = perf_counter()
    for i in range(n):
        linkedList.append(i)
    end = perf_counter()
    time_lists.append(end-start)
    return time_lists


def compare_list_remove_last(n):
    time_lists = []
    time_lists.append(n)
    for i in range(n):
        OrdinaryList.append(i)
        linkedList.append(i)
    start = perf_counter()
    for i in range(n):
        OrdinaryList.pop()
    end = perf_counter()
    time_lists.append(end-start)
    start = perf_counter()
    for i in range(n):
        linkedList.pop()
    end = perf_counter()
    time_lists.append(end-start)
    return time_lists


def mid(n):
    if n % 2 == 0:
        return n/2
    else:
        return ((n-1)/2)+1


def compare_list_accessmidelement(n):
    time_lists = []
    time_lists.append(n)
    for i in range(n):
        OrdinaryList.append(i)
        linkedList.append(i)
    midposition = int(mid(n))
    start = perf_counter()
    k = OrdinaryList[midposition]
    end = perf_counter()
    time_lists.append(end-start)
    start = perf_counter()
    k = linkedList.get_index(midposition)
    end = perf_counter()
    time_lists.append(end-start)
    return time_lists

# Comparacion Pilas Enlazado y ordinaria


def compare_stack_push(n):
    time_lists = []
    time_lists.append(n)
    start = perf_counter()
    for i in range(n):
        stack.push(i)
    end = perf_counter()
    time_lists.append(end-start)
    start = perf_counter()
    for i in range(n):
        linkedStack.push(i)
    end = perf_counter()
    time_lists.append(end-start)
    return time_lists


def compare_stack_pop(n):
    time_lists = []
    time_lists.append(n)
    for i in range(n):
        stack.push(i)
        linkedStack.push(i)
    start = perf_counter()
    for i in range(n):
        stack.pop()
    end = perf_counter()
    time_lists.append(end-start)
    start = perf_counter()
    for i in range(n):
        linkedStack.pop()
    end = perf_counter()
    time_lists.append(end-start)
    return time_lists

# Comparacion Cola Enlazado y ordinaria


def compare_queue_enqueue(n):
    time_lists = []
    time_lists.append(n)
    start = perf_counter()
    for i in range(n):
        queue.enqueue(i)
    end = perf_counter()
    time_lists.append(end-start)
    start = perf_counter()
    for i in range(n):
        linkedQueue.enqueue(i)
    end = perf_counter()
    time_lists.append(end-start)
    return time_lists


def compare_queue_dequeue(n):
    time_lists = []
    time_lists.append(n)
    for i in range(n):
        queue.enqueue(i)
        linkedQueue.enqueue(i)
    start = perf_counter()
    for i in range(n):
        queue.dequeue()
    end = perf_counter()
    time_lists.append(end-start)
    start = perf_counter()
    for i in range(n):
        linkedQueue.dequeue()
    end = perf_counter()
    time_lists.append(end-start)
    return time_lists


print(compare_queue_dequeue(10000))
