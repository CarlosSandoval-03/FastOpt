from Linked_Structures import *
from Structures import *
from time import *
import matplotlib.pyplot as plt

queue = Queue()
stack = Stack()
linkedQueue = LinkedQueue()
linkedStack = LinkedStack()
linkedList = LinkedList()
OrdinaryList = []

def init_():
    queue = Queue()
    stack = Stack()
    linkedQueue = LinkedQueue()
    linkedStack = LinkedStack()
    linkedList = LinkedList()
    OrdinaryList = [] 


def print_result(list):
    s = ''
    for i in list:
        s+=str(i)+' '
    print(s)

#Comparacion Listas - Ordinaria y linkeada
def compare_list_add(n):
    init_()
    time_lists = []
    time_lists.append(n)
    start = perf_counter()
    for i in range(n): OrdinaryList.append(i)
    end = perf_counter()
    time_lists.append(end-start)
    start = perf_counter()
    for i in range(n): linkedList.append(i)
    end = perf_counter()
    time_lists.append(end-start)
    return time_lists
    
def compare_list_remove_last(n):
    init_()
    time_lists = []
    time_lists.append(n)
    for i in range(n): 
        OrdinaryList.append(i)
        linkedList.append(i)
    start = perf_counter()
    while len(OrdinaryList)!=0: OrdinaryList.pop()
    end = perf_counter()
    time_lists.append(end-start)
    start = perf_counter()
    while linkedList.size != 0: linkedList.pop()
    end = perf_counter()
    time_lists.append(end-start)
    return time_lists

def mid(n):
    if n%2==0:
        return n/2
    else:
        return ((n-1)/2)+1

def compare_list_accessmidelement(n):
    init_()
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

#Comparacion Pilas Enlazado y ordinaria
def compare_stack_push(n):
    init_()
    time_lists = []
    time_lists.append(n)
    start = perf_counter()
    for i in range(n): stack.push(i)
    end = perf_counter()
    time_lists.append(end-start)
    start = perf_counter()
    for i in range(n): linkedStack.push(i)
    end = perf_counter()
    time_lists.append(end-start)
    return time_lists

def compare_stack_pop(n):
    init_()
    time_lists = []
    time_lists.append(n)
    for i in range(n): 
        stack.push(i)
        linkedStack.push(i)
    start = perf_counter()
    for i in range(n): stack.pop()
    end = perf_counter()
    time_lists.append(end-start)
    start = perf_counter()
    for i in range(n): linkedStack.pop()
    end = perf_counter()
    time_lists.append(end-start)
    return time_lists

def compare_stack_accessmidelement(n):
    init_()
    time_lists = []
    time_lists.append(n)
    for i in range(n): 
        stack.push(i)
        linkedStack.push(i)
    midposition = int(mid(n))
    start = perf_counter()
    k = stack.index(midposition)
    end = perf_counter()
    time_lists.append(end-start)
    start = perf_counter()
    k = linkedStack.get_index(midposition)
    end = perf_counter()
    time_lists.append(end-start)
    return time_lists

#Comparacion Cola Enlazado y ordinaria
def compare_queue_enqueue(n):
    init_()
    time_lists = []
    time_lists.append(n)
    start = perf_counter()
    for i in range(n): queue.enqueue(i)
    end = perf_counter()
    time_lists.append(end-start)
    start = perf_counter()
    for i in range(n): linkedQueue.enqueue(i)
    end = perf_counter()
    time_lists.append(end-start)
    return time_lists

def compare_queue_dequeue(n):
    init_()
    time_lists = []
    time_lists.append(n)
    for i in range(n): 
        queue.enqueue(i)
        linkedQueue.enqueue(i)
    start = perf_counter()
    for i in range(n): queue.dequeue()
    end = perf_counter()
    time_lists.append(end-start)
    start = perf_counter()
    for i in range(n): linkedQueue.dequeue()
    end = perf_counter()
    time_lists.append(end-start)
    return time_lists

def compare_queue_accessmidelement(n):
    init_()
    time_lists = []
    time_lists.append(n)
    for i in range(n): 
        queue.push(i)
        linkedQueue.push(i)
    midposition = int(mid(n))
    start = perf_counter()
    k = queue.index(midposition)
    end = perf_counter()
    time_lists.append(end-start)
    start = perf_counter()
    k = linkedQueue.get_index(midposition)
    end = perf_counter()
    time_lists.append(end-start)
    return time_lists

