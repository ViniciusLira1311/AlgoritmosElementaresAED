

class Sorter:
    def __init__(self):
        pass

    def insertionRecursivo(self, valores, i) -> [int]:
        j = i
        while (j > 0 and valores[j-1] > valores[j]):
            valores[j], valores[j-1] = valores[j-1], valores[j]
            j -= 1
        

        if (i + 1 < len(valores)):
            self.insertionRecursivo(valores, i+1)

        
        return valores

    def selectionRecursivo(self, valores, inicio) -> [int]:

        menor = inicio
        for j in range(inicio+1, len(valores)):
            if (valores[j] < valores[menor]):
                menor = j
        valores[inicio], valores[menor] = valores[menor], valores[inicio]

        inicio += 1
        if (inicio != len(valores)):
            self.selectionRecursivo(valores, inicio+1)

        return valores

    
    def insertionIterativo(self, valores) -> [str]:

        for i in range(len(valores)):
            for j in range(i, 0, -1):
                if (valores[j] < valores[j-1]):
                    valores[j], valores[j-1] = valores[j-1], valores[j]
                
                else:
                    j = 0
        
        return valores
    
    def SelectionLinkedList(self, linkedList) -> [int]:
        no = linkedList.inicio
        while no:
            menor = no
            prox = no.proximo
            while prox:
                if menor.valor > prox.valor:
                    menor = prox
                prox = prox.proximo
            no.valor, menor.valor = menor.valor, no.valor
            no = no.proximo