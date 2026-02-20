from Usuario import Usuario
from Carro import Carro
from Parqueadero import Parqueadero

usuario1= Usuario("10983152", "Julian Ayala","Cliente")
usuario2= Usuario("10934173","Breiner Bueno","Ingeniero en Sistemas")
usuaerio3= Usuario("10934173","Carlos Parra","Ingeniero en Sistemas")

carro1= Carro("ASD89", "Sedan", "Rojo")
carro2= Carro("GAY24H","Nexo", "Gris")
carro3= Carro("HRD27H","Serto", "Gris")

parqueadero= Parqueadero()

parqueadero.registrar_datos("45B", "2024-06-15", "08:00", "Ocupado",None)
info = parqueadero.armar_texto(usuario1,carro1)
registro= parqueadero.guardar_registro(info)

parqueadero.registrar_datos("34B","2024-06-15", "09:00", "Ocupado",None)
info = parqueadero.armar_texto(usuario2,carro2)
registro= parqueadero.guardar_registro(info)

parqueadero.registrar_datos("23C","2024-06-15", "10:00", "Salida","12:00")
info = parqueadero.armar_texto(usuaerio3,carro3)
registro= parqueadero.guardar_registro(info)

parqueadero.mostrar_registros()

