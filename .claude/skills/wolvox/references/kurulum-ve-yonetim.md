# Kurulum, Kontrol Paneli ve sistem yönetimi

## Mimari

- **Kontrol Paneli (WOK):** Sunucu bileşeni. Sadece **ana bilgisayara (sunucuya)** kurulur (offline kullanım hariç). Veritabanı bağlantısı, şirket tanımları, kullanıcılar ve yetkiler, lisans, yedekleme, devir ve veritabanı işlemleri (DBUpdate, transfer) buradan yönetilir. Tüm Wolvox programları Kontrol Paneli'ne bağlanarak çalışır. SDK da Kontrol Paneli'ne gömülüdür.
- **İstemci (client):** Diğer bilgisayarlara sadece kullanılacak WOLVOX programı (ERP, Genel Muhasebe vb.) kurulur. Kontrol Paneli kurulmaz.
- **Veritabanı:** Varsayılan Firebird (32 bit, 2.x sürümü). MSSQL de destekleniyor. Ayrıntılar `veritabani-ve-sql.md` dosyasında.
- **Varsayılan kurulum dizini:** `C:\AKINSOFT\Wolvox9` (Wolvox 9; yardımcı araçlar `C:\AKINSOFT\Wolvox9\Utils` altında). Eski sürümlerde `...\AKINSOFT\WOLVOX7` / `WOLVOX8`.

## Kurulum

1. akinsoft.com.tr'den **AKINSOFT Wolvox Installer**'ı indir. Installer Wolvox programlarını internetten indirip sunucu veya istemciye kurar, güncel sürümü kontrol eder ve sürüm güncellemesi yapar. Kurulumdan sonra program klasöründeki `AKINSOFT` dizininde de bulunur.
2. Installer programları listeler: kurulu değilse **Kur**, kurulu ama eskiyse **Güncelle** seçeneği çıkar.
3. Kontrol Paneli ilk açılışta veritabanı seçimi ister (Firebird / MSSQL). Firebird seçilip **Tamam**'a basılır.
4. Firebird parolası: daha önce değiştirilmediyse **`masterkey`** (kullanıcı `SYSDBA`). Makinede başka bir Firebird tabanlı AKINSOFT programı parolayı değiştirdiyse **en son verilen parola** geçerlidir. Firebird kaldırılıp yeniden kurulursa parola yine `masterkey` olur.
5. Kontrol Paneli açılışında "Deneme Sürümü Kurulumu" ya da "Lisanslı Kurulum" seçimi istenir.
6. Şirket kaydı: Kontrol Paneli → **Yetkili → Şirket Kayıt İşlemleri** → bilgileri gir → Kaydet.
7. Lisans: Kontrol Paneli → **Yetkili → WOLVOX Lisans** → **Online Lisans Al** → "Lisans kartım veya numaram var" → lisans numarası ve güvenlik kodu (veya müşteri şifresi).

> Güvenlik: `masterkey` bilinen bir varsayılan paroladır. Sunucu dışarıya açılacaksa (port yönlendirme, WebConnect) önce Firebird parolasını değiştir.

Kaynak makaleler: Bilgi Bankası 221 (kurulum talimatı), 3655 (Wolvox 8 indirme/kurulum), 3832/3839 (Wolvox 9 indirme/kurulum), 3829 (online lisans alma), 2799/4004 (İngilizce kurulum).

### Eski sürüm indirme (Bilgi Bankası 1302)
1. www.akinsoft.com.tr → sağ üstte **Müşteri Girişi** → **Müşteri Paneli**.
2. **Programlar** sekmesi → **Eski Sürümler**. Lisansında olan programı listede bul.
3. Yanındaki simge → **İndir** → doğrulama kodunu gir. İnen klasörü açıp kurulumu başlat.

## Önceki sürümden yükseltme (upgrade)

