import random
#import getpass   #PARA INGRESAR LA PALABRA A ADINIVAR Y QUE EL JUGADOR NO VEA LA PALABRA




def inicio():
    animalesSalvajes = ("elefante", "rinoceronte", "jirafa", "leopardo" )
    animalesDomesticos =("gato", "canario", "perro", "caballo")
    colores= ("azul", "amarillo", "rojo", "negro")
    vidas=7
    print ("********************************************")
    print("JUEGO DEL AHORCADO")
    print("tiene 7 vidas, se descontara 1 vida por cada letra incorrecta.")
    print("Puede arriesgar adivinar palabra, en caso incorrecto se le descontaran 3 vidas.") 
    print("Elija una tematica")
    print("1 Animales salvajes")
    print("2 Animales domesticos")
    print("3 Colores")
    print ("********************************************")
    opcion=int(input("ingrese una opción:   "))
    print ("********************************************")
    if opcion==1:
        palabra=definirPalabra(animalesSalvajes)
    elif opcion==2:
        palabra=definirPalabra(animalesDomesticos)
    elif opcion==3:
        palabra=definirPalabra(colores)
    else:
        print("ingrese una opción válida")
        inicio()
    print (f"La palabra tiene {len(palabra)} letras")
    print (f"La palabra comienza con la letra {palabra[0]} y termina con la letra {palabra[-1]}")

    main(palabra)



def definirPalabra(opcion):   
    return random.choice(opcion).upper()

    # palabra = (getpass.getpass("Indica Palabra ->")).upper()
    
    # validacionPalabra=(getpass.getpass("Repita su Palabra ->")).upper()
    # if palabra!=validacionPalabra:
    #     print ("palabra ingresada no coincide, inténtelo de nuevo...")
    #     ingresarPalabra()      
    # return list(palabra)

def restarVidas(vidas):
    vidas-=1
    return vidas

def verificarLetra(letra, palabra, respuesta, vidas): #los parámetros son la letra que arriesga el usuario, la palabra a adinvinar, la respuesta que tiene al momento y las vidas restantes
    flag=False          #puse "flag" pero es solo un indicador de que cambia cuando acierta o queda en false hata tango gane
    if letra not in palabra:
        vidas=restarVidas(vidas)        
        print("La letra ingresada no pertenece a la palabra, le restan {} vidas".format(vidas))
        return (respuesta, False, vidas)       
    else:    
        for indice,letras in enumerate(palabra):
            if letra==letras:
                
                respuesta[indice]=letras
                if flag==False:
                    print("Correcto, la letra ingresada pertenece a la palabra")
                #print("letras ingresadas: :",respuesta)
                    flag=True
        if palabra==respuesta:
            return (respuesta,True, vidas) 
        else:
            return (respuesta,False, vidas)   


def ingresarLetra():
    print("*************************************")
    letra=str(input("Ingrese una letra: ")).upper()
    print("*************************************")
    return letra

def adivinarPalabra( palabra, vidas):
    print("*************************************")
    intentoJugador=((input("Ingrese su palabra: ")).upper())
    print("*************************************")    
    if intentoJugador==palabra:
        print(intentoJugador,palabra)
        return (palabra, True, vidas)
    else:
        vidas=vidas-3
        print(intentoJugador,palabra)
        print("*************************************")
        print ("Palabra incorrecta...le restan {} vidas".format(vidas))
        print("*************************************")
        return (palabra, False, vidas)



 #---------------BLOQUE PRINCIPAL DEL PROGRAMA------------# 
def main(palabra):
    
    vidas=7
    respuesta=list()   
    for letras in palabra:   
        respuesta.append(" _")
    verificacion=(respuesta, False, vidas)  #con esta variable determinamos si adivinó (pasamos a True el segundo elemento), la cantidad de vidas que le quedan y las letras que va a adivinando
    while verificacion[1]==False: # and verificacion[2]>0:   #mientras no haya adivinado (false) y tenga mas de "0" vidas....    
        print("<-----------Adivinar Palabra de {} letras---------->".format(len(palabra)))
        print("Palabra: {}".format("".join(respuesta)))
        print ("Adivinar letra=(1)\nAdivinar Palabra =(2)")
        opcion=(int(input("Su Opción=??  ")))   
        if opcion==1:
            letra=ingresarLetra()
            #print(letra, palabra, respuesta, vidas)
            verificacion=verificarLetra(letra,palabra,respuesta, vidas)           
            respuesta=verificacion[0]
            vidas=verificacion[2]
            if vidas<=0:
                print("*************************************")
                opcion=int(input("Ud. perdió todas las vidas \n Desea jugar de nuevo, ingrese (1)\n Si desea salir, ingrese (2)"))
                print("*************************************")    
                if opcion==1:
                    inicio()
                elif opcion==2:
                    break

                
        elif opcion==2:
            verificacion=adivinarPalabra(palabra, vidas)
            print (verificacion)
            vidas=verificacion[2]
            if vidas==0:
                print("*************************************")
                opcion=int(input("Ud. perdió todas las vidas \n Desea jugar de nuevo, ingrese (1)\n Si desea salir, ingrese (2)"))
                print("*************************************")
                if opcion==1:
                    inicio()
                elif opcion==2:
                    break
        else:
            verificacion=(respuesta, False, vidas)
    if verificacion[1] ==True:
        print("*************************************")
        print ('Correcto, adívinó la palabra "{}" y finalizó con  {} corazones'.format("".join(palabra), verificacion[2]))  
        print("*************************************")
        nuevoJuego=int(input("Desea: \n Jugar de nuevo= (1) \n Salir= (2) \n"))
        if nuevoJuego==1:
            inicio()
        else:
            pass

inicio()
