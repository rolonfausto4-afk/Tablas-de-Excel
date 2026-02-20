class Usuario:
    def __init__(self,nombre, cedula):
        self.nombre= nombre
        self.cedula= cedula

    def get_nombre(self):
        return self.nombre
    
    def get_cedula(self):
        return self.cedula
    
    def set_nombre(self, nuevo_dato_nombre):
        self.nombre= nuevo_dato_nombre

    def set_cedula(self, nuevo_dato_cedula):
        self.cedula= nuevo_dato_cedula

    def mostrar_info(self):
        print(f"nombre {self.nombre} - cedula {self.cedula}")




