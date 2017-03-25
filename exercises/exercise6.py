
#Dada una lista de numeros,mostrar el más grande, el más pequeño y el promedio.

def main(lista):     
    menor = min(lista)
    mayor = max(lista)   
    promedio = sum(lista) / len(lista) 

    print ("el numero menor es: {}\n \
    el mayor es: {}\n \
    el promedio es: {}".format(menor, mayor, promedio))
    
listita = [1,45,67,87,90,21,4,55,22,564]
main(listita)