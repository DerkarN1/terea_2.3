#Fecha:17/06/2026
#Autor:Bryan Adriano Nazareno Quinonez
#Tema: Indice en cadenas de caracteres 

cadena = "PUCESE"
primera_letra = cadena[0]
print(f"La primera letra es {primera_letra}")

longitud = len(cadena)
print(f"La longitud de la cadena es {longitud}")
ultima_letra = cadena[longitud-1]
print(f"La ultima letra es {ultima_letra}")

letra_cualquiera = cadena[6//3+2]
print(f"La letra encontrada despues de la operacion es {letra_cualquiera}")
