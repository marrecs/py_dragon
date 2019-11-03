import random
import time

def mostrarIntroducción():
    print ('Estás en una tierra llena de dragones. Frente a tí')
    print ('hay dos cuevas. En una de ellas, el dragón es generoso y')
    print ('amigable y compartirá su tesoro contigo. El otro dragón')
    print ('es codicioso y está hambriento, y te devolverá inmediatamente')
    print ()

def elegirCueva():
    cueva = '' #variable unicamente valida para el entorno local, cuando acabe el def, se olvidará esta variable
    #Este es el entorno global
    while cueva != '1' and cueva != '2':
        print ('A qué cueva quieres entrar? (1 ó 2)')
        cueva = input()
        #Este ha sido el entorno local, dentro de while

    return cueva #sale de def con la variable asignada. Similar a break con while

def explorarCueva (cuevaElegida): #parámetro: variable local ordinaria
    print ('Te aproximas a la cueva...')
    time.sleep(2) #seconds
    print ('Es oscura y espeluznante...')
    time.sleep(2)
    print ('¡Un gran dragón aparece súbitamente frente a tí! Abre sus fauces y ...')
    print ()
    time.sleep(2)

    cuevaAmigable = random.randint (1,2)

    if cuevaElegida == str (cuevaAmigable): #str devuelve el valor de la cadena y lo transforma en mismo tipo de datos = if (int(cuE))=cuA
        print ('¡Te regala su tesoro!')
    else:
        print ('Te engulle de un bocado')

jugarDeNuevo= 'si'

while jugarDeNuevo == 'si' or jugarDeNuevo == 's':

    mostrarIntroducción()

    númeroDeCueva = elegirCueva()

    explorarCueva(númeroDeCueva)

    print ('¿Quieres jugar de nuevo? (si o no)')
    jugarDeNuevo = input()
