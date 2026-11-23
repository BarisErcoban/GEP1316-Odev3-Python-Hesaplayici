# GEP1316 – Ödev 3: Python ile Kişisel Hesaplayıcı

**Öğrenci:** Barış Erçoban  
**Ders:** GEP1316 – Kodlama Okuryazarlığı  
**Proje:** Kâr Marjı ve KDV Hesaplayıcısı

## Projenin Amacı

Bu projede Python kullanarak ekonomi ve işletme alanlarında kullanılabilecek bir kâr marjı ve KDV hesaplayıcısı geliştirdim.

Program, kullanıcıdan ürün adı, ürün adedi, alış fiyatı, satış fiyatı ve KDV oranını alarak toplam kârı, kâr marjını, KDV tutarını ve KDV dahil satış fiyatını hesaplar.

## Kullanılan Python Özellikleri

- Değişkenler ve veri tipleri (int, float, str, bool)
- input() ile kullanıcıdan veri alma
- int() ve float() ile tür dönüşümü
- Aritmetik ve karşılaştırma operatörleri
- Koşullu ifadeler
- f-string ile biçimli çıktı
- Hatalı giriş kontrolü

## Test Senaryoları

| Test | Beklenen Sonuç | Gerçek Sonuç |
|---|---|---|
| Normal kâr hesabı | 500 TL kâr | 500 TL |
| Zarar hesabı | -400 TL zarar | -400 TL |
| Sıfır kâr hesabı | 0 TL | 0 TL |
| Geçersiz ürün adedi | Hata mesajı | Hata mesajı |

## Mantık Hatası ve Düzeltme

Hata avı aşamasında kâr marjının yanlış hesaplandığını tespit ettim.

Hatalı formül: `kar / alis * 100`

Doğru formül: `kar / satis * 100`

Alış fiyatı 80 TL ve satış fiyatı 100 TL olan örnekte hatalı sonuç %25, düzeltilmiş sonuç ise %20 olmuştur.

## Dosyalar

- **hesaplayici.py:** Çalışan Python hesaplayıcısı
- **hatali_ornek.py:** Hata avında kullanılan ve düzeltilen örnek
- **test_sonuclari.txt:** Test senaryoları

## Programın Çalıştırılması

Terminal üzerinden aşağıdaki komut kullanılır:

`python3 hesaplayici.py`

## Yapay Zekâ Kullanımı

Projenin hazırlanmasında ChatGPT'den kod geliştirme, açıklama ve test senaryoları oluşturma konusunda destek aldım. Programı kendi bilgisayarımda çalıştırarak sonuçları kontrol ettim ve mantık hatasını düzelttim.
