"""GEP1316 - Ekonomi: Kar marji ve KDV hesaplayicisi."""

def hesapla(alis, satis, kdv_orani):
    """Fiyatlar KDV haric; oran yuzde olarak girilir."""
    if alis < 0 or satis < 0 or not 0 <= kdv_orani <= 100:
        raise ValueError('Fiyatlar negatif olamaz; KDV orani 0-100 arasinda olmali.')
    kar = satis - alis
    marj = (kar / satis * 100) if satis > 0 else 0.0
    kdv = satis * kdv_orani / 100
    return kar, marj, kdv, satis + kdv


def main():
    print('KAR MARJI VE KDV HESAPLAYICISI')
    urun = input('Urun adi: ').strip()  # str
    if not urun:
        print('Hata: Urun adi bos olamaz.')
        return
    try:
        adet = int(input('Urun adedi: '))  # int
        alis = float(input('Birim alis fiyati (TL, KDV haric): '))  # float
        satis = float(input('Birim satis fiyati (TL, KDV haric): '))
        kdv_orani = float(input('KDV orani (%): '))
        if adet <= 0:
            raise ValueError('Adet pozitif olmalidir.')
        kar, marj, kdv, toplam = hesapla(alis, satis, kdv_orani)
        karli_mi = kar > 0  # bool ve karsilastirma operatoru
        print(f'\nUrun: {urun} | Adet: {adet}')
        print(f'Toplam kar: {kar * adet:.2f} TL')
        print(f'Kar marji: %{marj:.2f}')
        print(f'Toplam KDV: {kdv * adet:.2f} TL')
        print(f'KDV dahil toplam satis: {toplam * adet:.2f} TL')
        print(f'Karli mi?: {"Evet" if karli_mi else "Hayir"}')
    except ValueError as hata:
        print(f'Gecersiz giris: {hata}')


if __name__ == '__main__':
    main()
