# Bilgi Bankası makale özetleri

AKINSOFT Bilgi Bankası makalelerinin **tam metinleri okunarak** (2026-09-24) çıkarılmış kısa özetler. Her maddedeki `[no]` makale numarasıdır. Tam metin için `python tools/bilgibankasi.py oku <no>` veya `https://bilgibankasi.akinsoft.net/tr/home/makale/<no>-...` (adres `bilgibankasi-dizini.json` dosyasında). Özetler kendi cümlelerimizle yazıldı; ekran görüntüleri ve ayrıntılı tablolar için makalenin kendisine bak.

Menü yolları Wolvox 8/9 masaüstü içindir. WOLVOX 26/WolvoxCloud farkları için `menu-haritasi.md` dosyasına bak.

## WOLVOX ERP Ön Muhasebe

### Modül paketleri: hangi özellik hangi modülde
- **[730] Stok 1 ile Stok 2 farkı.** Stok 2'ye özgü olanlar:
  - asorti sistemi, ana stok/alt stok, stoğa dosya ve resim ekleme, bloke/termin
  - diğer birimler, ek barkod, tedarikçi ve alternatif stok tanımı, stok bakiye uyarıları, olması gereken stok limitleri
  - **gelişmiş iskonto sistemi**, **gelişmiş satış fiyatı sistemi**, fiyat istatistikleri
  - stok sayımı ve düzenleme, stok tanım birleştirme, kâr/zarar raporları, yeterlilik ve analiz raporları
  - Seri etiket için Kartoteks modülü, promosyon ve bonus için kendi modülleri gerekir. Tam tablo makalede.
- **[731] Cari 1 ile Cari 2 farkı.** Cari 2'ye özgü olanlar:
  - departman ve not tanımları, resmi tatiller, toplu cari hareket
  - valör hesaplı rapor, manuel yaşlandırma, yaşlandırma raporları, KPB esaslı/hareketli/valörlü bakiye listeleri
  - dönemsel hareket raporları, cari analizleri, gün sonu raporları
  - adres tanımları (fatura ve sevk adresi), cariye resim/dosya ekleme, yetkililer, risk notları, nüfus bilgileri
  - Pazarlamacı raporları için Pazarlama modülü, bonus için Bonus modülü gerekir.
- **[655] Servis modülü** en az Cari 1 ve Stok 1 ister. İsteğe bağlı olarak Stok 2, Seri No, Döviz, Fatura, İrsaliye ve e-Ticaret ile çalışır. Caller-ID için uyumlu cihaz gerekir.
  - Akış: işlem tanımları → servis fişi (servis işlemleri sayfası) → teslim.

### Satış, fatura, iskonto, fiyat
- **[643] Fatura türleri:** yurt içi satış, yurt içi satıştan iade, yurt dışı satış (KDV hesaplanmaz), yurt dışı satıştan iade, alış, alıştan iade.
  - Alış ve satış faturalarının işleyişi aynıdır.
  - Alış faturasında **Ek Bilgiler → Ek Maliyet** ile nakliye gibi ek maliyetler stok maliyetine yansıtılır; kâr/zarar ek maliyet öncesi ve sonrası hesaplanabilir.
- **[648] Masraf faturası:** kırtasiye, fatura ödemesi gibi giderler için.
  - Hareket satırına eklenecek hizmetler önce Stok Yönetimi'nde **hizmet tanımı** olarak açılır.
  - Birden fazla ödeme şekliyle kapatılabilir ("ödeme ekle").
  - **Zamanlı Hesaplar**'a aktarılırsa aidat gibi düzenli ödemeler için zamanı gelince uyarı verir. Kopyalanabilir.
- **[628] İskonto tanımları (gelişmiş iskonto sistemi):**
  - Açmak için: Yetkili → Genel Ayarlar → Stok Ayarları → "Gelişmiş iskonto sistemi". **Stok 2 modülü gerekir.**
  - Açılınca **stok kartlarındaki iskonto oranları geçersiz olur.**
  - Cari grubu × stok grubu bazında iskonto tanımlanır.
  - Miktar iskontosu için ayrıca "Miktar aralığına göre iskonto sistemi kullan" açılmalı.