### Wolvox 8 (veya 6/7, OctoPlus, OctoPers) → Wolvox 9 (Bilgi Bankası 3831)
1. Wolvox 9 Kontrol Paneli'ni güncel sürüme getir.
2. Tüm bilgisayarlarda Wolvox programlarını kapat.
3. Kontrol Paneli'nden lisanslama yapıp programı lisanslı hale getir.
4. Kontrol Paneli'ni **Yetkili → Programdan Çık** ile kapat, sonra **yönetici olarak** çalıştır.
5. "Wolvox 8'den Upgrade yapılsın mı?" sorusu gelir. Wolvox 8'den geçiliyorsa **Evet**, değilse **Hayır**.
6. Kaynak programa göre aktarılanlar değişir:
   - **Wolvox 6:** Ön Muhasebe, Genel Muhasebe ve İnsan Kaynakları veritabanları aktarılır.
   - **OctoPlus:** Ön Muhasebe bilgileri aktarılır.
   - **OctoPers:** "Aktarılacak Modüller" kısmından seçilir.
- Wolvox 8'e yükseltme için ayrı makale: Bilgi Bankası 1145. İngilizce genel upgrade: 3852.

### Wolvox 9 Client Upgrade aracı (Bilgi Bankası 3864)
Wolvox 8'den 9'a geçerken istemcideki ayar dosyalarını taşır:
- Rapor ve form tasarımları (`Reports`, `Defdesign` klasörleri)
- Kullanıcı ve form ayarları (`Settings` klasörü)
- Mutfak, müşteri ve sıra ekranları; resim ve video dosyaları
- Ek program ayarları (`.INI`, `.DAT` dosyaları)

İki kullanım yolu var: program içinden çalıştırılırsa sadece o programın ayarları taşınır. `C:\AKINSOFT\Wolvox9\Utils` klasöründen elle çalıştırılırsa tüm programlar taranır ve seçilenler taşınır. İşlem bitince tüm programları kapatıp yeniden aç.

### Wolvox 9 → WOLVOX 26
Masaüstü kısayolları silinip yeniden oluşturulur. SDK makalesi (3994) WOLVOX 26 ve üzeri için güncel.

## Server/client bağlantısı (çok kullanıcılı kullanım)

**Sunucuda:**
1. Kontrol Paneli → **Kullanıcı İşlemleri → Kullanıcı Kayıt İşlemleri** ile kullanıcı oluştur.
2. Sunucunun yerel IP adresini not al (ör. 192.168.0.10). Sabit IP verilmesi önerilir.

**İstemcide:**
1. Sadece WOLVOX programını kur.
2. Programı aç, "Kullanıcı Girişi" ekranında **Sunucu Ayarları**'na bas.
3. **Ana Bilgisayar IP:** sunucu IP'si. **Ana Bilgisayar Bağlantı Portu:** değiştirilmediyse **3055**.

**Portlar:**
| Port | Kullanım |
|---|---|
| 3055 | Kontrol Paneli bağlantı (çalışma) portu. İstemciler buna bağlanır |
| 3054, 3056 | Kontrol Paneli'nin diğer servis portları (güncelleme portu dahil) |
| 3050 | Firebird veritabanı |
| 1433, 1434 | SQL Server (MSSQL kullanılıyorsa) |
| 8888 | WebConnect varsayılan çalışma portu |
| 80 | Uzaktan erişim senaryolarında gerekli |

- Yerel ağda bağlanamıyorsan güvenlik duvarında/antivirüste **3054, 3055, 3056** portlarını aç.
- **Uzaktan (internet üzerinden) erişim:** Firebird kullanıyorsan modemde Kontrol Paneli bilgisayarına **3050, 3054, 3055, 3056 ve 80** portlarını yönlendir. MSSQL kullanıyorsan **3055 ve 3056** ile birlikte SQL Server'ın **1433/1434** portları gerekir (Bilgi Bankası 211, 1894).
- Kontrol Paneli'ndeki "Çalışma Portu" ve "Güncelleme Portu" özel bir sebep yoksa değiştirilmemeli.

