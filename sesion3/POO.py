celular1_marca = "Xiaomi"
celular2_marca = "Samsung"
celular3_marca = "Apple"

celular1_modelo = "Redmi 9"
celular2_modelo = "S22"
celular3_modelo = "Iphone 13"

celular1_color = "Negro"
celular2_color = "Plata"
celular3_color = "Rojo"

celular1_camara = "64 MP"
celular2_camara = "48 MP"
celular3_camara = "128 MP"

# print (celular2_marca)

print(
    '''
    ===================================================
    PROGRAMACION ORIENTADA A OBJETOS (POO)
    ===================================================
    ''')

class Celular():
    marca = "Xiaomi"
    camara = "64 MP"
    color = "Negro"
    modelo = "Redmi 9"

celular1 = Celular()
celular2 = Celular()
celular3 = Celular()
print(celular1.color)

class Celulares:
    def __init__(self, marca, camara, color, modelo):
        self.marca = marca
        self.camara = camara
        self.color = color
        self.modelo = modelo
    
    def llamar(self):
        return('Estas realizando una llamada con tu ' + self.marca)

celular4 = Celulares("Huawei", "8MP",'Blanco',"P9")
celular5 = Celulares("Samsung", "18MP",'Negro',"S10")

print(celular5.llamar())