- **[629] İskonto kısıtlama:** Personel bazında azami iskonto oranı tanımlanır. İki şekli var:
  - **Toplam tutar:** belgedeki satırların iskonto ortalaması sınırı aşamaz.
  - **Hareket bazında:** her satır için ayrı sınır. Stok, grup, marka veya model bazında olabilir.
- **[626] Satış fiyat listesi:**
  - Açmak için: Yetkili → Tanımlar → Genel Ayarlar → Stok Ayarları → Genel → "Gelişmiş Satış Fiyatı Sistemini Kullan".
  - Açılınca **stok kartındaki satış fiyatı alanları pasifleşir** ve birçok ekranda fiyat seçimi engellenir.
  - Liste alanları: adı, para birimi, durum (Beklemede/Aktif/Tamamlandı/İptal), geçerlilik tarihi, şubeler, özel kod, cari kapsamı, gruplandırma, günler.
- **[443] Promosyon modülü:**
  - Tanım: Satış Yönetimi → **Promosyon Tanımları**.
  - Alanlar: ad (ör. "3 al 2 öde"), durum (pasif promosyon hesaplanmaz), geçerlilik tarihi, şubeler, gün ve saat kısıtı (ör. salı günleri, 18:00–20:00), müşteri kapsamı (cari, grup, ülke/il/ilçe), ürün kapsamı (ürün, marka, model, grup).
- **[572] Bonus sistemi:**
  - Açmak için: Yetkili → Genel Ayarlar → Cari kart ayarları → "Bonus sistemi kullan".
  - Bonus matrahı üç şekilde olabilir: iskonto öncesi ara toplam, iskonto sonrası ara toplam veya genel toplam (KDV dahil).
  - Bonus ödeme türü: **kapalı fatura** (fatura kapatırken bonus seçeneği çıkar) veya **iskonto** olarak.
- **[1621] Belge onay sistemi** (sürüm 8.12.01+):
  - Kapsam: yurt içi/dışı alınan/verilen teklif ve siparişler.
  - Tanım: Yetkili → Tanımlar → **Belge Onay Tanımları**. Tutar aralığına göre çok seviyeli onaycılar belirlenir; bir seviyede "n kişiden k'sinin onayı" gibi kurallar kurulabilir.
  - Akış: kullanıcı belgeyi kaydeder → İşlemler → Belge Onay Bilgileri → **onaya gönderir** (gönderildikten sonra belge değiştirilemez) → onaylanınca işleme devam edilir.
  - Onay e-postaları için: Yetkili → Tanımlar → Mail/Sms Şablonları.
- **[1986] Teklif/sipariş çıktısına stok resmi eklemek:**
  1. Yetkili → Özel Tanımlar → Özel Ayarlar → Teklif Ayarları (veya Sipariş Ayarları) → "Teklif yazdırırken stok resmini çek".
  2. Belgede Yazdır → **Aktif Raporu Tasarla** → "DB Bağlantılı Resim Ekle".
  3. Grup "Teklif Raporları", tablo "Teklif Yazdırma Özel Değerler", alan **STOK_RESIM**. Kaydet (Ctrl+S).
- **[1966] e-Fatura/e-Arşiv/e-İrsaliye'de döviz kurunu göstermek:**
  1. e-Fatura Ayarları → **Opsiyonel Alanlar** → "Fatura Hareket" alanına kur tanımlarını ekle.
  2. Gönderimden sonra oluşan XML program dizinindeki `Temp\<kullanıcı>\Efatura_Giden` klasöründe durur.
  3. Bu XML'i entegratöre gönderip görünüm tasarımına ekletmek gerekir.

### Stok ve depo
- **[613] Toplu stok hareketi:**
  1. "Stok Bul 2" ile stokları seç.
  2. Miktar, işlem türü ve fiyatı gir. Excel'den de alınabilir.
  3. **"Hrk. İşle"** ile işle. İşlenmeden çıkılırsa kaydedilmez.
- **[624] Toplu depo transferi:** Kaynak ve hedef depo seçilir. Stok listesi "Dosyadan Bilgi Al" ile Excel/metinden veya "İçe Aktar" ile bir fatura/siparişten alınabilir.
- **[625] Lokasyon tanımları:**
  - Depoya kroki eklenir, alt lokasyonlar (koridor → raf ağacı) tanımlanır.
  - **Lokasyon hareket girişi ayrı bir stok hareketi oluşturmaz.** Önce depoya stok girişi yapılır, sonra lokasyonlara dağıtılır.
