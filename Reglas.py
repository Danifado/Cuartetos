import json
import unit_propagate as D

with open('regla0.json', 'r') as file:
    reglas = json.load(file)

SAT, i = D.DPLL(reglas, {})
print("Satisfacible? ", SAT)
print("interp: ", i)
