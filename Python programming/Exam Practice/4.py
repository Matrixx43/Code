class Node :
    def __init__ ( self , value , next = None ) :
    self . value = value
    self . next = next

class LinkedQueue :
    def __init__ ( self ) :
    self . _head = None
    self . _last = None


    def filterApply(self, filterFunction, applyFunction):
        sol = LinkedQueue()
        i = self._head
        while i is not None:
            if filterFunction(i.value):
                sol.enqueue(applyFunction(i.value))
            i = i.next
        return sol


def pendiente(lis, pos):
    # YA IMPLEMENTADA
    # Devuelve -1=decreciente ==> Ir a la derecha
    # Devuelve 1=creciente ==> Ir a la izquierda
    # Devuelve 0=MINIMO ==> return lis[pos]

def busca_minimo(lis):
    # Con recursividad. Algoritmo tipo MERGE. Busqeda dicotomica
    return find_min_aux(lis, 0, len(lis)-1)

def find_min_aux(lis, izq, der):
    