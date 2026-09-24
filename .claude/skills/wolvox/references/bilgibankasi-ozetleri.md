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

## Hızlı Satış, yazarkasa (ÖKC), terazi, yazıcı

### Hızlı Satış
Ayarların çoğu **Yetkili → Özel Tanımlar → Özel Ayarlar** altında (Satış-İade 1–4, Genel Ayarlar 2, Entegrasyon Ayarları sekmeleri). İki arayüz var: **Basit Görünüm** ve **Normal Görünüm**. Sağ üstteki üç çizgi simgesi tasarım moduna geçirir.
- **[1487] / [2418] Yardım dosyası:**
  - Menüler: Yetkili (oturumu kapat, şirket seçimi), İşlemler (satış ekranı, fiyat gör, yazdır…).
  - İlk kullanımda ödeme türü seçimi, stok listesi kısayolları ve kullanıcı ayarları yapılır.
  - ERP ile tam entegre.
- **[1456] "Geçersiz kapalı fatura işlem türü":** Tasarım modunda ödeme butonlarını "Yok" yap, programı kapat-aç, ödeme türlerini yeniden tanımla.
- **[1480] Değişim:**
  1. Satış ekranı → Ek İşlemler → **Değişim İşlemi** → fişi bul → ürünü **"Seç"** → Tamam.
  2. Satıştaki ödeme türünü seç. Değişen ürün kırmızı görünür; yerine alınan ürün eklenir.
  - Fark pozitifse tahsil edilir, negatifse müşteriye ödenir.
- **[1645] Para üstü hesaplama penceresi:** Genel Görünüm → "Nakit ödemelerde hesaplama penceresini aç". [2367] Ödeme ekranı için: Satış-İade → "Satış işlemini kaydederken ödeme ekranını göster".
- **[1842] Satış ekranında cari bakiyesi:** Genel Ayarlar → "Satış ekranında cari bakiyesini göster".
- **Uyarılar ve kontroller:**
  - [1844] fiyatı olmayan ürün uyarısı
  - [1856] alış fiyatının altında satış uyarısı (Satış-İade 1)
- **[1857] Aynı ürünü tek satırda birleştirmek:** Satış-İade 2 → "Stok arama formunda aynı stok varsa" = **Stokları birleştir**. Barkod okutmada birleştirme için ayrı bir ayar var.
- **[1858] Cariye özel fiyat:**
  - Cari kartı → Hesap Bilgileri → **"Kullanılacak stok fiyatı"** (kaçıncı satış fiyatı).
  - Hızlı Satış → Satış-İade 4 → "Cari değişiminde stok fiyatını" = **Değiştir**.
- **[2023] Müşteri ekranı:** Özel Ayarlar → Müşteri Ekranı. İkinci monitör (monitör no seçilir) veya COM portlu cihazlar (Hugin FLY 385/485, Possify DynamicPos…).
  - **[2219] Web tabanlı müşteri ekranı:** Tarayıcıda açılır. Dosyalar program dizinindeki `MUSTERI_EKRANI` klasöründe (`index.html` satış, `idle.html` bekleme). Tanıtım görselleri `slideimages` klasörüne konur (yaklaşık 800×400).
  - **[3175] VCF müşteri ekranı script paketi:** Yetkili → Özel Tanımlar → Script Paket İşlemleri → Paket Yükle.
- **[2366] Ek barkodla arama:** Stok arama (F6) → Seçenekler → "Gelişmiş aramayı kullan" + "Stok ek barkod arama".
- **[2368] / [3543] Fiş tasarımı:** Yazdır → Aktif Raporu Tasarla → metin alanı ekle → parametre olarak "Ödeme Durumu", "Para Üstü", "Kalan Tutar" veya "Ödeme Toplamı" bağlanır.
- **[3588] Fişi yeniden yazdırmak:**
  1. Satış-İade → "Son … satış fişini sakla".
  2. Satış ekranını kapat-aç, Ek İşlemler → Kısayollar → **"Son Satış Fiş Logları"**.
- **[3595] Basamak ayracını kaldırmak** (POS tarzı giriş, 2500 → 25,00): Özel Ayarlar → Genel Ayarlar'daki basamak ayracı seçeneği.
- **[3584] Para simgesini tutarın soluna almak:** ERP'de Genel Ayarlar → Parasal Ayarlar, sonra Hızlı Satış ayarları.
- **[3635] Çekmece açma:** Entegrasyon Ayarları → Çekmece Ayarları → "Satış öncesi/sonrası çekmece aç" (nakit veya tüm işlemler) + çekmece yazıcısı. Ek İşlemler → Kısayollar'a "Çekmece Aç" eklenir.
- **[733] Buton font ve renkleri** (8.03.01+): Butona sağ tık → Tasarla → "Tasarımı Aktif Et". "Tasarımı Hafızaya Al" ile başka butonlara kopyalanır. Hazır stil dosyası: `...\HizliSatis\Settings\Ini\<kullanıcı>\ButtonStyle.ini`.
- **[2685] Otomatik e-Fatura:**
  1. Kontrol Paneli → Şirket → e-Devlet → Otomatik e-Fatura Gönderimi.
  2. Hızlı Satış → Satış-İade → Genel Ayarlar 2 → gönderim şekli: **Kuyruğa Ekle** (30 dk aralık), **Hemen Gönder** veya **Kullanıcı Onaylı**.
- **[1585] Depozito** ve **[1041] petrol/toptancı sistemleri** için `WOLVOX ERP Ön Muhasebe` ve `Genel bilgiler` bölümlerine bak.

### Yeni nesil yazarkasa (YNÖKC) ve POS entegrasyonları
- **Lisans:** Tüm YNÖKC entegrasyonları ERP'de **"Yazarkasa – Pos – Terazi"** lisansı ister. Bazı cihazlarda (ör. [3570] Hugin T300) müşteri panelinden **yıllık ÖKC eşleşme ücreti** ödenir.
- **Programlar:** Hızlı Satış ve Restoran. Cihaz ayarları **WOLVOX Market Otomasyonu** programında yapılır: yeni nesil ÖKC → cihaz → Ayarla.
- **Ortak ayarlar:**
  - **Fiş limiti:** bu tutarın üstünde fatura kesilmesi gerekir.
  - **Bağlantı:** IP/port veya seri port/COM ve hız.
  - **Aktif kasiyer:** 4 kasiyerden biri ve şifresi.
  - **Ödeme eşleştirmeleri:** cihazdaki ödeme tipleri ↔ Wolvox ödeme türleri.
  - "Cihaza ürünün diğer birimlerini gönder", EFT-POS kullanımı.
- **Desteklenen cihazlar ve makaleleri:**
  - inPOS M120 [489]
  - Hugin VX675 USB [491], FT202 ve FP300 [582], T300 [3570]
  - Olivetti MX915 [583]
  - Ingenico iWE280 [762], iDE280 [2282]
  - Beko 300TR [843]: Token X Store'da entegratör olarak "AKINSOFT Wolvox" seçilir, entegrasyon paketi alınır.
  - Profilo S900 [2311]
  - NBA Fiscal Box [2648] ([2660] Azerice)
  - NPos YN500 [3113]
  - Yurtdışı: Almanya TSE [3129] ve Avusturya RKSV [3266] **Fiskaltrust** üzerinden.
- **Sorunlar:**
  - [1818] **Satıştan sonra cihazdan fiş çıkmıyor:** Kontrol Paneli → Şirket Kayıt → e-Devlet → **"Yeni nesil yazarkasa kullan"**. Şube sistemi varsa şube kaydında da YNÖKC ayarı yapılır.
  - [3544] Beko 300TR "Cihazda önceki satış tamamlanmamış": Beko'nun ArExternalTest aracıyla cihaza bağlanıp açık satış kapatılır.
  - [2257] / [3571] Hugin "MatchEx Device": Cihazda harici donanım entegrasyonu tanımlı değil, servise başvurulur.
