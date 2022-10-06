import math

class Punto :
    def __init__ ( self , x , y ):
        self.x = x
        self.y = y

    def distancia ( self , other ) :
        return math.sqrt ( ( self.x - other.x ) **2 + ( self.y - other.y ) **2 )

#class Circulo :
    #def __init__( self , centro , radio ):
        #self.centro = centro # variable de tipo Punto
        #self.radio = radio # variable de tipo Float
    #def contiene( self , p ):
    # COMPLETAR_A
    #def intersecta( self , otroC ):
    # COMPLETAR_B


punto1 = Punto(0,0)
punto2 = Punto(10,23)

print(punto2.distancia(punto2))