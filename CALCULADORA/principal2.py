from Usuario import Usuario
from calculadora2 import Calculadora
from Numero import Numero

numero1= Numero(4)
numero2= Numero(8)

usuario1= Usuario("Camilo","012314805")

calculadora= Calculadora("fecha")

calculadora.hacer_operacion(numero1,numero2,"suma")

info= calculadora.guardar_info(usuario1,numero1,numero2)

calculadora.guardar_en_tabla(info)
calculadora.guardar_en_tabla(info)

calculadora.mostrar_tabla()