- **[1855] Karekod ile stok takibi (Wolvox 8):** Önce stok ayarlarından karekod tanımları yapılır. Sonra barkod alanına karekod okutulunca stok yoksa kaydedilir, varsa bilgileri gelir.
- **[1585] Depozito:**
  - Boş ve dolu olmak üzere iki stok kartı açılır, dolu stoğa depozito stoğu bağlanır.
  - Hızlı Satış'ta dolu ürün satılınca depozito stoğu alt kalem olarak otomatik düşer.
- **[639–641] Tüp/Su modülü:**
  - Tüp/su fişi, dolu ↔ boş stok **değişim tanımları**, rehin takibi, Caller-ID ile arayan müşteriyi tanıma.
  - Fişler tek tek veya toplu faturalanır ("Tüp/Su Fişi Faturalandırma").
  - Kısayollar: F5 cari bul, F6/Shift+F6 stok ekle, Shift+F3 satır sil, Ctrl+F8 stok kartı, Ctrl+F7 fiyatlar.
- **[564] Sevkiyat planlama:**
  1. Önce İrsaliye modülünde **Araç Tanımları** (plaka, şoför, kapasite) yapılır.
  2. Sonra İrsaliye → **Sevkiyat Planlama**: kaynak olarak onaylı siparişler veya faturalanmamış irsaliyeler seçilir, araçlara yüklenir.
  3. Yükleme tamamlanınca durum "Tamamlandı" yapılır ve giden irsaliyeye aktarılır.

### Üretim
- **[630] Üretim reçetesi (normal):**
  - Alanlar: stok, üretim kodu/adı, depo, durum, planlama miktarı, diğer maliyetler, stok bloke, hesap türü, "Şubelerde ortak kullan".
  - Mamul bilgilerinde fire oranı ve ara maliyetler net maliyeti belirler.
- **[631] Parçalama reçetesi:** Bir veya birkaç stoktan birden çok stok üretilir (ör. A+B → C, D, E). Üretilen her ürünün maliyeti, tüketilen tutarın **maliyet yüzdesi** ile dağıtılır.
- **[632] Eksiye düşen stokları otomatik üret:**
  - Reçetesi olan ürünler eksiye düşünce listelenir ve üretilir.
  - Otomatik çalışması için: Özel Ayarlar → Üretim Ayarları → "Eksiye düşen stokları otomatik üret", kontrol aralığı ve varsayılan depo seçilir.
- **[580] MRP II tanımları:**
  - Makine vardiya/mola ve duruş tanımları (ör. elektrik kesintisi).
  - **İş merkezleri** (boyahane, CNC). Personel yetkilendirmesiyle online iş merkezinde herkes sadece kendi operasyonlarını görür.
  - **Operasyon tanımları:** tür doğru seçilmeli; dışarıdan alınan ürün için "Tedarik", fason için ilgili tür.

### Finans: çek/senet, valör, CRM
- **[633] Çek/senet giriş:**
  - Vade, evrak no, tür, tutar ve banka girilir, cari kayıtta seçilir. Geçmiş tarihli evrakta harekete özel döviz kuru girilebilir.
  - **Havuz sistemi:** döviz çeki TL bakiyeden düşülecekse "Döviz Hesabına İşle" → "Havuz Sistemine Gönder". Havuzdaki evrak cari bakiyeye işlemez; tahsil veya ciro edilince belirlenen kurdan işlenir. Takip için cari hareket raporunda "Havuz sistemindeki evrakları ekle".
  - **Devir** işaretli evrak bakiyeye işlemez ama durum değişiklikleri işler.
  - Yanlış durum değişikliği "Son Yapılan İşlemi Sil (Shift+F3)" ile geri alınır.
- **[634] Çek/senet bordrosu:**
  - Bir cariye toplu evrak girişi yapılır. "Toplu Giriş" (ilk vade, vade artışı, adet, tutar) → Uygula → **"Hrk. İşle"**.
  - **İşlenmeyen bordro bakiyeye etki etmez.** "Kopyala" üst satırı çoğaltır.
