class Calculadora:

    def __init__(self,numero_1, numero_2):
        self.fecha= "02/02/2026"
        self.numero_1= numero_1.get_numero()
        self.numero_2= numero_2.get_numero()
        self.operacion= ""


    def get_operacion(self):
        return self.operacion
    
    def set_operacion(self,nueva_operacion):
        self.operacion= nueva_operacion

    def get_fecha(self):
        return self.fecha
    
    def set_fecha(self, nueva_fecha):
        self.operacion = nueva_fecha

    def mostrar_info(self):
        print(f"fecha: {self.fecha} numero 1: {self.numero_1} numero 2: {self.numero_2} operacion: {self.operacion}")

    def operacion_suma(self):
        suma= self.numero_1+self.numero_2
        self.set_operacion("suma")
        return suma
    
    def operacion_resta(self):
        resta= self.numero_1-self.numero_2
        self.set_operacion("resta")
        return resta
    
    def operacion_multiplicacion(self):
        multiplicacion=self.numero_1*self.numero_2
        self.set_operacion("multiplicacion")
        return multiplicacion
    
    def operacion_division(self):
        division= self.numero_1/self.numero_2
        self.set_operacion("division")
        return division
    
    def guardar_info(self,usuario, resultado):
        informacion= (f"cedula: {usuario.get_cedula()} | nombre: {usuario.get_nombre()} | numero a: {self.numero_1} | numero b: {self.numero_2} | operecion: {self.operacion} | resultado: {resultado} | fecha: {self.fecha}")
        return informacion
    


    
        

