
import getpass   #PARA INGRESAR LA PALABRA A ADINIVAR Y QUE EL JUGADOR NO VEA LA PALABRA

def ingresarPalabra():
    palabra = (getpass.getpass("Indica Palabra ->")).upper()
    
    validacionPalabra=(getpass.getpass("Repita su Palabra ->")).upper()
    if palabra!=validacionPalabra:
        print ("palabra ingresada no coincide, inténtelo de nuevo...")
        ingresarPalabra()      
    return list(palabra)

def restarVidas(vidas):
    vidas-=1
    return vidas

def verificarLetra(letra, palabra, respuesta, vidas): #palabra es una lista 
    flag=False
    if letra not in palabra:
        vidas=restarVidas(vidas)        
        print("La letra ingresada no pertenece a la palabra, le restan {} vidas".format(vidas))       
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
    letra=str(input("Ingrese una letra: ")).upper()
    return letra

def adivinarPalabra( palabra, vidas):
    intentoJugador=list((input("Ingrese su palabra: ")).upper())
    if intentoJugador==palabra:
        return (palabra, True, vidas)
    else:
        vidas=vidas-3
        return (palabra, False, vidas)



 #---------------BLOQUE PRINCIPAL DEL PROGRAMA------------# 
def main():
    palabra=ingresarPalabra()
    vidas=7
    respuesta=list()   
    for letras in palabra:   
        respuesta.append("_")
    verificacion=(respuesta, False, vidas)
    while verificacion[1]==False and verificacion[2]>0:       
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
        elif opcion==2:
            verificacion=adivinarPalabra(palabra, vidas)
            print (verificacion)
            vidas=verificacion[2]
        else:
            verificacion=(respuesta, False, vidas)
    if verificacion[1] ==True:
        print ('Correcto, adívinó la palabra "{}" y finalizó con  {} corazones'.format("".join(palabra), verificacion[2]))   
        nuevoJuego=int(input("Desea: \n Jugar de nuevo= (1) \n Salir= (2) \n"))
        if nuevoJuego==1:
            main()
        else:
            pass

main()
