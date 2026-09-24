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

## Genel bilgiler (kurulum, veritabanı, özelleştirme, ipuçları)

### Firebird ve veritabanı
- **[434] "unsupported on-disk structure for file SIRKET.FDB; found 11.2, support 11.1":** Program **Firebird 2.5.6 (32 bit)** ister. Kurulum eskiden 2.1.3 kuruyordu; bilgisayar değişince yanlış sürüm kalabiliyor. 2.1.3'ü kaldır, `Program Files\Firebird` klasörünü sil, **2.5.6 32 bit** kur. (ODS 11.2 = Firebird 2.5.)
- **[110]** Aynı hata DBUpdate sırasında da çıkar. Firebird Guardian ve Server servislerini durdur, kaldır, AKINSOFT sitesindeki Firebird'ü kur.
- **[569] Firebird 2.1'den 2.5'e geçiş:** Yedek al → programları ve Kontrol Paneli'ni kapat → Denetim Masası → Firebird 2.1 Server Manager → Stop → kaldır ("Yes to all") → klasörü sil → 2.5 kur.
- **[805] "Cannot attach to services manager":** Firebird Server Manager çalışmıyor. Denetim Masası → Firebird Server Manager → **Start**.
- **[340] "Bad parameters on attach or create database, character set WIN1254 is not defined":** Firebird'ü kaldırıp yeniden kur. Bu hata, veritabanlarının **WIN1254** karakter setiyle çalıştığını da doğruluyor.
- **[518] "Invalid request BLR at offset 56, function UPPERTR is not defined":** Program dizinindeki `Utils` klasöründen `WolvoxUDF7.dll` (ve `Wolvox7Udf_mssql.dll`) dosyalarını `Program Files\Firebird\Firebird_2_5\UDF` klasörüne kopyala. **Wolvox, Firebird'de özel UDF fonksiyonları kullanıyor** (ör. `UPPERTR`). Dış araçla sorgu yazarken bu fonksiyonlar UDF yüklü değilse çalışmaz.
- **[445] Firebird portunu değiştirmek** (ör. modem 3050'yi kullanıyorsa):
  1. `C:\Windows\System32\drivers\etc\services` dosyasına `gds_db 3051/tcp` ve `gds_db 3051/udp` satırlarını ekle.
  2. `firebird.conf` içinde portu 3051 yap.
  3. **Sunucuda ve bütün istemcilerde** yap, sonra yeniden başlat.
- **[1506] / [3517] IB Onarım:**
  - Bozulan Firebird/Interbase veritabanını onaran AKINSOFT aracı. akinsoft.com.tr'de "Onarım" diye aranır.
  - Önce yedek al, bağlı kullanıcı olmasın. Veritabanını seç → Onar → SYSDBA parolası.
  - Düzelmiyorsa genel merkez veya çözüm ortağı onarır. Bozulmanın tipik sebebi elektrik kesintisi veya ani kapanma.
- **[2025] "SIRKETKODU widestring" hatası** (Unicode uyumsuzluğu): `KontrolPaneli\Settings\ini\Kontrolpanel.ini` içindeki `DB_UNICODE=True` değerini `False` yap, ya da SIRKET veritabanını Unicode olarak yeniden oluştur.
- **[1916] Kontrol Paneli her program açılışında yeniden başlıyor:**
  - Güvenlik duvarı, Windows Defender ve antivirüste AKINSOFT exe'lerine izin ver.
  - `AKINSOFT` klasörüne izin ver, exe'leri yönetici olarak çalıştır, uyumluluk modunu doğru seç.
  - MSSQL'de instance bilgisini doğrula.
  - Firebird'de giriş ekranındaki **sunucu IP'si uzaktan bağlanılmıyorsa boş olmalı**.
- **[1531] "Address already in use (#10048 in Bind)":** Port çakışması. Programın çalışma portunu değiştir.
- **[3991] Kontrol Paneli sürüm güncelleme hatası (kod 1103):** Kontrol Paneli klasöründe `wupdater` ve `wupdater9` olmalı. `wupdater9` yoksa `wupdater` dosyasını kopyalayıp bu adı ver.
- **[3865] XML sabitleri** (kesinti kodları, birim kodları vb.): Güncel XML dosyası `C:\AKINSOFT\Wolvox8|9\CommonData` altındakiyle değiştirilerek sürüm beklemeden güncellenebilir.

### MSSQL
- **[165] Statik IP üzerinden MSSQL bağlantısı:** SQL Server Configuration Manager → Network Configuration → "Protocols for <INSTANCE>" → TCP/IP **Enabled** → IP Addresses bölümünde tüm IP'ler için TCP Dynamic Ports = 0 ve kendi belirlediğin TCP port (güvenlik için 1433 dışı önerilir) → servisi yeniden başlat.
- **[166] MSSQL güvenlik duvarı:** `sqlbrowser.exe` ve `...\MSSQL10_50.<INSTANCE>\MSSQL\Binn\sqlservr.exe` programlarını güvenlik duvarı istisnalarına ekle.
- **[3710] Windows güvenlik duvarı port kuralları:**
  - Gelen ve giden kural ayrı ayrı tanımlanır, **sunucuda ve her istemcide**.
  - Firebird için **3050, 3055, 3056**. MSSQL için **3055, 3056, 1433, 1434**. Kural adı "AKINSOFT".
  - Antivirüste de izin gerekir.
- **[164] "Socket Error #10054 Connection reset by peer":** **SQL Server Browser** servisi durdurulmuş. Configuration Manager veya Hizmetler'den başlat.
- **[567] MSSQL istemcisinde "Kullanıcı adı veya parolası yanlış":** Hem SSMS'te hem Kontrol Paneli'nde sunucu adını `SUNUCU\INSTANCE,port` gibi port ekleyerek gir (makalede `:port` biçimi gösteriliyor).
- **[468] "Bağlantı diğer bir hstmt sonuçları ile meşgul"** (istemcide rapor alırken): İstemciye sunucu sürümüyle uyumlu **SQL Server Native Client** kur.
- **[3434] "Login failed for user sa":**
  1. SSMS → Security → sa → Status → Login **Enabled**.
  2. Sunucu Properties → Security → **SQL Server and Windows Authentication mode**.
  3. Servisi yeniden başlat.
- **[398]** Tarih dönüştürme hatası `sa` oturumunun dilinin Türkçe olmasından kaynaklanır, English yap (bkz. 738).
- **[3433] Unicode veritabanı** (Latin dışı alfabeler):
  - SQL Server **İngilizce** kurulur, instance collation `..._CI_AI` olur (ör. `Latin1_General_100_CI_AI`).
  - Kontrol Paneli açılışında Unicode seçilir.
  - SQL 2019 32 bit desteklemez.
- **[1816] / [2220]** SQL Server 2012 ve 2019 Express kurulum adımları: SSMS ayrı kurulur, en az 6.5 GB boş alan gerekir.
- **[260]** İngilizce olmayan Windows'a SQL 2008 kurarken "Performance counter registry hive consistency" hatası Perflib kayıt değerleri düzeltilerek çözülür.

### Kurulum, sürüm, destek
- **[221] / [312] / [3655] / [3832] Installer:**
  - Wolvox programlarını indirip kuran ve günceleyen araç. İlk kez sitedeki "Kur Dosyası" ile kurulur.
  - **Kurulum şekli** seçilir: **Sunucu** ve **Sunucu-İstemci** Kontrol Paneli ile programları kurar, **İstemci** sadece programları kurar.
  - Firebird kurulumunda yetkili şifresi başlangıçta `masterkey`.
- **[351] Güncellemeden önce iki aşamalı yedek:**
  1. Kontrol Paneli → Veritabanı İşlemleri → Yedekleme → Şimdi Yedekle.
  2. Programlar kapalıyken bütün `AKINSOFT` klasörünü başka yere kopyala.
  - Kontrol Paneli **Yetkili → Programdan Çık** ile kapatılmalı, yoksa güncellenmez ve sürüm uyuşmazlığı çıkar.
- **[1346] Sektörel programlarda güncelleme:** `AKINSOFT` ve `AS_YEDEK` klasörlerini yedekle → Yardım → **Program Sürümünü Kontrol Et** → Güncelle → **aynı dizine** kur.
- **[1145] / [3831] Upgrade:**
  - **Kontrol Paneli'nde hiçbir şirket (demo dahil) oluşturmadan** upgrade yap. "Demo şirketi oluşturulsun mu?" sorusuna **İptal** de.
  - Kaynak program klasörünü önceden yedekle.
- **[3343] / [3610] / [3651] Müşteri paneli:**
  - musteri.akinsoft.net'te lisans no, telefon veya e-posta ile **yeni güvenlik kodu** alınır. Lisanslamada bu kod kullanılır.
  - "Ticket için tıklayınız" ile destek kaydı (LimonDesk) açılır. Ekler: zip, 7z, rar, jpg, png, gif, pdf.
- **[158]** Eski sürümler müşteri girişi → "Eski Sürümler" bölümünde.

### Yetki, güvenlik, KVKK
- **[253] Ek yetkilerle cari görünürlüğünü kısıtlamak:**
  - Kontrol Paneli → Kullanıcı Yetkilendirme → personel ve şirket → **Ek Yetkiler 1 → Cari** sekmesine SQL koşulu yazılır.
  - Örnek: `COALESCE(CARI.GRUBU,'') NOT IN ('X') AND COALESCE(CARI.ARA_GRUBU,'') NOT IN ('Z')`.
  - Ek yetkiler SQL `WHERE` parçasıdır.
- **[1436] Wolvox 8 ile gelen bazı yenilikler:**
  - Ek Yetkiler 2'de "farklı kullanıcıların kaydettiği veya değiştirdiği kayıtları değiştirme" yetkileri
  - Genel arama, raporlarda Ctrl+C, TC ve VKN ile hızlı arama, özel raporlara sanal alan ve renklendirme
- **[3009] KVKK anonimleştirme:**
  - Belirtilen tarihten eski kayıtlarda kişisel veriler anonimleştirilir.
  - Asgari sürümler: ERP (Restoran 8.15.07, Otel 8.08.02), Genel Muhasebe 8.04.02, İK 8.13.02.
- **[1932] Yönetici ekranı:**
  - Yetki: Kontrol Paneli → Kullanıcı Yetkilendirme → **ERP → Genel → Yönetici Ekranı**.
  - Açılışta gösterim: Yetkili → Özel Tanımlar → Özel Ayarlar → Genel Ayarlar → **"Açılışta Yönetici Ekranını Göster"**.

### Özelleştirme: script ve rapor tasarımı (geliştiriciler için)
- **[1716] Pascal Form Script:**
  - ERP, Genel Muhasebe ve İK'da her pencereye olay tabanlı Pascal Script kodu eklenebilir.
  - Pencere açıkken **Yetkili → Tanımlar → Aktif Form Script Tasarımı**:
    - solda bileşen ağacı ("Görsel Seçim" ile formdan bileşen seçilir)
    - **Event Script** (her olay için "İşlem Öncesi" ve "İşlem Sonrası")
    - **Genel Script** (ortak değişken ve procedure/function)
    - "Yazılan Script Olayları", "Full Script"
  - **Shift+Space** ile kullanılabilir sabit, değişken ve fonksiyon listesi açılır. **Ctrl+F9** "Scripti Hazırla" hata kontrolü yapar.
  - Scriptler **XML olarak dışarı/içeri aktarılır**. İçeri aktarma mevcut scriptleri siler.
- **Script paketleri (`.asspack`)** ([1905], [3561]):
  - Fatura penceresinde Aktif Form Script → **Paket Yükle** → parametreleri bir kez gir.
  - Örnekler: ÜTS/BKST/İTS için palet/koli karekod okuma (`Fatura_PaletKoliKarekodBarkodOkuma.asspack`), carinin sevk adresini faturaya otomatik ekleme (`Fatura_SevkAdresiSecimi.asspack`), konaklama vergisi.
- **[739] Özel raporda çift tıklama scripti.** Özel Rapor → Script → Çift Tıklama:
  ```pascal
  begin
    if SelectedField <> Nil then
    begin
      if SelectedField.FieldName = 'BLKODU' then
        OpenOldInvoice(DataSet.FieldByName('BLKODU').AsInteger, '', 0);
    end;
  end;
  ```
  - Diğer açma komutları:
    - `OpenOldDispatch(blkodu,'',0)`: irsaliye
    - `OpenOldOffer(...)`: teklif
    - `OpenOldOrder(...)`: sipariş
    - `OpenForm('YCariTanimlari1', BLCRKODU)`: cari kartı
    - `OpenForm('YStokTanimlari1', BLSTKODU)`: stok kartı
- **İki rapor tasarım motoru var:**
  - **ARP tasarımları** (QuickReport tarzı; `QRBand`, "Report2" sayfası; [466]). Standart tablo/alan listesinde olmayan alanlar **Expression** ile gösterilir, ör. `IF(ISK_ORAN_1=0,' ')`, karekodda `alan1+linebreak+alan2` ([1885]).
    - Alt toplamları satırların bittiği yerde göstermek için "Detay Özeti = Var" ile **Summary Band** eklenir ([1423]).
    - Yazıcıya gitmeyen alan için "Yazdırma" özelliği kullanılır ([30]).
  - **FastReport** (yeni tasarımlar; [4006]): Data → **AKINSOFT Query** nesnesi eklenir, SQL yazılır, `:PARAM` ile master tabloya bağlanır. Örnek:
    ```sql
    SELECT C.* FROM STOK_TEDARIKCI ST
    JOIN CARI C ON (C.BLKODU = ST.BLCRKODU)
    WHERE BLMASKODU = :PARAM   -- master: STOKETIKET, PARAM = STOK.BLKODU (INTEGER)
    ```
    Master ve Params, Nesne Yöneticisi'nden ayarlanır. Parametre olarak sayısal alan bağlanmalı, string yavaşlatır.
- **[1887] Stok kartı açıklamasını faturaya yazdırmak:** Özel Ayarlar → Fatura Ayarları → Fatura Genel → "Faturayı yazdırırken stok bilgilerini çek" + dizayna "Fatura Raporları – Fatura Stok Bilgileri" tablosundan `ACIKLAMA1` alanı.
- **[3836] Hazır veritabanları ve dizaynlar** (Wolvox 9): e-Business hazır veritabanları (`Wolvox_...`), MRP 2 veritabanları, Argox etiket dizaynları (raf etiketi, 4'lü/5'li etiket…), fatura dizaynları (2'li/3'lü fatura, A4 dikey iskonto/seri/açıklama/tevkifat…).
- **[1660] / [1659] Yerli üretim logolu etiket** (8.12.05+): "AKINSOFT-Yerli-Uretim" fontu (karakter "1"). Etikette fiyat değiştirme tarihi, birim fiyat ve üretim yeri otomatik gösterilir. Örnek tasarım makalede.

### Stok, fiyat, cari ipuçları
- **[13] / [1889] Toplu fiyat değiştirme:**
  - Stok Yönetimi → Raporlar → Tanım Listeleri → **Fiyat Değiştirme/Fiyat Listesi** → filtrele → İşlemler → **Fiyat Yenile**.
  - Oradan satış fiyatı oluşturma (baz fiyat + %), alış fiyatı, fiyat çevirme, yuvarlama, devir fiyatları. "Manuel Fiyat Değiştirme" de var.
- **[1276] / [1876] Alış faturasıyla stok alış fiyatını güncellemek:** Genel Ayarlar → Stok Ayarları → Stok Hareket Ayarları → "Stok alış fiyatını otomatik değiştir" = Birim Fiyatından / İskontolu Fiyattan / Değiştirme.
  - Alışta satış fiyatlarını da oluşturmak için: Özel Ayarlar → Fatura Ayarları → Alış Faturası → "Satış fiyatları oluşturma penceresini göster".
- **[3084] Fiyatı değişen stoklar:** Stok listesi raporlarında **Filtre 2** → "Satış fiyatı değişenler" (fiyat no + tarih aralığı).
- **[1888] Stokların eksiye düşmesini engellemek:**
  - Tek stok için: Özel Ayarlar 1 → "Stok eksiye düşerse uyar".
  - Toplu: Stok Tanımları Listesi → İşlemler → **Bilgi Güncelle** → Özel Bilgiler.
  - "Bilgi Güncelle" filtrelenmiş tüm kayıtlara uygulanır. Carilerde de var, ör. "Döviz hesabı kullan" [1892]. **Önce yedek al.**
- **[1891] İşlem görmeyen stokları pasife almak:** Analizler → İşlem Görmeyen Stoklar → İşlemler → Güncelle → Aktif işaretini kaldır.
- **[772] Hareketsiz ve ölü stok farkı:** Hareketsiz stok, dönem içinde hiç işlem görmemiş eldeki stoktur. Ölü stok, uzun süre talep veya tüketim görmemiş stoktur.
- **[1895] Envanterde birim fiyat ve tutar boş:** "Sadece miktar envanteri" işaretli, fiyat tanımı seçilmemiş veya stokta "Maliyetlerde eşleştirme yöntemi kullan" açık.
- **[1515] Envanter maliyet yöntemleri:** Alış fiyatı 1–4, en son alış, ortalama alış (basit ortalama), ortalama ağırlıklı (toplam tutar / toplam miktar), LIFO, FIFO.
- **[1717] Fiyat farkı, kur farkı ve iade faturalarını maliyete yansıtmak** (8.13.01+): Fatura tipi "fiyat farkı" seçilir, satırda ilgili alış faturası seçilir. Envanter maliyeti düzeltilir.
- **[1873] Stok miktarına göre otomatik sipariş:** Genel Ayarlar → Stok Kart Ayarları → Otomatik Sipariş Oluştur → "Sipariş listesine ekle" (eşik ve sipariş miktarı; blokeler dahil olsun mu).
- **[1874] Beklemedeki siparişi onaylamadan faturalamak:** Sipariş Durum Tanımları'nda "Muhasebelendirebilsin" işaretle → Sipariş Teslim Raporu → **Faturalandır**.
- **[1027] Siparişte "Stok Bloke/Termin" görünmüyor:** Genel Ayarlar → Sipariş Ayarları'nda ve Sipariş Durum Tanımları'nda bloke/termin açık olmalı.
- **[1041] Ek sistemler:**
  - **Petrol sistemi:** tutar ve fiyat girilir, miktar hesaplanır; en az 3 basamak hassasiyet gerekir.
  - **Toptancı sistemi:** tutar ve miktar girilir, fiyat hesaplanır.
- **[1370] Stok arama penceresinde kalan miktar:** Sağ üstteki seçenekler → "Bakiyeleri göster" + "Birim bakiyelerini göster".
- **[45] Fatura satırlarını kayıtta sıralamak:** Özel Ayarlar → Fatura Ayarları → Fatura Kayıt Formu → "Fatura hareket sıralaması".
- **[1881] Zorunlu alanlar:** Yetkili → Tanımlar → **Zorunlu Alanlar** → modül, tablo, alan (ör. Cari → T.C. Kimlik No).
- **[3085] Cari tahsilat/tediyede 2. döviz:** Genel Ayarlar → Cari Ayarları → Cari Hareket Ayarları → "2. Döviz Birimi Sistemini Kullan".
- **[3086] Çek işlemlerinde banka görünmüyor:** Çek sekmesindeki bağlı hesap no elle yazılmış (ör. 88888). Ok butonuyla alt hesaplardan seçilmeli.
- **[1311] Cari yaşlandırma raporu alanları:**
  - "Açık Hesap Günü": borcun kaç gündür açık olduğu.
  - "Gerç.Vade": kısmi ödemede kalan tutar için gün. Negatifse vadeye o kadar var, pozitifse vade o kadar geçmiş.
  - "Valör" aynı mantıkla çalışır. Alttaki mavi satır ortalamaları gösterir.
- **[1897] / [1898]** Ödenen/ödenmeyen taksitler: Finans Yönetimi → Raporlar → Taksit Raporları. İşlem türüne göre borç/alacak: Analizler → İşlem Türü Raporları.
- **[126] Pazarlamacı prim raporu 2:** Ciro basamağına göre (ör. 1000 TL %5, 2000 TL %10) veya ortalama fiyata göre prim hesaplanır.
- **[172] Durum değişince otomatik e-posta/SMS:**
  - Cari limit değişimi, tahsilat, çek/senet tahsilatı ve kargo no pazarlamacıya bildirilebilir.
  - Fatura kargo no cariye bildirilebilir.
  - Servis ve sipariş durum değişiklikleri müşteriye bildirilebilir.
- **[959] SMS:**
  - Sağlayıcı Mutlucell. SMS → SMS Kullanıcı Hesabı → kullanıcı adı/şifre → Listele → originatör seç → kaydet.
  - Posta Güvercini (Figensoft) de destekleniyor [2153]; orada "XML client uygulamaları kullanabilir" işaretli olmalı.
  - [247] SMS Server programı ücretsiz, Excel'den toplu SMS gönderebilir.
- **[332] Gmail gibi SSL e-posta gönderimi:** `libeay32.dll` ve `ssleay32.dll` (OpenSSL 0.9.8) program exe'sinin yanına konur. Gmail'de uygulama izni gerekebilir.
- **[3412] Türkçe karakterler bozuk:** Windows → Bölge → Yönetimsel → **Sistem yerel ayarı = Türkçe**. Tarih ve ondalık ayırıcı sorunları için Biçimler → Ek Ayarlar.
- **[1510] "Printer selected is not valid":** Varsayılan yazıcı yok, yazıcı çevrimdışı veya sürücü uyumsuz.
- **[1300] Excel aktarımında "Data too large for variable max len=30":** Alan sınırı aşılmış (ör. GRUBU 30 karakter). Excel hücresini kısalt.
- **[53] Eski programdan geçiş:** Cari ve stok kartları Excel'e alınıp Transfer modülüyle aktarılır. CRM aktiviteleri de aktarılabilir.
- **[244] Fiyat gör cihazı (Perkon FG1200):** Firebird ODBC sürücüsü kurulur, DSN tanımlanır (SYSDBA/parola), sonra cihaz programında ağdaki cihazlar bulunur ve ayarlanır.
- **[274] / [230] ₺ simgesi:** Windows 10'da ek kurulum gerekmez. Eski sistemlerde Microsoft KB2739286 gerekir, ERP 7.07.01+ olmalı.
- **[1290] / [1875] Şubeler arası kasa transferi:**
  1. Kaynak şube: Finans Yönetimi → İşlemler → Kasa İşlemleri → **Kasa Transferi** → Transferi Uygula.
  2. Hedef şube: Finans Yönetimi → Raporlar → Kasa Raporları → **Kasa Transfer Havuzu** → onayla.
- **[1294] / [1872] Şubeler arası stok transferi:**
  1. Kaynak şube: **Transfer İrsaliyesi** oluşturur.
  2. Hedef şube: Satın Alma (veya Satış) Yönetimi → Raporlar → İrsaliye Raporları → Transfer Raporları → Transfer İrsaliye Raporu → irsaliyeyi aç → durum **Onaylandı**, depo seç → Uygula.
- **[727] Offline'da otomatik veri gönderme:** Ana bilgisayar Kontrol Paneli → Diğer İşlemler → Offline → Offline Ayarlar → "Otomatik veri alma sistemini kullan" + gönderilecek tablolar.
- **[3133] Wolvox Reporter** (iOS/Android):
  - "Bağlantı ayarlarını düzenle"de ana bilgisayar IP'si ve Kontrol Paneli **güncelleme portu** girilir, sonra Wolvox kullanıcısıyla giriş yapılır.
  - Raporlar: yönetici ekranı, şube, fatura/çek/kasa analizleri. Dışarıdan erişim için port yönlendirme ve statik IP gerekir.
- **[3217] / [1855] Karekod ayarları:**
  - Genel Ayarlar → Stok Ayarları → Genel → Karekod Ayarları. Karekoddaki alanların uzunlukları tanımlanır (ör. barkod 14, seri/lot 5, SKT 6, açıklama 4).
  - Farklı formatlar için "Grup Ekle". Okutulan karekod gruplara sırayla uydurulur, **ilk uyan grup** kullanılır.
- **[3266] Avusturya RKSV:** Wolvox 9, Fiskaltrust middleware ile entegre. "Yazarkasa – Pos – Terazi" lisansı gerekir.

## e-Dönüşüm (e-Fatura, e-Arşiv, e-İrsaliye, e-Defter, e-Müstahsil)

### e-Fatura / e-Arşiv
- **[3008] Program ve entegratör destek matrisi** (WolvoxCloud, Wolvox ERP, OctoPlus 7, OctoCloud, Otel 5, NetSürücü Plus):
  - Entegratörler: Digital Planet, EDM, İzibiz, Süper Entegratör.
  - Fatura tipleri: satış, iade, tevkifat, istisna, ihraç kayıtlı, SGK, özel matrah, şarj, (şarj) ajanlık.
  - Senaryolar: temel, ticari, ihracat, yolcu beraber, kamu, enerji, ilaç/tıbbi cihaz, yatırım teşvik, IDIS.
  - Gönderim: e-Arşiv, e-Fatura, internet satış. e-İrsaliye (temel, sevk), e-Müstahsil, e-Adisyon.
  - Hangi programda hangisinin olduğu makaledeki tabloda.
  - Not: **Digital Planet'te `DTP.XML` formatı** kullananlarda bazı özellikler (e-Fatura Script butonu, kamu faturası) çalışmaz. **UBL formatına geçiş** için destek kaydı açılır.
- **[1741] EDM entegrasyonu:**
  1. Kontrol Paneli → Şirket Kayıt → e-Devlet → "e-Fatura sistemi kullan".
  2. EDM kullanıcı bilgileri ERP'de e-Fatura Ayarları → Kullanıcı Bilgileri'ne girilir.
  3. EDM portalında aktif yıl için **Tanımlar → Fatura Seri No → Yeni Kayıt**. e-Fatura, e-Arşiv ve internet satış için **ayrı seri** açılır.
  4. ERP'de sayaç tanımında **Şablon Kodu** alanına bu seri yazılır.
- **[768] Digital Planet şablonları:** Şablonlar DP tarafında tanımlanır. ERP'de Yetkili → Sayaç İşlemleri → Sayaç Tanımları → e-Fatura/e-Arşiv altında **Şablon Kodu** olarak seçilir. Birden fazla tasarım veya farklı numara başlangıcı için gerekir.
- **[3088] Eski tarihli e-Fatura gönderirken hata:**
  1. Portalda yeni 3 harfli seri aç.
  2. ERP'de sayaç tanımı ekle (şablon kodu = yeni seri).
  3. Sayaç Seçimi → e-Fatura No → "Aktif Sayacı Kullan" + "Aktif Sayacı Varsayılan Yap".
  4. Faturayı Düzenle → Kaydet.
  - Sebep: GİB'de bir serideki numaralar tarih sırasını bozamaz.
- **[474] Mükellef sorgusu otomatik:** e-Fatura ayarları yapılınca program açılışta cariler için VKN sorgusu yapar. Yeni carilerde de otomatik sorgular.
- **[3305] "Geçersiz cbc:ProfileID" / mükellef listesi:**
  - Carinin VKN/TCKN'si portalda aratılır; unvan ve posta kutusu ERP'ye kaydedilir.
  - **Satış Yönetimi → İşlemler → Faturalar → Mükellef Listesi**'nden elle ekleme veya silme yapılır.
- **[3012]** e-Fatura aktif şirkette carinin **TCKN ve VKN alanları aynı anda dolu olamaz** (8.19.01+).
- **[475] Gelen e-Fatura entegrasyonu:**
  - Önce **e-Fatura Eşleştirme**'de cari bazında fatura tipi (alış veya masraf) ve **hareket eşleştirme yöntemi** bir kez tanımlanır.
  - Masraf seçilse bile ÖTV/ÖİV/tevkifat varsa alış faturası olarak alınır. Gelen faturada olmayan KDV/ÖİV oranları için tanımdaki oranlar kullanılır.
- **[596] / [1966] Opsiyonel alanlar:**
  - e-Fatura Ayarları → **Opsiyonel Alanlar** (Fatura ve Fatura Hareket sekmeleri).
  - Veritabanındaki özel alanlar e-Fatura XML'ine eklenir; entegratör bunları görünüm tasarımına ekler.
  - Gönderilen XML: `<program dizini>\Temp\<kullanıcı>\Efatura_Giden`.
- **[3181] / [3182] Tedarikçi stok kodunu göndermek:**
  - Stok → Tedarikçiler → Tedarikçi Ekle (belgedeki cari) → "Stok Kodu Gir".
  - e-Fatura (veya e-İrsaliye) Ayarları → "Tedarikçi Stok Kodu Bilgisini Ekle".
  - Değer `BuyersItemIdentification` alanında gider.
- **[758] "InvoicedQuantity/UnitCode is invalid":** Stok birim tanımlarında **uluslararası birim kodu** yanlış veya boş. Düzelttikten sonra stok belgeye **yeniden eklenmeli**.
- **[1743] "Geçersiz cbc:InvoiceTypeCode":** Faturada "Fatura Tipi" boş.
- **[3351] Özel matrah faturası** (8.22.01+): e-Fatura/e-Arşiv alanındaki (?) → Fatura Tipi **Özel Matrah** → satırda özel matrah kodu seçilir.
- **[719] e-İhracat faturası** (1 Temmuz 2017'den beri zorunlu):
  - Sayaç tanımında şablon kodu **IHR**.
  - GTİP no: stok → Özel Ayarlar 2.
  - Yurt dışı faturada e-Fatura (?) → Senaryo **İhracat**. Satırda teslim/ödeme ülke-il-ilçe ve taşıma şekli alanları açılır.
- **[2687] Otomatik e-Fatura gönderimi:**
  - Kapsam: satış (e-Fatura/e-Arşiv), alıştan iade, alış (e-Müstahsil).
  - Programlar: Hızlı Satış 8.09.04+, Restoran 8.15.04+. Kontrol Paneli 8.03.49+, ERP 8.18.06+ gerekir.
  - Kontrol Paneli → Şirket → e-Devlet'te açılır, **en az 30 dakika** aralıkla çalışır.
  - **Offline sistemde çalışmaz.** Kuyruktaki faturalar merkeze aktarılınca gönderilir.
- **[3010] e-Arşiv gelen kutusu (İnteraktif Vergi Dairesi):**
  - Lisans gerekir. Kontrol Paneli → Şirket Kayıt → **e-Devlet 2**'ye TC/VKN/giriş kodu ve şifre girilir.
  - Hareket detayı gelmediği için tek bir stok veya hizmetle eşleştirilir. Tarih aralığı → Aktarıma Başla → İçeri Aktar.
- **[3391] Kontör satın alma:** akinsoft.com.tr → Bayi ve Müşteri Girişi → Müşteri Girişi (lisans no/telefon/e-posta + güvenlik kodu) → **Ürün Yenile / Satın Al** → entegratöre göre e-Fatura/e-Arşiv/e-İrsaliye kontör paketi.
- **[331]** e-Fatura zorunluluğu kapsamı (VUK 421 ve sonrası tebliğler) ve genel bilgilendirme. Güncel eşikler için GİB'e bak.

### e-İrsaliye
- **[3112] Posta kodu hatası:** 1 Eylül 2021'den beri ülke, il, ilçe ve posta kodu zorunlu. ERP 8.19.06+ ve Kontrol Paneli 8.03.64+ gerekir. Cari → Genel Bilgiler → **5 haneli posta kodu**.
- **Şoför ve taşıyıcı hataları** (satış irsaliyesi → **Ek Bilgiler 2**):
  - [3114] "DriverPerson NationalityID" → **Şoför TCKN** dolu olmalı.
  - [3115] "DriverPerson" → **Şoför Adı Soyadı** ad ve soyad birlikte, arada boşlukla yazılmalı.
  - [3116] "SchemeID VKN… 10 haneli" → **Taşıyıcı VKN/TCKN** geçerli olmalı.
- **[2223] Firma/kişi kontrolü hatası:** Cari e-İrsaliye mükellefi değilken kartta "e-İrsaliye kullan = Evet" işaretlenmiş. Hayır yap, cariyi irsaliyeye yeniden ekle.
- **[2229]** Windows Server'da Kontrol Paneli firma güncellemesi sırasında kapanıyor: İnternet Seçenekleri'nde entegratör siteleri güvenilir olarak tanımlanır.

### e-Müstahsil
- **[2124] Kurulum:**
  1. Kontrol Paneli → Şirket Kayıt → e-Devlet → "e-Müstahsil Sistemi Kullan".
  2. Genel Ayarlar → Fatura Ayarları → **Ek Kesintiler** → "Varsayılan e-Müstahsil kesintilerini yükle". Önceden elle kesinti tanımlandıysa uluslararası kodları seçilir.
  3. Cari → Hesap Bilgileri → "e-Müstahsil Kullan = Evet".
  4. Alış faturası kesilir. G.V. stopajı zorunlu.
- **[2642] Borsa tescil ücreti formülü:**
  - Formül: `TOPLAM_ARA_KPB - OZELALANTANIM_9 - OZELALANTANIM_12 - OZELALANTANIM_15`. Örnekte 9 G.V. stopajı, 12 mera fonu, 15 SGK prim kesintisi; numaralar veritabanına göre değişir.
  - Formül Yetkili → Tanımlar → Formül Tanımları'nda yazılır, ek kesintide seçilir.

### e-Defter
- **[536] Wolvox 9 e-Defter oluşturma ve gönderme:**
  - Kontrol Paneli → Şirket Kayıt → e-Devlet → **"e-Defter sistemi kullan"**. Kaydedildikten sonra **değiştirilemez**, bilgileri dikkatle gir.
  - Alanlar: başlangıç yılı/ayı, şube (varsa), **NACE kodu**, veritabanı yöneticisi adı (SYSDBA/sa fişleri bu isimle aktarılır), iletişim bilgileri.
- **[511] Ön koşullar:**
  - Kontrol Paneli'nde muhasebeci kaydı yapılıp şirkete bağlanır.
  - Mali mühür/e-imza sürücüleri (kamusm.gov.tr) ve **İmzager** kurulur.
  - e-Defter uygulamasında: Ayarlar → oluşturma dizini, Mali Mühür PIN'i, kart sistemi, donanım tipi.
- **Hatalar:**
  - [1233] / [3026] "gl-bus:organizationDescription 'Adı Soyadı'…": Şirket tipi yanlış seçilmiş. Şahıs firmasıysa **Şahıs/Gerçek** olmalı.
  - [1237] "Xml imzalama işlemi sırasında problem": PIN girilmemiş veya yanlış.
  - [1238] "Sertifika zinciri sorunlu": Güncel **Java** ve **İmzager** kur, gerekirse AKİS'i yenile.
  - [456] Kök sertifika uyarısı: `mmeshs-s1.crt` yüklenir; `C:\Users\<kullanıcı>\.sertifikadeposu` içindeki `.svt` dosyası kamusm'deki güncel sürümle değiştirilir.
  - [457] "USB imzalama aygıtı bulunamadı": AKİS Akıllı Kart İzleme Aracı kaldırılıp yeniden kurulur.
  - [454] 64 bit Windows uyarısı: Makale ekindeki DLL'ler `...\E-Defter\XmlSigner` klasörüne konur.
  - [1299] "XML yapısında uygunsuzluk (şematron)": Borç/alacak dengesi bozuk fiş var, ya da hesap planında veya fişlerde bağlı üst/alt hesaplar yanlış.
  - [1235] "Sistem belirtilen nesneyi konumlandıramıyor": Eski sürümdeki "Defteri Kebir" ve "Yevmiye Defteri" klasörleri yeni yapıda tek "Defterler" klasörüne taşınır (`...\E-Defter\Defterler\<VKN>\<dönem>\<ay>`).
- **[459] / [450] / [451] / [3265] Mevzuat notları:**
  - Her yevmiye kaydının belgeye dayanması şart değil (amortisman, virman).
  - Toplu masraflar icmal belgesiyle ("other") kaydedilebilir.
  - Tasfiye öncesi ve sonrası dönemler ayrı gönderilir.

## Lisans, yedek, devir, Kontrol Paneli, MSSQL

- **[1470] / [3829] Wolvox online lisans:**
  1. Tüm programlar kapalıyken Kontrol Paneli → Yetkili → **Wolvox Lisans**.
  2. (WOLVOX 26'da önce **paket seçimi**) → Online Lisans Al → "Lisans kartım veya numaram var" → lisans no + güvenlik kodu/müşteri şifresi.
  3. Bitir → "Lisansınız tekrar aktifleştirilsin mi?" Evet.
  - OctoPlus, CafePlus, NetSürücü ve Net Emlak'ta menü Yardım → Lisans/Aktivasyon ([1473], [1756], [1474], [1475]). İnternet yoksa 444 40 80.
- **[3455] Demo sistemi** (Kontrol Paneli 8.04.01+):
  - İlk açılışta **Lisanslı Kurulum** veya **Demo Kurulum** seçilir. Demo: "Yeni Demo Kaydı" veya "Demo Kaydım Var".
  - Demo süresince **internet bağlantısı gerekir**.
- **[369]** E-Ofis "Network Admin lisanslanan kayıt sayısı aşılmış": Network Admin → Bilgisayar Listesi'nden fazla kayıtları sil (Wolvox'taki client tanımları mantığı).
- **Yedekleme (sektörel programlar)** ([1655] OctoPlus, [1661] NetSürücü, [1663] RentAgent, [1664] E-Ofis, [1665] Otel, [1667] CafePlus): Hepsinde Yetkili → Veritabanı İşlemleri → **Yedekleme/Geri Yükleme**. Kaynak program dizinindeki `data` klasörü, hedef yedek klasörüdür. Geri yüklemede bağlı kullanıcı olmamalı. OctoPlus'ta geri yükleme şirket başına ayrı yapılır.
- **Devir:**
  - [29] Wolvox 6, [650] Wolvox 7 ve [118] OctoPlus 7 için yıllık devir makaleleri var. OctoPlus'ta devir **Yetkili Kişi → Şirket İşlemleri → Çalışma Yılları → Çalışma Yılı Oluştur** ile yapılır.
  - **[477] Durum tanımlarına göre devir:**
    - Toplu devir, durum tanımlı modüllerde sabit durumları aktarır (ör. teklifte "Teklifte" ve "Onaylandı").
    - Teklif, sipariş veya servis için **ek durum tanımı** oluşturduysan toplu devir yerine Kontrol Paneli → Şirket Kayıt İşlemleri → **Çalışma Yılı Oluştur** kullanılır ve aktarılacak durumlar seçilir.
- **[1626] Kontrol Paneli'ni Windows servisi olarak çalıştırmak:**
  - Sunucuda Windows oturumu açılmadan istemcilerin bağlanması için Kontrol Paneli → **Windows Servisi** → "Kontrol paneli servisini çalıştır" → çalışma portu (programın portuyla aynı) → Servisi Çalıştır.
  - Sunucu kilitli odadaysa veya kimse oturum açmıyorsa önerilir.
- **[1810] Girişte SMS doğrulaması:** Personel kaydında cep numarası olmalı. Kontrol Paneli → Yetkili → Özel Ayarlar → Kullanıcı Login → "SMS doğrulaması yap". SMS hesabı tanımlı olmalı.
- **[1802] Hızlı yetkilendirme:** Kullanıcı Yetkilendirme ekranında **F7**.
- **MSSQL:**
  - **[162] / [164] "Socket Error #10054":** SQL Server Browser → Başlangıç türü **Automatic** + Start.
  - **[2020] ".NET Framework… assembly ID 65536" (CLR):** Tüm kullanıcı veritabanlarına TRUSTWORTHY ON + sahibi `sa` uygulanır:
    ```sql
    EXEC sp_MSforeachdb 'IF ''?'' NOT IN (''master'',''model'',''msdb'',''tempdb'')
    BEGIN USE [?]
      DECLARE @sql NVARCHAR(MAX)
      SET @sql = N''ALTER DATABASE '' + QUOTENAME(DB_NAME()) + N'' SET TRUSTWORTHY ON;''
      EXEC sp_executesql @sql
      SET @sql = N''EXEC sp_changedbowner ''''sa'''';''
      EXEC sp_executesql @sql
    END'
    ```
    SQL 2019+'da ayrıca `C:\AKINSOFT\Wolvox9\Utils\Wolvox7Udf_mssql.dll` dosyası SQL Server'ın `...\MSSQL\Binn` klasörüne kopyalanır.
  - **[4034] "TRY_CONVERT" hatası:** SQL Server **2012+** ve veritabanı **compatibility level en az 2012 (110)** olmalı.
