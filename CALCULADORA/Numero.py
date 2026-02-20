class Numero:
    def __init__(self,numero):
        self.numero= numero

    def get_numero(self):
        return self.numero
    
    def set_numero(self, nuevo_dato_numero):
        self.numero= nuevo_dato_numero

    def mostrar_info(self):
        print(f"numero {self.numero}")