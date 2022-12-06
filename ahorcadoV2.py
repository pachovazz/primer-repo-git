import random

animalesSalvajes = ("elefante", "rinoceronte", "jirafa", "leopardo" )
animalesDomesticos =("gato", "canario", "perro", "caballo")
colores= ("azul", "amarillo", "rojo", "negro")

vidas=7
letraIncorrecta = vidas-1
palabraIncorrecta = vidas -3

print("JUEGO DEL AHORCADO")
print("tiene 7 vidas, se descontara 1 vida por cada letra incorrecta.")
print("Puede arriesgar adivinar palabra, en caso incorrecto se le descontaran 3 vidas.") 
print("Elija una tematica")
print("1 Animales salvajes")
print("2 Animales domesticos")
print("3 Colores")

palabra=random.choice(animalesSalvajes).upper()
print (palabra)

print (f"La palabra tiene {len(palabra)} letras")
print (f"La palabra comienza con la letra {palabra[0]} y termina con la letra {palabra[-1]}")

letra = input("Ingrese letra:" )
for letra in palabra:
	if letra == true:
		print("Letra encontrada")
	else:
		print("letra no encontrada")
		
else:
	vidas=vidas-1        
	print(f"La letra ingresada no pertenece a la palabra, le restas {vidas} vidas")
	

	




