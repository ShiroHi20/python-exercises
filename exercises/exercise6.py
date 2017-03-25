
#Dada una lista de numeros,mostrar el más grande, el más pequeño y el promedio.

def buscarMenor(lista):
    return min(lista)

def buscarMayor(lista):
    return max(lista)   
    
def sacarPromedio(lista):
    return sum(lista) / len(lista) 

def main(listita):     
    menor = buscarMenor(listita)
    mayor = buscarMayor(listita)
    promedio = sacarPromedio(listita)

    print ("el numero menor es: {}\n \
    el mayor es: {}\n \
    el promedio es: {}".format(menor, mayor, promedio))
    
listita = [1,45,67,87,90,21,4,55,22,564]
main(listita)