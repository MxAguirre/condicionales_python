# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Objetivo:
# Ingrese dos palabras cualesquiera
# y realice las sigueintes comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Alumno
# En cada desafio se le indicará que dada cierta condición
# modifique el valor de una variable o la cree con ese valor

# Compare las dos palabras y entre sí 
# utilizando if y else.
# - Si texto_1 es mayor (alfabéticamente) a texto_2, 
#   almacenar 1 en res_1
# - De lo contrario, almacenar 2 en res_1
if texto_1 > texto_2:
    rest_1 = 1
else:
    rest_1 = 2

# Imprimir en pantalla la variable res_1
print(rest_1)

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Utilice if, elif y else
# - Si texto_1 tiene más letras, almacenar 1 en res_2
# - Si texto_2 tiene más letras, almacenar 2 en res_2
# - Si tienen la misma cantidad de letras, almacenar 3 en res_2
if len(texto_1) > len(texto_2):
    rest_2 = 1
elif len(texto_1) < len(texto_2):
    rest_2 = 2
else:
    rest_2 = 3

# Imprimir en pantalla la variable res_2
print(rest_2)


# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# - Si la primera letra de texto_1 es mayor,
#   almacenar 1 en res_3
# - De lo contrario, almacenar 2 en res_3
if texto_1[0] > texto_2[0]:
    rest_3 = 1
else:
    rest_3 = 2


# Imprimir en pantalla la variable res_3
print(rest_3)

