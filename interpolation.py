from sympy import *

Abs = [1, 2, 3, 4]  
Ord = [1, 2, 4, 8]
C1 = 0
C2 = 0
C3 = 0
C4 = 0

LC = [C1, C2, C3, C4]

for i in range(0, len(Abs)):
    points = {Abs[i]: Ord[i]}
    print(points)

def intrpl():
    global C1, C2, C3, C4  
    n = 0  
    x = symbols('x')
    coeffs = []
    
    for idx, C in enumerate(LC):
        C = 1
        x0 = Abs[n]
        n += 1
        
        for i in range(0, len(Abs)):
            if Abs[i] != x0:
                C = C * (x - Abs[i]) / (x0 - Abs[i])
        
        print(expand(C))
        coeffs.append(C)
    
    
    C1, C2, C3, C4 = coeffs
    
    
    fun = Ord[0]*C1 + Ord[1]*C2 + Ord[2]*C3 + Ord[3]*C4
    print("\nFinal function:")
    print(expand(fun))
    
    return True

intrpl()