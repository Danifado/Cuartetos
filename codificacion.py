class Tree(object):
    def __init__(self, label, left, right):
        self.left = left
        self.right = right
        self.label = label

def String2Tree(A):
    letrasProposicionales=[chr(x) for x in range(256, 600)]
    Conectivos = ['O','Y','>','=']
    Pila = []
    for c in A:
        if c in letrasProposicionales:
            Pila.append(Tree(c,None,None))
        elif c=='-':
            FormulaAux = Tree(c,None,Pila[-1])
            del Pila[-1]
            Pila.append(FormulaAux)
        elif c in Conectivos:
            FormulaAux = Tree(c,Pila[-1],Pila[-2])
            del Pila[-1]
            del Pila[-1]
            Pila.append(FormulaAux)
        else:
            print(u"Hay un problema: el símbolo " + str(c)+ " no se reconoce")
    return Pila[-1]

def Inorderp(f):
    if f.right == None:
        return str(decodificaQ(f.label, Npalos, Nnumeros, Njugadores))
    elif f.label == '-':
        return f.label + Inorderp(f.right)
    else:
        return "(" + Inorderp(f.left) + f.label + Inorderp(f.right) + ")"

def codifica(p, n, Np, Nn):
    # Funcion que codifica un palo p y un número n
    carta = Nn * p + n
    # carta es un número que relaciona un palo (A = 0, B = 1, C = 2, D = 3) y un número (0,1,2,3)
    return carta

def decodifica(carta, Np, Nn):
    # Funcion que codifica una carta (un número entero) y retorna el palo y el número de la carta
    p = int(carta / Nn)
    n = carta % Nn
    return p, n


Npalos = 4
Nnumeros = 4
Njugadores = 4

# print(u"Números correspondientes a la codificación:")
# print("\npalos x numeros")
# for i in range(Npalos):
#     for j in range(Nnumeros):
#         v1 = codifica(i, j, Npalos, Nnumeros)
#         print(v1, end = " ")
#     print("")



# for v1 in range(16):
#     p, n = decodifica(v1, Npalos, Nnumeros)
#     print('Código: '+str(v1)+', Palo: '+str(p)+', Número: '+str(n))

# letras = []
# for i in range(Npalos):
#     for j in range(Nnumeros):
#         v1 = codifica(i, j, Npalos, Nnumeros)
#         cod = chr(v1 + 256)
#         letras.append(cod)


####################################################################################3

# CODIFICA LA FUNCIÓN Q, QUE RELACIONA JUGADOR, PALO Y NUMERO
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
for k in range(Nnumeros):
    print("Jugador: "+str(k))
    for i in range(Npalos):
        print("Palo " + str(i) + ": ", end=" ")
        for j in range(Nnumeros):
            cod = Q(i, j, k, Npalos, Nnumeros, Njugadores)
            print(cod, end = " ")
            letras.append(cod)
        print("")
    print('\n')



#########################################################################

#REGLA QUE ME DICE QUE SI UN JUGADOR TIENE UNA CARTA, NINGUN OTRO LA TIENE
def noRepeticion(j, p, n):
    jugadores = [0,1,2,3]
    jugadores = [x for x in jugadores if x!= j]
    inicial = True
    for x in jugadores:
        if inicial:
            formula1 = Q(p, n, x, Npalos, Nnumeros, Njugadores)
            inicial = False
        else:
            formula1 += Q(p, n, x, Npalos, Nnumeros, Njugadores) + "O"

    formula1 = formula1 + "-" + Q(p, n, j, Npalos, Nnumeros, Njugadores) + '='

    return formula1

def noRepsGrande():
    inicial = True
    for j in range(4): #Jugadores
        for p in range(4): #palos
            for n in range(4): #numeros
                if inicial:
                    formula = noRepeticion(j, p, n)
                    inicial = False
                else:
                    formula += noRepeticion(j, p, n) + "Y"
    return formula

formulaNoReps = noRepsGrande()
# print(formulaNoReps)
# print(Inorderp(String2Tree(formulaNoReps)))


################################################################
# AHORA VAMOS A CODIFICAR LA FUNCION PEDIR P, QUE RELACIONA UN PALO p Y AL JUGADOR j AL QUE DEBE PEDIRSELO

def codificaP(p, j, Np, Nj):
    # Funcion que codifica un palo p y un número n
    pide = Nj*p + j
    # pide es un número que relaciona un palo (A = 0, B = 1, C = 2, D = 3) y un jugador (0,1,2,3,4)
    codigo = chr(1000 + pide) #Una letra proposicional unica basada en el numero pide
    return codigo

def decodificaP(pide, Nj):
    # Funcion que codifica una carta (un número entero) y retorna el palo y el número de la carta
    x = ord(pide) - 1000
    p = int(x / Nj)
    j = x % Nj
    return j, p

print("Codificación de las letras para pedir: ")
for p in range(Npalos):
    for j in range(Njugadores):
        cod = codificaP(p, j, Npalos, Njugadores)
        palo, jug = decodificaP(cod, Njugadores)
        print("La letra ", cod," significa pide el palo ", palo, " al jugador ", jug)
    print("")
