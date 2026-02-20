from Usuario import Usuario
from Numero import Numero
from Calculadora import Calculadora
from Base_Datos import Base_datos  

base_datos= Base_datos()

def mostrar_menu():
    print("Calculadora 1000")
    print("Selecciones una opcion:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")

def seleccionar_opcion():
    opcion= int(input("Opcion: "))
    return opcion

def colocar_numero_1():
    numero1= int(input("Ingrese el primer numero: "))
    num1= Numero(numero1)
    return num1

def colocar_numero_2():
    numero2= int(input("Ingrese el segundo numero: "))
    num2= Numero(numero2)
    return num2

def pedir_datos_usuario():
    nombre= input("Ingrese su nombre: ")
    cedula= input("Ingrese su cedula: ")
    usuario= Usuario(nombre, cedula)
    return usuario

def colocar_calculadora():
        num1= colocar_numero_1()
        num2= colocar_numero_2()

        calculadora= Calculadora(num1, num2)
        return calculadora

def resultar_operacion(opcion, calculadora):
        if opcion==1:
            resultado= calculadora.operacion_suma()
        
        elif opcion==2:
            resultado= calculadora.operacion_resta()
        
        elif opcion==3:
            resultado= calculadora.operacion_multiplicacion()
        
        elif opcion==4:
            resultado= calculadora.operacion_division() 
        else:
            print("Opcion no valida")

        return resultado

def main():
    while True:
        mostrar_menu()
        opcion= seleccionar_opcion()

        if opcion==5:
            print("Gracias por usar la calculadora")
            break
        elif opcion> 5:
            print("opcion invalida")
            break
        
        calculadora= colocar_calculadora()

        resultado= resultar_operacion(opcion, calculadora)
        usuario= pedir_datos_usuario()
        informacion_guardada= calculadora.guardar_info(usuario, resultado)
        base_datos.agregar_registro(informacion_guardada)

    base_datos.mostrar_registros()

main()






