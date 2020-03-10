import time # Esta libreria se utiliza para conocer el tiempo final que tarda el algoritmo en ser ejecutado.

# El siguiente metodo denominado "hanoi" ingresa por parametros (1. la altura del disco, 2. la torre de origen, 
#                                                3.la torre de destido, 4. La torre auxiliar o la de en medio.)
def hanoi(altura,origen,destino,intermedio):
    # El siguiente condicional es utilizado para saber la altura del disco, teniendo en cuenta que estan ordenados
    # de forma descendente.
    if altura >= 1:
        # En la siguiente linea utilizamos la recursividad para mover el disco al medio.
        hanoi(altura-1,origen,intermedio,destino)
        moverDisco(origen, destino) # Esta linea es otro metodo que muestra la posicion de movimiento del juego
        hanoi(altura-1,intermedio,destino,origen) # Mueve las fichas al inicio para poder traer al intermedio la
                                                  # que se encuentra al final.

# El método denominado "moverDisco" toma como parametros (1. Desde donde se mueve el disco, 2. Hacia donde va
#                                                                                                   el disco)
def moverDisco(desde,hacia):
    print("mover disco de ", desde, " a ", hacia) # Esta linea de código muestra los movimientos por pantalla 
                                                  # hasta que todas las fichas se encuentren en el otro lado

hms = time.time()

num_discos = int(input("Por favor ingrese la cantidad de discos --> ")) # Aquí se ingresa el número de discos con 
                                                                        # el que el algoritmo movera en las torres.

hanoi(num_discos, "A", "B", "C") # Aquí se ingresa como parametros el nombre dispuesto a las tres torres donde:
                                 # A (Es el origen), B (Es la torre de la mitad) y C (la torre final), ademas de 
                                 # recibir como primer parametro el numero de discos tomado por pantalla anterior.

print((time.time()) - hms) # Por ultimo se imprime el tiempo que tardo en ser ejecutado el algoritmo.
