print("Esto es un menu")
salida = 0
while salida==0:
    print("1-Saludar")
    print("2-Multiplicar")
    print("3-salir")
    print(" ")
    boton=input()
    if int(boton) == 1:
        print("Hola")
    elif int(boton) == 2:
        numero1=input("Dame el primer número que quieres multiplicar")
        numero2=input("Dame el segundo número que quieres multiplicar")
        print("Resultado:")
        print(int(numero1)*int(numero2))
    elif int(boton) == 3:
        print("salimos del menu")
        break
    else:
        print("No has complido con las reglas del menu")
        break