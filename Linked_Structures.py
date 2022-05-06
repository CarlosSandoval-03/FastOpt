class Node:

    def __init__(self,var):
        #Se inicializa la variable de acuerdo al argumento de entrada
        self.var=var
        #Se incializa el apuntador en el valor nulo de Python
        self.next=None
        
    def get_var(self):
        # Retorna la variable guardada en el nodo
        return self.var
        
           
class LinkedList:

    def __init__(self):
        # Crea la lista enlazada desde 0
        self.head=None
        self.size=0

    def is_empty(self):
        #Verifica que la lista este vacía según el tamaño definido en size y la existencia de un objeto nodo en la referencia head 
        return self.head is None and self.size==0
        
    def size(self):
        #Retorna el tamaño de la lista (Cantidad de elementos enlazados)
        return self.size
        
    def inserts_beginning(self, new_var):
        # Creo el nuevo nodo a agregar
        new_node=Node(new_var)
        # Al puntero de este nuevo nodo, lo enlazo con la cabeza de la lista
        new_node.next=self.head
        # Conviertp al nuevo nodo en la cabeza de la lista
        self.head=new_node
        # Aumento el parametro tamaño de la lista
        self.size+=1
            
    def append(self, new_var):
        # Se crea el nuevo nodo a agregar
        new_node=Node(new_var)
        # En caso de que el puntero de el primer nodo de la lista apunte a none (No hay lista)
        # el nuevo nodo creado se agrega como la cabeza, (En este caso también es la cola)
        if self.is_empty():
            self.head=new_node
        else:
            # Suponiendo de que la lista ya posee nodos.
            # Creo una variable "locator" donde se presupone será el ultimo nodo.
            locator=self.head

            # Se comprueba si este "locator" es realmente el ultimo nodo de la lista.
            while(locator.next!=None):
                # En caso de que no sea así, el siguiente nodo, se convierte en el supuesto ultimo, se repite el proceso hasta 
                # llegar al verdadero ultimo.
                locator=locator.next
                # Una vez llegado al ultimo de los nodos, se enlaza el puntero con el nuevo nodo creado en un principio.
            locator.next=new_node
        #Agrega 1 al tamaño de la lista
        self.size+=1
            
    def get_index(self, index):
        #Se verifica que la lista este vacía
        if self.is_empty():
            print('Empty Structure - No elements to access')
        #Verifica que el índice ingresado no sea mayor a la cantidad de elementos en la lista
        elif index>=self.size:
            print('Index out of Boundaries')
        else:
            #Crea un nodo temporal para recorrer
            temp=self.head
            #Se recorre la lista hasta el índice requerido
            for i in range(index):
                if temp.next is not None: temp=temp.next
            #Se retorna el valor guardado en el nodo de la posición   
            return temp.get_var()
        
    def print(self):
        #Crea una cadena que mantiene la siguiente estructura:
        #[elemento1, elemento2, elemento3, ... ,elementon]
        #Donde n es la cantidad de elementos guardados en la estructura
        string = '['
        temp=self.head
        while(temp!=None):
            string+=str(temp.get_var())
            if temp.next!=None:
                string+=', '
            temp=temp.next
        #Imprime la cadena con la información
        print(string+']')

#La clase LinkedQueue hereda atributos y métodos de la clase LinkedList
class LinkedQueue(LinkedList):

    def __init__(self):
        #Se inicializan los atributos de size y head como en la LinkedList
        super().__init__()
        #Se inicializa un atributo adicional end
        self.end = None

    def is_empty(self):
        #Verifica que la LinkedQueue este vacía según el tamaño definido en size y la existencia de un objeto nodo en la referencia head y end
        return super().is_empty() and self.end is None

    def enqueue(self,new_var):
        #Se crea el nuevo nodo a encolar
        new_node = Node(new_var)
        #Se verifica que la LinkedQueue este vacía
        if self.is_empty():
            #Se encola el elemento partiendo de una LinkedQueue vacía
            self.end = new_node
            self.head = self.end
        else:
            #Se encola el elemento partiendo de una LinkedQueue que no está vacía
            self.end.next = new_node
            self.end = self.end.next
        #Agrega 1 al tamaño de la LinkedQueue
        self.size+=1

    def dequeue(self):
        #Se verifica que la LinkedQueue este vacía
        if self.is_empty():
            print('No elements to Dequeue')
        else:
            #Se crea Nodo Auxiliar para controlar el elemento a desencolar
            aux = self.head
            #Se verifica que la LinkedQueue tenga un único elemento
            if self.size == 1:
                #Se desencola el elemento partiendo de una LinkedQueue con un único elemento
                self.end = None
                self.head = None
            else:
                #Se desencola el elemento partiendo de una LinkedQueue con más de un elemento
                self.head = self.head.next
            #Se elimina el elemento a desencolar
            del aux
            #Se reduce en uno el tamaño de la LinkedQueue
            self.size-=1

    def front(self):
        #Se verifica que la LinkedQueue este vacía
        if self.is_empty():
            print('No front element')
        else:
            #Se retorna el primer elememnto que se encolo en la LinkedQueue
            return self.head.get_var()

#La clase LinkedStack hereda atributos y métodos de la clase LinkedList
class LinkedStack(LinkedList):
    
    def __init__(self):
        #Se inicializan los atributos de size y head como en la LinkedList
        super().__init__()
        #Se inicializa un atributo adicional end
        self.end = None

    def is_empty(self):
        #Verifica que la LinkedQueue este vacía según el tamaño definido en size y la existencia de un objeto nodo en la referencia head y end
        return super().is_empty() and self.end is None
    
    def top(self):
        if self.is_empty():
            print('No top element in empty Stack') 
        else:
            return self.end.get_var()

    def push(self,new_var):
        #Se crea el nuevo nodo a apilar
        new_node = Node(new_var)
        #Se verifica que la LinkedStack este vacía
        if (self.is_empty()):
            #Se apila el elemento partiendo de una LinkedStack vacía
            self.end=new_node
            self.head=self.end
        else:
            #Se apila el elemento partiendo de una LinkedStack que no está vacía
            self.end.next=new_node
            self.end=self.end.next
        #Se agrega 1 al tamaño de LinkedStack
        self.size+=1


    def pop(self):
        #Se verifica que la LinkedStack este vacía
        if (self.is_empty()):
            print("No elements to pop")
        else:
            if(self.size==1):
                #Se desapila partiendo de que la LinkedStack tenga un único elemento
                self.end=None
                self.head=None
            else:
                #Se desapila partiendo de que la LinkedStack tenga más de un elemento
                #Se crea un Nodo Auxiliar
                aux = self.end
                #Se crea un Nodo Temporal
                temp=self.head
                for i in range(self.size-2):
                    temp=temp.next
                temp.next=None
                self.end=temp
                #Se elimina el elemento a desapilar
                del aux
            #Se reduce en uno el tamaño de la LinkedStack
            self.size-=1