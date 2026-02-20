class Parqueadero:
    def __init__(self):
        self.puesto= ""
        self.fecha_entrada= ""
        self.hora_entrada= ""
        self.hora_salida= ""
        self.estado= ""
        self.tabla= ""
        
    def get_puesto(self):
        return self.puesto

    def set_puesto(self,puesto):
        self.puesto= puesto

    def get_fecha_entrada(self):
        return self.fecha_entrada
    
    def set_fecha_entrada(self,fecha_entrada):
        self.fecha_entrada= fecha_entrada

    def get_hora_entrada(self):
        return self.hora_entrada
    
    def set_hora_entrada(self,hora_entrada):
        self.hora_entrada= hora_entrada

    def get_hora_salida(self):
        return self.hora_salida
    
    def set_hora_salida(self,hora_salida):
        self.hora_salida= hora_salida

    def get_estado(self):
        return self.estado
    
    def set_estado(self,estado):
        self.estado= estado

    def mostrar_info(self):
        print(f"Puesto: {self.puesto}, Fecha entrada: {self.fecha_entrada} Hora entrada: {self.hora_entrada} Hora salida: {self.hora_salida} Estado: {self.estado} tabla: {self.tabla}")

    #resto de responsabilidades

    def registrar_datos(self,puesto,fecha_entrada,hora_entrada,estado,hora_salida):
        self.puesto= puesto
        self.fecha_entrada= fecha_entrada
        self.hora_entrada= hora_entrada
        self.estado= estado
        self.hora_salida= hora_salida

    def armar_texto(self,usuario,carro):
        info= f"Cedula usuario: {usuario.get_cedula()} | Nombre usuario: {usuario.get_nombre()} | Tipo usuario: {usuario.get_tipo_usuario()} | Placa carro: {carro.get_placa()} | Tipo carro: {carro.get_tipo_carro()} | Color carro: {carro.get_color_carro()} | Puesto parqueadero: {self.puesto} | Fecha entrada: {self.fecha_entrada} | Hora entrada: {self.hora_entrada} | Hora salida: {self.hora_salida} | Estado parqueadero: {self.estado} \n \n"
        return info
    
    def guardar_registro(self,info):
        self.tabla+= info
    
    def mostrar_registros(self):
        print(self.tabla)
        