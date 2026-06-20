#Fecha:19/06/2026
#Autor:Bryan Adriano Nazareno Quinonez
#Tema: La cadena de caracteres siguiente contiene números y letras: "1bc89x3m".
# Usando desempaquetado de caracteres, sume solo los valores numéricos que se encuentran en la cadena. Para este ejercicio el valor esperado es 21.
# Ayúdese con la función isdigit(). A continuación, defina que hace la función isdigit() y que hace la función isnumeric(). 
# Además investigue: Cual es la diferencia entre estas dos funciones. Use comentarios para escribir el texto de las funciones investigadas.

print("Ejercicio 4:")
cadena4 = "1bc89x3m"
suma = 0


for caracter in cadena4:
    if caracter.isdigit():
        suma += int(caracter)  

print(f"La suma de los valores numéricos es: {suma}")

'''
INVESTIGACIÓN SOBRE METODOS DE CADENA:

1. ¿Qué hace la función isdigit()?
   - Devuelve True si todos los caracteres de la cadena son dígitos numéricos 
     puros (del 0 al 9) y la cadena no está vacía. También reconoce algunos 
     superíndices numéricos (como ²).

2. ¿Qué hace la función isnumeric()?
   - Devuelve True si todos los caracteres son numéricos. Es mucho más amplia 
     que isdigit(), ya que acepta caracteres que representan números en otros 
     sistemas o formatos (como números romanos 'Ⅳ', fracciones '½', o caracteres 
     de otros idiomas que representen cantidades).

3. Diferencia entre isdigit() e isnumeric():
   - La diferencia principal radica en el alcance de los caracteres que aceptan.
   - .isdigit() es más estricta y se limita principalmente a los dígitos del 0 al 9 
     y caracteres Unicode de tipo dígito.
   - .isnumeric() es la más flexible de todas, ya que considera "numérico" a cualquier 
     carácter que tenga la propiedad de valor numérico en Unicode, incluyendo 
     fracciones, números romanos y numeración china, etc.
'''
print("-" * 50)