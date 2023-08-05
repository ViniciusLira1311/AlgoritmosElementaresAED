import sys

sys.path.append("..")

# importing
from ordenador import Sorter
from lista_ligada import LinkedList



def test_vazio():
    lst = Sorter()
    
    resposta = lst.selectionRecursivo([5, 2, 3, 4, 1], 0)
    assert resposta == [1, 2, 3, 4, 5]

    resposta = lst.insertionRecursivo([5, 2, 3, 4, 1], 1)
    assert resposta == [1, 2, 3, 4, 5]

    resposta = lst.insertionIterativo(['d', 'c', 'a', 'e', 'b'])
    assert resposta == ['a', 'b', 'c', 'd', 'e']

def test_Linked_List():
    lst = Sorter()
    lst2 = LinkedList()
    lst2.inserir_inicio(1)
    lst2.inserir_inicio(4)
    lst2.inserir_inicio(3)
    lst2.inserir_inicio(2)
    lst2.inserir_inicio(5)

    lst.SelectionLinkedList(lst2)
    valoresOrdenados = []
    no = lst2.inicio
    while no:
        valoresOrdenados.append(no.valor)
        no = no.proximo
    
    assert valoresOrdenados == [1, 2, 3, 4, 5]