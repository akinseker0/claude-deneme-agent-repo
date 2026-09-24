# Sektörel ve yardımcı programlar

## WOLVOX Hızlı Satış (WWH9): market, perakende, POS

- WOLVOX ERP ve WOLVOX Yazarkasa/Terazi programıyla tam entegre.
- **Yazar kasa / ÖKC:** Satışlar yazar kasadan basılır, ağda birden çok yazar kasa kullanılabilir. **Yeni Nesil ÖKC** destekli cihazlarla online/offline entegrasyon var; yazar kasadaki satışlar anında programa fatura olarak aktarılır.
- **Barkod:** AKINSOFT Barkod programıyla ürün grupları için barkod oluşturma ve etiket basımı.
- **Terazi:** YNÖKC ve online terazi entegrasyonu. Desteklenen elektronik terazilere ürün gönderimi. Desteklenmeyen teraziler için **script** yazılarak dosya üretilebiliyor.
- İade ve değişim kartı, ürün bekletme (bekleme listesi tüm kullanıcılarda görünür).
- Hızlı Satış için ayrı e-Fatura/e-Arşiv sayaç tanımı var. Otomatik e-Fatura gönderimi yapılabiliyor.
- **Fiş tasarımına para üstü, kalan tutar, ödeme toplamı eklemek** (Bilgi Bankası 3543): Tasarıma metin alanları eklenir ve her biri sırasıyla ilgili parametreye bağlanır. Fişin toplamlar bölümünde Toplam, İskonto, KDV ve Para Üstü gösterilir.
- Yardım dosyası: Bilgi Bankası 1487 (Wolvox 8/9), yardım dokümanı 2418.
- "Fiyat Gör" cihazlarıyla entegrasyon var (bayi kaynağı).

## WOLVOX Restoran (WOA9)

- Restoran, kafe, pastane, bar, disko, kulüp, otel restoranı için adisyon ve hesap yönetimi.
- Masa ve adisyon takibi, garson sipariş ekranı, **mutfak yazıcısı** yönlendirme, paket servis ve kurye yönetimi.
- **Garson el terminali (PDA):** iOS (OWR9) ve Android uygulamaları. Masa açma, sipariş alma, mutfağa gönderme, adisyon çıktısı.
- **QR menü** ve tablet menü (müşteri kendi siparişini verir).
- Yemeksepeti, Getir, Trendyol (Yemek) entegrasyonu.
- WOLVOX ERP ve WOLVOX Otel ile tam entegre: Cari, Kasa, Stok, Fatura, Banka ve Adisyon modüllerine doğrudan işler. e-Adisyon destekleniyor.

**Kullanım** (Bilgi Bankası 651):
- **Masa açma ekranı:** hangi masaların boş olduğu ve hangilerinin kalkmak üzere olduğu buradan izlenir. Masa krokisi sistemi de var (2266).
- **Ürünleri adisyona almak:** Ön muhasebedeki stoklar **Dizayn** butonuyla adisyon ekranına aktarılır. Dizayn modunda altta **Ürün Ekle** aktifleşir, ürünler tek tek seçilip departmanlara yerleştirilir. Ürün resmi adisyonda görünsün isteniyorsa stok kartına resim eklenir.
- **Sipariş:** Masayı aç → **Ürün Ekle** → ürünleri seç.

**Diğer özellikler:**
- Satılan menüden hammadde düşümü için otomatik üretim (3680).
- Şubelere tanım kopyalama (3657), otomatik e-Fatura gönderimi (2686).
- **PDA:** Android kurulumu 3687; Android/iOS yardım dosyası 3841. Wolvox 8 Restaurant yardım dosyası da var.

**Restoran ve Restoran Lite** (706): Restoran Lite daha sade bir paket. **Wolvox Veri Transferi** lisansıyla Yemeksepeti, Getir Yemek, Migros Yemek ve Trendyol Yemek entegrasyonu yapılabiliyor. MyFranchise, QR Menü ve MyRezzta sistemleriyle çalışıyor. Tam karşılaştırma tablosu makalede.

## WOLVOX Otel (WHO9)

- Rezervasyon, resepsiyon/ön büro, check-in/out, folyo, oda yönetimi, housekeeping, minibar/ekstra, ön kasa.
- Satış/kontrat, fiyat ve pansiyon planları, acente yönetimi, grup rezervasyon, blokaj, banket/organizasyon, forecast raporları, gün sonu, otel durum raporu, XML raporlar.
- **HotelRunner** entegrasyonu (channel manager üzerinden seyahat sitelerine bağlantı).
- **AKBS / Jandarma** bilgi sistemlerine otomatik kimlik bildirimi.
- Toplu e-posta/SMS. ERP ile tam entegre.
- Hızlı rezervasyon ve check-in, tek tıkla grup girişi. Check-in tarihi bilgisayarın sistem tarihinden alınır.
- Ayarlar: gün sonu sistemi, rezervasyon ekranında cari kayıt izni, mükerrer rezervasyon engelleme, yeni rezervasyonda varsayılan pansiyon ve oda tipi. Otel müşterilerinin ERP carileriyle nasıl eşleşeceği de ayarlanır.
- Yardım dosyası: Bilgi Bankası 1433 (Wolvox 8), 3844 (güncel).
- **Konaklama vergisi:** Otel'de aktif etme 3549. ERP'de fatura kesme script paketi 3561 (`sdk-ve-entegrasyon.md`).

## WOLVOX İnsan Kaynakları (WIK9): bordro ve personel

