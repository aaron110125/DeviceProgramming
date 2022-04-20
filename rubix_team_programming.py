
# Decorators Programming to illustrate the functions that can be treated as objects

def rubix_data(tuchel):
    return tuchel.upper()

def iscon_data(tuchel):
    return tuchel.lower()

def tavares(cedric):
# I am using cedric to pass previous functions to output
    mount = cedric("""Arsenal thrumps Chelsea""")
    print(mount)

def goal_calculator(x):
    def goal_deficit(y):
        return x-y
    print("Goal deficit is",end= ' ')
    return goal_deficit

chelsea_scoreline = goal_calculator(2)
print(chelsea_scoreline(0))

tavares(rubix_data)
tavares(iscon_data)

Premier_League = rubix_data
print(Premier_League("London is Red"))