- **[635] Kısmi tahsilat/tediye:** Kısmi ödeme evrak kaydına yansımaz. Sonraki işlemler bu ekrandan izlenmeli.
- **[636] Teminat çek/senedi:**
  - Kayıt anında bakiyeye etki etmez.
  - "Teminat senedi arkasından düşme" + "Hızlı Ödeme" ile kısmen veya tamamen tahsil edilince bakiyeye yansır.
- **[637] / [638] Valör hesaplı raporlar** (çek/senet ve cari hareket):
  - Ortalama vade = Σ(vade günü × tutar) / Σ tutar.
  - 30 günlük vade oranı ve opsiyon günü girilebilir, işlem veya vade tarihi baz alınabilir.
- **[581] CRM:**
  - Cari kartlardan aktiviteler, kampanyalar, destekler, servis ve belgeler görülür.
  - **Kampanyalar:** bütçe, durum, hedef kitle, "Ulaşıldı" işareti.
  - **Satış fırsatları** ve proje/satış takibi.

### Genel kullanım
- **[610] Tüm raporlarda ortak özellikler:**
  - Kriter sayfaları: **Hareket** (Alt+H, alan filtresi), **Aralıklar** (Alt+R, tarih vb. aralık), **Sıralama** (Alt+S, "Ters" ile tersten).
  - Rapor penceresi ortak düğmeler ve dışa aktarma ayrıntıları makalede.
- **[1985] Veri değişim logları:**
  - Açmak için: Yetkili → Veri Değişim Log → Veri Değişim Log Ayarları → "Veri değişimi için log sistemini kullan" → izlenecek tablo ve alanları seç (tablo başına en fazla 50 alan).
  - Rapor: Yetkili → Veri Değişim Log → Veri Değişim Logları.
  - **Performansı düşürebilir ve veritabanını büyütür.** Sadece gerekli alanları izle.
