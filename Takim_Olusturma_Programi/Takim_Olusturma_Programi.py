import random

BASLIK_GENISLIGI = 45

def karsilama_ekrani():
    print("=" * BASLIK_GENISLIGI)
    print("      ⚽ OTOMATİK TAKIM KURUCU PROGRAMI 🏀      ")
    print("=" * BASLIK_GENISLIGI)
    print("\nMERHABA! Bu program girdiğin isimleri adil bir")
    print("şekilde iki ayrı gruba ayırmanı sağlar.")
    print("\nNASIL KULLANILIR?")
    print("1. İsimleri tek tek gir")
    print("2. Bitince 'bitir' yaz")
    print("\n⚠️ En az 2 kişi girmelisin!")
    print("-" * BASLIK_GENISLIGI)

def grup_olustur():
    karsilama_ekrani()
    oyuncular = []

    while True:
        isim = input("Eklenecek Kişi: ").strip().lower()

        if isim == "bitir":
            break

        if not isim:
            print("❌ Geçerli bir isim gir!")
            continue

        if isim in oyuncular:
            print("⚠️ Bu isim zaten listede!")
            continue

        oyuncular.append(isim)
        print(f"✅ {isim} eklendi (Toplam: {len(oyuncular)})")

    if len(oyuncular) < 2:
        print("❌ Takım kurmak için en az 2 kişi gerekir!")
        return

    if len(oyuncular) % 2 != 0:
        print("⚠️ Kişi sayısı tek, bir grup 1 kişi fazla olacak.")

    random.shuffle(oyuncular)

    grup_boyutu = len(oyuncular) // 2
    grup_1 = oyuncular[:grup_boyutu]
    grup_2 = oyuncular[grup_boyutu:]

    print("\n" + "=" * 20)
    print(f"⚽ 1. GRUP ({len(grup_1)} kişi)")
    for i, kisi in enumerate(grup_1, 1):
        print(f"{i}. {kisi}")

    print(f"\n🏀 2. GRUP ({len(grup_2)} kişi)")
    for i, kisi in enumerate(grup_2, 1):
        print(f"{i}. {kisi}")
    print("=" * 20)

if __name__ == "__main__":
    grup_olustur()
