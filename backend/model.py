from gurobipy import Model, GRB, quicksum
from threading import Thread
from backend import db_functions

# --------------- CONJUNTOS / PARAMETROS ----------------------------------

PERSONS_DISP = {}
BOSS_DISP = {}
MODULES = list(range(35))

persons_thread = Thread(target=db_functions.get_disponible_modules,
                        args=("backend/bd/persons_bd.csv", PERSONS_DISP))
boss_thread = Thread(target=db_functions.get_disponible_modules, args=(
    "backend/bd/boss_bd.csv",
                                                                  BOSS_DISP))
persons_thread.start()
boss_thread.start()
# Se esperan a que terminen los threads
persons_thread.join()
boss_thread.join()

# ------------------ VARIABLES -------------------------------------------

modelo = Model()
x= {}
y = {}

for person in PERSONS_DISP:
    for mod in MODULES:
        x[person, mod] = modelo.addVar(vtype=GRB.BINARY,
                            name="person,{},{}".format(person, mod))


for j in BOSS_DISP:
    for mod in MODULES:
        y[j, mod] = modelo.addVar(vtype=GRB.BINARY,
                                     name="boss,{},{}".format(j, mod))


modelo.update()

# -------------------FUNCION OBJETIVO --------------------------------

modelo.setObjective(quicksum(x[i, m] for i in PERSONS_DISP for m in MODULES),
                    GRB.MAXIMIZE)

# ----------------------- RESTRICCIONES ---------------------------------

# 1)- Maximo de modulos por jefe/ Maximo de jefes por modulo

for j in BOSS_DISP:
    if j != "Tomas":
        modelo.addConstr(quicksum(y[j, m] for m in MODULES) <= 1)
    else:
        modelo.addConstr(quicksum(y[j, m] for m in MODULES) <= 2)



for j1 in BOSS_DISP:
    for j2 in BOSS_DISP:
        if j1 != j2:
            modelo.addConstr(quicksum(y[j1, m] + y[j2, m] for m in MODULES)
                             <= 3)

# 2)- Maximo de modulos de trabajo

modelo.addConstr(quicksum(y[j, m] for m in MODULES for j in BOSS_DISP) <= 4)

# 3)- Maximo de modulos asignados a cada tecnico

for i in PERSONS_DISP:
    modelo.addConstr(quicksum(x[i, m] for m in MODULES) <= 1)

# 4)- Solo se asgina un modulo si hay jefe en dicho modulo
for i in PERSONS_DISP:
        for m in MODULES:
            modelo.addConstr(x[i, m] <= quicksum(y[j, m] for j in BOSS_DISP))

# 5) Maximo de personas por modulo

for m in MODULES:
    modelo.addConstr(quicksum(x[i, m] for i in PERSONS_DISP) <= (len(
        PERSONS_DISP)//4)
                     + 15)

# Solo se asigna si se esta disponible en el modulo
for i in PERSONS_DISP:
    for m in MODULES:
        modelo.addConstr(x[i, m] <= PERSONS_DISP[i][m])

for j in BOSS_DISP:
    for m in MODULES:
        modelo.addConstr(y[j, m] <= BOSS_DISP[j][m])


