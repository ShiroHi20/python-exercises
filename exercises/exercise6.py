Zed :3, [24.03.17 23:07]
#Dada una lista de numeros,mostrar el más grande, el más pequeño y el promedio.

def buscarMenor(lista):
    i = 0 
    menor = lista[0]
    while i < len(lista): 
        if lista[i] < menor:
            menor = lista[i]
        i = i + 1 
    return menor 


def buscarMayor(lista):
    e = 0 
    mayor = lista[0]
    while e < len(lista):
        if lista[e] > mayor:
            mayor = lista[e]
        e = e +1
    return mayor 
    
    
def sacarPromedio(lista):
   return sum(lista) / len(lista) 
   

def main(listita):
    menor = buscarMenor(listita)
    mayor = buscarMayor(listita)
    promedio = sacarPromedio(listita)
    print ("el numero menor es:", menor, \
    ",el mayor es:", mayor, \
    ",el promedio es:", promedio)
    
    
listita = [1,45,67,87,90,21,4,55,22,564]

main(listita)