- **[3261] / [3263] Restoran + Ingenico iWE280/Move5000 mobil ödeme (TSM):**
  - Bir bilgisayar **TSM server** olur (açık port, kullanıcı/şifre AKINSOFT'tan). Masa ve paket adisyonları TSM'e gönderilir.
  - TSM için **sabit IP** gerekir. Yoksa No-IP gibi dinamik DNS kullanılır, alan adı entegrasyon formundaki "statik IP" alanına yazılır.
- **[296] Eski nesil yazarkasalar:**
  - IBM Entry, Sharp ER-A495T, Inter MPOS 2001, Hugin POS: ERP ile offline.
  - Hugin 425 TX, Olivetti OL 7000: ERP ile offline, Restoran/Hızlı Satış ile online.
  - [326] Hugin POS + Restoran: Menü → Program Ayarları → Yazarkasa Entegrasyonu → Hugin data dizini, 4 haneli kasiyer no.
- **[301] Yazarkasadan satış alırken "Cari bulunamadı":**
  - Kodu "Genel" olan genel müşteri carisi olmalı ve Özel Ayarlar → Fatura Ayarları → Fatura Genel → **Genel Müşteri Cari Kodu** seçili olmalı.
  - Oluşturmak için: "Hızlı Satış Kullan" işaretle → yeni satış faturası → Yeni Fatura.
- **[3586]** Market Otomasyonu'nda son kullanılan menüyü açılışta açmak için Ayarlar'da bir seçenek var. [2365] Manuel veri gönderimi için "Dosya sistemini kullan".

### Elektronik terazi
- **[223] Barkodlu tartım:**
  - Desteklenen modeller: CAS CL5000, CAS LP-1 / LP1000N, Densi (ACOM/NDP/Nets), Aclass LS2X, Digi SM100, Baster ELT-15/30.
  - Tartılı ürünün stok kartına terazi barkodunun **ilk 7 hanesi** yazılır (ör. `2907022`). Kalan haneler tartımda ağırlıkla üretilir.
- **Market Otomasyonu üzerinden aktarım:**
  - **[362] CAS CL5000:** CL-Works v2.70.5+ gerekir, `MAINDATA.mdb` seçilir → Tek/Tüm Stok Aktar → CL-Works'ten teraziye gönderilir. [3587] Aktarılacak fiyat no seçilebilir.
  - **[365] Densi:** Nets programında File → DB Open ile data oluşturulur, Market Otomasyonu'nda yolu seçilir (parola `814050`), NDP ile bağlanıp stok aktarılır.
  - **[375] Aclass:** `Aclasplu.txt` oluşturulur, Aclass programında açılıp PLU gönderilir (terazi IP'si).

### Yazıcı sorunları
- **[25] "Range check error"** / **[61] "Printer index out of range":**
  - Program varsayılan yazıcıda otomatik form boyutu oluşturmaya çalışıyor, yazıcı sürücüsü bozuk.
  - Sürücüyü kaldırıp yeniden kur. Önizleme yapmadan `.arp` dizaynını aç, sayfa boyutunu **Custom → A4** yap ve kaydet.
- **[153] "System Error Code 5 – Erişim engellendi"** (yazdırırken): Dizaynda sayfa boyutu Custom kalmış. Formun gerçek boyutunu (veya Default) seç.
- **[1011] "System Error Code 87":** Yazıcı kapalı veya dizaynda yazıcı seçilmemiş.
- **[1510] "Printer selected is not valid":** Varsayılan yazıcı yok, çevrimdışı veya sürücü uyumsuz.
- **[19] / [743] Etiket yazıcıları:** Argox için Bartender/Argobar, Zebra için Zebra Designer Pro ile `.prn` hazırlanır (kılavuzlar makalelerde). [43] Epson LX-300+ "Tear Off" ayarı font tuşu kombinasyonuyla yapılır.

### PDA
- **[293] Restoran PDA (eski Windows Mobile):** En az 320×240, Windows Mobile 5/6 veya CE 5, dokunmatik ve Wi-Fi. .NET Compact Framework 2.0/3.5 kurulur. Güncel PDA uygulamaları Android/iOS'tur (`sektorel-programlar.md`).

## Sektörel programlar

### WOLVOX Restoran
- **[710] / [3687] Garson ve PDA:**
  - Garson, ERP'de **cari** olarak açılır: Cari Tanımları → **Özel Bilgiler 2** → "Garson" işaretle + **PDA şifresi** (garson ekranı girişinde de kullanılır, her garsona ayrı). Yetkiler: Restoran → Menü → Yetkili → Garson Yetkilendirme.
  - **Android PDA:**
    1. Restoran program ayarlarında "Bu bilgisayar PDA server olarak kullanılacak" işaretlenir.
    2. Cihazda `http://<sunucu-ip>:<PDA port + 1>/MOBIL/index.html` açılıp APK indirilir (ör. PDA portu 4500 ise 4501).
  - [1500] PDA'dan sipariş mutfak yazıcısına veya mutfak ekranına gider, adisyon yazdırılabilir.
- **Web tabanlı ekranlar** (aynı port mantığı, PDA portu + 1):
  - [1164] **Sıramatik:** Program Ayarları → Müşteri Ekranı → "Web tabanlı sıramatik kullan" → `http://<ip>:<port>/SIRAMATIK/index.html`.
  - [3494] **Mutfak ekranı:** "Web tabanlı mutfak ekranını kullan" + Yazıcı Tanımları'nda mutfak yazıcısı olarak **`MUTFAKEKRANI_1`** seçilir. "Mutfağa yazdır" ile ekrana düşer.
- **[2266] Masa krokisi:** Program Ayarları → Görünüm → Masa Yerleşimi = **Kroki** → kroki resmi → Dizayn Modu'nda şekil ekle → nesneye masa bağla. [2138] "Basit masa görünümü" de var.
- **[3657] Şubelere tanım kopyalama:** Masa butonları ve grupları, kroki, adisyon butonları, süreli masa tarifeleri, otomatik üretim ve tüketim ayarları.
- **[3680] Otomatik üretim/tüketim:** Menü → Tanımlar → Otomatik Üretim → Stok Otomatik Üretim Ayarları (reçete). Fiş başına ve kişi başına otomatik tüketilecek ürünler (masa, paket satış 1/2).
- **Diğer tanımlar ve adisyon ekranı:**
  - [3673] Menü tanımları (Menü → Tanımlar → Stok Detayları → Menü Tanımları)
  - [3682] Stok bazında veya tüm ürünler için açıklama tanımları
  - [3684] Dönüşüm tanımları
  - [3658] Hızlı adisyon ekranına ERP stok gruplarından toplu aktarım
- **[1147] Kurye için ayrı fiyat:** Stok 2 + ERP'de gelişmiş satış fiyatı sistemi. Kuryeye özel fiyat listesi tanımlanır.
- **[1644] Hesap kapatma:**
  - Hızlı tutar butonları (5/10/20/50/100).
  - Oranlı bölme (1/2, 1/3, 1/X), ürün ve miktar bazında bölerek ödeme.
- **[3611] Kurye gün sonu:** Menü → Ekranlar → Kurye Gün Sonu Raporu. Paket satışlar kuryeye göre listelenir, açık fişler kapatılır, **para teslimi** kaydedilir.
- **[3612] Dışarıdan alınan ürün:** Ekstra → "Dışarıdan Alış". Kasa seçimi Program Ayarları → Ekstra-İndirim'de yapılır.
- **[1327] Gün sonu depo sayımı:** Farklı depolar (ör. içecek deposu) günlük sayılır. Satışla karşılaştırılır, açık veya fazla **sorumlu personelin carisine** işlenebilir.
- **Kart ve kredi sistemleri** (Disko-Bar-Kulüp giriş altyapısı):
  - [1428] **Kantin sistemi:** limitli öğrenci kartı. Program Ayarları → Disko-Bar-Kulüp Giriş → Ekle → Kredi → "Kredili giriş fişi oluştur".
  - [2065] Kredili kart (Menü → Kredili Kart → Kredili Kart İşlemleri).
  - [462] Sosyal tesis (turnike ve harcama kredisi).
  - [141] Ön ödemeli sistem (belirli ürünü süreli veya adetli ücretsiz ya da indirimli kullandırma, abonelik).
  - [740] Devlet yurdu yemekhane (ERP'de ek işlem türleri, restoranda saat aralığına göre sabit tutarla otomatik kapatma).
- **[1641] Telegram onayı:**
  - Yetkisi olmayan garson veya kullanıcı için indirim, ürün iptali, fiş tipi değişikliği, ikram/ödenmez ve adisyon iptali işlemlerinde yetkiliden Telegram üzerinden onay istenir.
  - **@BotFather** ile bot oluşturulur. Bot, **işletme yetkilisinin telefonunda** oluşturulmalı.
- **[3666] Otel ↔ Restoran entegrasyonu:** Restoranda kapanan hesap konaklayan misafirin folyosuna işlenir. Otelde gelir/ödeme tanımları **501'den başlayan hesap kodlarıyla** yapılır (500'e kadarı sistemde). Restoran → Program Ayarları → Otel → departman ayarları.
- **[2185] QR Menü:**
  - `qrmenuapp.akinsoft.com.tr` üzerinde kategori ve ürün tanımlanır, Sistem → Şubeler'de QR linki alınır.
  - Restoran entegrasyonuyla QR menüden sipariş alınabilir.
- **Sorunlar:**
  - [1028] Adisyon no **-1** ve "Toplu satışın yapılacağı adisyonlar" penceresi: Şube kodunda `-` veya `_` karakteri var, kaldır.
  - [2054] İptal raporunda "hatalı giriş" iptalleri görünmüyor: Kullanıcıdan "mutfağa yazdırılmayan hatalı girişleri direkt sil" yetkisini kaldır.
  - [1671] Caller-ID bildirimi birden çok kez çıkıyor: `C:\AKINSOFT\CallerIdServer1\Setting.ini` içindeki `IPNO=` satırına bu bilgisayarın IP'sini yaz.
  - [1128] Son kullanma tarihi takibi: Seri-Lot modülü (lot/parti izleme, "partiler parçalanabilir").
  - [1042] Marş sistemi ayarları ekran görüntülerinde.

### WOLVOX Otel ve Otel 5
Otel 5, WOLVOX Otel'den ayrı ve daha basit bir üründür. Kendi Firebird veritabanı (`AKINSOFT\Otel 5\Database_FB`), lisansı (Yardım → Lisans) ve güncellemesi (Yardım → Program Sürümünü Kontrol Et) vardır.
- **[715] / [716] Anlık kimlik bildirimi (AKBS/KBS):** Yetkili → Özel Ayarlar → Anlık Kimlik Bildirimi → "E.G.M anlık bildirim sistemini kullan" → **AKBS uygulamasını çalıştır** → EGM kullanıcı bilgileri. İşletme önce EGM kılavuzuna göre KBS'ye kaydolur.
- **[319] / [496] Kimlik ve pasaport tarama:** Plustek TR821 (kimlik/ehliyet), OpticSlim 550 (pasaport). Otel 4/5'te sadece TR821 destekleniyor.
- **[705] / [2105] HotelRunner ve online rezervasyon:** **WOLVOX Veri Transfer** programı ve ilgili lisans gerekir. `ssleay32.dll` ve `libeay32.dll` dosyaları System32 (32 bit) veya SysWOW64 (64 bit) klasörüne konur.
- **[3549] / [3551] Konaklama vergisi (%2):**
  - Genel Ayarlar → Folio (Otel 5'te Rezervasyon ayarları) → "Konaklama vergi sistemini kullan" (+ "oda ücretine dahil et"). Genel Muhasebe kodu da buradan girilir.
  - **Dahil** örneği (750 TL, %8 KDV): ara toplam 681,82, KDV 54,55, konaklama vergisi 13,64, toplam 750.
  - **Hariç** örneği: ara toplam 694,44, KDV 55,56, konaklama vergisi 13,89, toplam 763,89.
  - ERP tarafı için script paketi var ([3561]).
- **[3418] / [3416] e-Fatura:**
  - WOLVOX Otel: Genel Ayarlar → Folio → otomatik gönderim türü (Kullanma / Kuyruğa Ekle / Hemen Gönder / Kullanıcı Onaylı).
  - Otel 5: Genel Ayarlar → Firma Bilgileri → e-Devlet + e-Fatura Ayarları → entegratör ve kullanıcı bilgileri → bağlantı testi.
  - [3420] Otel 5 kamu faturası: IBAN Firma İletişim'e, cari "Kamu Kurumu", Harcama Birimi VKN (?) alanına.
  - [3665] Otelden kesilen fatura **otelden** iptal edilir: Fatura İşlemleri → Kesilmiş Faturalar → Ft.İptal.
- **[1457] Check-out yapılmış rezervasyonu silmek:** Folio → **Check Out İptal** → folio hareketlerini seç → Seçili Folio Hareketlerini Sil → rezervasyon → **Check In İptal** → sil.
- **[1735] Kale Kilit:** Özel Ayarlar → "Kale Kilit (Embedded)… aktif et". `...\Wolvox8\KaleKilit\KaleKilit.exe` ayarları Kale firmasından alınır.
- **[1871] / [1910] Oda temizlik durumu:** Resepsiyon → Ön Büro → Oda Listesi (Rack) → sağ tık; Rack Ekran; Odalar Yönetimi → House Keeping. Otel 5'te Rezervasyon → Otel Raporu.
- **[1317] Pansiyon tipleri:** BB (oda+kahvaltı), HB (+akşam), FB (+öğle+akşam), AI (her şey dahil), UAI (ultra her şey dahil).
- **[568] Kontrol ve dönem kayıtları:** Çocuk yaş grupları; dönem bazlı gecelik ücret (kişi başı veya oda).
- **Otel 5 diğer:**
  - [1904] Vadesi gelen çek hatırlatması
  - [1912] Oda özellikleri
  - [1913] Zorunlu misafir alanları
  - [3813] Otel raporunda boş oda dolu görünüyor: rapor giriş zamanı rezervasyon çıkışıyla çakışıyor
  - [4049] **TGA Tesis Künye** raporu (5.06.14+, uyruk ve ay bazında)
  - [3417] "Invalid BLR at offset 16": `WolvoxUDF7.dll` + `UDF_TRUP.DLL` Firebird `UDF` klasörüne konur
  - [3678] Yedek: Yetkili → Veritabanı İşlemleri veya `Database_FB` kopyası
- **[1433] WOLVOX 8 Otel yardım dosyası:** Çok kullanıcılı, Firebird veya MSSQL, mükerrer rezervasyon kontrolü, voucher, günübirlik girişler, folyoya göre faturalama.

### WOLVOX İnsan Kaynakları
- **[99] Başlangıç sırası:**
  1. Tanımlar → **İşyeri Tanımları**
  2. **Vardiya** planları (sabah/akşam/gece/tatil)
  3. Aylık **çalışma planları**
  4. **Yasal sabitler** (webden veya varsayılanlardan)
  5. Personel kayıtları
  6. Cihazdan giriş-çıkış verileri
- **[106] Personel puantajda görünmüyor:** Personel kartı → SSK Bilgileri → **SSK Başlama Tarihi** ve **İşe Giriş Tarihi (SSK)** boş.
- **[3260] 2022 bordro değişiklikleri:** AGİ kaldırıldı. Asgari ücrete kadar olan kısım gelir ve damga vergisinden istisna. Normal ve asgari ücret GV matrahları ayrı kümülatif izlenir. Emeklilerden SGDP kesilir.
- **[3633] EYT (15510 sayılı kanun):** İK 8.16.01+. Tanımlar → Teşvik Tanımları → Kanun No 15510 → Kaydet. Sonra personel → SGK Bilgileri → Kanun No.
- **[376] Huzur hakkı bordrosu:** Gelir ve damga vergisi kesilir, SGK kesilmez. Makalede İşyeri tanımıyla başlayan adımlar var.
- **[709] Magic Pass 20656 parmak izi "Sınıf kaydedilmemiş":** Programı bir kez yönetici olarak çalıştır.
- **[2679] 360 derece performans değerlendirme:** Web tarayıcıdan puanlama, ast/üst/eşit grupları. [2141] Gelişmiş iş başvuru: Genel Ayarlar → "Gelişmiş iş başvuru özelliklerini kullan" → özellik tanımlarını departmanlarla eşle.

### WOLVOX Genel Muhasebe ve Beyanname
- **[1672]** GM'yi kullanmak için Kontrol Paneli → Şirket Kayıt İşlemleri → **"Muhasebe Tipi" = Genel Muhasebe** olmalı. ERP, İK, e-Defter, Demirbaş ve Beyanname ile entegre.
- **[1415] Fiş sıralama:** Fiş İşlemleri → Fiş Sıralama → ay seç → aylık sırala → başlangıç numarası. **e-Defter kullanıcıları** bir önceki ay gönderilen son fiş numarasından devam etmeli.
- **[1653] Aylık KDV tahakkuku:** 391 (hesaplanan) ile 191 (indirilecek) mahsubu. Fark 360 (ödenecek) veya 190 (devreden) hesabına gider.
- **[2234] Dövizli muhasebe:** Genel Ayarlar → "Dövizli muhasebe kullan" → Diğer İşlemler → Döviz Tanımları (Merkez Bankası kodlarıyla USD, EUR) → hesap planında "Döviz hesabı".
- **[3652] Stok takibi:** "Stok takibi yap" → Stok Tanımları → hesap planında "Stok kodu".
- **[2669] KDV listelerinde tutar yok (elle fiş girilmiş):** B formu konusu hesap satırlarında (153, 600, 601, 610, 770…) Evrak No, B Formu ve Firma Kodu dolu olmalı. 191/391 satırlarında B Formu boş, Firma Kodu dolu olmalı (BA/BS için).
- **[2026] Yevmiye defterinde "Incorrect syntax near":** Rapordaki fiş açıklama ayarlarında (?) ayraç karakterini düzelt.
- **[578] / [1527] Beyanname:** GM, İşletme Defteri ve İK'dan veri alır. KDV1/KDV2, muhtasar gibi beyannameler otomatik veya elle hazırlanır, XML ve e-beyanname oluşturulur.
  - [2071] XML kontrolü için GİB'in güncel `UygulamaHazirlamaKilavuzu.zip` dosyası Beyanname klasöründeki `BeyannameKontrol` klasörüne açılır.
  - [93] KDV1'de bütün matrah tek satırda toplanıyor: Hesap planında **her KDV oranı için ayrı alt hesap** açılmalı, formüller doğru olmalı.

### MRP II ve Demirbaş
- **[270] Online İş Merkezi** ("Online İş Merkezi" lisansı gerekir):
  - Kontrol Paneli'nde Online İş Merkezi ayarları → "Online iş merkezi sistemi kullan" + **web servis portu** → Kontrol Paneli'ni yeniden başlat → kullanıcı yetkisi ver.
  - Operatör tarayıcıdan iş emrini başlatır, durdurur ve bitirir.
- **[770] / [754] / [1583]:**
  - İş merkezleri: personel yetkisi iş merkezi veya makine bazında verilir.
  - Makine duruş tanımları ve duruş girişleri: etkilenen makinelerin iş emirlerine yansır.
- **[1646] Makine bakım raporu:** Makine tanımında bakım hareketleri girilir. Uyarıcı/Hatırlatıcı → MRP Makine Bakım → "Makine bakımlarını otomatik kontrol et". Toplu güncelleme "Bilgi Güncelle" ile yapılır.
- **[1508] Demirbaş:** Sabit kıymet envanteri, amortisman, yeniden değerleme, zimmet. Çalışması için **Genel Muhasebe veya İşletme Defteri** kurulu olmalı.

## Entegrasyon programları: WebConnect, Web Entegrasyon, Veri Transferi, Mobil Satış

### WOLVOX WebConnect (tarayıcıdan ERP)
- **[1526] Bağlantı:**
  - "Yetkili" ya da "Kullanıcı" olarak girilir. Kullanıcı girişi için Kontrol Paneli → Kullanıcı Yetkilendirme → personel ve şirket seçilir → Program Kullanım Yetkileri'nde **WebConnect** işaretlenir.
  - WebConnect'te "Port Ayarları → Çalışma Portu" (örnekte 8888) kontrol edilir. Dışarıdan erişilecekse port modemde açılır.
  - Tarayıcıya `http://<sabit-ip>:<port>` yazılır → kullanıcı girişi → şirket seçimi.
- **[689] / [753] Servis sayfaları (en az 8.02.03, e-Ticaret sitesine eklenebilir):**
  - Garanti sorgulama: `<ip>:<port>/$/start?value=wgrntsrg`
  - Servis durumu sorgulama: `…?value=wsrvdrmsrg`
  - Servis ürün kaydı: `…?value=wsrvkayit`
- **[541] Servis randevusunu WebConnect'ten izleme:**
  - Önce Kontrol Paneli'nde kullanıcı oluşturulup yetkilendirilir.
  - Kullanıcı için cari kart açılır. Özel Bilgiler 2'de "servis personeli" işaretlenir. Özel Bilgiler 1'de "Wolvox kullanıcısı" seçilir.
  - Servis randevu kaydında bu kişi "servis işlemleri personeli" olarak eklenir.
- **[750] Android'de barkod:** "WConnect Barcode.apk" kurulur. Stok ekleme ekranındaki kamera kutucuğuyla barkod okutulur. WebConnect tarafında ayar gerekmez.
- **[2123] Mobil yazıcı çıktısı:** Dotmatrix formatlı `.arp` hazırlanır ve WebConnect klasöründeki `DefDesign` altına konur (ör. `...\Wolvox8\WMobil\DefDesign`). İndirilen dosya Android'deki "Mobil Printer" uygulamasıyla açılıp basılır.
- **[3606] Müşteri imzası (8.07.04+):** Sipariş ve servis randevu formlarında imza alınır. Çıktıda görünmesi için ERP tasarımına resim alanı eklenir:
  - parametre "Sipariş İmzası" / "Servis İmzası"
  - Otomatik boyut, Ortalama ve Sığdır: "var"
  - Veri tabanı: **Dosya 2**
- **[3821] 9.02.01:** Sipariş ve teklife not alanı, servis randevusuna kamera veya dosya eki, garanti bitiş tarihi, envanterde termin miktarı, CRM özel alanları eklendi.
- **[2355]** WebConnect ile Mobil Satış Android arasındaki farkları bir tablo olarak veriyor (tablo resimde).

### WOLVOX Web Entegrasyon (ERP ↔ AKINSOFT e-Ticaret)
- **[2207] Kurulum ve bağlantı:**
  - Program Installer'dan kurulur. Girişte **Kontrol Paneli yetkili kullanıcı adı ve şifresi** istenir.
  - e-Ticaret panelinde Kullanıcılar → Yöneticiler → Yeni Ekle → **"Muhasebe Kullanıcısı"** oluşturulur ve tüm yetkiler verilir. Bu kullanıcıyla panele girilemez. Kurulumda verilen normal kullanıcı API kullanıcısına çevrilmez.
  - e-Ticaret panelinde Entegrasyonlar → Ticari Program Yönetimi'nde senkronizasyon modu seçilir:
    - **Tam:** ERP'deki bütün stok işlemleri siteye akar.
    - **Kısmi:** Stok iki tarafta aynı kodla ayrı ayrı açılır. Yalnız işaretlenen alanlar (fiyat, miktar…) güncellenir.
    - **Yok:** Bağlantı olmaz.
  - Web Entegrasyon → Ayarlar → Genel → Web Sitesi Ayarları: Site adresi **`http://` ile** yazılır (`https` yazılmaz). Muhasebe kullanıcısı bilgileri girilir → **Test Et**.
  - Test Et hataları:
    - "Sunucu ile bağlantı kurulamadı" → adres https girilmiş.
    - "Kullanıcı Bulunamadı" → muhasebe kullanıcısı bilgileri yanlış.
    - "Öncelikle Senkronizasyon işaretlenmelidir" → panelde senkronizasyon seçilmemiş.
  - Ürünün ve grubunun gönderilmesi için ERP'de **"Webde Görünsün"** işaretli olmalı.
- **[3039] Stok ayarları:**
  - Açıklama bilgisi: Özel Ayarlar-1 özellik detayları.
  - Resim ve dosyalar: Stok 2'de "Dosya" altında eklenir, "Web'de Görünsün" işaretli olmalı.
  - Alt stoklarda aynı rengin resmi bütün bedenlere gönderilebilir.
  - Miktar gönderiminde termin/bloke dahil edilebilir (Stok 2 ve Sipariş gerekir).
  - Gelişmiş iskonto gönderimi: ERP genel ayarlarında açılır, e-Ticaret'te Kampanya modülü gerekir.
  - "Varsayılan ve diğer birim fiyat sistemi" ile "Birimler ve fiyatları gönder" birlikte kullanılamaz.
  - Diğer gönderimler: alternatif ürünler (ilgili ürün olarak), e-Ticaret özellik tanımları, ek kategoriler (Özel Ayarlar 2), lot (e-Ticaret'te Kumaş modülü gerekir), depo envanteri ("hangi mağazada").
  - Stokta döviz tanımlıysa yalnız döviz fiyatı gönderilebilir. Bu durumda TL fiyatı gitmez.
  - Uyumlu marka ve modeller de gönderilebilir.
  - Özellik filtresinde görünme şartı: özellik en az 3 üründe girilmiş olmalı ve en az 2 farklı değer almalı.
- **[3067] Stok alan eşleştirme:** Stok özel alanları e-Ticaret alanlarına eşlenir. Özel alanın veri tipi hedef alana uymalı:
  - Ek Bilgi 1 ↔ Açıklama
  - desi
  - Hızlı Kargo, Ücretsiz Kargo, Sitede Gösterme: **Var/Yok**
  - Kargolama süresi: **Tam sayı**
  - SEO alanları
  - Gösterilecek üye tipi: Metin. Değerler "Bayi", "Müşteri" veya "Bayi ve Müşteri" ([2680]).
  - Birimler: Metin, "Diğer Birimler" ile aynı yazım. Bütün stoklarda geçerlidir, temel birim kullanılamaz.
  - Garanti süresi: Çoktan seçmeli, değerler ay cinsinden.
- **[2211] Kategori eşleştirme:** Varsayılan kategori Grup > Ara Grup > Alt Grup'tur (3 seviye). Daha derin ağaç için "Stok Kategori Eşleştirme" kullanılır: ilk 3 seviye grup alanları, sonrası özel alanlar. Bu açıksa grup alanlarından kategori oluşturulmaz.
- **[2321] Ürünü birden fazla kategoride gösterme (ERP s8.17.01+):** Stok kartında Özel Ayarlar 2 → Kategori Bilgileri'ne ek kategoriler girilir. Adlar grup tanımlarıyla birebir aynı yazılmalı.
- **[3065] Sipariş kayıt ayarları:**
  - Alınan Sipariş sayacı ayrı seçilebilir.
  - **"Yeni siparişi direkt fatura olarak kaydet"** (Sipariş modülü yoksa): fatura, e-Fatura ve e-Arşiv sayaçları seçilir.
  - Siparişler "Beklemede" durumuyla gelebilir.
  - ERP'de olmayan ürün için iki seçenek: "Siparişi kaydetme" (uyarı verir; ürün aynı kod ve adla açılıp "Veri Al" yapılır) veya "Stok kartı açmadan sipariş kaydet".
  - Üye olmadan alışveriş yapanlar cari olarak kaydedilebilir. e-Fatura mükellefi isen e-Fatura ayarlarında "Gönderim bilgilerini fatura kartından al" açılmalı.
  - Siparişin ek bilgileri (promosyon kodu, kargo barkodu…) ERP siparişindeki Özel Tanımlar'a eşlenir.
  - "Sadece sipariş" kayıtlarında e-Fatura ödeme tipi "Dekont" olarak aktarılabilir.
- **[3907] 2. şirket (s9.02.02+):** Siparişler aynı anda ikinci bir şirkete de, **yalnız sipariş olarak**, kaydedilebilir. Şirket, şube ve çalışma yılı seçilir. Tek cari kodu verilebilir; boş bırakılırsa her sipariş için cari açılır. Ayar hatalıysa sipariş hiçbir şirkete yazılmaz.
- **[3068] / [3216] Cari ayarları:**
  - Carinin e-Ticaret'e gitmesi için cari kartındaki Özel Bilgiler 1'de web kullanıcı adı, parola ve e-posta dolu olmalı.
  - Varsayılan tip "ÜYE"dir. "BAYİ" için Özel Kodu 3 = "Bayi" yazılır ya da metin tipli bir özel alan "Üye tiplerini kaydet" ayarına bağlanır.
  - Seçenekler: alışveriş yapmayan üyeleri de kaydet, sitede değişen adresi ERP'de güncelle.
- **[3072] Virman (sanal pazar bakiyesi):**
  - Her pazar (N11 vb.) için ERP'de bir cari açılır ve kodu Virman Ayarları'na yazılır.
  - Sipariş faturalanınca tutar o cariye borç olarak virmanlanır. Müşteri carisinin bakiyesi 0 görünür.
- **[3119] Genel Muhasebe entegrasyonu:** Yeni cariler için varsayılan muhasebe alış ve satış kodları tanımlanır. Kargo satırının muhasebe kodu "Kargo Satırı Muh. K." alanına girilir.
- **[3128] "Bağlantı diğer bir HSTMT sonuçları ile meşgul" (MSSQL):** SQL Server Native Client kurulup program yeniden açılır.
- **Sürüm notları:**
  - [3919] s9.02.02: Birden fazla şirkete sipariş yazılabiliyor. Site adı küçük harfle kaydediliyor. Cari grup bilgisi aktarılıyor.
  - [3948] s9.03.01: ERP'de silinen stok sitede pasife çekiliyor. Üyeliksiz alışverişte her siparişe ayrı cari açılıyor. Yasal alanlar gönderiliyor. İskonto tanımlarındaki cari grupları gönderiliyor. Koçtaş siparişleri onaylı geliyor ve virman destekleniyor.

### WOLVOX Veri Transferi (dış sistem entegrasyonları)
Veri Transferi, ERP, Restoran ve Hızlı Satış'ı dış servislere bağlayan ayrı ve modül bazlı lisanslanan bir programdır.
- **[3468] Lisans (8.08.01+):** "Online Lisans Al" ile lisans no ve şifre girilir. Modül ekleme ve yenileme Yetkili → "Lisans Satın Al veya Yenile" ekranından kredi kartı ve 3D Secure ile yapılır.
- **[747] ÜTS / Hotel Runner / SanalSantral / Kobikom:** Ekteki `ssleay32.dll` ve `libeay32.dll` 32 bit Windows'ta `System32`, 64 bit Windows'ta `SysWOW64` klasörüne kopyalanır.
- **Yemek platformları (Restoran):** Getir Yemek [3007], Çırak [3137], Trendyol Yemek [3201], Yemeksepeti [1047], yeni Yemeksepeti [3628], Migros Yemek [3691], Fuudy [3793].
  - Hepsinde ortak akış: Veri Transferi → Restoran → ilgili entegrasyon → Ayarlar. Platformdan alınan anahtarlar girilir (secret key, API key, satıcı ID…).
  - Sipariş alma süresi, "Genel Müşteri BLKODU" ve uyarı süresi ayarlanır.
  - **Stok Eşleştirme**'de menü listesi platformun servisinden çekilir ve Restoran stoklarıyla eşlenir. Detay için CTRL+Enter. Ürün tipi "Normal" ya da "Açıklama/Fiş açıklaması" (seçenek) olur.
  - **Yeni Yemeksepeti (VT 8.08.03+):** Müşteri bilgisayarı host olur. **Sabit IP** (veya NoIP) ve modemde açık bir port gerekir. Başvuru ticket ile yapılır: lisans no, VKN, IP, port ve vendor id. Geçişler salı, çarşamba ve perşembe yapılıyor.
  - **Migros Yemek (VT 8.09.01, Restoran 8.23.03):** Panelde her şube için ayrı API Key üretilir (POS firması = AKINSOFT). "Server kullanılsın" ile port açılır.
  - **Fuudy (VT 8.11.01, Restoran 8.23.07):** Detaylı log `Veritransfer\FuudyYemekData` altında tutulur. Otomatik sipariş alma aralığı en az 31 sn.
- **[3437] Getir Çarşı (Hızlı Satış):** ShopID ve ChainID talep formuyla alınır. Stok birimi, sipariş durumu ve sipariş alanı eşleştirmeleri yapılır.
- **[751] SanalSantral:**
  - Kontrol Paneli'ndeki kullanıcı kaydına dahili numara yazılır.
  - Veri Transferi'ne Santral ID ve API Key girilir. CallerID ve bildirim portu ayarlanır.
  - ERP'de Yetkili → Özel Tanımlar → Özel Ayarlar → Caller ID'deki iletişim portu, Veri Transferi'ndeki bildirim portuyla **aynı** olmalı.
- **[1930] / [2148] ÜTS (tıbbi cihaz ve kozmetik takibi):**
  - Veri Transferi, ÜTS bildirimlerini yapar: verme, alma, tüketiciye verme, iade, üretim, ithalat…
  - "ERP Özel Alan Tanımlarını Aç" butonu gerekli özel alanları otomatik açar.
  - Kurum no ÜTS portalında "Firma Bilgilerim" altındadır. Token, Sistem Kullanıcısı Tanımlama'dan e-İmza ile alınır ([2137]: izinli IP listesini imza yetkilisi belirler).
  - Otomatik cari ve stok kaydı yapılabilir. İthalatta ülke kodları kullanılır [3447].
- **[1724] BKTS (bitki koruma ürünleri):** Bakanlık kararıyla **01.09.2025'ten itibaren kapatıldı**. Modül satıştan kaldırıldı.
- **[2158] GoBD (Almanya):** Program Almanca kurulur ve Kontrol Paneli GoBD moduyla çalıştırılır. Tarih aralığı, tablo ve alan seçilip CSV dışa aktarılır. ERP, Restoran, Hızlı Satış, Otel ve Mobil Satış'ta var.
- **[3667] / [3668] Ercom:**
  - Sipariş entegrasyonu Ercom'un "Muhasebe" klasörünü, üretim entegrasyonu "uretimrecete" klasörünü okur.
  - MySQL bağlantısı ve birim eşleştirmesi yapılır. İstenirse belli aralıklarla otomatik aktarır. Tanımsız cari ve stoklar ayrıca listelenir.
- **[3800] Excel entegrasyonu:** Excel'den fatura ve cari tahsilat aktarır. Klasör, başlık, cari/ürün kodu kolonları tanımlanır. Fatura ve tahsilat tipi, pazarlamacı, birim, depo ve e-Fatura senaryosu eşleştirilir.
- **[3631] Panorama:** ERP faturaları XML olarak export klasörüne yazılır. Şablonda alanlar `TABLO.ALAN` biçiminde verilir ve **yalnız FATURA ve FATURAHR** tablolarından okunabilir.

### WOLVOX Mobil Satış (saha satış) ve Mobil Server
Mimari: **Mobil Server** (PC) ERP verisini hazırlar, pazarlamacı ayarlarını ve tasarımları tutar. **Mobil Satış** (Android; eski sürümü Windows Mobile) senkronizasyonla veri alıp gönderir.
- **[2133] Bağlantı:**
  - Cihaza PC'nin IP'si (yerel ağda `ipconfig` ile bulunur, dışarıdansa statik IP), port ve kullanıcı şifresi girilir.
  - Pazarlamacı, ERP'de bir cari kart olarak açılır. Özel Bilgiler 2'de **"Pazarlama Sistemini Kullan"** işaretlenir ve **PDA Şifre** verilir.
- **[1879] APK kurulumu:** Mobil Server çalışırken cihaz tarayıcısında `http://<pc-ip>:<mobil server portu + 1>` açılır. "Bilinmeyen kaynaklar" izni verilir. APK açılmazsa Dosyalarım → Download klasöründen kurulur.
- **Pazarlamacı ayarları** Mobil Server → Yetkili'de:
  - "Kasa, POS ve Filtre Tanımları" pazarlamacı bazındadır [2654]. Tekrar yazdırma yetkisi [2342], vade aşımı kontrolü [3438] ve e-Fatura/e-Arşiv/e-İrsaliye sayaç ataması [2653] buradadır. Her pazarlamacıya ayrı sayaç verilmeli [3858].
  - "PDA Ayarları": çoklu stok seçimi [2341], ağırlıklı barkod [3591], fatura/cari/irsaliyeyi merkeze otomatik gönderme (Genel 2), stok grup resimleri ile katalog [3871].
  - Değişiklikten sonra cihazda **senkronizasyon/veri alma** yapılır.
- **[3349] / [3441] Otomatik e-Fatura / e-Arşiv / e-İrsaliye:** Pazarlamacının cihazında internet olmalı.
  - Kontrol Paneli → Şirket Kayıt → e-Devlet'te otomatik gönderim açılır.
  - Mobil Server'da PDA Ayarları → Genel 2'de merkeze gönderim açılır ve pazarlamacıya sayaç atanır.
  - Cihazda "Otomatik e-Fatura Gönderme" = Kullanıcı Onaylı seçilir.
  - [3460] e-İrsaliye ve özel matrah için Mobil Server 8.07.07 ve Android 8.07.01 gerekir.
- **[3438] Vade aşımı engeli:**
  - Pazarlamacıya bir Wolvox kullanıcısı atanır ve bu kullanıcıdan "Cari vade aşımında evrak girişine izin ver" yetkisi alınır.
  - ERP'de Cari kart ayarları 2'de "Vadesinde ödenmeyen bakiyelerin kontrolünü yap" açılır.
  - Mobil Server'da Cari Gönderimi'nde aynı kontrol açılır.
- **Tasarım (`.arp`):**
  - Mobil Server → Yazıcı Form Tasarımları'nda düzenlenir [2359]. Alanlar "Fatura Yazdırma" tablosundan seçilir.
  - "Tasarımı Mobil Satış formatına çevir" ile `.ini` dosyasına dönüştürülür [2647]. Cihaz "Rapor Tasarım Dosyalarını Al" ile çeker.
  - Birden fazla fatura tasarımı `fatura_<ad>.arp` adıyla eklenir, her biri ayrı çevrilir [3516].
  - Satır bitiminde kesmek için "Detay Özeti = Var" yapılır, alt toplamlar footer'a taşınır [2356].
  - Logo: `DefDesign` klasörüne ve cihazdaki `Pictures` klasörüne aynı adla konur. Alan adı `IMAGE_logo.png` olur, boyut ~50×50 px [3071].
  - Karekod: tasarıma eklenir ve merkeze gönderim açılır [3734].
- **Yazıcı:**
  - Bluetooth termal ya da dotmatrix (SKS1/SKS2, bluetoothlu Epson LX-300, RW-420) [299].
  - Android'de "Mobil Printer" APK'si ile yazıcı eklenir. Bluetooth taraması için konum izni açık olmalı [3262][3590].
  - Etiket için `.prn` tasarımı (Argox/Zebra) `...\MobilServer\DefDesign` altında durur. Cihaza `etiket.prn` adıyla elle kopyalanır [3708].
- **Saha işlemleri:**
  - Depo transferi, satıra açıklama eklenebilir [2650].
  - Stok sayımı: senkronizasyonla ERP'ye gider, ERP'de "Stok ve Sayım Düzenleme"den alınır [2651].
  - Rota: rota grubu tanımlanır, pazarlamacıya atanır, günlük veya haftalık planlanır [3594].
  - Sevkiyat planlama: yalnız "Beklemede" durumundaki siparişler listeye gelir [3491].
  - Faturada pazarlamacının görünmesi için ERP'de "Pazarlamacı kullan = Fatura bazında" seçilir [3593].
- **[3499] Otomatik veri oluşturma:** Mobil Server bütün pazarlamacıların verisini belirli saatlerde önceden hazırlar. Böylece veri alma hızlanır (9.02.01'de günlük/saatlik periyot eklendi [3825]).
- **Sürüm notları:**
  - [3825] 9.02.01: Pazarlamacı yetkisi kopyalama. **Tevsik kapsamında 7.000 TL'yi aşan nakit tahsilatı engelleme ayarı.** Yazdırma yetkileri. Taşıyıcı bilgileri.
  - [3875] 9.03.01: Çoklu stok grubu seçimi. 10 banka hesabı. Tarih formatı.
  - [3770] 8.08.08: Rota ve ziyaret notları.
- **[293] Restoran PDA (eski Windows Mobile):** En az 320×240 ekran, WM5/6 veya CE5, dokunmatik ve Wi-Fi gerekir. Önce .NET Compact Framework 2.0/3.5 kurulur.

## AKINSOFT e-Ticaret ↔ WOLVOX: sık sorulanlar ve sorun giderme
- **[3327] / [3647] ERP'den ürün siteye gitmiyor veya güncellenmiyor.** Kontrol sırası:
  1. Stok kartı **aktif** olmalı.
  2. Özel Ayarlar 1'de **"Web'de Görünsün"** işaretli olmalı.
  3. **Grubu** dolu olmalı ve grubun kendisi de "Web'de Görünsün" olmalı.
  4. e-Ticaret panelinde **Tam Senkronizasyon** seçili olmalı. Kısmi senkronizasyonda yeni ürün gitmez, yalnız güncelleme olur.
  5. Web Entegrasyon'da **Test Et** başarılı olmalı. Başarısızsa muhasebe kullanıcısının şifresi panelde yenilenip programa yeniden girilir.
  6. Web Entegrasyon → Stok Ayarları 2'deki **Özel Kodu 1/2/3 filtreleri**: doluysa yalnız aynı özel kodu taşıyan stoklar gider. Silinirse bütün stoklar gider, bu yüzden silmeden önce yetkiliye sorulmalı.
  7. Ürün panelde pasif listede olabilir (filtre "Durum: Hepsi").
  8. **Paket ürün limiti** (aktif ve pasif ürünler birlikte sayılır): Platinum 5.000, Professional 10.000, Advanced 50.000, Enterprise sınırsız.
- **[3383] Sipariş sonrası stok düşümü:** İki yol var.
  - Siparişi **direkt fatura** olarak kaydetmek.
  - **Sipariş olarak kaydedip bloke** kullanmak: Sipariş ve Stok 2 modülleri gerekir. ERP Genel Ayarlar → Sipariş Ayarları → Sipariş Bloke = Evet. Web Entegrasyon'da "Stok miktarına bloke miktarını dahil ederek gönder" açılır. Fatura kesilince bloke kalkar.
- **[3358] "Üyeliğiniz muhasebe sisteminde aktif değildir" (cari ödeme ve bakiye):**
  - Sitedeki bakiye sorgulama ve cari ödeme, e-Ticaret panelindeki "Entegrasyon Yönetimi (bakiye sorgulama ve ödeme)" ayarıyla **doğrudan Kontrol Paneli'ne bağlanır** (SDK altyapısı).
  - Gerekenler: **statik IP**, DB yetkili kullanıcı adı ve şifresi (MSSQL'e geçişte değişebilir), **3056 portu dışarıya açık**, doğru şirket kodu, şube kodu ve güncel çalışma yılı. Eski yıl seçilirse ödeme devredilmiş yıla yazılır.
  - Üyenin muhasebe kodu ERP'de yoksa Web Entegrasyon'dan "Carileri Al" yapılır.
- **[3382] Üye bakiyesini göremiyor:** Aynı Entegrasyon Yönetimi bağlantısı "Test Et" ile kontrol edilir.
- **[3361] Cari ödemeler ERP'ye düşmüyor:** Sanal POS taksit tanımları ERP banka taksit tanımlarıyla eşleştirilmemiş ([3360] "Ticari Program Eşleştirme").
- **[3386] Panelde "Wolvox'a gönderildi" yazıyor ama ERP'de yok:** Web Entegrasyon yanlış şirket, şube veya yılda açılmış olabilir ([3394] şirket adına tıklayıp değiştirilir). Yeniden gönderim için destek gerekir.
- **[3670] e-Faturalar sanal pazara gitmiyor:**
  - Web Entegrasyon ≥ s8.06.11 olmalı ve "e-Fatura/e-Arşiv PDF linklerini e-Ticaret'e otomatik gönder" açık olmalı.
  - Faturadaki e-Ticaret sekmesinde "E-Ticaret Satış" = Evet olmalı.
  - ERP'de e-Fatura Durum Sorgula çalıştırılır.
- **[3359] / [3216] Üye tipinin ERP'ye taşınması:** "Üye tiplerini kaydet" bir özel koda ya da özel alana bağlanır. Değerler "Bayi", "Üye" ya da "Toptancı" olur.
- **[3555] Sitede bozuk ülke/il/ilçe listesi:** Kaynağı ERP cari kartlarına elle ve hatalı girilmiş değerlerdir (sonda boşluk, yanlış alan).
  - ERP'de cari listesi ilgili alana göre filtrelenip düzeltilir.
  - Panelde Site İçerikleri → Ülke ve Şehirler'den hatalı kayıt silinir.
  - Web Entegrasyon'dan "Cari Gönder" yapılır.
- **[3639] KDV oran değişikliği (10.07.2023, %8→%10, %18→%20):** Panelde varsayılan KDV güncellenir. Senkronizasyon açıksa KDV ERP'den düzeltilip yeniden gönderilir.
- **[3500] "Hangi mağazada var":** ERP'de Depo modülü gerekir. Web Entegrasyon'da "Depo envanterini gönder" açılır ve Stok Ayarları 2'de depolar seçilir.
- **Salt e-Ticaret panel ayarları** (ERP'siz):
  - Üyeliksiz alışveriş [3324]. Online Market açıkken kapanır.
  - Sepete Ekle görünmüyor [3357]: tanıtım modu, fiyat yok, ya da stok yok ve stok kontrolü açık.
  - Sipariş alınamıyor [3345]: tanıtım modu, açık adres zorunlu, kargo tanımı eksik.
  - Kargo ücreti görünmüyor [3352]: alıcı ödemeli seçilmiş.
  - Liste fiyatı ile sepet fiyatı farklı [3461]: Ürün Listeleme Ayarları'nda B2B, B2C ve misafir için fiyat sırası aynı olmalı.
  - "Sanal pos bulunamadı" [3400]: varsayılan POS seçilmemiş.
  - Ödeme alındı ama sipariş düşmedi [3523]: 3D dönüşü tamamlanmadan sayfa kapatılmış.
  - Mail bildirimi gelmiyor [3393]: sistem mail tanımı.
  - Domain ve NS [3414][3458], Facebook ve Google Merchant doğrulaması [3472][3489][3490], desi hesabı (en×boy×yükseklik/3000; yurt dışında /5000) [3619], iade ve değişim [3582], B2B modülü [3331][3426][3556].

## WOLVOX ERP sürüm geçmişi ve yeni özellikler (2024–2026)
Sürüm numaralandırması 9.x'ten sonra **yıl bazlı** oldu (26.xx.xx = WOLVOX 26 dönemi).

| Sürüm | Tarih | Öne çıkanlar |
|---|---|---|
| 8.25.07 [3767] | 31.01.2024 | Sevkiyat planlama için mail/SMS. "Eksiye düşen stokta işleme devam", "Yazdırılanları düzenleyebilsin" yetkileri. "İade edilemez ürün". **Kur farkı faturası** tipi. |
| 9.02.01 [3817] | 01.07.2024 | Formlarda sevk adresi yerine fatura adresi. Faturada Birim 2 / Miktar 2 raporu. Tevkifat KDV tanımı uyarısı. e-Arşiv gelen kutusuna QR ile aktarım. e-İrsaliyede fiyatı 0 gönderme. Login'de son 5 kullanıcı adı hatırlanıyor. |
| 9.03.01 [3873] | 05.11.2024 | Hareket satırındaki çoktan seçmeli özel alanlarda **`CODE=QUERY()`** (seçenekleri SQL ile doldurma). K.V. stopaj. Zorunlu alanlara GTİP. İstisna kodlu stokta KDV 0. Lokasyon bazlı sayım. Excel stok aktarımında diğer birimler (`KG-2,5-C|Koli-10-C|Palet-1000-C`). Esnek kredi yapılandırma. |
| 9.03.02 [3883] | 09.12.2024 | Siparişten faturaya 301 istisna kodu. e-Müstahsilde GV stopajı 0. Vergi dairesi alanı 250 karakter. |
| 9.04.01 [3935] | 19.06.2025 | **WolvoxAI** eklendi. Açık Bankacılık (FinCloudy) iyileştirmeleri. POS/provizyon aylık analizi. **İlaç ve Tıbbi Cihaz** ile **SARJ/SARJANLIK** e-Fatura tipleri. Masraf faturasında tevkifat. |
| 9.05.01 [3970] | 01.10.2025 | Belge türü detayı. Fatura notu 2000 karakter. Seri/lot için Excel'den alma. 85 No'lu KDV uyarısı. Carinin varsayılan fatura senaryosu. 702 istisnada DİB satır kodları. 344 istisna kodu. ÖTV istisna kodları 101–108. **FastReport tasarımları veritabanında saklanıp paylaşılabiliyor**, aktif şirket ve şube parametreleri kullanılabiliyor. |
| 26.02.01 [3987] | 01.12.2025 | **Program dosyasının adı `werp9.exe` → `werp.exe` oldu.** Eski kısayollar otomatik silinir, yenileri oluşturulmalı. Seri/lotta üretim tarihi. UNO alanı 23 karakter. İlaç takibi için UNO/GTIN. Cari birleştirmede kaynak cari pasife alınabiliyor. |
| 26.03.01 [4017] | 09.03.2026 | **MRP reçete revizyon sistemi**. Cariye **zorunlu ödeme yöntemi** (tutarın tamamı ya da belirli yüzdesi ödenmeden fatura kaydedilmez). Gelen kutusunda cari ve stokların otomatik eşleşmesi, eksik olanların oluşturulması. `.webp` desteği. Depo transferinde maliyet hesabı. Yeni Online İş Merkezi izleme ekranları. WolvoxAI İngilizce. Takım birimi kodu 5B. |
| 26.04.01 [4083] | 11.08.2026 | **Obifin Açık Bankacılık**. Döviz ve virman hareketleri aktarımı. Dekont no son 6 hane → evrak no. **Satın alma talebi onay sistemi** (Genel Ayarlar → Program; "Durumu Beklemeye Alabilsin (Onay Sistemi)" yetkisi). Mal kabul ve sevkiyatta karekod. **Stok İhtiyaç Planlama** (tahmine dayalı; 3/6/9/12 ay; stok kartında "Tahmini üretim ve tedarik süresi"). Hizmette KKEG'ye düşen KDV için ayrı hesap. 226 istisnada 0 KDV. İDİS'te birden fazla etiket. Stok ve cari muhasebe kodları boş bırakılabiliyor. |

Diğer ürünlerin sürüm notları:
- **Veri Transferi 26.03.01 [4066]:** ÜTS API uçları güncellendi. Mükerrer seri/lot kontrolü. "11111111111" TCKN uyarısı.
- **Genel Muhasebe 26.03.01 [4069]:** Envanter defteri için ek hesaplar (Ayarlar 3). Zorunlu alanlar. Kira fişi sayacı. Geçmiş tarihli kur girişi. İndirilecek KDV listesine yeni kolonlar.
- **e-Ticaret 1.15.11 → 1.26.01 [3646…4090]:** Panel sürüm notları. Tam liste için `python tools/bilgibankasi.py baslik "e-Ticaret 1\."`.

### WOLVOX ERP kategorisindeki diğer makaleler
- **[3934] WolvoxAI (yapay zekâ asistanı):**
  - Fatura, stok ve cari için **yalnız listeleme ve rapor** sorgularına cevap verir. Kayıt eklemez, silmez, güncellemez. e-Fatura kontörü de buradan alınabilir.
  - Kurulum: Kontrol Paneli → Yetkili → Özel Ayarlar → Yapay Zekâ Kullanımı = ChatGPT, "+" ile **OpenAI API key** girilir. Ücreti OpenAI keser, AKINSOFT sorumlu değildir.
  - Yetki: "WolvoxAI Yapay Zekâ Asistanını Kullanabilsin". Asistan yetkili düzeyinde çalışır.
  - ERP'de arama düğmesinin yanındaki AI simgesiyle açılır.
  - Ses tanıma ve seslendirme Kontrol Paneli'nden açılır. Yerel WolvoxAI motoru için NVIDIA GTX 1050 veya üstü gerekir; diğer seçenek OpenAI (token başına ücretli).
- **[3306] Firebird'i kaldırıp yeniden kurma:**
  - Önce Denetim Masası → Firebird Server Manager'dan **sürüm** öğrenilir. Yeni makineye aynı sürüm kurulur.
  - Kaldırdıktan sonra `Program Files (x86)\Firebird` klasörü (32 bit Windows'ta `Program Files\Firebird`) silinir ve bilgisayar yeniden başlatılır.
  - Yeniden kurulunca kullanıcı SYSDBA, şifre masterkey olur. Güvenlik için değiştirilmeli ([1457] Firebird şifresi değiştirme).
- **[3538] Maliyet muhasebesi (MRP II'ye bağlı, fiili maliyet yöntemi):**
  - Genel Ayarlar → Genel Muhasebe Ayarları → Genel2'de "Maliyet Muhasebesi Kullan" açılır.
  - Stok kartında dört hesap tanımlanır: mamul yansıma, gider yansıma (711), ilk madde gider (710) ve maliyet.
  - Dönem tanımlarında çalışmayan kısım gider oranı girilir. Gider tanımlarında hesap kodu, yansıma kodu ve MRP II eşleştirmesi yapılır.
  - İşlem sırası: ilk madde → dağıtım → çalışmayan kısım fişi → yarı mamul (151) → mamul (152) → stok hareket fiyatını güncelle → MRP II maliyetini güncelle → satılan mamul maliyeti.
  - Birim maliyet: `BM = (İMM + ((GG + İG) / ToplamMiktar) × ÜrünMiktarı) / ÜrünMiktarı`.
  - Bu açıkken MRP II kendi maliyetini hesaplamaz.
  - Raporlar gider, stok ve üretim bazındadır.
- **[3640] KDV oran değişikliği (2023):** ERP en az 8.24.06 olmalı. Stok Tanımlar Listesi → filtrele → İşlemler → **Bilgi Güncelle** ile KDV toplu değiştirilir. GM'de yeni KDV tanımları açılır.
- **[3701] TCMB kur indirme hatası:** İnternet Seçenekleri → Gelişmiş'te "sunucu sertifikası iptalini denetle" ve "şifreli sayfaları diske kaydetme" kapatılır.
- **[3787] Pazarlamacı hedefi:** Pazarlamacı kartında Özel Bilgiler 2 → Hedef Tanımları (gün, ay ya da yıl; dövizde hesap seçilir) → "Pazarlamacı Hedef Analizi" raporu.
- **[3789] Stok sayım ve düzenleme:**
  - Depo seçilir ve "Envanter son tarih" (sayımın yapıldığı gün) girilir.
  - Excel veya txt'den kod/barkod ve miktar kolonları okunur. Sayım tipi: depo sayımı, stok girişi ya da çıkışı.
  - "Sayılmayan ama bakiyesi olan stokları ekle" seçeneği var.
  - Son adım "Stok harekete işle". Giriş/çıkış tipinde "Muhasebelendir" ile irsaliye veya fatura oluşturulur.
- **[3792] Şube izleme ekranı:** Ana şubeden diğer şubelerin nakit, dekont ve POS işlemleri otomatik yenilemeyle izlenir.
- **[3816] Program bazlı modül bağımlılıkları:** Restoran, Hızlı Satış, Otel ve İK içindeki cari, kasa ve stok işlemleri ERP lisansındaki Cari 1 / Kasa / Stok 1 / Depo / Fatura modüllerini ister. GM'de bütçe için Bütçe, kur için Döviz modülü gerekir.
- **[3998] Ters kur girişi:** KPB'si yabancı para (ör. USD) olan ülkeler için `gunlukterskurgiris.asspack` script paketi Yetkili → Tanımlar → Script Paket İşlemleri → Paket Yükleme ile kurulur, program yeniden açılır. Script paketlerinin gerçek bir kullanım örneği.

## Wolvox 9/26 sistem yönetimi ve geliştirici ipuçları (ek)

### Tasarım ve rapor (ARP, Gelişmiş Tasarım, FastReport)
- **[4081] ARP tasarımına başka bir tablodan SQL ile veri çekme** (makaledeki GIF'ten okunmuştur):
  1. Tasarıma bir **Alt Detay** (QRSubDetail) bandı eklenir. Özelliklerinde Veritabanı = `1`, "Dataset Adı" (ör. `STOK_TEDARIKCI`) ve Master = `Report1` olur.
  2. "SQL Sorgu" alanına sorgu yazılır. Ana tablodaki alan **`GETVALUE(TABLO.ALAN)`** ile bağlanır:
     ```sql
     SELECT STOKKODU AS TEDARIKSTOK
     FROM STOK_TEDARIKCI
     WHERE BLMASKODU = GETVALUE(SIPARISHR.BLSTKODU)
     ```
  3. Değer detay satırında bir expression ya da data alanıyla gösterilir (örnekte "TEDARIK" kolonu).
  - Bu örnek iki şeyi doğruluyor: `STOK_TEDARIKCI.BLMASKODU` stok kartının BLKODU'suna bağlanır, `STOKKODU` tedarikçinin stok kodudur.
- **[3920] Gelişmiş Tasarım Sistemi (FastReport tabanlı):**
  - Formun Yazdır → Ayarlar ekranında bir `.arp` seçilip **"Gelişmiş Rapora Dönüştür"** ile çevrilir.
  - Alanlar sağdaki Veri Ağacı'ndan sürüklenir. Metin nesnesinde Σ ile expression ve koşul yazılır, Format sekmesinden biçim verilir.
  - 9.05.01'den beri tasarımlar veritabanında saklanıp paylaşılabiliyor ([3970]).
- **[4035] FastReport'ta stok resmi:** Resim nesnesinin "File Link" alanına `[As_StokResim(<TEKLIFHR."BLSTKODU">)]` yazılır. Fonksiyon Veri Ağacı → Fonksiyonlar → AKINSOFT altındadır.
- **[3944] ARP'de stok resmi:** Rapor veri setinde BLSTKODU veya STOK.BLKODU bulunmalı. Resim alanında:
  - Parametre = "Aktif Stok Resmi", Bağ Tablo = hareket veri seti, Bağ alanı = BLSTKODU
  - **Veritabanı = "Dosya"** (resimler `dosya.fdb` tarafında durur)
  - **Bağ kodu formatı `WO_STLOGO_%sb_%ad`**
- **[3600] Fatura Özel Raporu:** Gruplanacak alanlar seçilerek serbest rapor hazırlanır. Fatura, stok ve cari filtreleri kullanılabilir.
- **[1953] Joker karakter eşleştirme (SQL veritabanı, ERP 8.14.05+):** F7 Filtre Düzenleme'de Türkçe karakter varyantları (Ümit/Umit, Yiğit/Yigit) tek aramada bulunur.

### Yetki, lisans, offline
- **[3739] Ek Yetkiler 1: SQL koşuluyla satır bazlı yetki.**
  - Yeri: Kontrol Paneli → Kullanıcı Yetkilendirme → Ek Yetkiler 1. Kullanıcı, şirket ve yıl bazında tanımlanır.
  - Cari, stok, fatura, irsaliye, teklif, sipariş, doküman takibi, İK ve hesap planı listelerine **WHERE'e eklenen bir SQL koşulu** yazılır. Örnekler:
    - `COALESCE(CARI.GRUBU,'') NOT IN ('X') AND COALESCE(CARI.ARA_GRUBU,'') NOT IN ('Z')`
    - `STOK.GRUBU NOT IN ('GIDA','İÇECEK')`
    - `HESAP_PLANI.HESAP_KODU NOT LIKE '335%' AND HESAP_PLANI.HESAP_KODU NOT LIKE '500%'`
  - Bu örnekler tablo ve alan adlarını da doğruluyor: `CARI.GRUBU`, `CARI.ARA_GRUBU`, `STOK.GRUBU`, `HESAP_PLANI.HESAP_KODU`.
- **[3826] Kullanıcı–modül eşleştirme (Wolvox 9 lisansı):**
  - Kullanıcı hakkı modül bazında verilir. Atanmamış modül kullanıcıya görünmez. **SYSDBA/sa'ya da atama gerekir.**
  - Renkler: yeşil = atanmamış, mor = hakkı dolmamış, gri = hakkı bitmiş, kırmızı = uygun değil.
  - Toplu atama sağ tıkla yapılır. Kaynak kullanıcının yetkileri hedef kullanıcıya kopyalanabilir.
- **[3834] Offline sistem (Wolvox 9):**
  - Lisansta **Şube modülü** gerekir. Şirket kaydında "offline kullanıma izin ver" açılır, Şube Kayıt'ta "Offline Personel Ata" yapılır.
  - Bir kullanıcı yalnız bir şubede offline olabilir. SYSDBA/sa ile offline çalışılamaz.
  - Veri Al/Gönder kullanıcı bilgileriyle yapılır.
- **[3717] Tarih kontrol sistemi:** Genel Ayarlar → Program Ayarları'nda iki ayar var.
  - Çalışma yılı: aktif yıl dışına izin verme / sorarak onay al / kontrol etme.
  - Tarih: aktif ay öncesine / aktif gün öncesine / onay tarihi öncesine izin verme.
  - İstisna tutulacak kullanıcıya Kontrol Paneli'nde "Onay Tarihi Kontrolü Yapma" verilir.
- **[3868] Güncelleme paketi (WOL9 GP) isteyen mobil uygulamalar:**
  - İsteyenler: Reporter (iOS/Android), Fiyat Gör, DepoMaster, Restoran Mobil iOS.
  - İstemeyenler: Restoran Mobil Android, Mobil Satış (Android/WM), **Wolvox SDK**.

### Güncelleme ve sürüm sorunları
- **[3863] Sürüm güncelleme:**
  1. Kontrol Paneli → Veritabanı İşlemleri → Yedekleme → **Şimdi Yedekle** (hedef `AS_YEDEK`).
  2. Programlar kapalıyken `AKINSOFT` klasörü başka bir yere kopyalanır.
  3. Kontrol Paneli **Yetkili → Programdan Çık** ile kapatılır. Kapatılmazsa sürüm uyuşmazlığı çıkar.
  4. Installer (AKINSOFT klasöründe ya da akinsoft.com.tr'de) ile programlar seçilip kurulur. "Sadece dosyaları indir" seçeneği de var.
- **[3869] Kontrol Paneli sürüm hatası:** `AKINSOFT\Wolvox9\KontrolPanel\sysas.ask` silinir ve yeniden lisanslanır. Düzelmezse `C:\Windows\System32\drivers\etc\hosts` dosyasındaki yönlendirme kaldırılır.
- **[4037] "-90" güncelleme hatası:** Makaledeki `kontrolpanelfix` aracı Kontrol Paneli kapalıyken kurulum dizini seçilerek çalıştırılır. Araç süreli.
- **[3850] Wolvox 8 → güncel sürüm farkları:** Açık Bankacılık, DepoMaster, Tüp/Su modülü, `CODE=QUERY()` ve diğerleri (ayrıntı [3817]/[3873] sürüm notlarında).

### Depo, stok, maliyet
- **[3872] Wolvox DepoMaster (Android sayım uygulaması):**
  - Depo ve Stok 2 modülleri ve Kontrol Paneli 9.02.13+ gerekir.
  - APK `http://<sunucu-ip>:3056/depomaster/index.html` adresinden indirilir (**güncelleme portu 3056**).
  - Kullanıcı ve sunucu bilgisiyle girilir, şirket/yıl/şube seçilip senkronize edilir. Sayım listesi aktarımı ayarlardan açılmalı.
  - Kaydedilen sayım ERP'de **PDA Sayım Listesi**'ne gelir.
- **[499] Lokasyon yönetimi (Depo modülü içinde):** Depoya lokasyon ve alt lokasyon tanımlanır, kroki üzerinde işaretlenir. "Lokasyon Hareket Girişi" ile giriş ve çıkış yapılır. 9.03.01 ile lokasyon bazlı sayım geldi.
- **[3601] Transfer irsaliyesinde FIFO:** Genel Ayarlar → İrsaliye Ayarları → İrsaliye sabitleri → stok fiyatı = FIFO. Transferde eski giriş hareketleri listelenir.
- **[3964] Kâr/zarar raporunun maliyet seçenekleri:**
  - Alış fiyatı 1–4, en son alış.
  - **Ortalama** (fiyatların basit ortalaması).
  - **Ağırlıklı ortalama** (Σtutar / Σmiktar).
  - **FIFO** ve **LIFO**.
  - Seçilen yönteme göre sonuç değişir. Karşılaştırma yapılırken hangi yöntemin seçildiğine bakılmalı.

### Finans: banka entegrasyonu, mutabakat, kur farkı, finansal analiz
- **[4085] Açık Bankacılık (FinCloudy veya Obifin):**
  - Banka modülü gerekir. Kontrol Paneli → Şirket Kayıt → Açık Bankacılık İşlemleri'ne bilgiler girilip **Test Et** yapılır:
    - FinCloudy: kullanıcı adı, parola, kurum kodu/ID.
    - Obifin: kullanıcı adı, parola, API key.
  - Eşleştirme: cari **gönderen/alıcı IBAN ve vergi no** ile, banka **IBAN** ile bulunur. Eşleşmeyenler elle seçilir. Virmanda karşı banka seçilmelidir.
  - İşlem türü kodları: `TRFGEL`, `TRFGID` (havale/EFT), `VIRMGEL`, `VIRMGID`, `PERSODE`, `OGSHGS`, `MASRKOM`, `KARTODE`, `KRDODE`.
  - Eski "Banka Online Veri Al" modülüne göre farkı: giden EFT, FAST ve portal da gelir. 11 yerine 23 banka desteklenir. Ücret banka sayısına göredir.
- **[1718] / [2278] Banka Online Veri Al (eski modül):**
  - Bankaya imzalı "online ekstre" formu verilir ve bankadan kullanıcı adı ile parola alınır.
  - Kontrol Paneli'nde şirket kaydı → Özel Bilgiler'de **"Online veri al"** açılır.
  - ERP'de Banka Tanımı'nda IBAN ve API bilgileri (entegrasyon bankası, kullanıcı, parola, son işlem tarihi) girilir.
  - [3011] "Could not load SSL library" (ör. Windows Server 2012): Kontrol Paneli kapatılır, dizinine `ssleay32.dll` ve `libeay32.dll` konur ya da yenilenir.
- **[1946] / [3719] / [3720] / [4084] e-Mutabık (e-mutabakat, BA/BS ve cari):**
  - ERP'de B formlarından ya da bakiye listesinden gönderilir. e-mutabik.com kullanıcı bilgileriyle çalışır.
  - Ücreti yalnız gönderen öder (kontör). Onaylayan tarafın üye olması gerekmez.
  - Kullanıcı izinleri ve HTML şablon tasarımı web panelinden yapılır.
- **[3758] Kur farkı faturası (8.25.07+):**
  - Önkoşul: carinin döviz hesabına dövizli bir hareket ve karşı dövizli hareket olmalı. İkisi **manuel yaşlandırma** ile kapatılır.
  - "Kur Farkı Faturalandırma" raporunda durumlar: yaşlandırma yapılmamış / tamamlanmamış / fatura alınacak / fatura kesilecek. "Faturalandır" ile fatura oluşturulur.
  - Oluşan faturanın özellikleri:
    - Tipi "Kur Farkı", KDV dahil tutarı kur farkına eşit.
    - Cari ya da stok hareketine işlemez, iskonto ve formül uygulanmaz.
    - e-Fatura notuna "Kur Farkı Faturası" yazılır.
    - Bağlantısında asıl faturanın numarası tutulur. Kur farkı faturası silinmeden asıl fatura değiştirilemez.
  - Yetki, hizmet tanımı, hizmet muhasebe kodu ve fatura sabitleri önceden ayarlanır.
- **[3799] / [3804] / [3807] Finansal analiz:** Likit kontrol seviyesine göre "nakit temin edilmeli" ya da "yatırım yapılabilir" raporlar.
  - Hesaba katılabilecekler: cari bakiyeler, opsiyonlu, rotatif ve vadeli banka hesapları, zamanlı hesaplar, protestolu çek/senet.
  - Periyot günlük, haftalık, aylık, 3/6 aylık ya da yıllık seçilir.
- **[3707] Bütün carilerin döviz hesabını kapatma:** Cari Tanımlar Listesi → filtrele → İşlemler → **Bilgi Güncelle** → Diğer → "Döviz hesabı kullan" işareti kaldırılır. Bilgi Güncelle genel bir toplu güncelleme aracıdır.
- **[3703] e-Faturada döviz kuru:** e-Fatura Ayarları → "Not alanına eklenecek döviz kuru": güncel ya da fatura kuru, alış/satış.

### Satış ve evrak ayarları
- **[3716] Kaynak iskonto:** Fatura, irsaliye, teklif, sipariş ve servis ayarlarında iskontonun kaynağı seçilir: **Genel Ayarlar** (sabit oran), **Cari** (Cari kart → Hesap Bilgileri) ya da **Stok**.
- **[3602] İrsaliye faturalanınca cari hareket faturaya bağlansın:** Fatura sabitlerinde "irsaliyenin faturalandırılması sırasında cari hareket entegrasyonunu fatura ile ilişkilendir" açılır.
- **[3677] Tekliften siparişe özel alan aktarımı:** Teklif bilgilerindeki "Özel tanım aktarma ayarları"nda eşleştirme yapılır, sonra İşlemler → Kopyala.
- **[3662] İhraç kayıtlı fatura:**
  - Yurt içi satış faturasında Ek Bilgiler 1'de "İhraç Kaydı" işaretlenir.
  - Satırda istisna kodu seçilir.
  - e-Fatura "?" ekranında tip = İhraç Kayıtlı yapılır.
- **[3709] Belgeye QR kod:** Tasarıma karekod eklenip içine bir URL yazılır.

### Yıl sonu devri ve WolvoxCloud'a geçiş
- **[3845] / [3718] 2026'ya devir (Wolvox 9 ve Wolvox 8):**
  - Önce bütün programlar güncellenir ve **yedek alınır**.
  - Teklif, sipariş veya servis için ek durum tanımları varsa, devirden önce Şirket Kayıt → "Çalışma Yılı Oluştur" ile taşınır.
  - Bütün kullanıcılar çıkar. Kontrol Paneli → Yetkili → **Devir İşlemleri**'nde oluşturulacak yıl (2026) ve devir için son işlem tarihi (31.12.2025) girilir, şirketler ve modüller seçilir, "Tüm kontrollerimi yaptım" → **Devir İşlemine Başla**.
  - Devirden sonra bakiyeler kontrol edilir.
  - Yeni yılda devirden gelen kayıtlar değiştirilemez. Eski tarihli işlem de girilemez.
- **[4056] WolvoxCloud'a aktarım:**
  - Kontrol Paneli son sürüm olmalı, güncelleme paketi bulunmalı. Bulut şirketinin **VKN**'si Kontrol Paneli'ndeki şirketle aynı olmalı.
  - Kontrol Paneli → **Upgrade → WolvoxCloud Aktarımı** → klasör seçilir → şirketin aktarım dosyası oluşturulur (istenirse dosya, resim ve PDF'ler dahil) → Aktarım İşlemine Başla → WolvoxCloud sayfasında yüklenir.
- **[4078] WolvoxCloud yardımı:** Menü yapısıyla eğitim videolarının listesi (bkz. `menu-haritasi.md`). **[4096] WolvoxCloud 1.03.01** (15.09.2026): yetki grupları yeniden düzenlendi, stok ve cari arama iyileştirildi.
- **[3857] Enflasyon muhasebesi:**
  - Genel Muhasebe ve Demirbaş modülleri gerekir.
  - Yasal şart: Yİ-ÜFE son üç dönemde %100'ü, içinde bulunulan dönemde %10'u aşarsa **yalnız bilanço** düzeltilir.
  - Makalede adım adım uygulama var.

### e-Dönüşüm (ek makaleler)
- **[1801] e-Fatura ayarlarının tamamı:**
  - Önce Kontrol Paneli'nde şirket kaydı → **e-Devlet 1** sekmesinde e-Fatura / e-Arşiv / e-İrsaliye / e-Müstahsil açılır.
  - Ayarlar ERP'de Satış Yönetimi → Faturalar → e-Fatura → e-Fatura Ayarları'ndadır.
  - **Genel sekmesi:** not aktarımı, şahıs firmasında unvanı ad-soyada yazma, gönderimden sonra fatura no'yu güncelleme, PDF'i dosyalara kaydetme, kayıtta "gönderilsin mi?" sorusu, VKN ve e-posta zorunluluğu, cari bakiyesi, bağlı evrak no, vade, tedarikçi stok kodu.
  - **Varsayılan sekmesi:** senaryo (Temel / Ticari; ticari faturayı alıcı reddedebilir), gönderim tipi kağıt/elektronik (elektronik e-ticaret içindir), hesap/döviz.
  - **Entegratörler:** EDM Bilişim, Digital Planet, İzibiz, Süper Entegratör. EDM'de "taslak olarak portala kaydet" seçeneği var.
  - **Sayaç:** Yetkili → Sayaç İşlemleri. Basamak sayısı 9'a tamamlanır. "Başa Ekle" = 3 harf + yıl. Birden fazla kullanıcı gönderiyorsa şablon kodları girilir. EDM'de portal sayacı da tanımlanır.
- **[3726] Opsiyonel alanlar:** e-Fatura/e-İrsaliye Ayarları → Opsiyonel Alanlar'dan fatura, hareket, irsaliye ve stok alanları XML'e eklenir.
  - Gönderimden sonra oluşan XML şu klasöre yazılır: `<ERP dizini>\Temp\<kullanıcı>\Efatura_Giden` (ya da `Eirsaliye_giden`).
  - Tasarımda görünmesi için bu XML entegratöre gönderilir. **Bu klasör UBL çıktısını incelemek için de kullanışlı.**
- **[3199] Dış modül bağlantıları (UBL):** "Dış Modül Bağlantı Bilgilerini Gönder" açılırsa sipariş `cac:OrderReference/cbc:ID`, irsaliye `DespatchDocumentReference` içinde gider.
  - Elle yazılıyorsa "İrsaliye" ve "Sipariş" baş harfi büyük yazılmalı.
  - İkisi birlikte gidecekse akış sipariş → irsaliye → fatura olmalı.
- **Fatura tipleri** (e-Fatura "?" ekranı):
  - Tevkifat [3672]: satırda tevkifat kodu ve oranı.
  - SGK [3674]: cari SGK vergi numarasıyla açılır, SGK alanları doldurulur.
  - İstisna [3675]: satırda istisna kodu.
  - İhraç kayıtlı [3662].
  - **İlaç ve Tıbbi Cihaz [3936]:** senaryo `ILAC_TIBBICIHAZ`. Stokta tür ve GTIN girilir. İlaçta parti, seri ve SKT, tıbbi cihazda parti, seri ve üretim tarihi zorunludur (Seri/Lot'tan gelir).
  - **Yatırım Teşvik [3995]:** senaryo `YATIRIMTESVIK`; tipler SATIS, ISTISNA, IADE, TEVKIFAT, TEVKIFATIADE. e-Arşivde YTBSATIS vb. 26.03.01'den itibaren cari ve yevmiyeye KDV yansımaz.
  - **IDIS (inşaat demiri) [3996]:** senaryo `IDIS`. 26.04.01'de birden fazla etiket no girilebiliyor.
  - Alıştan iade [3916]: iade edilen faturanın bilgileri "Fatura Bilgileri" sekmesine girilir (Wolvox 8 ≥ 8.25.22, Wolvox 9 ≥ 9.03.04).
- **Hatalar:**
  - "Fatura numarasındaki tarih ile fatura tarihi tutarsız" [3669]: sayaçta "Başa Ekle" eski yılda kalmış. Yıl düzeltilir, "basıma hazır no" 1 yapılır.
  - `java.lang.RuntimeException: kullanıcı bilgisi sistemde bulunamadı` [3659]: mükellef listesindeki posta kutusu (PK) etiketi portaldakiyle aynı değil.
  - Sertifika iptal uyarısı [3548]: İnternet Seçenekleri'nde "sunucu sertifikasını denetle" kapatılır.
  - Gönderilen fatura raporda görünmüyor [3546]: önce **Durum Sorgula** yapılır, GİB'de başarılı olanlar "Gönderilmiş e-Faturalar"a geçer.
  - Gönderildiği halde gönderim ekranında kalan fatura [3740]: **"Mnl.Ft.Ony."** ile GUID/ETTN girilerek elle onaylanır.
  - e-İrsaliye `EntityValidationErrors` [3982]: alıcı firma entegratörün adres defterinde yok, elle eklenir.
- **Gelen kutusu:**
  - İçeri aktarmada ürün adının kaynağı seçilir: gelen faturadaki ad ya da ERP'deki stok adı [3547].
  - Kayıtlı alış irsaliyesiyle eşleştirme yapılabilir; irsaliyenin cari/stok hareketine işlenip işlenmeyeceği seçilir [3713] ([3715] sipariş eşleştirme).
- **[3960] EDM Türmob:** Cari kartında VKN/TCKN'nin yanındaki "Cari bilgilerini EDM servisinden getir" butonu unvan, adres ve vergi dairesini doldurur. Her sorgu 1 kontör.
- **[3972] ASELSAN'a e-Fatura:** İki `.asspack` script paketi (`EFATURA.asspack` vb.) yüklenir.
  - KOBİ ve EYDEP bilgi ve tarihleri `AdditionalDocumentReference`'a, yerlilik oranı `AdditionalItemIdentification`'a, sipariş no `OrderReference`'a, kalem no `BuyersItemIdentification`'a yazılır.
  - **Script paketlerinin UBL XML'ini değiştirebildiğini gösteren resmî örnek.**
- **[3688] e-Defter "XML imzalama sırasında problem":** Yevmiye açıklamalarında kontrol karakterleri (ASCII 2, 28–31) vardır. Şu sorguyla bulunur:
  ```sql
  -- Firebird
  select tarihhr, hesap_kodu, hesap_adi, aciklama from yevmiyehr
  where aciklama like '%' || ascii_char(30) || '%'
  -- MSSQL
  select TARIHHR, HESAP_KODU, HESAP_ADI, ACIKLAMA from YEVMIYEHR
  where ACIKLAMA like '%' + NCHAR(30) + '%'
  ```
- **[4003] e-Envanter defteri:** Tebliğ Sıra No:6 ile envanter defteri de e-Defter olarak tutulabiliyor. Açılış ve kapanış envanteri, mali mühürle imzalanır. GM 26.03.01'de Ayarlar 3'te ek hesaplar tanımlanır.
- **e-Beyan (Beyanname programı, 9.04.01+):**
  - Damga vergisi [3932] (Mayıs 2025'ten itibaren), KDV-1 [3951], KDV-2 [3981].
  - Dijital Vergi Dairesi → e-Beyan → profil → **Entegrasyon Yönetimi → Oluştur** ile **token** alınır ve saklanır, sonra programa girilir.
  - Hata `Rest request failed: Error adding header (87)` [4060]: Beyanname klasörünün adı değiştirilip program yeniden kurulur.
  - [3977] KDV-1 özel matrah işlem kodları: 1001 altın, 1002 gümüş, 1003 kıymetli taş, 1004 ikinci el araç, 1005 ikinci el taşınmaz… İşlem bedeline KDV hariç tutar yazılır.

### ERP kullanım ipuçları (ek)
- **Tasarım:**
  - Fatura tasarımında stok resmi [3539]: Resim Sığdır = Var, Bağ Tablo = `FATURAHR`, Bağ Alan = `BLSTKODU`, Veritabanı = Dosya, Bağ Kodu Formatı = `WO_STLOGO_%sb_%ad`.
  - Çeki listesinde GTİP [3542]: Özel Ayarlar → Fatura Genel → "Faturayı yazdırırken stok bilgilerini çek" açılır. Tablo "Fatura Stok Bilgileri", alan `GTIP_NO`.
  - Etikette 2. birim fiyatı [3599]: tablo "Stok Etiket Yazdırma", alan "Diğer Birim Fiyatı 1".
  - Çoklu etiket [3463]: tablo "Stok Etiket Yazdırma". Detay bandında "Yeni Sayfa Aç" = Yok ise bir sayfaya birden çok etiket basılır, Var ise her etiket ayrı sayfaya.
  - Asorti matrisi [3913]: SubDetail bandı eklenir, tablo "Asorti Hareketleri Matris"; her beden için ayrı alan.
  - MRP II özel alanları [3738]: `MRP_EMIRLERI` tablosundan eklenir.
  - `Dizayn.arp cannot be read` [229]: `...\Wolvox9\ERP\DefDesign\` altındaki dosya silinmiş ya da taşınmış, yolu yeniden gösterilir.
  - Yazdırırken `Access violation … WERP9.exe` [246]: tasarımda "Detay" bandı "Var" yapılır (kaldırılırsa içindeki alanlar da silinir).
- **Fiyat etiketi yönetmeliği [3308] (8.21.07+):**
  - Genel Ayarlar → Stok Ayarları → Genel'de loglama türü (alış, satış ya da tümü) ve süresi (yasal olarak 30 gün) seçilir.
  - Etikete "Stok Etiket Yazdırma → En Düşük Fiyat" alanı eklenir (son 30 günün en düşük fiyatı). Çabuk bozulan ürünlerde bir önceki fiyat da basılabilir.
  - Restoranlar için bkz. [3756].
- **Bilgi Güncelle (toplu değişiklik):** Liste raporlarında İşlemler → Bilgi Güncelle ile KDV [3640], döviz hesabı [3707], istisna kodu, özel matrah kodu ve kâr marjı (26.04.01) toplu değiştirilir.
- **Excel aktarımları (Transfer menüsü):**
  - Cari ve stok kartı [441]: çalışma sayfası numarası, "ilk satır başlık", mevcut kayıtları güncelleme ya da yeni açma.
  - Hizmet [3790], cari yetkili [3794] ve cari kredi limiti [3797]: cari kodu eşleşmeli, para birimi simgeyle yazılır ($, €), her para birimine ayrı limit verilir.
  - Alan eşleştirmesi "+" ile şablon olarak kaydedilir.
- **Ayar noktaları:**
  - Alış faturasında satış fiyatı oluşturma penceresi [2024]: Özel Ayarlar → Fatura → Alış Faturası (istenirse "alış fiyatına KDV ekle").
  - Teklif ve siparişte tevkifat [3454]: Program Ayarları.
  - Masraf faturasında döviz [3598].
  - MRP üretim emrinde başlangıç tarihini otomatik doldurma [3597].
  - İrsaliye faturalanınca stok hareket fiyatını güncelleme [3147]: açıkken hareket aktarma seçenekleri değiştirilemez, stok hareket raporunda fatura fiyatı görünür.
- **Modüller:**
  - **Tüp/Su** [639–641]: fiş, rehin takibi, dolu ve boş stok değişim tanımları, toplu faturalandırma, Caller-ID.
  - **Mal Kabul** [2089]: onaylı siparişten kontrollü irsaliye oluşturur.
  - **İthalat Yönetimi** [2245][2252]: ithalat dosyası (teslim, ödeme, menşei, gümrük), hareket dökümü, stok **millileştirme** ve ithalat envanteri.
  - **Bonus** [402]: Genel Ayarlar → Cari Kart Ayarları → "Bonus Sistemi Kullan" ve fatura bonus matrahı.
  - **Eksiye düşen stokları otomatik üret** [1987]: reçetesi olanlar Üretim → İşlemler'den üretilir.
  - **Gün Sonu Raporu 1/2/3** [3788]: kasa, çek ve senet; faturalar, işlem gören cari ve stoklar; transfer irsaliyeleri. Yetkiliye SMS gönderilebilir.
  - Cari doğum günü SMS'i [2022]: Kontrol Paneli → Mail/SMS → Otomatik SMS Tanımları.
- **Kullanıcı arayüzü:**
  - Rapor gridinde Ctrl+ / Ctrl− ile kolon genişliği otomatik ayarlanır [3515].
  - Excel'e aktarma butonu kaybolduysa kullanıcıya "Raporları dışa aktarabilsin (Excel/HTML)" yetkisi verilir [3700].
  - Servis randevusunda cari ve servis özel alanları eşleştirilebilir [3503].
- **Mobil Fiyat Gör [3685]:** Kullanıcı adı, parola, IP ve **güncelleme portu (3056)** ile bağlanır. Barkoddan resim, fiyat, birim, KDV ve miktar gösterir.
- **Genel hatalar:**
  - "Dynamic SQL Error" [1976]: Kontrol Paneli → Veritabanı İşlemleri → **Veritabanı Bakımı** bütün veritabanları seçilerek çalıştırılır. Hata sürerse veritabanı onarımı gerekir.
  - "Mail editör bileşeni yüklenemedi" [251]: `xstandard.ocx` `system32`'ye konup `regsvr32 xstandard.ocx` çalıştırılır.
  - Toplu SMS'te "List index out of bounds (0)" [1466]: mesaj dışarıdan yapıştırılmış, elle yazılır.
  - Windows 7'de genel ayar ve lisans ekranı [143]: UAC "hiçbir zaman uyarma" yapılır ve bölge ayarları sıfırlanır.
  - Restoranda "geçersiz değer" [2028]: Windows bölge ve dil ayarları sıfırlanır.
  - NOD32 veya ESET [168]: programın exe'sine güvenlik duvarında izin kuralı eklenir.
  - Yedekleme programında bulut sunucusu izni beyaz ekranda kalıyor [741]: Sunucu Yöneticisi'nde "IE Artırılmış Güvenlik Yapılandırması" kapatılır.
  - Eski Paradox tabanlı programlarda "Index is out of date" [31][37]: **PxOnar** aracı çalıştırılır. **WOLVOX için geçerli değildir.**
  - OctoPlus/OctoPers'te "function UPPERTR is not defined" [52]: `UDF_TRUP.DLL` ve `OCTOPUS.DLL` (OctoPlus 7'de ayrıca `WOLVOXUDF7.DLL`) Firebird'ün `UDF` klasörüne kopyalanır. Wolvox'taki UPPERTR hatası da aynı nedenden çıkar.
  - Firebird şifresi unutulduysa [9]: aynı sürüm Firebird kaldırılıp yeniden kurulur (bkz. [3306]).
- **Yazarkasa (ÖKC) zorunluluğu [4033]:**
  - 02.08.2024 tarihli tebliğe göre ÖKC muafiyeti olmayan Hızlı Satış ve Restoran kullanıcıları yeni nesil ÖKC'yi **entegre** kullanmak zorunda.
  - Son tarih **15.06.2026**. Gereken sürümler: Kontrol Paneli 26.02.16 (zorunluluk 26.02.12'den itibaren), Hızlı Satış 26.02.06 (26.02.04'ten), Restoran 26.03.04 (26.03.02'den), Yazarkasa 26.04.02.
  - Muaf olanlar müşteri panelinde Lisanslarım → **ÖKC kullanım muafiyeti bildirimi** yapar, belgeyi yükler ve onay SMS'ini bekler.
  - Muaf olmayanlarda Yazarkasa modülü veya VUK507 ek hizmeti yoksa **program açılmaz**. Kural yalnız yurt içi lisanslar için geçerli.
- **[4061] Yazarkasa satış sorgulama:** İletişim hatası yüzünden cihazda kapanıp programda açık kalan satış cihazdan sorgulanır ve otomatik kapatılır. Kapsam entegrasyona göre değişir: PAVO (Rest, Cloud, P2P) ve diğerleri.
- **[4068] SMS Server 2.03.07:** Ülke bazlı servis sağlayıcı seçilir. Azerbaycan için public ve private key gerekir.

### Donanım entegrasyonları
- **[292] Caller ID:**
  - Destekleyen programlar: ERP, Restoran (Lite dahil), Hızlı Satış, Otel, RentAgent, NetSürücü Plus, NetEmlak.
  - PC'ye **AKINSOFT Caller ID Server** kurulur. Desteklenen cihazlar: CID2 (Sistemler) ve ARG. Diğer seri port cihazları özel ayarla bağlanır. Hugin [380]: USB-seri, sanal COM portu Aygıt Yöneticisi'nden bulunur.
  - Caller ID Server'da cihaz seçilir, "Portu Test Et" ile denenir. ERP'de Yetkili → Özel Ayarlar → Caller ID → "Arayan Numarayı Tanıma Aktif". Restoranda Program Ayarları → Caller ID.
  - **İletişim portu programda ve Server'da aynı olmalı.** Aynı anda cihazla tek bir program konuşabilir (test programı açıksa Server çalışmaz). Hatta numara gösterme servisi açık olmalı.
- **[300] / [1723] Kimlik tarama:**
  - Programlar: ERP, Otel (Wolvox 8/9), Otel 4/5, RentAgent.
  - Cihazlar: Plustek TR-821 (kimlik, ehliyet) ve TR-550 (pasaport). TR-550'de aktarım üreticinin (ERAYSOFT) `Batch_Archiv.exe` ara yazılımıyla yapılır, programda ayar gerekmez.
- **[290] / [1507] / [3604] PDKS (İK, Personel Takip modülü):**
  - Proximity kart, parmak izi ve yüz tanıma cihazları desteklenir.
  - Online kullanımda **Wolvox Kapı Ekranı** gerekir (ayrı bir PC'ye kurulabilir). Offline kullanımda cihazdan veri çekilir.
  - ZK Teco TRFace 100 yalnız veri çekme modunda çalışır: cihaz tipi BIOCLOCK, iletişim TCP/IP, IP ve port girilir.
- **[238] Karekodla belge aktarımı (WOLVOX'tan WOLVOX'a):**
  - Cari kart → Hesap Bilgileri → "Karekod Transfer" = barkod / stok kodu / tedarikçi stok kodu.
  - Genel Ayarlar → Program Ayarları'nda karekodun maksimum uzunluğu belirlenir.
  - Tasarımda "DB Bağlantılı Karekod Ekle" → tablo "Fatura Yazdırma Karekod", alan "Karekod". Ürün çoksa yan yana birkaç karekod konur.
  - Alıcı firma formda İşlemler → **Karekoddan Veri Al** ile okutur.
- **[150] Santral Server 3 – Karel MS48:** Santral tipi seçilir. İletişim: CM kartı varsa orijinal, printer kartı varsa printer çıkışı. Seri port 4800-8-N-1, RTS/DTR handshake.
- **[3830] e-Adisyon (Restoran):**
  - Lisansta Restoran ve Fatura modülleri gerekir. Kontörle çalışır. Entegratörler SuperEntegratör ve EDM.
  - Kontrol Paneli → e-Devlet 1'de "e-Adisyon Sistemini Kullan" (ve otomatik gönderim) açılır.
  - Ayarlar ERP'de Satış → Faturalar → e-Adisyon'dadır. Sayaç Yetkili → Sayaç İşlemleri'nden tanımlanır.
  - Restoranda Program Ayarları → Ö.Muhasebe/G.Muhasebe → Sayaç ve Kodlar'dan sayaç seçilir. Gönderim tipi: Kuyruğa ekle / Hemen gönder / Kullanıcı onaylı.
  - Gönderim ekranları hem ERP'de hem Restoranda var.

### Akaryakıt, otopark ve diğer sektörel programlar
- **[1432] / [3843] / [2236] / [3520] Akaryakıt Veri Aktarımı:**
  - Turpak, Asis, Türksis ve Mepsan pompa otomasyonlarındaki satışları ERP'ye **irsaliye veya sipariş** olarak aktarır. Taşıt tanıma işlemlerini de alır. **Offline sistemde çalışmaz.**
  - Ayarlar → Tablo Alanları → "Oluştur" gereken özel alanları açar.
  - Vardiya script'i irsaliye modülüyle çalışır, TXT veya XML seçilir, vardiya için genel bir cari açılır.
  - [3558] Vardiya dosyası okunamıyorsa bölge ve dil ayarları sıfırlanır.
- **Otopark:**
  - [669] Metcom plaka tanıma kamerayla bariyeri açar, LED panelde ücreti gösterir. Metcom'da tanıma yöntemi "sürekli" olmalı.
  - [1899] Abonelik bitiş uyarısı Genel Ayarlar → Uyarılar'dan ayarlanır.
- **ProKuaför [2190][2193][3729]:** Kuaför için bulut randevu sistemi. İşletme, domain, kullanıcı ve hizmet tanımlanır.
- **Kendi alan adı [3397][3980] (MyRezzta, QR Menü, ProKuaför):** Hosting yoksa Cloudflare üzerinden, varsa DNS'te **CNAME** kaydıyla alt alan adı yönlendirilir.
- **Diğer:**
  - NetEmlak "Unable to write to Netemlak.INI" [746]: UAC kapatılır ya da program yönetici olarak çalıştırılır.
  - E-Ofis Network Admin kurulumu [81]: makaledeki PDF.
- **Online İK [3215][3833]:**
  - Personel web üzerinden giriş/çıkış kayıtlarını, maaş dökümünü, anket, sınav ve duyuruları görür. Kontrol Paneli 8.03+ gerekir.
  - 9.02.01 ile mazeret ve yıllık izin talep/onay ekranları geldi.
- **Üretim:**
  - [4019] **Reçete revizyonu:** Genel Ayarlar → MRP Ayarları → Genel Ayarlar-2 → "Üretim reçetelerinde revizyon kullan". Yeni revizyon açılınca eskisi pasife düşer, revizyon geçmişi izlenir.
  - [4021] **Online İş Merkezi izleme ekranları** (26.03.01): devam eden ve bekleyen işler, ilerleme, plan uyumu, gecikmeler, iş merkezi yükü.
- **[4067] Pazarlamacı takibi ve harita rota planlama (ERP 26.03.05+):** Kontrol Paneli → Özel Ayarlar → Harita Servisi'ne **Google Maps API key** girilir (Google Cloud Console → Credentials) ve rota planlamada harita servisi açılır.
- **Mobil sürüm notları:**
  - [4063] Mobil Satış / Server 26.03.01: zorunlu alanlar, mobilde mal kabul, cari konum güncelleme.
  - [4065] WebConnect 26.03.01: seri/lot ve stok giriş/çıkış, e-Fatura portalına geçiş, makbuz no.
  - [4031] Mobil Satış'ta fiyat güncellemesi gelmiyorsa "Standart ilk 4 stok fiyatı kullan" yetkisi kaldırılır.

### Yazarkasa (YNÖKC / VUK507) uyumluluk tablosu ve cihaz notları
**[3912] Cihaz ve program uyumu** (R = Restoran, HS = Hızlı Satış, K = MyRezzta Kiosk):

| Marka | Model | Tür | R | HS | K |
|---|---|---|---|---|---|
| inPOS | M120 | YNÖKC | ✓ | ✓ | – |
| inPOS | M530 | YNÖKC/TSM | ✓ | ✓ | – |
| Hugin | VX675, FT202, FP300, T300 | YNÖKC | ✓ | ✓ | – |
| Hugin | S1 | Android | ✓ | ✓ | – |
| Olivetti | MX915 | YNÖKC | ✓ | ✓ | – |
| Olivetti | PBT990 | YNÖKC | – | ✓ | – |
| Beko | 300TR Token | YNÖKC | ✓ | ✓ | – |
| Beko | X30TR kablolu / kablosuz | Android | ✓ | ✓ | – |
| Profilo | S900 | YNÖKC | ✓ | ✓ | – |
| NBA | FiscalBox, e-Kassa (Azerbaycan) | YNÖKC | ✓ | ✓ | – |
| Omnitech | e-Kassa (Azerbaycan) | YNÖKC | ✓ | ✓ | – |
| Fiskaltrust | Almanya, Avusturya | YNÖKC | ✓ | ✓ | – |
| NPOS | YN500, YN200 | YNÖKC | ✓ | ✓ | – |
| Ingenico | iWE280, iDE280, Move 5000F | YNÖKC | ✓ | ✓ | – |
| Ingenico | Move 5000F | TSM | ✓ | – | – |
| Verifone | VX680 | TSM | ✓ | – | – |
| PAX | A910SF | Android | ✓ | ✓ | – |
| PAVO | N86 | Android | ✓ | ✓ | – |
| PAVO | UN20 | Android | – | – | ✓ |
| Inter MPOS | 2001 | YNÖKC | – | ✓ | – |
| Perkon Digi | IPT 360 | YNÖKC | – | ✓ | – |

- **Ortak kurulum:** Lisansta **Yazarkasa** (eski adı "Yazarkasa-POS-Terazi") modülü gerekir. Kontrol Paneli → Şirket Kayıt → e-Devlet 1'de **"Yeni Nesil Yazarkasa / YNÖKC Entegrasyonu Kullan"** açılır. Wolvox **Yazarkasa** programında (eski adı Market Otomasyon) cihaz seçilip "Ayarla" ile fiş limiti, IP ve port girilir.
  - Kaynaklar: [3706] Move5000F, [3760] inPOS M530, [3993] PAX A910SF, [3683] NBA e-Kassa, [3895]/[3897] Omnitech.
- **TSM modu (Restoran):** Bilgisayar TSM sunucusu olur. **Sabit IP** ve modemde açık bir port gerekir, kullanıcı adı ve şifreyi AKINSOFT girer ([3992] PAX TSM, [4001] inPOS M530 TSM).
- **Beko:**
  - X30TR kablolu [3950][3963] ile kablosuz [3974] arasında geçiş yapılamaz, satın alma bağlantıları farklı.
  - Kablosuz modda 21.04.2026'dan sonra (Restoran 26.03.01, Yazarkasa 26.04.01) cihaz seri no, sabit IP ve port ticket ile bildirilir.
  - 300TR Token [3978]. Branch ID cihazdaki karekoddan okunur [4045].
  - "POS ödeme başarısız … CANCELLED" [4011]: KDV oranı ile KDV departmanı uyuşmuyor.
- **Hugin S1 PC Link [4073]:**
  - Cihazın Entegrasyon ekranına AKINSOFT'un VKN'si girilir (makalede yazılı).
  - `ERR_UNAUTHORIZED-X-hardwareid` [4082]: cihaz başka bir bilgisayara kilitli. Servis modunda PC Link eşleşmesi kaldırılır (şifreyi Hugin verir).
- **Diğer cihaz hataları:**
  - Profilo S900 "satış moduna geçemedi" [3967]: "Şifreleme kullanılsın" işaretlenir.
  - inPOS M530 "1030" [3968]: MarketOtomasyon klasörünün adı değiştirilip program yeniden kurulur. Stok adı, birim, KDV oranı ve KDV departmanı dolu olmalı.
  - Ingenico'da yemek kartı için "Global Yemek Çeki" uygulaması kurulur [3917]: sicil numaraları Ingenico'ya gönderilir, sonra parametre güncellenir.
  - CAS PDI 30 kg terazide "online veri al" modu açık olmalı [3973].
- **PAVO N86 (VUK 507 – GMÖEBYS) [3906][3928]:** Android POS ile belge ve ödeme entegrasyonu yapılır. **PAVO kullanılırken ERP'de "Gün sonu sistemi kullan" kapalı olmalı**, açıksa hesap kapatırken "Sistem belirtilen nesneyi konumlandıramıyor" hatası çıkar [4077].

### Restoran, Hızlı Satış, Otel, İK, GM, Demirbaş (sürüm notları ve ipuçları)
- **Restoran:**
  - [651] Kullanım kılavuzu: masa aç, adisyon, müşteri seçimi…
  - [3765] Adisyon fişinde stok **Özel Kod 3**'e göre gruplama: Yazdırma Ayarları'nda açılır, tablo "Fiş Hareketleri (Gruplandırılmış)".
  - [3815] Gün sonunda görünen adisyon sayacını sıfırlama: ERP'de "Gün sonu sistemi kullan", Restoranda "Görünen Adisyon Numarası Sayacı", gün sonunda "Görünen sayaçları sıfırla".
  - [4030] Gün sonunda "I/O error 103": varsayılan gün sonu tasarımı seçilmemiş.
  - [4028] **Happy Hours**: gün ve saat bazlı indirim, X al Y öde, özel fiyat.
  - [4089] Online platform siparişinde "teslim edildi" bildirimini otomatik göndermeme ayarı (kurye dışarıdan geliyorsa).
  - [3880] Afanda müşteri ekranı `.asspack` script'i: Wolvox 9 için `VCFDisplayW9`, Wolvox 8 için `VCFDisplayW8`. Restoranda Menü → Tanımlar → **Script Paket İşlemleri** bulunur.
  - [3756] Restoranlarda fiyat listesi zorunluluğu (19.12.2023 yönetmeliği; kapı önü ve masada).
  - Sürüm notları: 8.23.04 [3768], 9.02.01 [3819], 9.03.01 [3884] (web mutfak, garsona göre filtre), 26.02.01 [3989] (entegrasyonu olmayan cihazların seri no'su e-Adisyona Özel Kod 2 ile gider).
- **Hızlı Satış:**
  - Sürüm notları: 9.02.01 [3824], 9.02.04 [3882] (PAX A910S), 26.02.01 [3985] (PAVO para üstü, KDV departmanına göre oran, ödeme türüne göre çekmece).
  - [1822] Normal görünümde ödeme türlerinin yeri değiştirilebilir.
- **Otel:**
  - HotelRunner rezervasyonları Veri Transferi üzerinden gelir [3704].
  - Sürüm notları:
    - 9.02.01 [3820]: AKBS bildirimleri otomatik, forecast tasarımı.
    - **26.03.01 [4012]:** folyoda Fiş A/B/C ile masraflar farklı ödeyenlere bölünür.
    - 26.04.01 [4047]: rack ekranında kroki.
  - [4048] 26.04.03'te TGA **Tesis Künye Bilgi Sistemi** için uyruk ve ay bazlı rapor geldi.
  - Otel 5: güncelleme [3676], kurulum [3679], lisans [3681] (makine kodu uyarısı gelirse Evet).
- **İK:**
  - 9.02.01 [3818].
  - 9.02.02 [3870]: 3294 teşviki, kısa vadeli prim %2,25, GV matrahı indirimli gösteriliyor, PDKS'de sabit maaş.
  - 9.03.01 [3921]: Perkotek YT-32/33 PDKS, departman aktif/pasif, personel bazlı muhasebe entegrasyonu.
- **Genel Muhasebe entegrasyonu [969]:** ERP Genel Ayarlar → Genel Muhasebe → "Genel Muhasebe Sistemini Kullan" + entegrasyon tipi:
  - **Anlık:** fişler hemen oluşur.
  - **Toplu:** ERP'de Diğer İşlemler → G.Muhasebe → Entegrasyon Dosyası Oluştur (XML, tarih aralığı), GM'de Fiş İşlemleri → Transfer Dosyasından Fiş Oluştur → Fiş Oluştur.
  - GM 9.02.01 [3822]: "Eski fişler" menüsünün adı "Muhasebe Fişleri" oldu.
- **Demirbaş:**
  - 9.02.01 [3823]: zimmet devri.
  - 9.02.04 [3959]: GM yetkisi olmadan kullanılabiliyor, ek harcama yetkisi, enflasyon filtresi.
- **OctoPers 5 / OctoPlus 6 devri [3749]:** Server'da Yetkili Kişi → Şirket İşlemleri → Çalışma Yılları → Çalışma Yılı Oluştur.
