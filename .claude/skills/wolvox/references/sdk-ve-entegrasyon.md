# SDK ve entegrasyonlar

## WOLVOX SDK

- **Ne:** WOLVOX ERP'deki verileri **XML olarak dışarı almak** ve dışarıdan gelen XML'i **ERP'ye kaydetmek** için geliştirme arayüzü.
- **Mimari:** Programlama dilinden bağımsız. **HTTP ve XML** standartlarında, **Kontrol Paneli'ne gömülü** bir servis. Ayrı sunucu kurulmaz; Kontrol Paneli çalışıyorsa SDK da çalışır.
- **İki işlem türü:**
  1. **Veri Raporlama:** Cari listesi, stok listesi gibi verileri XML olarak döndürür.
  2. **Veri Ekleme (kayıt fonksiyonları, "XML Post"):** Belirli formatta hazırlanmış XML'i girdi alır. XML, makalenin ekindeki **örnek formatlara birebir uygun** olmalı.
- **Dönüş değeri (kayıt fonksiyonları):**
  - Başarılı: `BLKODU=1234` (yeni kaydın BLKODU'su)
  - Hatalı: `Error : <Hata Mesajı>`
- **Bağlantı parametreleri:**
  - **Host:** Kontrol Paneli'nin kurulu olduğu bilgisayarın IP'si (yerelde `127.0.0.1`)
  - **Port:** Kontrol Paneli'nin **güncelleme portu** (Kontrol Paneli ayarlarından bak)
  - **Kullanıcı adı / parola:** Kontrol Paneli'nde tanımlı WOLVOX kullanıcısı
  - **Şirket kodu** ve **çalışma yılı**
  - **Ek Şart (SQL):** Raporlamada filtre. Ör. cari listesinde sadece tedarikçileri almak için ilgili tabloya WHERE koşulu.
- **AKINSOFT WOLVOX SDK programı:** Bilgisayara ayrıca kurulan bir test/yardımcı araç. "Komut" alanında iki grup var:
  - **XML Post'a kadar olan komutlar** (ör. cari listesi) veri raporlama içindir.
  - **XML Post altındaki komutlar** XML'den kayıt içindir.
  - Seçilen komutun isteği bu araçla oluşturulup gönderilebiliyor. Aktif tablolara ait alanlar isteğe göre eklenip çıkarılabiliyor.
- **Resmi doküman (PDF):** "AKINSOFT Wolvox9 SDK Doküman" (2024). İçinde "CARİ XML DOSYASI" gibi kayıt örnekleri var.
  - https://akinsoft.net/bilgibankasi/data/upload/257/wolvox9_sdk_dokuman1734088631.pdf
  - https://akinsoft.net/bilgibankasi/data/upload/257/wolvox9_sdk_dokuman1721372145.pdf (eski revizyon)
  - İlgili makaleler: Bilgi Bankası 257 (WOLVOX ERP Programı SDK İşlemleri), 3994 (WOLVOX SDK İşlemleri; WOLVOX 26 ve üzeri için güncel)

> **Bu bilgi tabanına fonksiyon adları, uç nokta (endpoint) adresleri ve XML şemaları henüz işlenmedi.** Oluşturulurken PDF'e erişilemedi. SDK ile kod yazmadan önce yukarıdaki PDF'i oku (WebFetch) ve öğrendiğin fonksiyon, parametre ve XML örneklerini bu dosyaya ekle. Fonksiyon adı veya XML etiketi **uydurma**.

### SDK ile entegrasyon yazarken önerilen yaklaşım
1. Önce Veri Raporlama ile küçük bir okuma yap (ör. cari listesi). Bağlantı, port ve kullanıcı bilgisini doğrula.
2. Veri Ekleme için PDF'teki XML örneğini birebir kopyalayıp **test şirketinde** dene.
3. Dönen metni ayrıştır: `BLKODU=` ile başlıyorsa başarılı, `Error :` ile başlıyorsa hata.
4. Kimlik bilgilerini ortam değişkeninde tut. SDK portunu internete açma; gerekiyorsa VPN kullan.

## Script paketleri

- WOLVOX ERP hazır **script paketleri** yükleyerek genişletilebiliyor: **Yetkili → Tanımlar → Script Paketi İşlemleri** → indirilen dosyayı seç, yükle, parametre değerlerini girip kaydet.
- Örnek: **Konaklama vergisiyle fatura kesme scripti** (Bilgi Bankası 3561). Asgari sürümler: Kontrol Paneli s8.04.12, ERP s8.24.02, Otel s8.08.15. Parametreler: konaklama vergisi oda fiyatına dahil mi (Evet/Hayır), satış ve alış için konaklama vergisi muhasebe kodları. Genel Muhasebe kullanılıyorsa kodlar zorunlu.
  - Ön koşul: ERP genel ayarlar → fatura ayarları → satış faturasında **KDV kullanımı** seçili olmalı. Konaklama vergisi işaretlenince "Döviz Kullan" pasifleşir.
- Hızlı Satış'ta desteklenmeyen teraziler için script yazılıyor. Özel raporlarda da script sekmesi var (`veritabani-ve-sql.md`).

## AKINSOFT e-Ticaret ↔ WOLVOX ERP (Web Entegrasyon, WWB9)

- **WOLVOX Web Entegrasyon programı**, AKINSOFT e-Ticaret sunucusuyla otomatik haberleşir. Siparişleri ERP'ye aktarır. Stok, sipariş, fatura ve cari verileri senkronize edilir.
- e-Ticaret yönetim panelinde: **Entegrasyonlar → Ticari Program Yönetimi → "Tam Senkronizasyon"** seçili olmalı. Böylece ERP'deki tüm stok işlemleri e-Ticaret paneline yansır (Bilgi Bankası 492).

### Bağlantı kurulumu (Bilgi Bankası 2207)
1. **e-Ticaret panelinde:** **Kullanıcılar → Yöneticiler → Yeni Ekle** → tür olarak **"Muhasebe Kullanıcısı"** seçilip kullanıcı oluşturulur.
2. **Web Entegrasyon programında:** **Ayarlar** → **Genel** sekmesi → **Web Sitesi Ayarları**:
   - **Site Adresi:** e-ticaret sitesinin adresi, **`http://` ile** yazılır (`https`'deki "s" olmadan), ör. `http://test.com`.
   - **Kullanıcı Adı / Şifre:** 1. adımdaki muhasebe kullanıcısı.
   - **Test Et** → başarılıysa bağlantı kuruldu.

### Diğer ayarlar
- **Sipariş kayıt ayarları** (3065, 3907):
  - Üye olmadan alışveriş yapan müşteriler, siparişteki bilgilerle ERP'de cari olarak açılabiliyor.
  - e-Ticaret'teki Ek Bilgi, Promosyon Kodu ve Kargo Barkodu alanları, ERP'deki alınan sipariş ekranının özel tanım başlıklarıyla eşleştirilebiliyor.
  - Siparişler aynı anda **iki şirkete** kaydedilebiliyor. 2. şirket için sabit bir cari kodu verilebilir veya boş bırakılırsa her siparişten cari oluşturulur.
- **Cari ayarları** (3068):
  - Müşteri e-Ticaret'te adresini değiştirince ERP'deki cari adresinin otomatik güncellenmesi seçilebiliyor.
  - e-Ticaret'e hangi carilerin aktarılacağı özel kod alanı değerine göre filtrelenebiliyor.
- **Stok ayarları** (3039), **sanal pazar virman hesapları** (3072).
- **Taksit entegrasyonu** (3473; video `86qscM7yBow`, `JJXK_VkTPqk`):
  - ERP'de cariye oluşturulan taksitler e-Ticaret'e aktarılır, müşteri sitede görüp ödeyebilir. Ödenen taksit bir süre sonra ERP'de "Ödendi" olur.
  - Gereksinim: e-Ticaret'te **Online Tahsilat** modülü, ERP'de **Banka** ve **Taksit Takip** modülleri, Kontrol Paneli **s.8.03.96+**, ERP **s.8.22.12+**.
  - e-Ticaret'te Ticari Program Yönetimi ekranında **"Carinin taksit borçları görüntülenebilsin ve ödeme yapılabilsin"** seçeneği işaretlenir.
- **B2B/B2C/müşteri tipine göre ürün gösterimi** (2680):
  1. ERP'de stok tanımlarındaki **Özel Alan Tanımı** ile **veri tipi "Metin"** olan bir alan açılır.
  2. e-Ticaret panelinde **"Gösterilecek Üye Tipi"** bu alanla eşleştirilir. Böylece bir ürün bayilere görünüp üyelere gizlenebilir.
- **e-Ticaret + ERP + Genel Muhasebe** (3119): Web Entegrasyon'un Genel Muhasebe bölümünde **"Yeni Cariler İçin Varsayılan Muhasebe Kodları"** (Alış Kodu, Satış Kodu) tanımlanır. e-Ticaret'ten gelen yeni cariler ERP'ye bu kodlarla kaydolur.
- e-Ticaret tarafında gelişmiş fiyat listesi de var (3510).

### Üçüncü taraf e-ticaret ve pazaryeri entegratörleri
T-Soft, Sentos, Entegra Bilişim, Ayen Software ve Projesoft (B2B) Wolvox entegrasyonu sunuyor. Genelde gereken bilgiler: Wolvox bağlantı/API bilgileri, firma ve ambar/depo tanımları, ürün-varyant kod yapısı, fatura seri/sıra şeması, e-Fatura/e-Arşiv yetkileri.

## WebConnect (IWM9)

- ERP'ye tarayıcıdan (masaüstü, telefon, tablet) erişim sağlayan web uygulaması.
- Cari, Kasa, Stok, Fatura, Sipariş, Servis, İrsaliye, Günsonu ve Restoran raporları. Veri girişi de yapılabiliyor.
- **Kurulum ve bağlantı** (Bilgi Bankası 1526; eski makale 537):
  1. WebConnect'i aç → **Port Ayarları**. Varsayılan çalışma portu **8888**. Başka program kullanıyorsa değiştir.
  2. Bu portu modemden WebConnect bilgisayarına yönlendir.
  3. Kontrol Paneli → **Kullanıcı İşlemleri → Kullanıcı Yetkilendirme** → personeli ve şirketi seç → **Program Kullanım Yetkileri**'nde **WebConnect**'i işaretle → Yetkileri Kaydet.
  4. Tarayıcıdan `http://<sabit-dış-IP>:8888` adresine gir.
- MSSQL kullanılıyorsa **SQL Server 2012+** gerekir.

## WOLVOX Reporter (ARP2) ve mobil uygulamalar

- Android'den ERP'ye bağlanıp rapor alma.
- Mobil Satış (APD9) sahada senkronize çalışıyor (`sektorel-programlar.md`).
- Mobil uygulamalarda güncelleme paketi (WOL UP/GP) kontrolü var (Bilgi Bankası 3868).

## WOLVOX ERP ↔ Genel Muhasebe

Entegrasyon iki yolla yapılır:
1. **Anlık entegrasyon:** ERP'de **"Genel Muhasebe Sistemi Kullan"** işaretlenir ve **Anlık Entegrasyon** seçilir. ERP'deki işlemler anında Genel Muhasebe'ye yansır.
2. **Toplu entegrasyon:** Aynı ayarda **Toplu Entegrasyon** seçilir. Sonra:
   - ERP'de: **Diğer İşlemler → G.Muhasebe → Entegrasyon Dosyası Oluştur** (XML üretir).
   - Genel Muhasebe'de: **Fiş İşlemleri → Fiş Oluşturma → Transfer Dosyasından Fiş Oluştur** → XML'i seç → "Toplu Fiş Oluşturma" ekranı açılır.
- **Hesap kodu eşleştirme:** Carileri tek bir muhasebe koduyla izlemek için cari kartında **"Muh. Alış Kodu"** ve **"Muh. Satış Kodu"** alanlarına kod yazılır. Çek/senet hesap kodları ayrıca ayarlanır.
- Genel Muhasebe e-Defter ile entegre çalışıyor (WDF9). Demirbaş amortismanları da Genel Muhasebe'ye aktarılabiliyor.
- Kaynak: Bilgi Bankası 969. Video: Ufuk Aydın, "Wolvox Genel Muhasebe Nasıl Kullanılır? Entegrasyon ve Örnekli Anlatım" (`E4VGhPMoRcQ`).
