#Fecha:19/06/2026
#Autor:Bryan Adriano Nazareno Quinonez
#Tema: 2) Transforme la cadena "fundamentos de programación" en "Fundamentos DE Programación". Use el índice de las cadenas.

cadena2 = "fundamentos de programación"

palabra1 = cadena2[0:11].capitalize()  
palabra2 = cadena2[12:14].upper()       
palabra3 = cadena2[15:].capitalize()   

nueva_cadena2 = palabra1 + " " + palabra2 + " " + palabra3

print("Ejercicio 2:")
print(nueva_cadena2)
print("-" * 50)