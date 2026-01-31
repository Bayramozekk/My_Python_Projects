import math

# -----------------------------
# Şekil fonksiyonları
# -----------------------------

# Dikdörtgen / Kare
def alan_dikdortgen(u, g):
    return u * g

def cevre_dikdortgen(u, g):
    return 2 * (u + g)

def alan_kare(k):
    return k ** 2

def cevre_kare(k):
    return 4 * k

# Üçgen
def alan_ucgen_taban_yukseklik(t, y):
    return (t * y) / 2

def cevre_ucgen(a, b, c):
    return a + b + c

# Daire
def alan_daire(r):
    if r <= 0:
        raise ValueError("Yarıçap pozitif olmalıdır.")
    return math.pi * r ** 2

def cevre_daire(r):
    if r <= 0:
        raise ValueError("Yarıçap pozitif olmalıdır.")
    return 2 * math.pi * r

# Paralelkenar
def alan_paralelkenar(t, h):
    return t * h

def cevre_paralelkenar(a, b):
    return 2 * (a + b)

# Eşkenar dörtgen
def alan_eskenar_dortgen(d1, d2):
    return (d1 * d2) / 2

def cevre_eskenar_dortgen(k):
    return 4 * k

# Yamuk
def alan_yamuk(a, b, h):
    return ((a + b) / 2) * h

def cevre_yamuk(a, b, c, d):
    return a + b + c + d

# Altıgen
def alan_altigen(s):
    return (3 * math.sqrt(3) / 2) * s**2

def cevre_altigen(s):
    return 6 * s

# Beşgen
def alan_besgen(s):
    return (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * s**2

def cevre_besgen(s):
    return 5 * s  # HATA DÜZELTİLDİ: 6*s yerine 5*s yapıldı.

# -----------------------------
# Kullanıcı etkileşimi
# -----------------------------

print("--- Geometrik Hesaplayıcıya Hoş Geldiniz ---\n")
print("Sorgulanabilir Şekiller: kare, dikdörtgen, üçgen, daire, yamuk, altıgen, beşgen, paralelkenar, eşkenar dörtgen\n")
print("Çıkış için 'q' yazabilirsiniz.\n")

while True:        
    sekil = input("Şekliniz: ").strip().lower()
    if sekil in ("q", "quit", "çıkış", "cikis"):
        print("Programdan çıkılıyor... Görüşmek üzere:)")
        break

    islem = input("İşleminiz(çevre/alan): ").strip().lower().replace("ç", "c")
    if islem not in ("alan", "cevre"):
        print("❌ Geçersiz işlem! Lütfen 'alan' veya 'çevre' yazın.")
        continue

    try:
        match sekil:
            case "kare":
                k = float(input("Kenar uzunluğu: "))
                if islem=="alan":
                    print("✅ Sonuç:", alan_kare(k))
                else:
                    print("✅ Sonuç:", cevre_kare(k))

            case "dikdörtgen" | "dikdortgen":
                u = float(input("Uzun kenar: "))
                g = float(input("Geniş kenar: "))
                if islem=="alan":
                    print("✅ Sonuç:", alan_dikdortgen(u, g))
                else:
                    print("✅ Sonuç:", cevre_dikdortgen(u, g))


            case "daire":
                r = float(input("Yarıçap: "))
                if islem=="alan":
                    print("✅ Sonuç:", alan_daire(r))       
                else:
                    print("✅ Sonuç:", cevre_daire(r))


            case "üçgen" | "ucgen":
                if islem == "alan":
                    t = float(input("Taban: "))
                    y = float(input("Yükseklik: "))
                    
                    print("✅ Sonuç:", alan_ucgen_taban_yukseklik(t, y))
                else:
                    a = float(input("1. Kenar: "))
                    b = float(input("2. Kenar: "))
                    c = float(input("3. Kenar: "))
                    print("✅ Sonuç:", cevre_ucgen(a, b, c))

            case "yamuk":
                a = float(input("Alt taban: "))
                b = float(input("Üst taban: "))
                if islem == "alan":
                    h = float(input("Yükseklik: "))
                    print("✅ Sonuç:", alan_yamuk(a, b, h))
                else:
                    c = float(input("Yan kenar 1: "))
                    d = float(input("Yan kenar 2: "))
                    print("✅ Sonuç:", cevre_yamuk(a, b, c, d))

            case "altigen" | "altıgen":
                s = float(input("Bir kenar uzunluğu: "))
                print(f"✅ Sonuç: {alan_altigen(s) if islem == 'alan' else cevre_altigen(s)}")

            case "besgen" | "beşgen":
                s = float(input("Bir kenar uzunluğu: "))
                print(f"✅ Sonuç: {alan_besgen(s) if islem == 'alan' else cevre_besgen(s)}")

            case "paralelkenar":
                if islem == "alan":
                    t = float(input("Taban: "))
                    h = float(input("Yükseklik: "))
                    print("✅ Sonuç:", alan_paralelkenar(t, h))
                else:
                    a = float(input("Yan kenar 1: "))
                    b = float(input("Yan kenar 2: "))
                    print("✅ Sonuç:", cevre_paralelkenar(a, b))

            case "eskenar dortgen" | "eşkenar dörtgen":
                if islem == "alan":
                    d1 = float(input("1. Köşegen: "))
                    d2 = float(input("2. Köşegen: "))
                    print(f"✅ Sonuç: {alan_eskenar_dortgen(d1, d2)}")
                else:
                    k = float(input("Bir kenar uzunluğu: "))
                    print(f"✅ Sonuç: {cevre_eskenar_dortgen(k)}")

            case _:
                print("❓ Bu şekil henüz listemizde yok.")    
    
    except ValueError as e:
        print(f"❌ Hata: {e}. Lütfen sayısal bir değer girin.")