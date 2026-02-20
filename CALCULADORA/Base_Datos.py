class Base_datos:
    def __init__(self):
        self.registros=[]

    def agregar_registro(self,registro):
        self.registros.append(registro)

    def remover_registro(self,dato_remover):
        self.registros.remove(dato_remover)

    def mostrar_registros(self):
        for i in range(len(self.registros)):
            print(f"{i+1} | {self.registros[i]} ")