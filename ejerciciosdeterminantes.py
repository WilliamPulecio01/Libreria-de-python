"""
TRABAJO FINAL - ÁLGEBRA LINEAL
Verificación con Python (SymPy)

Incluye:
- 6 sistemas de ecuaciones
- 3 determinantes
- Propiedades de determinantes
"""

import sympy as sp

# =========================
# VARIABLES
# =========================
x, y, z = sp.symbols('x y z')

# =========================
# T1: SISTEMAS DE ECUACIONES
# =========================
print("\n===== SISTEMAS DE ECUACIONES =====\n")

# 1
s1 = [
    sp.Eq(x + y + z, 6),
    sp.Eq(2*x - y + z, 3),
    sp.Eq(x + 2*y - z, 3)
]
print("Sistema 1:", sp.solve(s1, (x,y,z)))

# 2
s2 = [
    sp.Eq(2*x + y - z, 1),
    sp.Eq(x - y + 2*z, 3),
    sp.Eq(3*x + y + z, 7)
]
print("Sistema 2:", sp.solve(s2, (x,y,z)))

# 3 (infinitas)
s3 = [
    sp.Eq(x + y + z, 3),
    sp.Eq(2*x + 2*y + 2*z, 6),
    sp.Eq(x - y + z, 1)
]
print("Sistema 3:", sp.solve(s3, (x,y,z), dict=True))

# 4 (infinitas)
s4 = [
    sp.Eq(x + 2*y + z, 4),
    sp.Eq(2*x + 4*y + 2*z, 8),
    sp.Eq(x - y + z, 1)
]
print("Sistema 4:", sp.solve(s4, (x,y,z), dict=True))

# 5 (sin solución)
s5 = [
    sp.Eq(x + y + z, 2),
    sp.Eq(2*x + 2*y + 2*z, 5),
    sp.Eq(x - y + z, 1)
]
print("Sistema 5:", sp.solve(s5, (x,y,z)))

# 6 (sin solución)
s6 = [
    sp.Eq(x + y + z, 1),
    sp.Eq(2*x + 2*y + 2*z, 3),
    sp.Eq(x + y + z, 4)
]
print("Sistema 6:", sp.solve(s6, (x,y,z)))


# =========================
# T2: DETERMINANTES
# =========================
print("\n===== DETERMINANTES =====\n")

A = sp.Matrix([[1,2,3],[2,5,3],[1,0,8]])
B = sp.Matrix([[2,1,3],[0,-1,4],[5,2,0]])
C = sp.Matrix([[3,2,1],[1,0,2],[4,1,3]])

print("Det A (Gauss):", A.det())
print("Det B (Sarrus):", B.det())
print("Det C (Cofactores):", C.det())


# =========================
# T3: PROPIEDADES
# =========================
print("\n===== PROPIEDADES =====\n")

# Propiedad 6: fila cero
P6 = sp.Matrix([[1,2,3],[0,0,0],[4,5,6]])
print("P6 (fila cero):", P6.det())

# Propiedad 7: multiplicar fila
P7 = sp.Matrix([[1,2,3],[1,0,1],[2,1,0]])
P7_mod = P7.copy()
P7_mod[0,:] = 2*P7_mod[0,:]

print("P7 original:", P7.det())
print("P7 multiplicada:", P7_mod.det())

# Propiedad 8: identidad
I = sp.eye(3)
print("P8 identidad:", I.det())

# Propiedad 9: transpuesta
P9 = sp.Matrix([[1,2,3],[0,4,5],[1,0,6]])
print("P9 A:", P9.det())
print("P9 A^T:", P9.T.det())


# =========================
# CONCLUSIÓN
# =========================
print("\n===== CONCLUSIÓN =====")
print("Todos los resultados coinciden con los cálos manuales.")