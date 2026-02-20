class Usuario:
    def __init__(self,cedula,nombre,tipo_usuario):
        self.cedula= cedula
        self.nombre=nombre
        self.tipo_usuario= tipo_usuario

    def get_tipo_usuario(self):
        return self.tipo_usuario
    
    def set_tipo_usuario(self, tipo_usuario):
        self.tipo_usuario = tipo_usuario

    def get_cedula(self):
        return self.cedula
    
    def get_nombre(self):
        return self.nombre
    
    def set_cedula(self,cedula):
        self.cedula=cedula

    def set_nombre(self,nombre):
        self.nombre=nombre

    def mostrar_info(self):
        print(f"Cedula: {self.cedula}, Nombre: {self.nombre} Tipo usuario: {self.tipo_usuario}")