# e-Dönüşüm: e-Fatura, e-Arşiv, e-İrsaliye, e-Defter

## Kapsam

- WOLVOX ERP içinde: **e-Fatura, e-Arşiv, e-İrsaliye, e-Müstahsil**, e-SMM, e-Adisyon, **e-İhracat faturası**.
- **e-Defter:** WOLVOX ERP ve WOLVOX Genel Muhasebe ile entegre (ayrı ürün WDF9).
- e-Arşiv OctoCloud'da da var. Hızlı Satış ve Restoran programlarından **otomatik e-Fatura gönderimi** yapılabiliyor (Bilgi Bankası 2686).
- Belge gönderimi **kontör/kredi** ile çalışır. AKINSOFT hesabında bakiye olmalı.

## Özel entegratörler

AKINSOFT belgeleri anlaşmalı özel entegratörler üzerinden gönderiyor:
- **Digital Planet (DP)**: eskiden beri en yaygın olanı
- **EDM Bilişim**
- **İzibiz**
- **Süper Entegratör**

Wolvox 8 kaynaklarında Digital Planet ve EDM geçiyor. Wolvox 9 kaynaklarında bunlara ek olarak İzibiz ve Süper Entegratör var. Entegratör **servis kullanıcısı bilgileri** güncel olmalı. Parola değişikliği, hesap yetkisi veya servis erişim sorunu gönderimi keser.

## Ayarlar

- **e-Fatura sistemini açma:** Kontrol Paneli → **Şirket Kayıt İşlemleri → e-Devlet 1** → **"e-Fatura Sistemini Kullan"**.
- **e-Fatura ayarları:** ERP'de **Satış Yönetimi → Faturalar → e-Fatura → e-Fatura Ayarları**. Kullanıma göre ilgili seçenekler aktif edilir.
- **Sayaç (belge numarası):** **Yetkili → Sayaç İşlemleri → Sayaç Tanımları**.
  - e-Fatura numarası 16 hanedir: 3 karakter ön ek + 4 hane yıl + 9 hane sıra numarası (GİB standardı).
  - Sayaç hane sayısı sıra kısmını 9 haneye tamamlayacak şekilde seçilir. **"Başa Ekle"** alanına belge türünü ayıran kısa ön ek yazılır (e-Fatura, e-Arşiv ve e-İhracat için ayrı ayrı).
  - Hızlı Satış için ayrı e-Fatura/e-Arşiv sayaç tanımı var.
- **e-Fatura/e-Arşiv şablonu** (görünüm tasarımı) tanımlanabilir.
- **Dış Modül Bağlantı Bilgilerini Gönder:** Fatura sipariş veya irsaliyeden oluşturulduysa, "Bağlantılar" bölümündeki sipariş/irsaliye numaraları e-Faturaya bu ayar açıkken eklenir (Bilgi Bankası 3199).
- Fatura ve irsaliyedeki **not bilgileri** e-Fatura, e-Arşiv ve e-İrsaliye gönderiminde belgeye aktarılabiliyor. Şahıs faturalarında ticari unvan bilgisi ad-soyad alanına aktarılır.
- Bir firmanın e-Fatura mükellefi olup olmadığı GİB'in kayıtlı kullanıcı listesinden kontrol edilebilir (efatura.gov.tr).
- Kapsamlı rehber: "Tüm Detayları İle Wolvox e-Fatura İşlemleri" (Bilgi Bankası 1801; Wolvox 8 ve 9 sürümleri var).

## Kamu kurumlarına e-Fatura (Bilgi Bankası 2146, 3042)

19.03.2021'den beri kamu faturalarında **IBAN** ve ödemeyi yapacak **harcama biriminin VKN'si** zorunlu.

