class Carro:
    def __init__(self,placa,tipo_carro,color_carro):
        self.placa= placa
        self.tipo_carro= tipo_carro
        self.color_carro= color_carro

    def get_placa(self):
        return self.placa
    
    def get_tipo_carro(self):
        return self.tipo_carro
    
    def get_color_carro(self):
        return self.color_carro
    
    def set_placa(self,placa):
        self.placa=placa

    def set_tipo_carro(self,tipo_carro):
        self.tipo_carro=tipo_carro

    def set_color_carro(self,color_carro):
        self.color_carro=color_carro

    def mostrar_info(self):
        print(f"Placa: {self.placa}, Tipo carro: {self.tipo_carro} Color carro: {self.color_carro}")
