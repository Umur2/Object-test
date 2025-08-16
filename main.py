# circle.py dosyasındaki Circle sınıfını içe aktar
from circle import Circle

# Kullanıcıdan dairenin yarıçapını al ve float tipine çevir
radius = float(input('Dairenin yarıçapı:'))

# Girilen yarıçap ile bir Circle nesnesi oluştur
Circy = Circle(radius)
# Circle sınıfının metodunu kullanarak dairenin alanını hesapla
area = Circy.circle_area()
# Circle sınıfının metodunu kullanarak dairenin çevresini hesapla
peremiter = Circy.circle_perimetre()

# Hesaplanan alanı ve çevreyi ekrana yazdır
print(f'Dairenin Alanı:{area}')
print(f'Dairenin Çevresi{peremiter}')
