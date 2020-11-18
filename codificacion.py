def codifica(p, n, Np, Nn):
    # Funcion que codifica un palo p y un número n
    carta = Nn * p + n
    # carta es un número que relaciona un palo (A = 0, B = 1, C = 2, D = 3) y un número (1,2,3,4)
    return carta

def decodifica(carta, Np, Nn):
    # Funcion que codifica una carta (un número entero) y retorna el palo y el número de la carta
    p = int(carta / Nn)
    n = carta % Nn
    return p, n


Npalos = 4
Nnumeros = 4
print(u"Números correspondientes a la codificación:")
print("\npalos x numeros")
for i in range(Npalos):
    for j in range(Nnumeros):
        v1 = codifica(i, j, Npalos, Nnumeros)
        print(v1, end = " ")
    print("")



for v1 in range(16):
    p, n = decodifica(v1, Npalos, Nnumeros)
    print('Código: '+str(v1)+', Palo: '+str(p)+', Número: '+str(n))

letras = []
for i in range(Npalos):
    for j in range(Nnumeros):
        v1 = codifica(i, j, Npalos, Nnumeros)
        cod = chr(v1 + 256)
        letras.append(cod)

for cod in letras:
    print('Letra = '+cod, end=', ')
    p, n = decodifica(ord(cod)-256, Npalos, Nnumeros)
    print('Palo = '+str(p), end=', ')
    print('Numero = '+str(n))

def Q(p, n, j, Np, Nn, Nj):
    # Funcion que codifica el palo p, el número n, y el jugador j
    v1 = codifica(p, n, Np, Nn)
    v2 = codifica(v1, j, Np * Nn, Nj)
    codigo = chr(256 + v2)
    return codigo

def decodificaQ(codigo, Np, Nn, Nj):
    # Funcion que codifica un caracter en su respectiva fila f, columna c y objeto o
    x = ord(codigo) - 256
    v1, j = decodifica(x, Np * Nn, Nj)
    p, n = decodifica(v1, Np, Nn)
    return p, n, j

letras = []
Njugadores = 4
for k in range(Nnumeros):
    print("Jugador: "+str(k))
    print("palos x numeros")
    for i in range(Npalos):
        print("Palo " + str(i) + ": ", end=" ")
        for j in range(Nnumeros):
            cod = Q(i, j, k, Npalos, Nnumeros, Njugadores)
            print(cod, end = " ")
            letras.append(cod)
        print("")
    print('\n')



for cod in letras:
    print('Letra = '+cod, end=', ')
    p, n, j = decodificaQ(cod, Npalos, Nnumeros, Njugadores)
    print('Jugador = '+str(j), end=', ')
    print('Palo = '+str(p), end=', ')
    print('Numero = '+str(n))
