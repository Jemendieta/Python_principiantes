# Estos son mis primeros pasos con Python

# comentarios de varias lineas
"""
Este es un 
comentario de 
varias lineas
"""
'''
Este es un
comentario de varias
lineas con comillas
simples
'''
# Primer hola mundo
print('Hola mundo desde Python...')

# las cadenas de texto se pueden escribir con comillas dobles "" o comillas simples ''
print("Mi nombre es Jorge")
print('Mi apellido es Mendieta')

# Con type() podemos conocer el tipo de dato
print(type('soy un string')) #Tipo 'str' de string
print(type(36)) #tipo 'int' de entero

# Variables
mi_variable = "Mi primera variable"
print(mi_variable)
mi_nombre = "Jorge Mendieta"
print(mi_nombre)
mi_edad = 36
print(mi_edad)

# concatenación de variables en un print
print(mi_nombre, mi_variable, mi_edad)

# Variables en una sola linea
name, surname, alias, age = "jorge", "Mendieta", "jorem", 36
# imprimimos nuestras variables concatenandolas
# No es recomendable este uso por buenas prácticas
print("me llamo:",name,surname,", mi alias es:",alias,"y mi edad es:",age)

# Inputs

name = input('¿Cuál es tu nombre?')
age = input('¿CUantos años tienes?')
print(name)
print(age)

# Funciones del sistema len(), permite conocer la longitud de caracteres de un string
print(len(mi_nombre))