# SDK ve entegrasyonlar

## WOLVOX SDK

- **Ne:** WOLVOX ERP'deki verileri **XML olarak dışarı almak** ve dışarıdan gelen XML'i **ERP'ye kaydetmek** için geliştirme arayüzü.
- **Mimari:** Programlama dilinden bağımsız. **HTTP ve XML** standartlarında, **Kontrol Paneli'ne gömülü** bir servis. Ayrı sunucu kurulmaz; Kontrol Paneli çalışıyorsa SDK da çalışır.
- **İki işlem türü:**
  1. **Veri Raporlama:** Cari listesi, stok listesi gibi verileri XML olarak döndürür.
  2. **Veri Ekleme (kayıt fonksiyonları):** Belirli formatta hazırlanmış XML'i girdi alır.
- **Dönüş değeri (kayıt fonksiyonları):**
  - Başarılı: `BLKODU=1234` (yeni kaydın BLKODU'su)
  - Hatalı: `Error : <Hata Mesajı>`
- **Bağlantı parametreleri:**
  - **Host:** Kontrol Paneli'nin kurulu olduğu bilgisayarın IP'si (yerelde `127.0.0.1`)
  - **Port:** Kontrol Paneli'nin **güncelleme portu** (Kontrol Paneli ayarlarından bak)
  - **Kullanıcı adı / parola:** Kontrol Paneli'nde tanımlı WOLVOX kullanıcısı
  - **Şirket kodu** ve **çalışma yılı**
  - **Ek Şart (SQL):** Raporlamada filtre. Ör. cari listesinde sadece tedarikçileri almak için ilgili tabloya WHERE koşulu.
- **AKINSOFT WOLVOX SDK programı:** Komutları deneyip XML üretmek için bir test/yardımcı araç. "Komut" alanından (ör. cari listesi) seçilen işlemin isteği oluşturulup gönderiliyor.
- **Resmi doküman (PDF):** "AKINSOFT Wolvox9 SDK Doküman" (2024).
  - https://akinsoft.net/bilgibankasi/data/upload/257/wolvox9_sdk_dokuman1734088631.pdf
  - https://akinsoft.net/bilgibankasi/data/upload/257/wolvox9_sdk_dokuman1721372145.pdf (eski revizyon)
  - İlgili makaleler: Bilgi Bankası 257 (WOLVOX ERP Programı SDK İşlemleri), 3994 (WOLVOX SDK İşlemleri)

> **Bu bilgi tabanına fonksiyon adları, uç nokta (endpoint) adresleri ve XML şemaları henüz işlenmedi.** Oluşturulurken PDF'e erişilemedi. SDK ile kod yazmadan önce yukarıdaki PDF'i oku (WebFetch) ve öğrendiğin fonksiyon, parametre ve XML örneklerini bu dosyaya ekle. Fonksiyon adı veya XML etiketi **uydurma**.

### SDK ile entegrasyon yazarken önerilen yaklaşım
1. Önce Veri Raporlama ile küçük bir okuma yap (ör. cari listesi). Bağlantı, port ve kullanıcı bilgisini doğrula.
2. Veri Ekleme için PDF'teki XML örneğini birebir kopyalayıp **test şirketinde** dene.
3. Dönen metni ayrıştır: `BLKODU=` ile başlıyorsa başarılı, `Error :` ile başlıyorsa hata.
4. Kimlik bilgilerini ortam değişkeninde tut. SDK portunu internete açma; gerekiyorsa VPN kullan.

## AKINSOFT e-Ticaret ↔ WOLVOX ERP (Web Entegrasyon, WWB9)

- **WOLVOX Web Entegrasyon programı**, AKINSOFT e-Ticaret sunucusuyla otomatik haberleşir. Siparişleri ERP'ye aktarır. Stok, sipariş, fatura ve cari verileri senkronize edilir.
- e-Ticaret yönetim panelinde: **Entegrasyonlar → Ticari Program Yönetimi → "Tam Senkronizasyon"** seçili olmalı. Böylece ERP'deki tüm stok işlemleri e-Ticaret paneline yansır.
- Ayar makaleleri: genel ayarlar (Bilgi Bankası 2207), entegrasyon ayarları (492), cari ayarları (3068), sipariş kayıt ayarları (3065), taksit entegrasyonu (3473), B2B/B2C/müşteri tipine göre ürün gösterimi (2680), e-Ticaret + ERP + Genel Muhasebe üçlü entegrasyonu (3119).

### Üçüncü taraf e-ticaret ve pazaryeri entegratörleri
T-Soft, Sentos, Entegra Bilişim, Ayen Software ve Projesoft (B2B) Wolvox entegrasyonu sunuyor. Genelde gereken bilgiler: Wolvox bağlantı/API bilgileri, firma ve ambar/depo tanımları, ürün-varyant kod yapısı, fatura seri/sıra şeması, e-Fatura/e-Arşiv yetkileri.

## WebConnect (IWM9)

- ERP'ye tarayıcıdan (masaüstü, telefon, tablet) erişim sağlayan web uygulaması.
- Cari, Kasa, Stok, Fatura, Sipariş, Servis, İrsaliye, Günsonu ve Restoran raporları. Veri girişi de yapılabiliyor.
- Kurulum sonrası modemden ilgili port açılır (Bilgi Bankası 1526 bağlantı ayarları). Web tabanlı olduğu için uzak bağlantıda hızlı.

## WOLVOX Reporter (ARP2) ve mobil uygulamalar

- Android'den ERP'ye bağlanıp rapor alma.
- Mobil Satış (APD9) sahada senkronize çalışıyor (`sektorel-programlar.md`).

## WOLVOX ERP ↔ Genel Muhasebe

Entegrasyon iki yolla yapılır:
1. **Anlık entegrasyon:** ERP'de **"Genel Muhasebe Sistemi Kullan"** işaretlenir ve **Anlık Entegrasyon** seçilir. ERP'deki işlemler anında Genel Muhasebe'ye yansır.
2. **Toplu entegrasyon:** Aynı ayarda **Toplu Entegrasyon** seçilir. Sonra:
   - ERP'de: **Diğer İşlemler → G.Muhasebe → Entegrasyon Dosyası Oluştur** (XML üretir).
   - Genel Muhasebe'de: **Fiş İşlemleri → Fiş Oluşturma → Transfer Dosyasından Fiş Oluştur** → XML'i seç → "Toplu Fiş Oluşturma" ekranı açılır.
- **Hesap kodu eşleştirme:** Carileri tek bir muhasebe koduyla izlemek için cari kartında **"Muh. Alış Kodu"** ve **"Muh. Satış Kodu"** alanlarına kod yazılır. Çek/senet hesap kodları ayrıca ayarlanır.
- Genel Muhasebe e-Defter ile entegre çalışıyor (WDF9).
- Kaynak: Bilgi Bankası 969.
