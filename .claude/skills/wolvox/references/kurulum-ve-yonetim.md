# Kurulum, Kontrol Paneli ve sistem yönetimi

## Mimari

- **Kontrol Paneli:** Sunucu bileşeni. Sadece **ana bilgisayara (sunucuya)** kurulur (offline kullanım hariç). Veritabanı bağlantısı, şirket tanımları, kullanıcılar ve yetkiler, lisans, yedekleme, devir ve veritabanı işlemleri buradan yönetilir. Tüm Wolvox programları Kontrol Paneli'ne bağlanarak çalışır.
- **İstemci (client):** Diğer bilgisayarlara sadece kullanılacak WOLVOX programı (ERP, Genel Muhasebe vb.) kurulur. Kontrol Paneli kurulmaz.
- **Veritabanı:** Varsayılan Firebird. MSSQL de destekleniyor. Ayrıntılar `veritabani-ve-sql.md` dosyasında.

## Kurulum

1. akinsoft.com.tr'den kurulum dosyasını (Installer) indir. Installer sonradan program klasöründeki `AKINSOFT` dizininde de bulunur.
2. Installer programları listeler: kurulu değilse **Kur**, kurulu ama eskiyse **Güncelle** seçeneği çıkar.
3. Kontrol Paneli ilk açılışta veritabanı seçimi ister (Firebird / MSSQL).
4. Firebird parolası: daha önce değiştirilmediyse **`masterkey`** (kullanıcı `SYSDBA`). Makinede başka bir Firebird tabanlı AKINSOFT programı parolayı değiştirdiyse **en son verilen parola** geçerlidir.
5. Şirket kaydı: Kontrol Paneli → **Yetkili → Şirket Kayıt İşlemleri** → bilgileri gir → Kaydet.
6. Lisans: Kontrol Paneli → **Yetkili → WOLVOX Lisans** → **Online Lisans Al** → "Lisans kartım veya numaram var" → lisans numarası ve güvenlik kodu (veya müşteri şifresi).

> Güvenlik: `masterkey` bilinen bir varsayılan paroladır. Sunucu dışarıya açılacaksa (port yönlendirme, WebConnect) önce Firebird parolasını değiştir.

Kaynak makaleler: Bilgi Bankası 221 (kurulum talimatı), 3655 (Wolvox 8 indirme/kurulum), 3832/3839 (Wolvox 9 indirme/kurulum), 3829 (online lisans alma), 3831 (önceki sürümlerden Wolvox 9'a upgrade), 1302 (eski sürümleri indirme).

## Server/client bağlantısı (çok kullanıcılı kullanım)

**Sunucuda:**
1. Kontrol Paneli → **Kullanıcı İşlemleri → Kullanıcı Kayıt İşlemleri** ile kullanıcı oluştur.
2. Sunucunun yerel IP adresini not al (ör. 192.168.0.10).

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
| 80 | Uzaktan erişim senaryolarında gerekli |

- Yerel ağda bağlanamıyorsan güvenlik duvarında/antivirüste **3054, 3055, 3056** portlarını aç.
- **Uzaktan (internet üzerinden) erişim:** Firebird kullanıyorsan modemde Kontrol Paneli bilgisayarına **3050, 3054, 3055, 3056 ve 80** portlarını yönlendir. MSSQL kullanıyorsan **3055 ve 3056** gerekir (Bilgi Bankası 211). SQL Server'ın kendi portu da gerekebilir; bunu kaynaktan doğrula.
- Kontrol Paneli'ndeki "Çalışma Portu" ve "Güncelleme Portu" özel bir sebep yoksa değiştirilmemeli.
- MSSQL kullanıcıları için ayrı bağlantı makalesi: Bilgi Bankası 1894.

## Kullanıcılar ve yetkiler

- Kullanıcı kaydı: Kontrol Paneli → **Kullanıcı İşlemleri → Kullanıcı Kayıt İşlemleri**.
- Yetkilendirme: **Kullanıcı İşlemleri → Kullanıcı Yetkilendirme**. Ayrıca "Hızlı Kullanıcı Yetkilendirme" var (Bilgi Bankası 1802).
  - **Terminal Yetkileri:** kullanıcının hangi bilgisayarlardan girebileceği.
  - **Yetki Vereceği Personeller:** bu kullanıcının hangi personele yetki verebileceği.
  - **CRM Aktivite:** kullanıcının kaydettiği CRM aktivitelerini kimlerin görebileceği.
  - **Ek Yetkiler:** kullanıcının görebileceği veya göremeyeceği carilere özel tanımlar.
- Kaynak: Bilgi Bankası 1673.

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
- Kaynaklar: Bilgi Bankası 351 (Wolvox 8), 3863 (Wolvox 9).

## Yedekleme ve geri yükleme

- **Yedek al:** Kontrol Paneli → **Veritabanı İşlemleri → Yedekleme → Yedekle** → dosyaları seç → **Şimdi Yedekle**.
- **Otomatik yedek:** Kontrol Paneli → Veritabanı İşlemleri → **Yedekleme Ayarları**. Varsayılan yedek klasörü **`AS_YEDEK`**.
- **Geri yükle:** Kontrol Paneli → **Veritabanı İşlemleri → Yedekleme → Geri Yükle** → yedek klasörünü göster → **Listele** → şirket veritabanı dosyasını seç (Firebird: `.fdb`, MSSQL: `.mdb` olarak listelenir) → Geri Yükle.
- Manuel yöntem (Firebird): program kurulum dizinindeki `DATABASE_FB` klasörünün kopyası saklanır ve gerekirse geri kopyalanır. Bunu yaparken Kontrol Paneli ve Firebird servisi kapalı olmalı, yoksa dosya bozulabilir (Bilgi Bankası 942).
- Klasör, Firebird, MSSQL ve MySQL verileri için manuel/otomatik yedekleme destekleniyor.
- Kaynaklar: Bilgi Bankası 798 (geri yükleme), 942 (Firebird datadan yedek).

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

## Diğer yönetim makaleleri

- Veritabanı transferi (Firebird → MSSQL): Bilgi Bankası 1684. MSSQL Server 2008 veya üstü gerekir.
- Admin panel erişimi (İngilizce): Bilgi Bankası 3287.
- Yardım dosyaları: Genel Muhasebe (1672 / 3851), İnsan Kaynakları (1458), Otel (1433 / 3844), Demirbaş (1508), CafePlus (2657), Restoran kullanımı (651).
