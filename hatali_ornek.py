"""SADECE HATA AVI ICIN: kasitli mantik hatasi bulunan ornek."""
def hatali_kar_marji(alis, satis):
    if satis <= 0:
        return 0.0
    kar = satis - alis
    return kar / satis * 100  # HATA: kar marji icin payda satis olmali!

print(hatali_kar_marji(80, 100))  # Yanlis: %25, dogru: %20
