# Example of LP using PuLP
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

# Create the model
model = LpProblem(name="part-A", sense=LpMaximize)

# Initialize the decision variables
butterscotch = LpVariable(name="butterscotch", lowBound=0, cat='Integer')
cinnamon = LpVariable(name="cinnamon", lowBound=0, cat='Integer')

# # Add the constraints to the model
model += (butterscotch + cinnamon == 100)

# # Add the objective function to the model
obj_func = (
    (-1 * butterscotch + 2 * cinnamon) * # capacity
    (-2 * butterscotch + 3 * cinnamon) * # durability
    (6 * butterscotch - 2 * cinnamon) * # flavor
    (3 * butterscotch - cinnamon)   # texture
)
model += obj_func

# Solve the problem
print('\nSolving problem ...\n\n')
status = model.solve()

print('\n\nShowing the problem ....\n\n')
print(model)

print('\n\nShowing the solution ...\n\n')
print(f"status: {model.status}, {LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")
print("variables:")
for var in model.variables():
    print(f"{var.name}: {var.value()}")
for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")

