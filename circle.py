# Matematiksel fonksiyonlara (ör. pi) erişmek için math modülünü içe aktar
import math 
π = math.pi
# Daireyi temsil eden Circle sınıfını tanımla
class Circle:

    #Circle nesnesini yarıçap ile başlat
    def __init__(self, radius):
        self.radius = radius

    
    #Dairenin alanını hesapla ve döndür (π * r^2)
    def circle_area(self):
        return  π * self.radius **2

    #Dairenin çevresini (perimetre) hesapla ve döndür (2π * r)
    def circle_perimetre(self):
        return π * 2 * self.radius