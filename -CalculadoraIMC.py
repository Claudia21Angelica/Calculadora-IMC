#Cadena de texto para informar sobre la funcion del programa, instrucciones
print("Este programa tiene la finalidad de calcular el IMC.")
print("----------------------------------------------------")
print("Favor de responder acorde a lo que se solicita")
#Se declara la variable personas para visualizar la cantidad de consultas a realizar
while True:
        try:
            personas = int(input( "Cantidad de personas que realizaran la consulta: "))
        except ValueError:
            print("Debes escribir un numero")
            continue
        if personas <= 0:
            print("Debes escribir numeros positivos")
            continue
        else:
            break
print("----------------------------------------------------") 
#Mientras la variable sea menor o igual a 0 se cierra la encuesta.
while personas > 0:
    print("----------------------------------------------------") 
    #Asignamos las preguntas con su debida validación para no dejar ingresar datos erróneos ni espacios
    #Nombre
    while True:
        try:
            n = str(input("Su nombre: ")) 
            letras = n.isalpha()
        except ValueError:
            print ("Favor de solo utilizar letras.")
        if letras == False:
            print("Favor de solo utilizar letras.")
            continue
        else:
            break
    #Apellido paterno
    while True:
        try:
            f = str(input("Su apellido paterno: ")) 
            letras = f.isalpha()
        except ValueError:
            print ("Favor de solo utilizar letras.")
        if letras == False:
            print("Favor de solo utilizar letras.")
            continue
        else:
            break
    #Apellido materno
    while True:
        try:
            g = str(input("Su apellido materno: ")) 
            letras = g.isalpha()
        except ValueError:
            print ("Favor de solo utilizar letras.")
        if letras == False:
            print("Favor de solo utilizar letras.")
            continue
        else:
            break  
    #Edad      
    while True:
        try:
           e = int(input("Su edad en años por favor: "))
        except ValueError:
            print("Favor de escribir su edad con numeros enteros.")
            continue
        if e <= 0:
            print ("Debes escribir numeros positivos.")
            continue
        else:
            break
    #Estatura
    while True:
        try:
            a = float(input ("Su estatura en metros por favor: "))
        except ValueError:
            print("Favor de escribir su estatura con numeros.")
            continue
        if a <= 0:
            print("Debes escribir numeros positivos")
            continue
        else:
            break
    #Peso
    while True:
        try:
            m = float (input("Su peso en kilogramos por favor :"))
        except ValueError:
            print("Favor de escribir su peso en kilogramos con numeros.")
            continue
        if m <= 0:
            print("Debes escribir numeros positivos")
            continue
        else:
            break
#Asignamos el valor de la variable IMC con su respectiva formula para comparar resultados más adelante.
    IMC = m / a**2
#Se imprime el nombre completo de la persona.
    print("----------------------------------------------------")
    print(n,f,g)
    print("-Su edad es:")
    print (e)
#Verificamos si es mayor de edad
    if(e < 18):
        print("-Usted es menor de edad-")
    else:
        print("-Usted es mayor de edad-")
#Se imprime el resultado del IMC y se realiza comparacion para desplegar el mensaje adecuado acorde a su resultado.
    print("-Su estatura es de:")
    print(a)
    print("-Su peso es de:")
    print(m)
    print("-Su IMC es:")
    print("IMC: " + str(IMC) )
    print("-Su rango de IMC es:")
    if IMC >= 0 and IMC <= 15.99 :
        print ("Delgadez severa")
    elif IMC >= 16.00 and IMC <= 16.99 :
        print ("Delgadez moderada")
    elif IMC >= 17.00 and IMC <= 18.49:
        print ("Delgadez leve")
    elif IMC >= 18.50 and IMC <= 24.99 :
        print ("Normal")
    elif IMC >= 25.00 and IMC <= 29.99:
        print ("Sobrepeso")
    elif IMC >= 30.00 and IMC <= 34.99:
        print ("obesidad leve")
    elif IMC >= 35.00 and IMC <= 39.00:
        print ("obesidad media")
    elif IMC >= 40.00:
        print ("obesidad morbida")  
    #Se resta una persona por consulta para no hacer una consulta infinita
    personas = personas - 1
    continue
#Si se realizan las encuestas solicitadas se realiza una salida del programa presionando cualquier tecla.
if personas == 0: 
    print("----------------------------------------------------") 
    print('-Fin de la consulta-')
    input("Presione cualquier tecla para cerrar el programa.")
 