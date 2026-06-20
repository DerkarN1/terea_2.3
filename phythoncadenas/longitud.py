#fecha:17/06/2026
#Autor:Bryan Adriano Nazareno Quinonez
#tema:concatenacion de caracteres

nombres = "Juan"
apellidos = "Andrade"
edad = "21"
espasio = " "
cadena_concatenada = "Soy" + nombres + espasio + apellidos + "y Tengo" + edad + "años"


peso = 70

cadena_peso = "y peso" + str(peso) +  "Kilogramos"
print(cadena_concatenada, "loggitud:", len(cadena_concatenada))
print(cadena_peso,"longitud:", len(cadena_peso))

#33 > 20
print(len(cadena_concatenada) > len(cadena_peso)) #True
