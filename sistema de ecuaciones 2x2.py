
## solicitar el sistema de ecuaciones al usuario
## resolver el resultado de x y y
import re
import numpy as np

def get_numbers(equation):
    processed_eq = equation.replace(' ', '')
    
    x_match = re.search(r'([-+]?\d*)x', processed_eq)
    y_match = re.search(r'([-+]?\d*)y', processed_eq)
    constant_match = re.search(r'=([-+]?\d+)', processed_eq)

    # Coeficiente de x
    if x_match:
        coeff = x_match.group(1)
        if coeff in ['', '+']:
            coeff_x = 1
        elif coeff == '-':
            coeff_x = -1
        else:
            coeff_x = int(coeff)
    else:
        coeff_x = 0

    # Coeficiente de y
    if y_match:
        coeff = y_match.group(1)
        if coeff in ['', '+']:
            coeff_y = 1
        elif coeff == '-':
            coeff_y = -1
        else:
            coeff_y = int(coeff)
    else:
        coeff_y = 0

    # Constante
    constant = int(constant_match.group(1)) if constant_match else 0
    
    return [coeff_x, coeff_y, constant]

def det_method(matrix):
    if matrix.shape != (2, 3):
        return "Error: La matriz debe ser de 2x3 para este método."
    a, b, c = matrix[0, 0], matrix[0, 1], matrix[0, 2]
    d, e, f = matrix[1, 0], matrix[1, 1], matrix[1, 2]
    delta = a * e - d * b
    deltax = c * e - f * b
    deltay = a * f - d * c
    if delta == 0:
        return "El sistema no tiene una solución única (delta es cero)."
    x = deltax / delta
    y = deltay / delta
    return x, y


eq1_str = input('Ingresa la primera ecuación (ej. 3x-4y=7): ')
eq2_str = input('Ingresa la segunda ecuación (ej. -x+2y=-1): ')

eq1_val = get_numbers(eq1_str)
eq2_val = get_numbers(eq2_str)

eq_syst = np.array([eq1_val, eq2_val])

solution = det_method(eq_syst)

print("\n--- La solución del sistema es: ---")
if isinstance(solution, str):
    print(solution)
else:
    print(f"x = {solution[0]}")
    print(f"y = {solution[1]}")
