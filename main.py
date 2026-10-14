
import json
import os

DOSYA_ADI = "ogrenciler.json"


def ogrencileri_yukle():
    if os.path.exists(DOSYA_ADI):
        with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
            return json.load(dosya)
    return []


ogrenciler = ogrencileri_yukle()


def ogrencileri_kaydet():
    with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
        json.dump(ogrenciler, dosya, ensure_ascii=False, indent=4)

def ortalama_hesapla(vize, final):
    return vize * 0.4 + final * 0.6


def ogrenci_ekle():
    ad = input("Öğrenci adı: ")
   
    try:
        vize = float(input("Vize notu: "))
        final = float(input("Final notu: "))
    except ValueError:
        print("Hata: Lütfen geçerli bir sayı giriniz!")
        return

    if not (0 <= vize <= 100 and 0 <= final <= 100):
        print("Hata: Notlar 0 ile 100 arasında olmalıdır!")
        return


    ortalama = ortalama_hesapla(vize, final)

    ogrenci = {
        "ad": ad,
        "vize": vize,
        "final": final,
        "ortalama": ortalama
    }

    ogrenciler.append(ogrenci)
    ogrencileri_kaydet()

    print("Öğrenci başarıyla kaydedildi!")
    print("Öğrencinin ortalaması:", ortalama)


def ogrencileri_listele():
    if not ogrenciler:
        print("Henüz öğrenci bulunmuyor.")
        return

    for ogrenci in ogrenciler:
        print(ogrenci["ad"], "-", ogrenci["ortalama"])


while True:
    print("\n1- Öğrenci Ekle")
    print("2- Öğrencileri Listele")
    print("3- Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        ogrenci_ekle()
    elif secim == "2":
        ogrencileri_listele()
    elif secim == "3":
        break
    else:
        print("Geçersiz seçim!")