### MSSQL kullanıcıları için ek ayarlar (Bilgi Bankası 1894)
1. Windows **Kullanıcı Hesabı Denetimi (UAC)** en düşük seviyede olmalı.
2. Windows güvenlik duvarında SQL portları için **gelen ve giden kuralı** tanımla. Modemin güvenlik duvarında da izin ver.
3. **SQL Server Configuration Manager**'da TCP/IP'yi **Enabled** yap. İç IP (sunucu IP'si) ve dış IP için portları yaz. Sonra **SQL Server Services** altında ilgili instance'a sağ tık → **Restart**.
4. Ana makinede ve istemcilerde **Windows ODBC ayarlarına SQL Server** tanımla.
5. `AKINSOFT` klasörüne tüm izinleri ver, program exe'lerini **yönetici olarak** çalıştır.
- Statik IP üzerinden MSSQL bağlantısı için bayi rehberi de var (akinsoftistanbulbb.com).

## Kullanıcılar ve yetkiler

- Kullanıcı kaydı: Kontrol Paneli → **Kullanıcı İşlemleri → Kullanıcı Kayıt İşlemleri**.
- Yetkilendirme: **Kullanıcı İşlemleri → Kullanıcı Yetkilendirme** → şirketi seç → alttaki modül yetkilerini işaretle → **Yetkileri Kaydet**.
  - **Terminal Yetkileri:** kullanıcının hangi bilgisayarlardan girebileceği.
  - **Yetki Vereceği Personeller:** bu kullanıcının hangi personele yetki verebileceği.
  - **CRM Aktivite:** kullanıcının kaydettiği CRM aktivitelerini kimlerin görebileceği.
  - **Ek Yetkiler:** kullanıcının görebileceği veya göremeyeceği carilere özel tanımlar.
  - **Program Kullanım Yetkileri:** ör. WebConnect'e giriş için buradan "WebConnect" işaretlenir.
- **Hızlı Yetkilendirme** (Bilgi Bankası 1802): tüm modüller için "Ekleme, Silme, Düzenleme" yetkilerini tek seferde verir.
- **Yönetici paneli (admin ekranı)** (Bilgi Bankası 3287, İngilizce makaleden çeviri):
  - ERP açılışında yönetici panelinin gelip gelmemesi özel ayarlardaki genel ayarlardan açılıp kapatılır. Yol yaklaşık **Yetkili → Özel Tanımlar → Özel Ayarlar → Genel Ayarlar**, seçenek "Başlangıçta Yönetici Panelini Göster". Türkçe menü adlarını doğrula.
  - Kullanıcıya Kontrol Paneli → Kullanıcı Yetkilendirme'den **Wolvox ERP → Genel → Yönetici Paneli** yetkisi verilmeli.
- Kaynak: Bilgi Bankası 1673. Video: "Akınsoft Wolvox 8'de Kullanıcı Tanımlama ve Yetkilendirme" (YouTube `v-RNfIKvKe0`).

## Lisans ve client sayısı

- Lisanstaki bilgisayar sayısı, Kontrol Paneli'ne bağlanan **makine isimleri** ile kayıt altına alınır.
- Bilgisayar değişirse veya makine kodu değişirse şu hata çıkar: **"Lisanslanan client sayısı aşılmış. Veritabanı yöneticinize başvurunuz."**
- Çözüm: Kontrol Paneli → **Yetkili → WOLVOX Lisans** → sağdaki **Client Tanımları** → hatanın alındığı programı (ERP, İK, Genel Muhasebe…) seç → eski kayıtları **Sil**. Bilgisayarlar yeniden bağlandıkça tekrar kaydolur. PDA/el terminalleri için de aynı mantık geçerli.
- Kaynak: Bilgi Bankası 697.

## Sürüm güncelleme

1. Kontrol Paneli dahil **tüm programları kapat**. Başka kullanıcının bağlı olmadığından emin ol.
2. Program klasöründeki `AKINSOFT` dizininden **Installer**'ı çalıştır.
3. Seçenekleri işaretle. Sadece indirip sonra kuracaksan "Sadece Dosyaları İndir".
4. Programları seç → İşleme Başla.
5. **Sunucu ve tüm istemciler aynı sürümde olmalı.** Sürüm uyuşmazlığı güncelleme sonrası "Field not found" gibi hatalara yol açabilir.
6. Veritabanı yapısı program sürümünün gerisinde kaldıysa: Kontrol Paneli → **Veritabanı İşlemleri → DBUpdate** (Bilgi Bankası 3836).
- Kaynaklar: Bilgi Bankası 351 (Wolvox 8), 3863 (Wolvox 9). Sürüm notları Bilgi Bankası'nda "Wolvox ERP 9.02.01", "Wolvox Kontrol Panel 8.04.24" gibi başlıklarla yayımlanıyor.

## Yedekleme ve geri yükleme

### Kontrol Paneli ile
- **Yedek al:** Kontrol Paneli → **Veritabanı İşlemleri → Yedekleme → Yedekle** → dosyaları seç → **Şimdi Yedekle**.
- **Otomatik yedek:** Kontrol Paneli → Veritabanı İşlemleri → **Yedekleme Ayarları**. Varsayılan yedek klasörü **`AS_YEDEK`**.
- **Geri yükle:** Kontrol Paneli → **Veritabanı İşlemleri → Yedekleme → Geri Yükle** → yedek klasörünü göster → **Listele** → önce sistem veritabanı `sirket.fdb`'yi (MSSQL: `sirket.mdb`) seçip **Sisteme Geri Yükle** (Kontrol Paneli kendini kapatıp açar). Sonra aynı ekrandan şirket veritabanlarını yükle: `wolvox`, `gmuhasebe`, `imuhasebe`, `ikaynak`, `dosya` (`.fdb` / `.mdb`) (Bilgi Bankası 798).

### Klasör kopyalayarak (Firebird, Bilgi Bankası 942)
- **Yedek:**
  1. Tüm AKINSOFT programlarını kapat.
  2. **Denetim Masası → Yönetimsel Araçlar → Hizmetler**'den **Firebird Server** ve **Firebird Guardian** servislerini durdur. Durdurmazsan yedek bozuk veya boş olur.
  3. Kurulum dizinindeki **`DATABASE_FB`** klasörünü harici diske kopyala.
- **Geri yükleme:**
  1. AKINSOFT programları kurulu olmalı. Hepsini kapat ve Firebird Guardian'ı durdur.
  2. Yedekteki `DATABASE_FB` klasörünü kurulum dizinindekinin üzerine kopyala.

### Klasör kopyalayarak (MSSQL, Bilgi Bankası 943)
- **Yedek:** Kurulum dizinindeki **`DATABASE_MSSQL`** klasörünü harici diske kopyala. Makalede geçmiyor ama genel SQL Server bilgisi: servis çalışırken veri dosyaları kilitlidir, önce AKINSOFT programlarını kapatıp SQL Server servisini durdur.
- **Geri yükleme:**
  1. MSSQL'i ve AKINSOFT programlarını kur, programları çalıştırma.
  2. **SQL Server Configuration Manager** → SQL Server servisini durdur. Makaleye göre servis hesabını "Network Service" yerine "Local Service" yapmak da gerekiyor.
  3. Yedekteki `DATABASE_MSSQL` klasörünü kurulum dizinine kopyala. Hedefte başka bir veri klasörü varsa önce onun adını değiştir.

### AKINSOFT Yedekleme programı (Bilgi Bankası 1893, 3177)
- Ayrı ve ücretsiz bir yedekleme aracı. Klasör, Firebird, MSSQL ve MySQL verilerini manuel veya otomatik yedekler. **Bulut yedekleme sunucusuna** veya bir dizine yedek alabilir.
- SQL için: **Yeni Ekle → Microsoft SQL Server Yedekleme** → SQL Server kullanıcı bilgileri → veritabanı → yedek dizini.
- **NBackup Kullan:** Son yedekten bu yana değişen verileri yedekler (artımlı yedek), disk tasarrufu sağlar.
- Geri yükleme: kaynak dizin, veritabanı dosyası ve yedeğin ay/gün/saati seçilir, geri yüklenecek veritabanı adı verilir.

## Yıl sonu devir işlemleri

1. Çok kullanıcılı sistemde **herkesin oturumu kapatmasını sağla**.
2. **Önce mutlaka yedek al.**
3. Kontrol Paneli → **Yetkili → Devir İşlemleri** (Wolvox 7/8/9/26'da aynı yer).
4. "Oluşturulacak Çalışma Yılı" alanına yeni yılı yaz, devre baz alınacak **son işlem tarihini** gir ve devredilecek şirket(ler)i seç.
5. Modül bazında hangi verilerin aktarılacağını işaretle. İstemediklerinin işaretini kaldır.
6. "Durum tanımlarına göre devir" seçeneği de var (ör. sadece belirli durumdaki sipariş/teklifleri devretmek için).

## Excel ile toplu aktarım

- **Excel'den cari kartı:** **Diğer İşlemler → Excel Transfer → Excelden Cari Kart Aktarım**. Alan eşleştirmesi yapılır. Bakiye bilgileri de aktarılabilir.
- **Excel'den stok kartı:** Wolvox 8 ve sonrası **Diğer İşlemler → Excel Transfer → Excelden Stok Kartı Aktarımı**. Wolvox 7'de **Transfer → Excelden Stok Kartı Aktarımı**.
- Var olan kayıtlar güncellenebilir, olmayanlar oluşturulabilir. Excel ile toplu fiyat güncellemesi de bu yolla yapılıyor.
- **Uyarı:** Toplu aktarımın **toplu geri alması yok**. Yanlış aktarılan kayıtlar tek tek düzeltilir. Aktarımdan önce yedek al.
- **Dışarı aktarma:** SQL Monitör'de `SELECT * FROM CARI` veya `SELECT * FROM STOK` çalıştır → tabloda sağ tık → **Aktar → Excel** (Bilgi Bankası 1124).
- Kaynak: Bilgi Bankası 441.

## Veritabanı dönüştürme

### Firebird → MSSQL (Bilgi Bankası 1684)
- Gereksinim: **MSSQL Server 2008+**. WebConnect kullanılıyorsa **2012+**. Önce yedek al.
- Adımlar:
  1. Kontrol Paneli → **Yetkili → Özel Ayarlar** → arayüz dilini **İngilizce** yap → Tamam.
  2. Kontrol Paneli'ni kapatıp aç (İngilizce açılır).
  3. **Upgrade** sekmesi → **Transfer to MSSQL Server Database** → seçimleri yap, bitmesini bekle.
  4. Kontrol Paneli yeniden başlar. SQL kurulumunda verdiğin **INSTANCE** adını seçip **OK**'a bas.
- **Transfer yalnızca 1 kez yapılabilir.** Tüm kontrolleri önceden yap.

### Firebird → MSSQL Unicode (Bilgi Bankası 3592)
- Firebird veritabanı Wolvox'ta Unicode desteklemiyor. Arapça, Kiril gibi Latin dışı karakterler `?` olarak kaydedilir.
- Çözüm:
  1. SQL Server kur. Yedek al, `AKINSOFT` klasörüne izin ver, Kontrol Paneli'ni yönetici olarak aç.
  2. SQL kurulumunda seçilen collation'ı seç ve **"Unicode Character Set"** seçeneğini aktif et.
  3. Transferin bitmesini bekle.
