#Fecha:19/06/2026
#Autor:Bryan Adriano Nazareno Quinonez
#Tema:Use índice de cadenas para invertir la siguiente palabra: "PUCESE". El resultado esperado será "ESECUP". 
#Luego pida una cadena de caracteres por teclado, y usando un bucle while/for e índice de cadenas, invierta esa cadena.

print("Ejercicio 3:")
palabra_fija = "PUCESE"

palabra_invertida = palabra_fija[::-1]
print(f"Palabra fija invertida: {palabra_invertida}")

cadena_usuario = input("Ingrese una cadena de caracteres para invertir: ")
cadena_usuario_invertida = ""

for i in range(len(cadena_usuario) - 1, -1, -1):
    cadena_usuario_invertida += cadena_usuario[i]

print(f"Su cadena invertida es: {cadena_usuario_invertida}")
print("-" * 50)