- Personel kartları, **puantaj ve bordro**, yıllık izin takibi, personel analizi.
- SGK: **e-Bildirge'ye uygun XML**, aylık bildirgeler, işe giriş/çıkış bildirgeleri, vizite kağıtları, işyeri bildirgeleri. SGK online bordro gönderimi.
- **PDKS:** Parmak izi, yüz tanıma, proximity ve barkodlu kartlarla giriş-çıkış takibi.
- İş başvuru ve iş ilanı kayıtları, ziyaretçi takibi.
- **Web portalı:** Çalışanlar kullanıcı adı ve parolayla kendi bilgilerine erişir.
- ERP (ön muhasebe), Genel Muhasebe ve beyanname modülleriyle entegre. Yetkilendirme sistemi var.
- **Puantaj:** Listedeki personele belirtilen ay için otomatik puantaj oluşturulur. Çalışılan gün, hafta sonu gibi bilgiler girilip Tamam'a basılır.
- **Bordro hesaplama:** Listede **kırmızı** satırlar hesaplanmamış, **beyaz** satırlar hesaplanmış personeli gösterir. **"Belirtilen Ay İçin Otomatik Bordro Hesapla"** ile hesaplanır.
- Personel kartında AGİ hesaplaması vardı. AGİ 2022'de kaldırıldığı için güncel sürümde karşılığını kontrol et.
- Yardım dosyası: Bilgi Bankası 1458. Sürüm notu örneği: 1586.

## WOLVOX Servis (VSV9)

`wolvox-erp-moduller.md` dosyasındaki "Servis ve CRM" bölümüne bak.

## WOLVOX Mobil Satış (Android, APD9)

- Plasiyer ve saha satış ekipleri için: araçta fatura kesme, sipariş toplama, tahsilat.
- Cari kart kaydı, fatura, sipariş, irsaliye, çek kaydı, tahsilat ve makbuz yazdırma.
- Anlık stok, fiyat, cari bakiye görüntüleme. Online veri alma/gönderme.
- Bluetooth araç yazıcılarıyla yerinde belge basımı.
- Eski sürüm Windows Mobile (APD8) idi. Yardım dosyası bayi bilgi kütüphanelerinde var.

## WOLVOX Genel Muhasebe (WOG9) ve e-Defter (WDF9)

- Bölümler: hesap planı, fiş işlemleri, tanımlamalar, dönem sonu işlemleri, defterler, mizan/raporlar, mali tablolar, bütçe.
- **Fiş türleri:** Tahsil, Tediye, Mahsup, Açılış, Kapanış. Sık kullanılan fişler için **hızlı fiş girişi tanımları** yapılabiliyor.
- **Hesap planı:** Tek Düzen Hesap Planı'na uygun alt hesaplar açılır. Hesap planı Excel'den aktarılabilir veya başka şirketten kopyalanabilir.
- KDV tanımları yapılıp fiş girişinde KDV hesaplatılıp ayrıştırılabiliyor.
- ERP ve İnsan Kaynakları ile entegre. ERP'den anlık veya toplu fiş aktarımı (`sdk-ve-entegrasyon.md`). WOLVOX Beyanname, Demirbaş ve e-Defter ile tamamlanıyor.
- Yardım dosyası: Bilgi Bankası 1672 (Wolvox 8) / 3851. Beyanname yardım dosyası 1527 ve 578.

## WOLVOX Demirbaş (WOD9)
- Demirbaş ve zimmet yönetimi, envanter ve amortisman takibi.
- Sabit kıymet kaydına genel bilgiler, alış, satış ve amortisman bilgileri girilir, amortismanın yıl ve dönem değerleri hesaplatılır.
- Zamanı gelen amortismanlar kontrol edilip muhasebeleştirilir. Hesaplanan değerler WOLVOX Genel Muhasebe'ye veya İşletme Defteri'ne entegre aktarılır.
- Yardım dosyası: Bilgi Bankası 1508 (Wolvox 8), 3853 (güncel).

## OctoPlus ve OctoCloud

- **OctoPlus (WPL7):** Uygun fiyatlı, basit, paketli ön muhasebe programı. **Paket 2** ve **Paket 4** seçenekleri var (içerik farkı bu bilgi tabanında henüz yok). AKINSOFT'a göre "Türkiye'nin en çok satan muhasebe programı". Küçük işletmeler için Wolvox'a alternatif giriş ürünü.
- **OctoCloud:** Bulut tabanlı ön muhasebe. Web ve iOS/Android uygulaması. e-Arşiv desteği var. AKINSOFT e-Ticaret ile entegre çalışabiliyor.

## AKINSOFT e-Ticaret (IET1)

- B2B ve B2C, pazaryeri/sanal mağaza entegrasyonları, varyant yönetimi, Excel veri transferi, fiyat/stok alarmı, PDF katalog, kampanya yönetimi, dövizli satış, WhatsApp/telefonla sipariş, XML veri paylaşımı, mobil uygulama, blog, çoklu dil.
- WOLVOX ERP ve OctoCloud ile entegre (`sdk-ve-entegrasyon.md`).

## CafePlus (WCP12)

- İnternet kafe, PlayStation salonu, bilardo salonu, laboratuvar ve web filtreleme için.
- Bölümler: Bilgisayar, Vision, Mutfak, PlayStation/Bilardo, Masa. İnternet web filtreleme.
- Yardım dosyası: Bilgi Bankası 2657. Site: cafeplus.com.tr.

## Diğer sektörel programlar

Kuaför/güzellik merkezi, sürücü kursu, akaryakıt, otopark, emlak, sosyal tesisler, eğitim (okul), sağlık, araç satış. Bu programların detayları bu bilgi tabanında henüz yok. Gerekirse akinsoft.com.tr/programlar sayfasından araştır.
