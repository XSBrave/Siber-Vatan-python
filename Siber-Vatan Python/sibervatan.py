# cumle = input("bir cümle gir: ")
# duzenlenmis_cumle = cumle.strip().lower()
# print(duzenlenmis_cumle)



# cumle = input("bir cümle gir: ")
# karakter = input("aranacak karakter: ")
# sayi = cumle.count(karakter)
# print(f"{karakter} karakteri {sayi} kez geçiyor.")



# kelime = input("Bir kelime girin: ")
# harf = input("Aranacak harfi girin: ")
# sayi = kelime.count(harf)
# print(f"{harf} harfi {sayi} kez içeriyor.")



# string1 = input("Birinci stringi girin: ")
# string2 = input("İkinci stringi girin: ")
# birlesik_string = string1 + string2
# aranan_substring = input("Aranacak substringi girin: ")
# konum = birlesik_string.find(aranan_substring)
# print(f"Aranan substring '{aranan_substring}' {konum}. konumda bulunuyor.")



# cumle = input("Bir cümle girin: ")
# kelimeler = cumle.split()
# sirali_kelimeler = sorted(kelimeler)
# print("Sıralı kelimeler:", " ".join(sirali_kelimeler))



# string1 = input("Birinci stringi girin: ")
# string2 = input("İkinci stringi girin: ")
# birlesik_string = (string1 + string2).lower()
# print(birlesik_string)

# ana_string = input("Ana stringi girin: ")
# eski_substring = input("Değiştirilecek substringi girin: ")
# yeni_substring = input("Yeni substringi girin: ")
# yenilenmis_string = ana_string.replace(eski_substring, yeni_substring)
# print(yenilenmis_string)

# kelime = input("Bir kelime girin: ")
# yenilenmis_kelime = kelime.replace('a', '@')
# print(yenilenmis_kelime)

# kelime = input("Bir kelime girin: ")
# if kelime == kelime[::-1]:
#     print("Bu kelime bir palindromedir.")
# else:
#     print("Bu kelime bir palindrom değildir.")
# cumle = input("Bir cümle girin: ")
# kelimeler = cumle.split()
# en_uzun_kelime = max(kelimeler, key=len)
# print("En uzun kelime:", en_uzun_kelime)

# liste = [1, 2, 3, 4, 5]
# orta_eleman = liste[len(liste) // 2]
# print("Listenin ortasındaki eleman:", orta_eleman)

# my_tuple = (10, 20, 30, 40, 50)
# yeni_tuple = (my_tuple[1], my_tuple[3])
# print("Yeni tuple:", yeni_tuple)

# my_set = {1, 2, 3, 4, 5}
# sayi = int(input("Bir sayı girin: "))
# my_set.add(sayi)
# print("Set:", my_set)
# my_set.remove(sayi)
# print("Set (sayı çıkarıldı):", my_set)

# my_dict = {'anahtar1': 'değer1', 'anahtar2': 'değer2'}
# yeni_anahtar = input("Yeni anahtar girin: ")
# yeni_deger = input("Yeni değer girin: ")
# my_dict[yeni_anahtar] = yeni_deger
# print("Dict (yeni çift eklendi):", my_dict)

# sil_anahtar = input("Silinecek anahtar girin: ")
# del my_dict[sil_anahtar]
# print("Dict (anahtar silindi):", my_dict)

# liste = [1, 2, 3, 4, 5]
# yeni_sayi = int(input("Yeni sayı girin: "))
# liste.insert(len(liste) // 2, yeni_sayi)
# print("Listenin güncellenmiş hali:", liste)

# liste = [1, 2, 3, 4, 5]
# orta_eleman = liste[len(liste) // 2]
# tuple_ekle = (orta_eleman,)
# print("Tuple eklenmiş liste:", liste + list(tuple_ekle))

# my_set = {1, 2, 3, 4, 5}
# liste = list(my_set)
# toplam = sum(liste)
# print("Set elemanlarının toplamı:", toplam)

# my_dict = {'anahtar1': 'değer1', 'anahtar2': 'değer22', 'anahtar3': 'değer333'}
# karakter_sayisi = sum(len(deger) for deger in my_dict.values() if isinstance(deger, str))
# print("String değerlerin toplam karakter sayısı:", karakter_sayisi)

# liste = [15, 3, 27, 8, 12]
# en_buyuk_sayi = max(liste)
# print("En büyük sayı:", en_buyuk_sayi)

# my_dict = {'anahtar1': 'Merhaba', 'anahtar2': 'Dünya', 'anahtar3': 'Python'}
# birlesik_string = ''.join(my_dict.values())
# print("Birleştirilmiş string:", birlesik_string)