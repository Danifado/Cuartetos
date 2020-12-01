print("Importando paquetes...")
import FNC as F
import codificacion as R
import json

print("Listo!")

def guardar_polaca(regla_polaca, archivo, letrasProposicionalesA, letrasProposicionalesB):
    print("Creando arbol...")
    regla_arbol = R.String2Tree(regla_polaca)
    print("Creando cadena inorder...")
    regla_inorder = R.Inorder(regla_arbol)
    print("Transformacion de Tseitin...")
    regla_fnc = F.Tseitin(regla_inorder, letrasProposicionalesA, letrasProposicionalesB)
    print("Forma clausal...")
    regla_clausal = F.formaClausal(regla_fnc)
    print(f"Guardando a archivo {archivo}...")
    with open(archivo + '.json', 'w') as outfile:
        json.dump(regla_clausal, outfile)
    print("Terminado!")

def guardar_inorder(regla_inorder, archivo, letrasProposicionalesA, letrasProposicionalesB):
    print("Transformacion de Tseitin...")
    regla_fnc = F.Tseitin(regla_inorder, letrasProposicionalesA, letrasProposicionalesB)
    print("Forma clausal...")
    regla_clausal = F.formaClausal(regla_fnc)
    print(f"Guardando a archivo {archivo}...")
    with open(archivo + '.json', 'w') as outfile:
        json.dump(regla_clausal, outfile)
    print("Terminado!")

def guardar_fnc(regla_fnc, archivo, letrasProposicionalesA, letrasProposicionalesB):
    print("Forma clausal...")
    regla_clausal = regla_fnc#F.formaClausal(regla_fnc)
    print(f"Guardando a archivo {archivo}...")
    with open(archivo + '.json', 'w') as outfile:
        json.dump(regla_clausal, outfile)
    print("Terminado!")

print("Creando reglas...")
# Creacion de la regla 0
regla_polaca = R.noRepsGrande()
letrasProposicionalesA = [chr(x) for x in range(256, 1000)] # Modificar de acuerdo a reglas
letrasProposicionalesB = [chr(x) for x in range(1000, 2000)] # Modificar de acuerdo a reglas
guardar_polaca(regla_polaca, 'regla0', letrasProposicionalesA, letrasProposicionalesB)
# Creacion de la regla 2
regla_polaca = R.P()
letrasProposicionalesA = [chr(x) for x in range(256, 2005)] # Modificar de acuerdo a reglas
letrasProposicionalesB = [chr(x) for x in range(2005, 3000)] # Modificar de acuerdo a reglas
guardar_polaca(regla_polaca, 'regla2', letrasProposicionalesA, letrasProposicionalesB)
print("Finalizado!")

#############################
# Las reglas se leen con:
# with open('regla0.json', 'r') as file:
#     reglas = json.load(file)
