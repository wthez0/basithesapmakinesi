print("Lütfen Yapacağınız İşlemi Seçiniz")
print("---------------------------------")
print("1-Çarpma")
print("2-Bölme")
print("3-Toplama")
print("4-Çıkarma")

secim = int(input("Lütfen Bir Seçim Yapınız : ")) 

# burada int yazma sebebimiz sayı girilmesini istememizdir,
# yani karakter de  girilmesini istersek int komutunu kaldırırız ama biz sayı girilmesini istediğimiz için int komutunuz kullanırız

sayi1 = int(input("Lütfen 1.Sayıyı Giriniz : "))
sayi2 = int(input("Lütfen 2.Sayıyı Giriniz : ")) 

# burada input yazma sebebimiz ise soru soruyp cevap almaktı, dizini çalıştırdığımızda bizlere bir değer soracak ve
# girdiğimiz değer artık sayi 1 olucak

if secim == 1 :                    # if ise diğer demektir yani başka yollar demektir
    sonuc = sayi1*sayi2
    print("Sonuç : ", sonuc)
elif secim == 2 :                  # elif ise alt seçeneklerdir seçenek belirtir
    sonuc2 = sayi1/sayi2
    print("Sonuç : ", sonuc2)
elif secim == 3 :
    sonuc3 = sayi1+sayi2
    print("Sonuç : ", sonuc3)
elif secim == 4 :
    sonuc4 = sayi1-sayi2
    print("Sonuç : ", sonuc4)
else:                              # else olumsuzdur dizin sonudur
    print("Geçersiz İşlem")