x = []
for i in range(1,11): 
    x.append(i*10)
for i in range(2,11): 
    x.append(i*100)
for i in range(2,11): 
    x.append(i*1000)

print('Finish Indexes',x)

#Lists
addlists = [compare_list_add(n) for n in x]
addorlist = [n[0] for n in addlists]
addlinlist = [n[1] for n in addlists]
print('Finish Adding')
removelists = [compare_list_remove_last(n) for n in x]
removeorlist = [n[0] for n in removelists]
removelinlist = [n[1] for n in removelists]
print('Finish Removing')
getlists = [compare_list_accessmidelement(n) for n in x]
getorlist = [n[0] for n in getlists]
getlinlist = [n[1] for n in getlists]
print('Finish Get')

plt.plot(x, addorlist, label = "Add Ordinary List")
plt.plot(x, addlinlist, label = "Add Linked List")
plt.plot(x, removeorlist, label = "Remove Ordinary List")
plt.plot(x, removelinlist, label = "Remove Linked List")
plt.plot(x, getorlist, label = "Get Ordinary List")
plt.plot(x, getlinlist, label = "Get Linked List")
plt.legend()
plt.show()

#Queues
addlists = [compare_list_add(n) for n in x]
addorlist = [n[0] for n in addlists]
addlinlist = [n[1] for n in addlists]
print('Finish Adding')
removelists = [compare_list_remove_last(n) for n in x]
removeorlist = [n[0] for n in removelists]
removelinlist = [n[1] for n in removelists]
print('Finish Removing')
getlists = [compare_list_accessmidelement(n) for n in x]
getorlist = [n[0] for n in getlists]
getlinlist = [n[1] for n in getlists]
print('Finish Get')

plt.plot(x, addorlist, label = "Add Ordinary List")
plt.plot(x, addlinlist, label = "Add Linked List")
plt.plot(x, removeorlist, label = "Remove Ordinary List")
plt.plot(x, removelinlist, label = "Remove Linked List")
plt.plot(x, getorlist, label = "Get Ordinary List")
plt.plot(x, getlinlist, label = "Get Linked List")
plt.legend()
plt.show()

#Stacks
addstack = [compare_stack_push(n) for n in x]
addorstack = [n[0] for n in addstack]
addlinstack = [n[1] for n in addstack]
print('Finish Adding')
removestack = [compare_stack_pop(n) for n in x]
removeorstack = [n[0] for n in removestack]
removelinstack = [n[1] for n in removestack]
print('Finish Removing')
getstack = [compare_stack_accessmidelement(n) for n in x]
getorstack = [n[0] for n in getstack]
getlinstack = [n[1] for n in getstack]
print('Finish Get')

plt.plot(x, addorstack, label = "Push Ordinary Stack")
plt.plot(x, addlinstack, label = "Push Linked Stack")
plt.plot(x, removeorstack, label = "Pop Ordinary Stack")
plt.plot(x, removelinstack, label = "Pop Linked Stack")
plt.plot(x, getorstack, label = "Get Ordinary Stack")
plt.plot(x, getlinstack, label = "Get Linked Stack")
plt.legend()
plt.show()

#Queues
addqueue = [compare_queue_enqueue(n) for n in x]
addorqueue = [n[0] for n in addqueue]
addlinqueue = [n[1] for n in addqueue]
print('Finish Adding')
removequeue = [compare_queue_dequeue(n) for n in x]
removeorqueue = [n[0] for n in removequeue]
removelinqueue = [n[1] for n in removequeue]
print('Finish Removing')
getqueue = [compare_queue_accessmidelement(n) for n in x]
getorqueue = [n[0] for n in getqueue]
getlinqueue = [n[1] for n in getqueue]
print('Finish Get')

plt.plot(x, addorqueue, label = "Enqueue Ordinary Queue")
plt.plot(x, addlinqueue, label = "Enqueue Linked Queue")
plt.plot(x, removeorqueue, label = "Dequeue Ordinary Queue")
plt.plot(x, removelinqueue, label = "Dequeue Linked Queue")
plt.plot(x, getorqueue, label = "Get Ordinary Queue")
plt.plot(x, getlinqueue, label = "Get Linked Queue")
plt.legend()
plt.show()