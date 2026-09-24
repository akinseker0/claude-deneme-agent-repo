# WOLVOX ERP modülleri ve iş akışları

## Modül listesi

Resmi tanıtımda geçen modüller:

- **Genel:** çoklu dil desteği, yönetici ekranı, şube sistemi, offline çalışma sistemi
- **Finans:** cari (müşteri/tedarikçi) kartları, kasa, banka, çek/senet, dövizli işlemler, pazarlama
- **Stok:** stok (malzeme) kartları, depo, depo lokasyon yönetimi, barkod sistemi, seri no takip, garanti takip, LOT takip, promosyon yönetimi
- **Satış/Satın alma:** teklif, sipariş, irsaliye, fatura, satın alma süreç yönetimi
- **e-Dönüşüm:** e-Fatura, e-Arşiv, e-İrsaliye (ayrıntılar `e-donusum.md` dosyasında)
- **Üretim:** üretim, MRP II, fason takip yönetimi
- **Müşteri:** CRM, mobil CRM, servis
- **Perakende/Sektörel:** perakende mağazacılık sistemi, restoran sistemi, garson el terminali, yazar kasa entegrasyonu, terazi entegrasyonu

Hitap ettiği sektörler: elektrik-elektronik, telekom, bilişim, döviz büroları, otomotiv, sigortacılık, market, tekstil, maden, inşaat, taşıma, gıda, üretim, turizm, mali müşavirler.

Eski paket isimleri (Wolvox 7/8 dönemi bayi listelerinde geçer): "Paket-4" = Cari 1, Kasa, Stok 1, Fatura, Çek Senet, İrsaliye, Teklif, Sipariş, Döviz, Depo, Banka, Transfer, Analiz. Stok-2, Cari-2 gibi gelişmiş modüller ayrı satılırdı. WOLVOX 26'da paketlerin yerini esnek modül seçimi aldı.

## Temel kavramlar

- **Şirket ve çalışma yılı:** Her şirket Kontrol Paneli'nde tanımlanır. Veriler şirket ve çalışma yılı (dönem) bazında tutulur. Yıl geçişi "Devir İşlemleri" ile yapılır (`kurulum-ve-yonetim.md`).
- **Kart / hareket ayrımı:** Ana kayıtlar "kart" (cari kartı, stok kartı), bunlara bağlı işlemler "hareket" (cari hareketi, stok hareketi). Veritabanında da `CARI` / `CARIHR`, `STOK` / `STOKHR` diye ayrılır.
- **BLKODU:** Her kaydın benzersiz iç numarası. Bağlantılar bu numarayla kurulur (`veritabani-ve-sql.md`).

## Satış süreci

Akış: **Teklif → Sipariş → İrsaliye → Fatura**. Her adım bir öncekinden aktarılarak oluşturulabilir.

- Fatura ekranına menüden ulaşılır: **Satış Yönetimi → Faturalar** (Alış Faturası / Satış Faturası).
- Sipariş ve irsaliye numarasının e-Faturada görünmesi için sipariş irsaliyeye, irsaliye faturaya aktarılmalı. Ayrıca e-Fatura Ayarları'nda **"Dış Modül Bağlantı Bilgilerini Gönder"** açık olmalı. Bilgiler faturanın "Bağlantılar" bölümünden gelir.
- Gelen e-Fatura, sistemde kayıtlı sipariş veya irsaliye ile eşleştirilebilir (Bilgi Bankası 3713, 3715).
- **Mal fazlası çalışma sistemi** destekleniyor (Bilgi Bankası 1060).
- **Gelişmiş satış fiyat listeleri** tanımlanabiliyor (Bilgi Bankası 311). Veritabanında `STOK_FIYAT_LISTE` ve `STOK_FIYAT_LISTE_DT` tablolarında durur.
- Fatura üzerinde formül tanımlama yapılabiliyor.

### Fatura tasarımı (fatura dizayn)
1. Alış veya satış faturası listesinden bir faturanın içine gir.
2. **İşlemler → Şablon Seçenekleri**.
3. Şablon adını yaz, **Yeni Şablon Ekle** ile kaydet.
4. Şablonu seç, **Göster** → **Rapor Tasarımı** ile tasarım ekranını aç.
5. Logo, birim fiyat, miktar, stok adı/kodu gibi alanları ekle. Logo için nesnenin çark simgesi → üç nokta ile dosya seçilir, boyut/konum ölçülendirme alanından ayarlanır.
6. Sol üstteki menü simgesinden kaydet.

Hızlı Satış fiş tasarımına para üstü, kalan tutar ve ödeme toplamı eklenebiliyor (Bilgi Bankası 3543). Wolvox 9 için hazır veritabanı ve dizaynlar Bilgi Bankası 3836'da.

## Stok yönetimi

- Stok, hizmet, depo, lokasyon, marka, model, renk-beden, fiyat ve paket tanımları.
- Çoklu depo ve şubeler arası transfer. Raf lokasyonu (adresleme) ile toplama/yerleştirme.
- **Sayım:** sayım modülü fark fişlerini oluşturur. El terminaliyle depo sayımı yapılabilir.
- Seri no, LOT, garanti takibi. Negatife düşen stoklar üretimle otomatik tamamlanabilir.

## Finans

- **Cari:** müşteri/tedarikçi kartları. Grup, ara grup, alt grup ve döviz kullanımı alanları var. Genel Muhasebe entegrasyonu için "Muh. Alış Kodu" / "Muh. Satış Kodu" alanları.
- **Kasa, banka, döviz.**
- **Çek/senet:** keşideci, borçlu/alacaklı, vade, tutar, banka/şube, belge türü ve portföy durumu tutulur. Ödeme, tahsil, ciro ve bankaya gönderme işlemleri yapılır. Toplu çek/senet girişi, teminat çek/senetleri ve kısmi ödeme destekleniyor. Günlük, haftalık ve aylık vade listeleri nakit akışını gösteriyor. Banka modülüyle birlikte kullanılınca bankaya gönderilen çeklerin hareketi izleniyor. Genel Muhasebe hesap kodları ayrıca ayarlanmalı.

## Üretim

İki seviye var:
- **Basit üretim:** üretim reçetesi, birleştirme/parçalama üretimi, siparişten üretime aktarım, üretim planlama ve hammadde tedarik listesi, seri/lot üretimi.
- **MRP II:** operasyonların adım adım tanımı, kayıp zaman takibi, hammadde giriş kontrol raporları, Gantt şeması, kalite kontrol raporları. İş emirleri tek, günlük veya saatlik olarak oluşturulabiliyor.
- **Fason takip** ayrı modül.

## Servis ve CRM

- **Servis modülü:** teknik servise giren ürünün girişinden teslimine kadar iş akışı, yapılan işlemlerin detaylı kaydı ve raporu, bakım sözleşmeleri, yerinde servis randevuları, seri no ve garanti takibi. Otomotiv, beyaz eşya, bilgisayar, cep telefonu gibi servisler için. Ayrı ürün olarak VSV9 da var.
- **CRM:** aktiviteler. Kullanıcı yetkilerinde "CRM Aktivite" görme yetkisi ayrıca tanımlanıyor. Mobil CRM de var.

## Diğer

- **Excel transfer:** cari/stok kartları Excel'den alınıp verilebilir (`kurulum-ve-yonetim.md`).
- **Özel raporlar / SQL Monitör:** `veritabani-ve-sql.md`.
- **Genel Muhasebe entegrasyonu:** `sdk-ve-entegrasyon.md`.
