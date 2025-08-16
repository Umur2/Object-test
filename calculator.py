# Basit aritmetik işlemleri gerçekleştirmek için Calculator sınıfını tanımla
class Calculator:    
    # İki sayıyı toplayıp sonucu döndüren metot
    def add(self,x,y):
        return x + y
    # İki sayıyı çıkarıp sonucu döndüren metot
    def subtract(self,x,y):
        return x-y
    # İki sayıyı çarpıp sonucu döndüren metot
    def multiply(self,x,y):
        return x*y

    # İki sayıyı bölüp sonucu döndüren metot
    def divide(self,x,y):
        if y != 0:
            return x/y
        else:
            return 'Sıfıra bölersen bozulurum'
    # Eğer payda sıfır ise hata mesajı döndür