- **[484] Cep telefonu girilen cari kaydedilirken "Veri tabanı bağlantısı koptu" hatası:** Makale ekindeki `WolvoxUDF7.dll` dosyası `C:\Program Files\Firebird\Firebird_2_5\UDF` klasörüne kopyalanır. Firebird UDF eksikliği.
- **[652] Wolvox 8 upgrade** (OctoPers, OctoPlus, Wolvox 6/7'den):
  - Kontrol Paneli bir kez **yönetici olarak** çalıştırılır. "Wolvox 7'den upgrade yapılsın mı?" sorusuna Evet denir, ya da sonra Upgrade → "Wolvox 8 Upgrade".
  - Wolvox 7'den tüm veri ve ayarlar gelir. Diğer kaynaklarda modül seçilir.
  - **İki sürüm aynı portu kullanamaz.** Upgrade sırasında Wolvox 7'yi kapat; Wolvox 8'de de aynı portları (3055/3056) kullan.
- **[1673]** Kullanıcı kaydı ve yetkilendirme `kurulum-ve-yonetim.md` dosyasında. Hızlı yetkilendirmeyle bir personelin yetkileri başka personele, bir şirketin yetkileri başka şirkete kopyalanabilir. CRM aktivite yetkisi başkalarının kayıtlarını görme, ekleme, düzenleme ve silmeyi ayrı ayrı kapsar.
- **[1684]** Firebird ↔ MSSQL transferi `kurulum-ve-yonetim.md` dosyasında. Makalede MSSQL'den Firebird'e geri dönüş adımları da var.

## Genel sorunlar ve ipuçları (ERP)

### Kayıt işlemleri
- **[12] Silinen faturayı geri almak:** Fatura → Fatura Dökümü → soldaki **Yetkili** → "Silinen kayıtları göster" → filtrele → **"Aktif Kaydı Geri Al"**. Silinen kayıtlar veritabanında işaretli olarak durur. Aynı mantık cari ve stok hareket raporlarında da var.
- **[16] / [644] Fatura kopyalama** (şirketler arası da olur):
  1. Fatura → **Fatura Kopya Oluşturma** → faturaları seç (Ctrl/Shift) → "Seçilenleri Kopyala" → `.fkd` dosyası kaydedilir.
  2. Hedef şirkette yeni fatura → İşlemler → **"Kopyala 2"** → dosyayı seç. Tarih ve numara değişsin mi sorulur.
  3. Her fatura tek tek kaydedilir. Hedefte olmayan cari ve stoklar otomatik açılır.
  - Aynı şirkette farklı türe (satış → alış, iade…) kopyalamak için: İşlemler → Kopyala.
- **[952] / [958] Cari veya stok kartını tamamen silmek:**
  1. Kartın hareket raporunu aç, her hareketi açıp sil.
  2. Rapor içinde Yetkili → "Silinen Kayıtları Göster" → her birini **"Aktif Kaydı Veritabanından Sil"**.
  3. En son kartı sil.
  - **Geri alınamaz, önce yedek al.**
- **[1820] "Aktif kayıt önceki dönemlere ait olduğu için kayıt üzerinde işlem yapılamaz":** Yetkili → Genel Ayarlar → Program Ayarları → "Hareketler için tarih kontrolü" → **Kontrol Etme**. Sürerse destek kaydı açılır (musteri.akinsoft.net / bayi.akinsoft.net → Ticket).

### Ayarlar
- **[1039] Miktar veya fiyat yuvarlanıyor** (1,50 → 2): Yetkili → Tanımlar → Genel Ayarlar → Stok Ayarları → Stok Kart Ayarları → **Miktar Hassasiyeti**, **2. Birim Hassasiyeti**, **Birim Fiyat Hassasiyeti** basamak sayısını artır.
- **[664] Sayısal alanlarda formül:** Ondalık alanlara `(85*18)/100` gibi ifade yazılabilir. `Abs`, `Ceil`, `Floor` gibi fonksiyonlar da var (Wolvox 8+).
- **[230] Yeni TL simgesi:** Yetkili → Tanımlar → Genel Ayarlar → Parasal Ayarlar → KPB → "Yeni TL Simgesine Göre Kullan" (AbakuTLSymSans fontu).
- **[426] Joker karakter aramaları:** F7 "Filtre Düzenleme" → Joker Karakter. Ör. U/Ü/ı/i joker yapılınca "Ümit", "Umit", "Umıt" hepsi bulunur.
- **[600] Raporlarda otomatik yenileme:** Liste üzerinde sağ tık → Tam Ekran → sol altta "Otomatik Yenilenme Süresi (dakika)". Pano ekranı gibi kullanılabilir.
- **[1337] Döviz birimi "1" geliyor:** Birimi "1" olan kur girişini sil. Sonra özel ayarlarda varsayılan para birimini bir dövize çevir, programı kapat-aç, tekrar varsayılana al.
- **[951] Stok limit kontrolleri:**
  - Depo kullanılıyorsa önce Genel Ayarlar → Stok Ayarları → Stok Kart Ayarları → "Stok limit ve uyarıları depo bazında kullan" işaretini kaldır.
  - Stok kartı → Özel Ayarlar 1 → "Limitler dışına çıkarsa uyar" + olması gereken limitler.
  - Toplu uygulama Stok Tanımlar Listesi'nden yapılır. **Geri alınamaz, önce yedek al.**
- **[334] / [1834] Cari kredi limitleri:**
  - Limitler açık hesap, sipariş, irsaliye ve çek/senet için ayrı ayrı verilebilir.
  - Genel Ayarlar → Cari Kart Ayarları → **Risk Limiti Ayarları:**
    - "Otomatik kredi limiti oluştur": yeni carilerin toplam riskine yazılır
    - "Cari limit kontrollerinde limit aşımına izin verme": aşımda işlem engellenir
    - Cirolanan evrak için limit kontrolü ayrıca seçilir
- **[1040] Sipariş durumlarına göre uyarı:**
  1. Yetkili → Tanımlar → **Uyarıcı/Hatırlatıcı Ayarları** → Sipariş Durum → durum seç → "Uyarı Sistemi Kullan".
  2. **"Uyarılacak Personeller"** seç. Uyarılar sağ altta çıkar.
- **[146] 85 nolu KDV tebliği** (GSM kontör bayileri):
  1. Genel Ayarlar → Fatura Ayarları → "85 Nolu KDV Tebliğini Kullan".
  2. **Bayi fiyat no** alanına perakende satış fiyatının yazıldığı fiyat numarasını gir.
  3. Satış fiyatı 1'e dağıtıcı fiyatı gir. Bayi kârına düşen KDV ayrıca hesaplanır.
- **[122] Asorti (varyant) sistemi:**
  1. Marka, model, renk ve beden tanımlarını yap.
  2. Ana stok kartını aç, **"Ana stok" + "Asorti sistemi kullan"** işaretle.
  3. Alt stokları varyant kombinasyonlarıyla oluştur.
  - Belgelerde ana stok seçilir, alt stokların bakiyesi etkilenir. Stok 2 gerekir.
- **[404] Paket tanımları (asorti paket):** Stok → Paket Tanımları → "Asorti" + ana stok (ana stok ve asorti işaretli olmalı) → içerik stokları ve miktarları. Belgede paket görünür, içerikteki stokların bakiyesi düşer.
- **[330] Ek özellik tanımları** (Stok 2 gerekir):
  1. Stok → Stok Ek Özellik Tanımları: tanım → detay → alt detay ağacı.
  2. Alınan sipariş ve verilen teklif satırlarında ürün seçenekleri ve fiyat farkları seçilir, üretime aktarımda kullanılır.
- **[264] / [315] Formül tanımları:**
  - Önce hareket veya stok **özel alanları** sayısal/ondalıklı açılır (ör. en, boy).
  - **Yetkili → Formül Tanımları** veya fatura → İşlemler → Formül Tanımları'nda formül yazılır. Alan listesi için **Shift+Space**.
  - Sonuç miktar veya özel alana aktarılır. Örnekler: hacim, m² hesabı, çeki listesi.
- **[305] Stok envanterinde "Dönemsel istatistikleri kullan":** İşaretliyse satış tarihine kadarki alışlar maliyete girer. İşaretli değilse tüm alışlar girer (ör. ortalama ağırlıklı maliyette fark eder).
- **[416] Stok yeterlilik raporu:**
  - Günlük satış ortalaması = çıkan miktar / (kayıt tarihinden bugüne gün).
  - Aylık = günlük × 30. Yeterlilik günü = kalan miktar / günlük ortalama.
- **[1230] Genel Muhasebe entegrasyonunda uyarılar:**
  - "Aktif cari satıcılar hesabına ait hesap kodu belirtilmemiş": carisiz masraf faturası "Genel Müşteri" carisini kullanır, o carinin muhasebe **Alış/Satış kodu** girilmeli.
  - "Yuvarlama hesabına ait hesap kodu belirtilmemiş": Genel Ayarlar → Genel Muhasebe → **Yuvarlama Karları** hesap kodu girilmeli.
- **[302] / [1864] Satış faturası iskontosunu Genel Muhasebe'ye yansıtmak** (ÖnMuh 7.08.01+, GM 7.06.02+): Genel Ayarlar → Genel Muhasebe → "Satış Faturası İndirimlerini Yansıt" + stok kartı → Muhasebe → **Satış İndirimi** hesap kodu.
- **[1349] Pazarlamacı prim raporunda "Primleri İşle" yok:** Genel Ayarlar → Fatura Ayarları → Fatura Sabitleri → Pazarlamacı Ayarları → Entegrasyon → **"Toplu Entegrasyon Yap"**. Anlık entegrasyonda primler otomatik işlenir.
- **[1348] Belgede pazarlamacı görünmüyor:** Pazarlamacının cari kartındaki **Adı/Soyadı** boştur, doldurup yeniden seç.

### Tasarım ve çıktı
- **[30] PDF'te alt toplamlar görünmüyor:** Aktif Raporu Tasarla → ilgili alanları seç → "Yazdırma" özelliğini **Hiçbiri** yap.
- **[1863] Sıfır iskontoyu çıktıda boş göster:** Dizayna Expression ekle, `IF(ISK_ORAN_1=0,' ')`.
- **[1814] / [1821] Ayrıntılı cari hareket raporu dizaynına fatura türü veya işlem türü eklemek:** Veri alanı ekle → tablo "Cari Raporları – Ayrıntılı Cari Hareket Raporu" → alan `FATURA_DURUMU_C` veya `ISLEM_TURU_C` (kodun metin karşılığı).
- **[333] B formu tarih aralığını çıktıda göstermek:**
  1. Filtre alanında Yetkili → **"Aktif Nesne İsmini Göster"** (nesne adı panoya kopyalanır).
  2. Tasarımda Memo'ya `command=Getpropvalue` ve alt satıra `<NesneAdı>.text` yaz (ör. `TF_FaturaBFormF.DateEdit1.text`).
  - Başka form alanlarını çıktıya taşımak için de aynı teknik kullanılır.

### Diğer modüller
- **[237] Seri/Lot ve geriye dönük izlenebilirlik:**
  - Stok kartında lot aktifse **tüm giriş ve çıkışlarda lot girilmelidir**, yoksa raporlar bozulur.
  - Lot; MRP II'de, basit üretimde, alış faturası, gelen irsaliye, alınan sipariş ve stok hareketi girişlerinde oluşturulur.
  - Net maliyet lot bazında izlenir.
- **[234] Sevkiyat sistemi** (Sipariş + Servis modülü gerekir; beyaz eşya, mobilya gibi montajlı teslimatlar için):
  - Stok özel alanına montaj süresi (dk), sipariş özel alanına ek süreler girilir.
  - Araç ve ekip planlaması yapılır.
- **[303] Offline çalışma sistemi** ("Offline" lisansı gerekir):
  - ERP, Restoran, Hızlı Satış ve Fiyatmatik'te var. ERP modülleri: Cari, Kasa, Stok, Seri No, Depo, Çek/Senet, Fatura, İrsaliye, Teklif, Sipariş, Banka, Döviz, Analiz…
  - Her şube veya pazarlamacıya **ayrı Kontrol Paneli** kurulur ve offline modda çalışır. Merkeze belirli aralıklarla internet üzerinden veri aktarılır.
  - Yerel ağda çalıştığı için hızlı.
- **[1010] Online şube sisteminde şubeler arası depo transferi:**
  - Gerekenler: Şube Sistemi + İrsaliye (+ Depo, talep ekranı için + Sipariş).
  - Kaynak şube: **Satış Yönetimi → İşlemler → İrsaliyeler → Transfer İrsaliyesi** → kaynak şube, depo, hedef şube → miktar → kaydet.
  - **Hedef şube onaylar.** Hedef depo ve durum hedefte seçilir.
  - **Offline sistemde şubeler arası transfer yapılamaz**, merkez üzerinden yapılır.
- **[453] E-Teklif sistemi:**
  - Satın alma talebinden tedarikçilere web üzerinden teklif istenir. Tedarikçi fiyat, vade ve teslim süresi girer, ERP'de değerlendirilir.
  - Gereksinim: en az **Paket 4** + e-teklif lisansı (döviz yoksa Paket 3). **WebConnect kurulu** olmalı, şirket kaydında mail sunucusu tanımlı olmalı.
- **[563] Doküman takip:** Diğer İşlemler → Doküman Kayıt. Geçerlilik tarihi uyarısı, dosya ekleme (veritabanında saklanır), cari/stok eşleştirme ve özel alanlar var.
- **[607] SMS'e "listeden çık" linki:** Gönderim ekranında "Sms listesinden çıkma linkini gönder" (66 karakter). Tıklayan cari kara listeye girer.
- **[1296] SMS gönderirken "old version of the Topaz skin" hatası:** Program dizinindeki `Utils\SmsServer.exe` dosyasının adını değiştir, güncel SmsServer'ı indirip `Utils` klasörüne koy.
- **[947] POS tanımlama** (Banka modülü gerekir):
  1. Banka Tanımları → Alt Hesaplar (hesap tanımı, no, tür) → **Pos** sekmesi → "Pos Kullan".
  2. Tanım, taksit sayısı, provizyon oranı gir. Bağlı hesabı ok butonuyla seç, **elle yazma**.
  3. **Vade günü zorunlu.**
- **[948] Kendi çekini tanımlarken banka görünmüyor:** Banka → Alt Hesaplar → **Çek** sekmesi → "Çek Kullan" → çek tanımı, başlangıç/bitiş/verilmeye hazır no → bağlı hesap ok butonuyla seçilir.
- **[949] Çek/senet durum değiştirme** (Çek/Senet İşlemleri → evrak türü → uygulanacak işlem → İşlemi Uygula; ciroda cari seçilir):
  - Müşteri çeki/senedi: Takasta, Banka Kredisi, Tahsil Edildi, Ciro Edildi, Şube Transferi
  - Kendi çekim/senedim: Bankadan Ödendi, Kasadan Ödendi
  - Takastakiler: Tahsil Edildi, İade Alındı
- **[309] İhracat faturası teslim şekilleri:** Yurt dışı satış faturası → Döviz Alt Toplamlar. EXW, FOB, CIF, DAP… (bilgi amaçlı).

### Veritabanı ve sistem hataları
- **[761] / [3187] MSSQL "CLR nesne yürütme hatası":** Programları kapat. SSMS'te her Wolvox veritabanı için:
  ```sql
  USE master
  GO
  ALTER DATABASE WOLVOX8_001_2021_WOLVOX SET TRUSTWORTHY ON
  USE WOLVOX8_001_2021_WOLVOX
  GO
  EXEC sp_changedbowner 'sa'
  ```
  MSSQL'de veritabanı adları **`WOLVOX<sürüm>_<şirket kodu>_<yıl>_<modül>`** biçiminde (ör. `WOLVOX8_001_2021_WOLVOX`, demo için `WOLVOX8_DEMOWOLVOX_2014_WOLVOX`).
- **[738] "SQL Server Native Client 11.0 karakter dizesinden tarihe dönüştürülürken işlem başarısız":** SQL oturumunun (sa) **Default language** değeri Türkçe. SSMS → Security → Logins → sa → **English** yap.
- **[1923] "Bu modül kullanımda olduğu için özel alan tanımı oluşturulamıyor":** Tüm kullanıcılar çıkar, Kontrol Paneli kapanır, SQL Server servisi yeniden başlatılır (SSMS / Configuration Manager).
- **[170] Azerice kullanım:** Firebird'de Azeri desteği yok, **MSSQL zorunlu**. Kurulumda dil "Azerbaycan", collation `Azeri_Latin_100_CI_AI` veya `Azeri_Cyrillic_100_CI_AI`, **"Unicode Karakter Seti" işaretli**.
- **[152] "Hedef makine etkin olarak reddettiğinden bağlantı kurulamadı":** Firebird servisi çalışmıyor. Denetim Masası → Firebird → Start. Çalışıyorsa antivirüs portları kapatıyor.
- **[39] Vista ve sonrası:** Programlar düzgün çalışmıyorsa UAC kapatılır veya en düşüğe alınır.
- **[1983] Şube sisteminde "Operation Aborted" (eksiye düşenleri üret):** Üretim sayacı geride kalmış. Yetkili → Tanımlar → Sayaç Ayarları → ilgili şubenin sayacını seç.
- **[2257] Hugin VX675 "MatchEx Device" hatası:** Cihazda harici donanım entegrasyonu tanımlı değil, cihaz servisine başvurulur.
- **[1754] e-Fatura "Alıcının GİB posta kutusu etiketi hatalı":** Cari → Hesap Bilgileri → e-Fatura ayarları → **Posta Kutusu** alanında carinin GİB'e bildirdiği etiketi seç.

### CafePlus (internet kafe)
- [1] Deep Freeze gibi disk koruma programları istemcinin sunucu IP'sini kaydetmesini engeller. Korumayı açıp bağlantıyı kur, sonra korumayı geri aç.
- [17] Kapalı bilgisayarı uzaktan açmak (Wake-on-LAN) için BIOS ayarı ve Kontrol → "Tüm bilgisayarlardan MAC adres iste" gerekir.
- [58] "Sınıf kaydedilmemiş" hatası: Flash eksik.
- [1153] "System error code 123": Bilgisayar kaydında IP boş.
- [1204] NTVDM hatası: antivirüs `cpfupdate.exe` dosyasını silmiş.
- [1321] "Disable Task Manager" hatası: `reg add HKCU\...\Policies\System /v DisableTaskMgr /t REG_DWORD /d 0 /f`.
- [1789] / [1792] URL log ve Steam otomatik giriş sorunları: KB3033929 veya Windows 10 1809 güncellemesi.
- [265] Caller ID: test programı açıkken Caller ID Server numarayı alamaz, birini kapat.
