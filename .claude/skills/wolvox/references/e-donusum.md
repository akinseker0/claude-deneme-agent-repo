# e-Dönüşüm: e-Fatura, e-Arşiv, e-İrsaliye, e-Defter

## Kapsam

- WOLVOX ERP içinde: **e-Fatura, e-Arşiv, e-İrsaliye, e-Müstahsil**, e-SMM, e-Adisyon.
- **e-Defter:** WOLVOX ERP ve WOLVOX Genel Muhasebe ile entegre (ayrı ürün WDF9).
- e-Arşiv OctoCloud'da da var.
- Belge gönderimi **kontör/kredi** ile çalışır. AKINSOFT hesabında bakiye olmalı.

## Özel entegratörler

AKINSOFT belgeleri anlaşmalı özel entegratörler üzerinden gönderiyor:
- **Digital Planet (DP)**: eskiden beri en yaygın olanı
- **EDM Bilişim**
- **İzibiz**
- **Süper Entegratör**

Wolvox 8 kaynaklarında Digital Planet ve EDM geçiyor. Wolvox 9 kaynaklarında bunlara ek olarak İzibiz ve Süper Entegratör var. Entegratör **servis kullanıcısı bilgileri** güncel olmalı. Parola değişikliği, hesap yetkisi veya servis erişim sorunu gönderimi keser.

## Ayarlar

- Menü: **Satış Yönetimi → Faturalar → e-Fatura → e-Fatura Ayarları**. Kullanıma göre ilgili seçenekler aktif edilir.
- **e-Fatura/e-Arşiv şablonu (XSLT görünümü)** tanımlanabilir.
- **Dış Modül Bağlantı Bilgilerini Gönder:** Fatura sipariş veya irsaliyeden oluşturulduysa, "Bağlantılar" bölümündeki sipariş/irsaliye numaraları e-Faturaya bu ayar açıkken eklenir (Bilgi Bankası 3199).
- **Fatura sayacı / seri:** e-Fatura numarası 16 hanelidir (3 karakter seri + 4 hane yıl + 9 hane sıra). Sayaç 16 hane değilse gönderim hata verir. Hızlı Satış için ayrı e-Fatura/e-Arşiv sayaç tanımı var.
- **e-İhracat faturası** ERP'den gönderilebiliyor.
- Kapsamlı rehber: "Tüm Detayları İle Wolvox e-Fatura İşlemleri" (Bilgi Bankası 1801; Wolvox 8 ve 9 sürümleri var).

## Gelen belgeler

- Gelen e-Fatura, sistemdeki **sipariş** (Bilgi Bankası 3715) veya **irsaliye** (3713) ile eşleştirilebilir.

## Sık hatalar

| Hata | Olası sebep / çözüm |
|---|---|
| **"Tutamaç yanlış durumda"** | Genelde entegratör (Digital Planet) portalındaki teknik çalışmadan kaynaklanır. (1) Entegratörü arayıp çalışma olup olmadığını sor (bayi kaynağında DP için 444 9 328 geçiyor, teyit et). (2) İnternet bağlantısını kontrol et. (3) Entegratör portalına tarayıcıdan girebiliyor ama programdan giremiyorsan güvenlik duvarı/antivirüs programın internet erişimini engelliyordur. |
| **"Invalid InvoiceId"** | Fatura numarası/sayaç formatı hatalı. 16 hane formatını ve seriyi kontrol et. |
| **Kamu faturası gönderilemiyor** | Bilgi Bankası 3042'deki kontrol listesini izle (alıcı kurum bilgileri, kamu faturasına özel alanlar, ödeme bilgileri). |
| **Firma/kişi kontrolü hatası (e-İrsaliye/e-Fatura)** | Genel e-Fatura bilgisine göre: alıcının VKN/TCKN'si ile e-Fatura mükellefiyeti ve etiket (posta kutusu) bilgisi uyuşmuyor. Cari kartındaki vergi no/TC ve mükellef bilgisini güncelle. |
| **"Unable to complete network request to host '127.0.0.1'"** (e-İrsaliye gönderirken) | Program yerel veritabanı/servis bağlantısına ulaşamıyor. Firebird servisi ve Kontrol Paneli çalışıyor mu, port 3050/3055 açık mı bak (`sorun-giderme.md`). |

## Video

- "AKINSOFT WOLVOX 8 ERP e-Fatura, e-Arşiv ve e-İrsaliye İşlemleri" (YouTube: `GrlugoZA0ew`).
