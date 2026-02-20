class Calculadora:

    def __init__(self,fecha):
        self.fecha= fecha
        self.tipo_operacion= ""
        self.resultado= 7
        self.tabla= ""

    def get_resultado(self):
        return self.resultado
    
    def set_resultado(self, nuevo_resultado):
        self.resultado= nuevo_resultado

    def get_operacion(self):
        return self.tipo_operacion

    def set_operacion(self, nueva_operacion):
        self.tipo_operacion= nueva_operacion

    def get_fecha(self):
        return self.fecha
    
    def set_fecha(self, nueva_fecha):
        self.operacion = nueva_fecha

    def mostrar_info(self):
        print(f"fecha: {self.fecha} numero 1: {self.numero_1} numero 2: {self.numero_2} operacion: {self.operacion}")
    
    def hacer_operacion(self,numero1,numero2,operacion):
        numero1= numero1.get_numero()
        numero2= numero2.get_numero()
        match operacion:
            case "suma":
                self.resultado= numero1+numero2
            case "resta":
                self.resultado= numero1-numero2
            case "multiplicacion":
                self.resultado= numero1*numero2
            case "division":
                self.resultado= numero1/numero2
            case _:
                print("operacion no obtenida")

        self.set_operacion(operacion)

    def guardar_info(self,usuario,numero1,numero2):
        informacion= (f"cedula: {usuario.get_cedula()} | nombre: {usuario.get_nombre()} | numero a: {numero1.get_numero()} | numero b: {numero2.get_numero()} | operecion: {self.tipo_operacion} | resultado: {self.resultado} | fecha: {self.fecha} \n")
        return informacion
    
    def guardar_en_tabla(self,informacion):
        self.tabla+= informacion

    def mostrar_tabla(self):
        print(self.tabla)
