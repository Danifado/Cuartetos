### Este archivo no es necesario correrlo,
##puesto que el trabajo de este se hace en visualizcion.py
## de la línea 206 a 214
import json
import unit_propagate as D
import codificacion as C

with open('regla0.json', 'r') as file:
    reglas = json.load(file)

with open('regla1.json', 'r') as file:
    reglas += json.load(file)

i = {'Ā': 1, 'Ą': 1, 'Ĉ': 1, 'Č': 1, 'ā': 1, 'ĕ': 1, 'ę': 1, 'ĝ': 1, 'Ģ': 1, 'Ħ': 1, 'Ī': 1, 'Į': 1, 'ĳ': 1, 'ķ': 1, 'Ļ': 1, 'Ŀ': 1}


SAT, i = D.DPLL(reglas, i)

print("Satisfacible? ", SAT)
# print("interp: ", i)