1. **IBAN:** Kontrol Paneli'nde şirketin banka bilgilerine girilir, e-Faturaya banka hesap bilgisi olarak eklenir. `TR` ile başlamalı ve boşluksuz yazılmalı.
2. **Cari kartı:** **Cari tanımları → Hesap Bilgileri → "Kamu Kurumu"** işaretlenir. Bu carinin satış faturasında fatura tipi otomatik **KAMU** olur.
3. **Harcama Birimi VKN:** Satış faturasında e-Fatura bölümündeki **soru işareti (?)** butonu → "Diğer Bilgiler" → **Harcama Birimi Vergi No** doldurulur. Genel bütçeli kurumlarda bu VKN faturanın kesildiği VKN ile aynıdır. Özel bütçeli kurumlarda genelde farklıdır.

**Kamu faturası hata verirse kontrol listesi (3042):**
- Asgari sürüm: **Wolvox ERP 8.19.03**, **Kontrol Paneli 8.03.58**.
- Cari kartındaki vergi numarasının sonunda **boşluk olmamalı**. Cari e-Fatura mükellefi olmalı.
- "Kamu Kurumu" işaretli mi? Harcama Birimi VKN boş mu?
- Kontrol Paneli → Şirket Kayıt İşlemleri → e-Devlet 1 → "e-Fatura Sistemini Kullan" işaretini kaldır, Kontrol Paneli'ni kapat-aç, tekrar işaretle, sonra faturayı yeniden gönder.

## Gelen belgeler

**Gelen e-Faturayı siparişle eşleştirme (Bilgi Bankası 3715):**
1. e-Fatura gelen kutusu modülünde faturayı içeri alırken sağdaki eşleştirme alanında **sipariş seçim** butonuna bas.
2. Açılan sipariş raporundan ilgili alış siparişini seç → Tamam. Seçilen sipariş sağdaki listeye gelir.
3. Eşleşen siparişin cari ve stok hareketlerine işlenmesi isteniyorsa sağ üstteki ilgili kutuları işaretle.

**Gelen e-Faturayı irsaliyeyle eşleştirme** aynı mantıkla yapılır (Bilgi Bankası 3713).

## e-İhracat
ERP'den e-İhracat (gümrüklü satış) faturası gönderilebiliyor (Bilgi Bankası 719). Ayrı sayaç ön eki kullanılır.

## Sık hatalar

| Hata | Olası sebep / çözüm |
|---|---|
| **"Tutamaç yanlış durumda"** | Genelde entegratör (Digital Planet) portalındaki teknik çalışmadan kaynaklanır. (1) Entegratörü arayıp çalışma olup olmadığını sor (bayi kaynağında DP için 444 9 328 geçiyor, teyit et). (2) İnternet bağlantısını kontrol et. (3) Entegratör portalına tarayıcıdan girebiliyor ama programdan giremiyorsan güvenlik duvarı/antivirüs programın internet erişimini engelliyordur. |
| **"Invalid InvoiceId"** | Fatura numarası/sayaç formatı hatalı. 16 hane formatını ve ön eki kontrol et. |
| **Kamu faturası gönderilemiyor** | Yukarıdaki kontrol listesine bak (3042). |
| **Firma/kişi kontrolü hatası (e-İrsaliye/e-Fatura)** | Genel e-Fatura bilgisine göre: alıcının VKN/TCKN'si ile e-Fatura mükellefiyeti ve etiket (posta kutusu) bilgisi uyuşmuyor. Cari kartındaki vergi no/TC ve mükellef bilgisini güncelle. Vergi no sonunda boşluk olmasın. |
| **"Unable to complete network request to host '127.0.0.1'"** (e-İrsaliye gönderirken) | Program yerel veritabanı/servis bağlantısına ulaşamıyor. Firebird servisi ve Kontrol Paneli çalışıyor mu, port 3050/3055 açık mı bak (`sorun-giderme.md`). |

## Video

- "AKINSOFT WOLVOX 8 ERP e-Fatura, e-Arşiv ve e-İrsaliye İşlemleri" (YouTube: `GrlugoZA0ew`).
