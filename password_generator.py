import random
import string

#Cuando definimos una función en Python, le damos parámetros que son como "variables vacías" o "contenedores" que recibirán valores cuando la función sea llamada.
def generador_contrasenas(longitud_contrasena,incluir_mayus,
incluir_num,incluir_sim):
#Estos parámetros no tienen valores todavía. Solo son nombres que dentro de la función se van a rellenar cuando la llamemos.
    caracteres = string.ascii_lowercase #incluye las letras de la a-z

    if (incluir_mayusculas in ["Si","si","s","SI"]):
        caracteres += string.ascii_uppercase  # Agrega mayúsculas
    if (incluir_numeros in ["Si","si","s","SI"]):
        caracteres += string.digits  # Agrega números
    if (incluir_simbolos in ["Si","si","s","SI"]):
        caracteres += string.punctuation # Agrega símbolos especiales
    

    contrasena = ''.join(random.choice(caracteres) for i in range(longitud_contrasena))
    return contrasena #''.join(...) → Une todos los caracteres en una sola cadena.

while True:
    try:
        longitud_contrasena = int(input("Ingrese la longitud de la contraseña (debe ser un número entero): "))
        if longitud_contrasena > 0:  # Asegúrate de que la longitud sea positiva
            break
        else:
            print("Por favor, ingrese un número mayor a 0.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero. ")
        
incluir_mayusculas = input("Le gustaria que la contraseña incluya Mayúsculas?: ") 
incluir_numeros = input("Le gustaria que la contraseña incluya Numeros?: ") 
incluir_simbolos = input("Le gustaria que la contraseña incluya Simbolos?: ") 
#Cuando llamamos la función, le pasamos valores reales que se asignarán a esos parámetros. A estos valores se los llama argumentos
contrasena = generador_contrasenas(longitud_contrasena,incluir_mayusculas,incluir_numeros,incluir_simbolos)
print("Su nueva contraseña es: ", contrasena)  
#Cuando llamás a una función en Python, los valores que pasás como argumentos deben estar en el mismo orden en que fueron definidos los parámetros en la función.