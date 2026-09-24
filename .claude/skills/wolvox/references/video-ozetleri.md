# YouTube eğitim videoları: altyazılardan çıkarılan özetler

- **Kaynak:** AKINSOFT'un resmi YouTube kanallarındaki (AKINSOFT Eğitim, AKINSOFT) Wolvox ile ilgili **946 Türkçe videonun** otomatik Türkçe altyazıları. 2026-09-24'te indirildi. 906 videonun altyazısı alınabildi ve okundu (500 WOLVOX ERP, Kontrol Paneli, Hızlı Satış, Restoran, Otel, İK, MRP, Mobil Satış, e-Ticaret videosu ve 406 WolvoxCloud videosu). 40 videonun Türkçe altyazısı yok.
- **Video açıklamaları:** Hepsi okundu; neredeyse tamamı yalnız başlığı tekrarlıyor, ek bilgi yok. Dailymotion açıklamaları da sadece eski ürün sayfası bağlantısı.
- **Bu dosyadaki içerik:** Altyazılardan yalnız işe yarayan bilgi kendi cümlelerimizle yazıldı: menü yolu, gereken modül/lisans, ayar adı, iş akışı, sınırlar. Bilgi Bankası'nda zaten ayrıntılı olanlar kısaca anıldı. WolvoxCloud videoları kısa ekran tanıtımları olduğu için yalnız yeni bilgiler alındı; en kapsamlı kaynak 104 dakikalık resmi eğitim {W0NOHUVbouA}.
- **Kaynak gösterimi:** Her maddedeki `{ID}` YouTube video kimliğidir. İzlemek için `https://www.youtube.com/watch?v=<ID>`. Videonun başlığı `video-dizini.md` dosyasında.
- **Sürüm notu:** Anlatımların çoğu WOLVOX 8 dönemine aittir; güncel sürümde (WOLVOX 9 / 26) menü adları değişmiş olabilir. Ücret, lisans ve "şu an yok" gibi ifadeler video tarihine aittir.
- **Sınırlar:** Otomatik altyazıda ses tanıma hataları olur ("volvoks", "wallbox" = Wolvox gibi). Ekrandaki tıklamalar altyazıya girmez. Kesin menü yolu için programın kendisine veya Bilgi Bankası'na bak. Ham altyazılar telif nedeniyle repoya konmadı.

## Kontrol Paneli

- **Şirket kaydı {2EfTLtY1IHQ}:** Yetkili → Şirket Kayıt İşlemleri → Yeni Kayıt Ekle.
  - **Genel bilgiler:** kod, kısa ad, unvan, vergi dairesi ve numarası.
  - **Dizin ayarları:** "Rapor dizini" ile başka bir tasarım klasörü gösterilebilir. "Veri yolu kullan" ile şirket verisi varsayılan klasör dışında tutulabilir.
  - **Açılabilen seçenekler:** "Bu şirket için offline kullanıma izin ver", "Stok resimlerini gönder", aktif/pasif.
  - **Özel Bilgiler sekmesi:** banka hesapları, **mail sunucusu** (otomatik mail ve e-Arşiv maili için gerekli). Otomatik döviz kuru alma, otomatik mail ve SMS, banka online veri al seçenekleri de buradadır.
  - **e-Devlet 1 sekmesi:**
    - e-Fatura, e-Arşiv, e-İrsaliye, e-Adisyon ve e-Müstahsil sistemlerinin açılması; otomatik gönderim ve kontrol aralığı.
    - "Android yeni nesil ÖKC kullan" ve "Pavo N86 entegrasyonu kullan".
    - **e-Adres** (e-Faturada unvanın altında çıkan adres).
- **Kullanıcı işlemleri {upk3Soq8cec}:**
  - Önce Kullanıcı Kayıt'ta ad, kullanıcı adı ve şifre girilir; istenirse personel resmi ve imzası eklenir.
  - Sonra Kullanıcı Yetkilendirme'de personel ve şirket seçilir. Çalışma yılı boş bırakılırsa yetki bütün yıllara geçerli olur.
  - Yetki ağacında sağ tıkla "tüm yetkileri ver/kaldır" yapılabilir.
  - **CRM aktivite** sekmesi: seçili kullanıcının hangi kullanıcıların aktivitelerini görüp düzenleyebileceği.
  - **Ek Yetkiler 1:** modül listelerine SQL koşulu (bkz. Bilgi Bankası 3739).
  - **Ek Yetkiler 2:** başka kullanıcıların kaydettiği veya değiştirdiği kayıtları düzenleme yetkileri.
- **Veritabanı işlemleri {m3eY2VdIwak}:** Yedekleme Ayarları'nda şunlar belirlenir:
  - yedek dizini, otomatik yedek
  - "Resim/dosya veritabanı her zaman yedeklensin", "Sadece değişen veritabanlarını yedekle"
  - periyot (saatlik veya günlük)
  - **Maksimum yedek dosyası:** ör. 10 yazılırsa son 10 yedek kalır, 0 yazılırsa hiç silinmez. "Sadece değişenleri yedekle" ile birlikte önerilmez.
  - Geri yüklemede şirket, yıl ve veritabanına göre filtrelenir, tarih seçilip "Seçili dosyayı sisteme geri yükle" denir.
  - Aynı menüde veritabanı bakımı ve güncellemesi de var.
- **Şirket kaydı, devamı {2EfTLtY1IHQ}:**
  - **e-Defter** alanları da e-Devlet 1'dedir. Etkinleştirmek için genel merkeze **ticket** açılır.
  - **e-Devlet 2 sekmesi:** e-Arşiv gelen kutusu modülü için İnteraktif Vergi Dairesi giriş kodu ve şifresi girilir.
  - **Çalışma Yılları:** çalışma yılı oluşturma ve silme.
  - **Şube işlemleri (Şube modülü):** şube kaydı ve personel atama. "Boş olan kayıtları bu şubeye eşitle" seçeneği var. **Cari kartları ve döviz hareketleri şubeler arasında ortak** kullanılabilir.
  - **Açık Bankacılık sekmesi:** FinCloudy kullanıcı adı, parola, kurum kodu ve ID → Test Et.
- **Kullanıcı işlemleri, devamı {upk3Soq8cec}:**
  - "Yetki verebileceği personeller": kullanıcının kimlere yetki dağıtabileceği.
  - Kullanıcı modül eşleştirmesinde hızlı filtreler (atanmamış, hakkı biten, hakkı olan). "Kaynak kullanıcının modül atamalarını kaldır" seçeneği.
  - **Aktif Kullanıcılar:** sisteme bağlı kullanıcıları gösterir.

### Diğer işlemler
- Windows servis olarak çalıştırma: servis portu 3055'ten farklı olmalıdır. Servis yalnızca oturum isteklerine cevap verir; otomatik yedekleme, mail gönderimi ve otomatik güncelleme servis modunda çalışmaz. {6VrkeDIUF1s}
- Offline şube çalışmasında otomatik gönderim süresi ve hangi tabloların gönderileceği ayarlanır; veri transfer geçmişi buradan izlenir. {6VrkeDIUF1s}
- Online İş Merkezi portu ve Online İK ayarları da bu bölümdedir. {6VrkeDIUF1s}
- Şirket kaydında e-Defter için özel mali yıl tanımlanabilir; şubeye terminal atanır. Sonradan şubeli yapıya geçilirse "kayıtları aktar" ile mevcut kayıtlar bir şubeye bağlanır. {BeHlXcdWa-I}
- Kullanıcı işlemlerinde terminal bazlı yetki verilebilir; aktif kullanıcılar listesinde bağlı makine bilgisi görülür. {QtjP8U0wyY0}
- Windows servis: NT tabanlı sistemde oturum açmadan istemcilerin KP'ye bağlanabilmesi için "Kontrol Paneli servisini çalıştır" işaretlenir ve çalışma portu girilir. Offline ayarlarda şubelerin otomatik veri gönderme süresi girilir; süre yoksa gönderim elle yapılır. Otomatik veri alma için tablolar seçilir. Offline veri transfer geçmişi kullanıcı bazında son alma/gönderme zamanını gösterir. {W0QQHBoWSHk}
- Online İş Merkezi: lisansta modül varsa ayarlardan açılır, web servis portu girilir ve program yeniden başlatılır. Sistem ön izlemesi ve önbellek (cache) temizleme buradan yapılır; tablet/PC, KP IP'si ve portuyla bağlanır. Online İK da buradan açılır (personel paneli, giriş-çıkış paneli, admin paneli). {W0QQHBoWSHk}

### Şirket kaydı ve geçiş (upgrade)
- Şirket kaydı genel bilgilerde "farklı dizin kullan" ile veritabanı başka klasörde tutulabilir. Offline şube varsa "bu şirket için offline kullanıma izin ver" ve gerekirse "stok resimlerini gönder" işaretlenir. Kayıttan sonra çalışma yılı oluşturulur. {GEd9hqzD67g}
- Özel bilgilerde kamu kurumlarına e-Fatura için IBAN, mail sunucu bilgileri, otomatik mail/SMS seçenekleri ve banka online ver-al seçeneği var. Noterler Birliği entegrasyonu için kullanıcı adı/parola girilince cari kartında TC kimlik no ile bazı bilgiler otomatik dolar (videoda bu bilginin hangi entegrasyon hesabı olduğu net anlaşılmıyor). {GEd9hqzD67g}
- e-Devlet sekmesinde e-Fatura, e-İrsaliye ve e-Müstahsil kullanımı işaretlenir. Restoran/Hızlı Satış'ın otomatik fatura göndermesi için ilgili seçenek ve kaç dakikada bir kontrol edileceği ayarlanır. Yeni nesil ÖKC için "yeni nesil yazarkasa kullan" işaretli olmalıdır. e-Defter ayarları için AKINSOFT genel merkeze başvurulur. e-Devlet 2 sekmesinde interaktif vergi dairesi bilgileriyle gelen e-Arşivler içeri alınabilir. {GEd9hqzD67g}
- Şube kaydında cari kartların ve döviz hareketlerinin şubelerde ortak kullanılıp kullanılmayacağı seçilir. "Personel ata"da şubeye yetkili kullanıcılar belirlenir. Hiç kullanıcı atanmamışsa herkes girer; bir kullanıcı hiçbir şubeye atanmamışsa tüm şubelere girer. {GEd9hqzD67g} {dofF2h2d18U}
- WOLVOX 6/7, OctoPers ve OctoPlus'tan WOLVOX 8'e geçiş: KP ilk açılışta sorar; atlandıysa KP'deki upgrade/geçiş menüsünden yapılır. Eski programın data dizini gösterilir. WOLVOX 7'den geçişte KP ayarları ve veriler olduğu gibi taşınır; OctoPers/OctoPlus'ta modül seçilir. WOLVOX 7 ve 8 kontrol panellerinin aynı port numarasını kullandığından emin olunmalıdır. {MOFjMLcqyMY}
- Windows 8 ve üstünde upgrade için KP bir kez yönetici olarak çalıştırılmalıdır. WOLVOX 7'den geçişte iki program aynı porta sahip olduğundan WOLVOX 7 KP kapatılır, WOLVOX 7 klasörünün tam yolu verilir. Upgrade sonrası veritabanı güncellemesi otomatik yapılır. Açılıştaki çalışma ve güncelleme portları aynı olmalıdır. Kurulu olmayan modüller aktarım listesinde pasif görünür. {7EMxx6-gdL0}
- İstemci (client) kurulumu: WOLVOX Installer'da "bu bilgisayar istemci olarak kullanılacak" seçilir, ana makinenin IP'si ve güncelleme portu girilir. WOLVOX 7 kurulu istemcide ayarlar, tasarımlar ve özel ayarlar WOLVOX 8'e otomatik taşınır. {QJRtI0v3hGE}

### Şube ve offline sistem
- Şube sisteminin amacı: tüm şubelerin verisi tek veritabanında, her şube için ayrı şirket açmadan, tek ekrandan raporlanır. Stok kartları ortaktır; envanter ve kâr-zarar şube bazında çalışır; cari ve döviz hareketleri isteğe bağlı ortak olur. Sonradan şubeye geçilirse eski kayıtlar merkez veya başka bir şubeye eşitlenir. {dofF2h2d18U}
- Offline kullanım: şirket kaydında offline izni, kullanıcı yetkilerinde offline alanı ve altında tablo bazlı yetkiler işaretlenir. "WOLVOX veritabanını komple gönder" seçilirse alttaki tablo yetkileri geçersiz olur. Offline bilgisayara Kontrol Paneli de kurulur, girişte "offline modunda kullan" seçilir. Diğer işlemler > offline ver-al ekranında merkez IP, KP portu, kullanıcı adı/parola ile bağlanılıp veri alınır/gönderilir. {dofF2h2d18U}

## WOLVOX ERP: genel ayarlar ve araçlar

### Özel Ayarlar (Yetkili → Özel Tanımlar → Özel Ayarlar; kullanıcı bazlı)
- **Fatura {PGSjmEAFhwQ}:**
  - Satış faturası: orduevi iç dağıtım sistemi, elektronik terazi, hızlı satış modu. Ek sistemler: **Petrol sistemi / Toptancı sistemi**.
  - Alış faturası: satış fiyatı oluşturma penceresi, alış fiyatına KDV ve **ek maliyet** ekleme, yeniden oluşturulacak satış fiyatı sayısı.
  - Genel: hareket sıralaması (düz veya ters); okutulan barkod kayıtlı değilse stok kaydı sorulsun; açılışta yeni fatura; yazdırırken stok fiyat, stok bilgisi ve depo bilgisi çekilsin.
  - **POS vade farkı:** ayrı satırda ya da stok fiyatına yansıtılarak.
  - Diğer: genel müşteri cari kodu, seri yazdırma karakter sayısı.
  - Hızlı satış: aynı barkod birleştirilsin mi, barkoddan sonra yeni satıra mı miktar sütununa mı geçilsin.
  - Masraf faturasında döviz.
- **İrsaliye {iYBhXxb9SWI}:** yazdırmada **iç tadil belgesi** oluşturma, hızlı satış, elektronik terazi, orduevi, yazdırmada stok/depo bilgisi, sıralama, Petrol/Toptancı ek sistemi. Transfer irsaliyesinde stok seçilince KDV oranının aktarılması.
- **Stok {WTv4iPs6qsk}:**
  - Stok listesinde resim yazdırma. **Stok listesini Excel'e aktarırken şifre** isteme.
  - Paket tanımlarında miktar sorma ve paket içeriği sıralaması.
  - **Hızlı satış miktar çarpanı karakteri:** ör. `5*barkod` okutulunca miktar 5 gelir.
  - Hızlı stok tanımından sonra miktar sorma; yeni stok kartı açılırken tam form mu hızlı tanım mı açılsın.
- **Cari {A0YQSu8dkRc}:** cari listesinde resim, **kara liste kontrolü**, **kimlik tarama programı yolu**, yeni kayıtta imlecin nereye konumlanacağı, cari hareket girişinde ödenmemiş taksit uyarısı.
- **Depo {L0Z73kqH1Kc}:** toplu depo transferinde barkoddan sonra miktar sorma, varsayılan depo.
- **Sipariş {6umHQkSNMfM} / Teklif {GAmm4-Yszig}:** hareket sıralaması, konumlanma, yazdırmada stok bilgisi, resim ve depo; hızlı satış; toptancı sistemi.
- **Çek/Senet {9n8gKa_rrjw}:** aynı evrak numarası girilince uyarı.
- **Servis {SlQcwHgaAuU}:**
  - Cari arama kriteri: ürün adı, marka, model ya da seri no.
  - Yapılacak işlemler toplamı hangi hareket tipiyle aktarılır: bağımsız, hizmet tanımı ya da işlem tanımı.
  - Varsayılan teslim alan ve eden kişi.
  - Seri no daha önce servise gelmiş mi kontrolü.
  - Randevuda varsayılan genel müşteri; randevudan fişe aktarılınca fiş durumu; günlük personel iş yükü.
- **Üretim {gFGJLa3gqT4}:**
  - Orduevleri için muadil sistemi, mamul sıralaması.
  - Satış fiyatı oluşturma (birim maliyete KDV ekleme).
  - **Eksiye düşen stokları otomatik üret:** yenileme aralığı (dk), depo, bloke dahil.
- **MRP II {mCffjqp28BU}:** Gantt bilgilerini otomatik oluştur ve güncelle, sonuçlandırmada miktar yuvarlama, üretim emrinde başlangıç = sistem tarihi.
- **CRM {3ANJl0qr6Ik}:** CRM ajandasını randevu paneli olarak kullan, yalnız aktif personeli göster, grupları ağaç olarak göster, varsayılan aktivite tipi (randevu, toplantı, iş, hatırlatma).
- **Banka {JApulKV03SQ}:** POS tanımlarının sıralaması.
- **Caller ID {K10-2MGio98}:**
  - Caller ID Server portu. **Telefon gelince açılacak ekran:** cari kartı, yurt içi satış faturası ya da servis fişi.
  - Arama sırasında aktivite ya da müşteri destek kaydı açılabilir.
  - Alan kodu, uyarının ekranda kalma süresi, **gelen aramaları kaydet**.
- **Sanal santral {Ja0DBZyywPE}:** Veri Transferi'nde SanalSantral lisansı ve ayarları olmalı. Bilgisayarı birden fazla kişi kullanıyorsa dahili no buraya yazılır. Başka santraller için bir "App link" alanı var.
- **Tüp/Su {0TyO-OsaO_c}:** Değişim bilgisini otomatik aktarma (sor / sormadan / aktarma), "teslim edildi" otomatik işaretli, depo bölümü ve varsayılan depo, faturalandırmada güncel fiyat (sor / kullan / kullanma).

### Diğer ERP işlemleri
- **Anonimleştirme (KVKK) {ge1sapyn25E}:**
  - ERP, Restoran, Otel, GM ve İK'da var.
  - Tarih aralığı (başlangıç zorunlu değil), imha evrak adı, yöntem ve tablolar seçilir. Aynı kayıt ikinci kez işlenmez.
  - Anonimleştirme raporu ve kayıt formu (yalnız kayıt amaçlı) ayrıca var.
- **Doküman takibi {BjabsSOvwtc}:** Diğer İşlemler → Doküman Takip. Doküman no, grup, uyarı tarihi, durum (beklemede, aktif, tamamlandı), özel kodlar, bağlı cari ve stok, özel alanlar, dosya ekleri, doküman listesi ve grup tanımları.
- **Excel'den stok aktarımı {hcuXNNI4A0Q}:** Diğer İşlemler → Excel'den Transfer.
  - Excel'de boş veya yanlış hücre olmamalı. "İlk satır başlık" ve çalışma sayfası seçilir.
  - Eşleştirme stok koduna ya da barkoda göre yapılır. Kayıt varsa "güncelle" ya da "değiştirme" seçilir.
  - Kolonlar eşlenir, kullanıcıların çıktığından emin olunup aktarılır. Sonunda güncellenen ve eklenen sayısı gösterilir.
- **Şubeler arası kasa transferi {r4Kn-uVodnQ}:** Kasa İşlemleri → Kasa Transferi (kaynak ve hedef kasa). Karşı şube Finans → Raporlar → Kasa Raporları → **Kasa Transfer Havuzu**'ndan "Transferi Onayla" der.
- **Siparişten üretim {ar3oWJDkrsI}{A4ltDkXxqXA}:**
  1. Alınan siparişte İşlemler → Üretime Aktar (reçetesi olan ürün gelir) ile üretim emri oluşur.
  2. Üretim Planlama Listesi'nde durum "Planlama → Üretimde" yapılır, ok işaretiyle "Yeni Üretim Yap"a aktarılır.
  3. Durum "Tamamlandı" yapılınca üretim kaydı oluşur.
- **Servis fişini faturalandırma {XZK4hSnHJCo}:** Servis fişinde İşlemler → Faturaya Aktar / İrsaliyeye Aktar.
- **Tekliften siparişe özel alan aktarımı {-kFwELXutEc}:** Bilgi Bankası 3677 ile aynı.
- **Etiket tasarımı {ssmJIXZD4mw}:**
  - **Kartoteks modülü** gerekir.
  - Stok Tanımlar Seri Etiket'te ürünler sağa aktarılır → Yazdır → Aktif etiket dosyasını tasarla.
  - Veri alanı ekle: tablo "Stok Raporları → Stok Etiket Yazdırma".
  - "DB bağlantılı barkod ekle": barkod alanı ve barkod tipi seçilir.
  - Raporun genel tablosu da "Stok Etiket Yazdırma" olmalı.

### WOLVOX 8 arayüzü
- Sık kullanılanlar ve hızlı erişim menüsüne sağ tık ile ekleme yapılır. Genel aramada cari ve stok da aranabilmesi için performans ayarlarında "genel aramada carileri ara / stokları ara" işaretlenir. Menü tek/çift tık davranışı ve dizilimi (soldan sağa / yukarıdan aşağı) değiştirilebilir. {qK4Mqk69S3Q}
- WOLVOX 8'de modüller iş alanı gruplarına taşındı: stok, satın alma, satış, üretim (basit üretim ve MRP2), servis, finans (tahsilat, tediye, taksit, kasa, banka, döviz), CRM ve "diğer işlemler" (transfer, özel raporlar, SMS, araçlar, notlar). Her grupta işlemler / tanımlar / raporlar ayrımı var. {G1s3CMAXE60}

### Özel rapor, özel tanım ve raporlama
- Özel rapor: diğer işlemler > özel raporlar; rapor adı, kodu ve SQL girilir, "kodu çalıştır" ile denenir, kaydedilip açılır. {sMN6_k0y_cs}
- Özel tanım (özel alan): ekranlardaki özel tanımlar sekmesinde ayar butonuyla kategori ve alanlar (veri tipiyle) eklenir; sıralama değiştirilebilir. {CCo6v-kgN7E}
- Filtre kriterini çıktıda göstermek: kritere tıklayıp yetkili menüsünden "aktif nesne ismini göster" ile adı kopyalanır; rapor tasarımında çok satırlı metne yapıştırılıp sonuna ".Text" eklenir. {rBW4FByBDw4}

### Mail/SMS şablonları
- Önce KP şirket kaydı özel bilgilerde ve KP özel ayarlarda "otomatik mail/SMS gönderme sistemi kullan" işaretlenir. ERP'de mail SMS şablonlarında modül (ör. satış faturası), durum (mail, SMS, ikisi, gönderme), otomatik ya da onaylı gönderim, alıcı (cari veya yetkili maili) ve şablon metni belirlenir. Gönderilenler mail SMS listesinden izlenir. {6936o2LnNhI}

## Finans (kasa, banka, cari, döviz, taksit)

### Diğer finans işlemleri
- **Banka Online Veri Al {X9H9JUwL1mo}:**
  - Desteklenen bankalar Bilgi Bankası A2217'de, başvuru formları A1718'de.
  - **Entegrasyon tipleri:** **MT940** (bankayla anlaşılan periyotta dosya) ve **web servis** (15 dakikada bir sorgu).
  - Kurulum: Kontrol Paneli'nde şirket → Özel Bilgiler → "Banka online veri al". Banka tanımında alt hesaplar sekmesine alt hesap no ve **26 haneli IBAN** girilir. "Entegrasyon kullan" açılır, banka seçilir ve bankanın verdiği bilgiler girilir. **Son işlem zamanı** buradan ayarlanır.
  - Kullanım: Finans → Banka İşlemleri → Bankadan Online Veri Al. Hedef modül: cari / banka transferi / entegrasyon yok. Cari kartında IBAN kayıtlıysa eşleşme otomatik olur. Sonra "Hareketleri işle".
- **Pazarlamacı prim raporu 1 {giBIJEGgh7g}:**
  - Pazarlama modülü gerekir. Pazarlamacı cari olarak açılır: Özel Bilgiler 2'de "pazarlama sistemini kullan", üründen ve işçilikten prim yüzdesi, PDA şifresi.
  - Finans → Raporlar → Pazarlamacı Raporları. Maliyet hesabı seçilebilir.
  - Primler **otomatik olarak pazarlamacının cari hareketine** geçer. İstenmiyorsa Genel Ayarlar → Fatura Ayarları → Fatura Sabitleri → pazarlamacı = "Toplu entegrasyon" yapılır ve "Primleri işle" ile işlenir.
- **Pazarlamacı prim raporu 2 {3Rqpk7Bv-P0}** (Ayarlar'dan tanımlanan kurallar):
  - **Ciro basamakları:** ör. 5–10 bin %5, 10–20 bin %7,5. "Kademeli prim basamağı" seçilirse her kademe ayrı hesaplanır.
  - Diğer seçenekler: "bilgileri faturadan al", satış ve iade fatura grubu filtresi.
  - **Ortalama fiyat** basamağı: iskontoyla satışı caydırır.
  - **Cari sayısı** basamağı: "aynı cari bir kez sayılsın", ek SQL filtre şartı.
  - İade kesinti oranı.
  - **Tahsilat kontrol sistemi:** prim tahsil edildikçe kazanılır. Carinin Özel Bilgiler 2'sinde "ilgili pazarlamacı" seçili olmalı.
- **Doküman takip {_C790nz77Vg}:** Önceki doküman takip videosuyla aynı.
- **Banka tanımı: Kredi kartı {uWK4fL0vnEw}:** Hesap (TL/döviz), kart no, **hesap kesim günü**, son ödeme günü, limit, asgari ödeme oranı, özel bilgiler, aktif/pasif, "diğer şubeler kullanabilsin", ek kart.
- **Banka tanımı: POS {jbrIpKqJWSs}:**
  - POS tanımları: taksit sayısı, **provizyon oranı**, provizyon kesinti tipi (vade farkı satırlara eşit dağıtılır ya da ilk satırdan düşülür), satış vade oranı, bağlı alt hesap.
  - **Vade günü:** çekim hesaba kaç gün sonra geçer.
  - Taksit sayısına göre farklı oranlar girilebilir.
- **Cari yaşlandırma raporu {Nd8TAAkcfuA}:** Finans → Raporlar → İşlem Raporları.
  - Tahsilatlar en eski borçtan başlayarak kapatır (ör. 590 TL'lik faturanın 446 TL'si ödenmişse 144 TL açık kalır).
  - Kolonlar: vade günü, **açık hesap günü**, gerçekleşen vade, **ortalama vade**, bakiye ödeme tarihi.
  - Seçenekler: yaşlandırma grubu (alıcı = borç, satıcı = alacak), hareket tipi (tümü ya da yalnız fatura/irsaliye/devir), yaşlandırma tarihi, açık hareketlerden hesaplama.
  - **Dönemsel yaşlandırma:** günlük, 7, 15 günlük, aylık, 3 aylık ya da elle aralık.
  - "Vade tarihini yalnız borç hareketlerine uygula". Döviz hesabına göre filtre. Sonuç SMS ya da mail ile gönderilebilir.
- **Taksit işlemleri {dlr40UlKtFA}{Wo1BCSwdZRU}:**
  - **Yeni taksit girişi:** cari, satış ya da alış, TL ya da döviz, tutar → **Otomatik taksitlendir** (adet, peşinat, ilk taksit tarihi, aralık, yuvarlama tutarı, **gecikme cezası**). Senet, sözleşme ve plan yazdırılabilir; satır iptal edilebilir; faiz uygulanabilir.
  - **Taksit tahsilatı:** "Tümünü işaretle" ya da **tutara göre işaretle**. Eksik ödenen tutar seçilen aya "kalan taksit" olarak aktarılır. Ödeme türü kasa, banka ya da çek/senet. Yanlış ödeme silinebilir; ödenmemişlerin tümü iptal edilebilir.
- **Seri senet basımı {jqmV3Z5BdBo}:** Çek/senet modülü gerekir. Kayıtlar **yalnız çıktı içindir**, cariye hareket işlemez. Kefil, ilk taksit tarihi, vade artışı (ay/gün), adet ve tutar girilir → Uygula → yazdır.
- **Toplu cari hareket {IQ03ZtxDzhA}:**
  - Birden fazla cariye tahsilat ya da tediye tek ekrandan girilir. **Excel'den içeri alınabilir.**
  - Kolaylıklar: tutarı boş olanları sil, alanı ya da satırı kopyala, "açıklamaya girilen bilgiyi formül olarak kullan".
  - Sonunda **"Hareketleri işle"**.
- **Çek/senet:**
  - **Tahsilat bordrosu {ak8JKI9oHPc}:** satır satır ya da toplu giriş. Döviz ve **havuz sistemi**, devir hareketi, GM entegrasyonu ve portföy hesap kodu, eski bordroyla ilişkilendirme. Sonunda "hareketleri işle".
  - **Çek tahsilatı {GEyEdpT00LQ}:**
    - Evrak no otomatik verilebilir (Genel Ayarlar → Çek/Senet).
    - **Havuz sistemi:** Evrak tahsil ya da ciro edilene kadar cari bakiyeye işlenmez, o günün kuruyla işlenir. Cari hareket raporunda "havuz sistemindeki evrakları ekle" ile görünür.
    - Diğer işaretler: "protesto oldu", "devir" (cariye işlenmez, mükerreri önler), GM entegrasyonu.
    - Durum geçişleri: portföy → takasta (banka) → tahsil edildi / iade alındı; banka kredisi; nakit tahsil; ciro; iade. İşlem tarihi ve açıklaması sonradan değiştirilebilir.
    - Asıl borçlu farklıysa (ciro edilmiş çek) seçilebilir.
  - **Çek/senet işlemleri (toplu durum değiştirme) {Z36hN7LnCFM}:** Filtrele → Ctrl ile çoklu seç → yeni durum (takasta, banka kredisi, tahsil, ciro, iade) → banka, kasa ya da cari seç → Uygula.
  - **Kısmi tahsilat {kneXXqJZjyw}:** Ödenmedi ya da portföydeki evraklarda kısmi ödeme tarihi, tutar ve tür (nakit/dekont/POS/evrak) girilir. Kalan borç gösterilir. Cariye ve asıl borçluya SMS gönderilebilir.
- **Şubeler arası kasa transferi {TbpRyS0FQwo}:** Önceki videoyla aynı (Kasa Transfer Havuzu → onay).

### Banka ve kasa işlemleri
- Banka borç/alacak girişinde işlem türü seçilir; "tahakkuk" türleri muhasebe entegrasyonunda Genel Muhasebe fişi üretir. "Devir" türü açılış bakiyesi girmek içindir. {QnxHpptmRBQ}
- Bankadan kasaya / kasadan bankaya transfer tek fişte yapılır; döviz cinsi seçilebilir. {bajjbxLmiTg} {hI0Y4U3Lxqs}
- Kasa ve banka kartlarında döviz cinsi tanımlanır; kayıt ekranındaki "muhasebe entegrasyonu yap" işaretiyle hareket Genel Muhasebe'ye aktarılır. {K1TOOWCw9tM}
- Banka alt hesapları vadeli/vadesiz olarak açılır. Şube kullanımında hangi şubenin gelir/gider hareketi girebileceği ayrıca izinlendirilir. Alt hesapta açılış/kapanış tarihi, opsiyon kredi limiti ve rotatif kredi bilgisi tutulur. {8N-RNHMg4FU}
- Videoda online (API) entegre bankalar olarak Akbank, Garanti, VakıfBank, ING, İş Bankası, Yapı Kredi, Albaraka, QNB Finansbank, Kuveyt Türk ve Ziraat sayılıyor (video tarihindeki liste; güncel liste için Bilgi Bankası'na bakılmalı). {8N-RNHMg4FU}
- Banka-kasa transferi için lisansta banka ve kasa modülleri gerekir; kaynak banka, hedef kasa, evrak no, grup, tutar ve açıklama girilip "transferi uygula" denir. {glZfEn1SeBg}
- Banka → kasa transferinde kaynak banka ve hedef kasa, kasa → banka transferinde kaynak kasa ve hedef banka seçilir. {HgUP0zwnK_8} (videonun başlığı "kredi kartı taksitlendirme" olsa da içeriği transferdir)
- Bankalar arası transfer için banka modülü gerekir. Kaynak/hedef banka ve kaynak tutar girilir; farklı dövizde parite kurdan otomatik hesaplanır, elle değiştirilebilir. İşlem ücreti ve "muhasebe entegrasyonu yap" seçenekleri var. {gS6egLT6xUI}

### Cari işlemler
- Cari tanım birleştirme: kaynak cari seçilir, hareketleri hedef cariye taşınır; sonra kaynak kart silinebilir. Mükerrer açılmış cariler için. {TsC-Xo23DcE}
- Cari özel tanımlar: kullanıcı tanımlı ek alanlar; raporlarda "özel alan filtreleme" ile süzülebilir. {qr16E3wAmMI}
- Cari virman: bir cariden diğerine bakiye aktarma fişi; farklı döviz cinsleri arasında yapılabilir, "yer değiştir" ile borçlu/alacaklı tarafı çevrilir. {cHMAynsO37A}

### Döviz
- Döviz modülünde döviz tanımları yapılır; kur ondalık hassasiyeti parasal ayarlardan gelir. Kurlar elle girilebilir ya da internetten indirilebilir; geçmiş kurlar kur arşivinde tutulur. {abDlYUCkWs8}

### Kredi kartı ve taksit
- Kredi kartı taksitlendirme: satış veya iade için taksit planı oluşturulur; erteleme (ilk taksit ötelemesi) ve yuvarlama seçenekleri var. "Toplam tutar alacaklandırılır" ve "taksit planını cariye işle" seçenekleri carinin nasıl etkileneceğini belirler. Banka tarafı kredi kartı ekstrelerinden izlenir. {I5hWDL18Sqs}
- Taksit virman: bir carinin ödenmemiş alış taksitleri başka bir carinin satış taksitleriyle mahsup edilir; iki taraftaki seçili toplamlar eşit olmalıdır. {p3gHRZDnF9M}

### Çek/senet ve kredi
- Kısmi tahsilat/tediye: durumu "portföy" veya "ödenmedi" olan çek/senette "kısmi ödeme" ile tutarın bir kısmı kasa veya bankaya alınır; ödeme hareketlerine yazılır. {6CtlR64qHjk}
- Kredi işlemleri: toplam tutar, vade (ay), faiz, BSMV, KKDF ve ilk taksit tarihi girilip ön izlenir. Taksitler eşit değilse "planı manuel değiştirmeye izin ver" seçilir. "Krediyi kullan" ile kaynak/hedef banka ve kredi masrafı işlenir. Kredi kullanım raporundan taksit ödenir (banka/kasa) veya kredi erken kapatılır (bugün kapatılırsa ödenecek tutar gösterilir). {uVEoV4MBi0A}
- Kredi: banka ödeme planı Excel'den içeri alınabilir. Kaynak banka rotatif kredi hesabı olan banka, yoksa paranın girdiği banka olmalıdır. Genel muhasebe entegrasyonu seçilebilir. Kredi kullanım raporunda düzenle, iptal (kalan taksitler), sil ve öde vardır. Ödeme bankadan, kasadan veya entegrasyonsuz yapılır; ödenen taksit yeşil görünür. {jNBTSQbC5dM}

### Taksit takip
- Faturadan bağımsız "yeni taksit girişi": cari, toplam tutar, satış/alış, döviz seçilir; "otomatik taksitlendir"de taksit sayısı, peşinat, ilk taksit tarihi ve ay/gün aralığı verilir. Küsurat için minimum tutar ve farkın ekleneceği ay seçilebilir. {gwMC0mp3828}
- Gecikme cezası: genel ayarlar > taksit takipte "gecikme faizi uygula", aylık oran ve opsiyon günü tanımlanır. Resmi tatil grubu seçilirse tatile denk gelen taksit sonraki iş gününe kayar (tanım: finans > tanımlar > resmi tatiller). Tek bir plan için "gecikme cezası uygulama" işaretlenebilir. {gwMC0mp3828}
- Tahsilat: carinin planı açılır, ödenecek aylar işaretlenir; eksik ödemede kalanın hangi aya aktarılacağı sorulur. Ödeme sonrası makbuz basılabilir. "Tüm taksitler"den hatalı ödeme silinir veya ödenmemiş taksitler iptal edilir. {gwMC0mp3828}
- Taksit virman ve kasa transferi için ayrıca bkz. {_FyCP6XfWrU} {ZehXJ6Vd47Y}; banka borç/alacak girişi {RG6NYySRq50}.

### Tanımlar
- Banka tanımı: banka ve şube bilgileri, resmi tatil tanımı (tatile denk gelen POS/kredi kartı vadesi tatil sonrasına atılır). Alt hesapta IBAN, SWIFT, hesap türü, şube paylaşımı, açılış/kapanış, opsiyon kredi limiti ve rotatif kredi bilgisi girilir. Şubelere yalnızca gelir hareketi izni verilirse o şube bankanın raporlarını göremez, girişleri cari hareket raporundan izler. {TnJrvFvOIAs}
- Banka kartındaki POS tanımı: taksit sayısı, provizyon oranı, provizyon kesinti tipi (eşit dağıt / ilk hareketten düş; faturaya vade farkı yansıtılırken kullanılır), satış vade oranı, vade günü (ertesi gün geçiyorsa 1) ve farklı taksitler için POS vadeleri. Ayrıca kredi kartı (hesap kesim ve son ödeme günü), çek defteri ("çek kullan" işaretli değilse çek/senet modülünde seçilemez) ve e-Ticaret sanal POS ayarları. {TnJrvFvOIAs}
- Kasa tanımı: aktif/pasif; terminal yetkileri ve kullanıcı yetkileri ile kasayı yalnız belirli terminal veya kullanıcıların kullanması sağlanır. {rsLKgo9vO3c}
- Cari tanımı: durum aktif / pasif / potansiyel müşteri. Cari kodu için "cari kodunu otomatik ver" (genel ayarlar > cari kart ayarları); "varsayılan il ve ilçeleri otomatik yükle". Hesap bilgilerinde cari iskontosu, vade oranı, kullanılacak stok fiyatı, karekod transfer alanı, cari özel vade, riskli müşteri / kara liste ve risk notu, her seçimde açılan mesaj metni, alıcı grubu (KDV), yaşlandırma grubu ve döviz hesabı var. {RMBMP-4PYkQ}
- Cari kart diğer sekmeleri: yetkililer (SMS gönder = evet olan yetkiliye fatura SMS'i), e-Ticaret giriş bilgileri, mobil satış rota bilgileri, özel bilgiler 2'de "pazarlama sistemi kullan" + prim oranları + PDA şifresi (cari, pazarlama personeli ve mobil satış kullanıcısı olur), servis personeli ve garson işaretleri. Diğerleri: notlar, bonus (ödeme limiti dolmadan kullanılabilir bonus 0 görünür), bakiye/kredi (devir girişi, açık hesap/irsaliye/sipariş ve çek/senet limitleri), servis bilgileri (satış faturasındaki stokları otomatik servis ürünü yapma ayarı var) ve özel tanımlar. "Kopyala" ile kart çoğaltılır. {RMBMP-4PYkQ}
- Cari adres tanımları: cari kartta adresin yanındaki butonla birden fazla adres girilir; belgelerde sevk adresi olarak seçilir. {RVuTuFciK6A}
- Banka çek defteri: "çek kullan" işaretlenir; başlangıç, bitiş ve verilmeye hazır numara, seri ön eki ve basamak sayısı girilir; defter, önceden açılmış alt hesaba bağlanır. {yWfTKmRBgmY}
- Resmi tatil tanımları (finans > tanımlar > resmi tatiller): tarih ve açıklama girilir. "Otomatik aktar" ile bir tarih aralığında hafta sonu günleri toplu tatil yapılır. Banka kartında resmi tatil seçilirse tatile denk gelen POS/kredi kartı vadesi tatil bitimine kayar. {JGPupH66slc}

### Kasa ve çek/senet işlemleri
- Gelir/gider girişi yalnız kasayı etkiler, entegrasyonu yoktur (ör. cari/muhasebe). Evrak no otomatik verilebilir (genel ayarlar > kasa hareket ayarları), döviz desteklenir. {afYdP3YRSas}
- Çek/senet bordrosu: "toplu giriş" ile evrak türü, vade başlangıcı, ay/gün artışı, adet ve tutar verilip seri çek/senet üretilir; "hareketleri işle" ile kaydedilir. {dDjM3iP_oPM}

### Cari tahsilat/tediye
- Cari seçilince ödenmemiş taksiti varsa uyarı gelir. İşlem türü nakitse kasa, dekont/POS ise banka seçilir. Ek işlem türleri genel ayarlar > cari hareket ayarlarında tanımlanır. "Döviz hesabına işle" ile carinin döviz hesabına yansır. Borcun tamamı "aktar" ile alacak tutarına getirilir. "Kaydı aç" entegrasyonla oluşmuş kaynağı (ör. satış faturası) açar; hareketten taksitlendirme de yapılabilir. {tmrILPKi99U}
- Taksit planı faturadan da oluşturulabilir (işlemler > taksitlendir). Gecikme faizi günlük veya aylık seçilir; aylıkta opsiyon günü tanınır, resmi tatil grubundaki günlerde ceza işlemez. {RcOLwp78AQI}
- İşlem türüne sağ tıklanarak genel muhasebeye aktarılacak hesap kodu seçilebilir. "Kredi kartı iade" türünde banka ve kredi kartı seçilir. "Muhasebe entegrasyonu yap" ile GM fişi oluşur. İşlemler menüsünden virmana bağlı cari, dosya, yevmiye fişi, cari rapor ve bakiye açılır. {YXA9MMfQk1w}

### Cari kart sekmeleri (ayrıntı)
- Genel bilgiler: durum (aktif/pasif/potansiyel) raporlarda filtre olur; birden fazla adres "adres tanımları"ndan; konum (enlem/boylam); ülke tanımları yetkili > tanımlardan. Şahıs firmasında TC kimlik no, değilse vergi no doldurulmalı (e-Belge için vergi dairesi önemli). {0og0pJFbODg}
- Hesap bilgileri: carinin iskonto 1-2-3 değerlerinin belgede kullanılması için ilgili modül ayarında "kaynak iskonto" = cari seçilir. e-Devlet 1 bölümünde cariye özel e-Fatura senaryosu, gönderim tipi, hesap ve posta kutusu; e-Devlet 2'de e-Müstahsil kullanımı ve "kamu kurumu" (kamu faturaları için işaretli olmalı). Alıcı grubu toptan/perakende KDV seçimidir (stok kartında iki KDV tanımı gerekir). "Taksitli işlem" işaretliyse faturada taksit penceresi otomatik açılır. Ek kesintiler cari bazında oran/tutar olarak girilir. {-qkZDRp1CSY}
- Bakiye/kredi: cirolu çek/senetlerin limite dahil edilmesi (hiç, vadeye kadar, vade + opsiyon gün) ve "vadesinde ödenmeyen bakiyelerin kontrolü" (tolerans gün) genel ayarlarda; cari bazında borç bakiye limiti. {nvlt0XaEhgw}
- Bonus: cari kart ayarlarında "bonus sistemi kullan". Kaynak tutar: iskonto öncesi ara toplam, iskonto sonrası ara toplam veya genel toplam. Bonus ödeme türü: kapalı faturada ödeme olarak ya da iskonto olarak. Bonus tanımında hesaplama tipi tutar (ör. her 100 TL'ye 10 bonus), aralık (tutar aralığına göre oran) veya stoktan al; bir bonusun TL karşılığı, alt/üst limit ve ödeme limiti. {tEJqNdi_0Ko}
- CRM sekmesi: sektör, yıllık kazanç, çalışan sayısı, potansiyel müşteri durumu, rating, kaynak, kampanya ve CRM müşteri listeleri. {k6PP6pbekOo}
- Notlar: not tanımları finans > tanımlar > notlar; karta elle veya tanımlardan eklenir. {7cuwCG4B5T0}
- Yetkililer: departman (finans > tanımlar > departman tanımları) bazında otomatik mail/SMS bildirimi yapılabilir; yetkiliye e-Ticaret kullanıcı adı ve parolası verilebilir. {6-T-ekG2DeE}
- Özel bilgiler 1: kredi kartı/banka bilgisi (yalnız bilgi amaçlı), ikinci adres, e-posta (e-Arşiv faturası bu adrese entegratör veya programdaki mail sunucusu üzerinden gönderilir), web, notlar, mobil satış rota bilgileri, e-Ticaret kullanıcı adı/parolası. Servis modülünde kullanıcıyı servis personeliyle eşleştirince kullanıcı yalnız o personelin fişlerini görür. {edBosOWl7XQ}
- Özel bilgiler 2: kefil, fatura adresi, sevk adresi; "pazarlama sistemi kullan" (ürün ve işçilik prim yüzdeleri, PDA şifresi, haftalık/aylık/3 aylık/yıllık hedefler), bağlı pazarlamacı, servis personeli ve garson (Restoran PDA şifresi). {ejH3yzXdx5Y}
- Servis bilgileri: carinin servis alabileceği ürünler (ürün, marka/model tanımlarından), filtreleme ve servis fişindeki özel alanlarla eşlenebilen özel tanımlar. {eiPYMw3HdIM}
- Kasa tanımında terminal/kullanıcı aktarılmazsa tüm terminaller ve kullanıcılar yetkili sayılır; kasa adı "kasa adı değiştir" ile değiştirilir. {8NHk1D3pH34}
- Kredi kartı taksitlendirme: cari, toplam tutar, taksit sayısı, ay aralığı, erteleme (ay) girilir, "taksit ön izleme" yapılır, banka seçilip "taksit planını cariye işle" denir. "Toplam tutarı cariye alacak olarak işle" seçiliyse cariye alacak hareketi de düşer. {08QdblFE328}

## Stok yönetimi

### Stok tanımları ve işlemleri
- **Toplu stok hareketi {H_vISNoxHwo}:**
  - Stok → İşlemler. Barkodla hızlı ekleme ("miktar sorma" kapatılabilir). Seri/lot takipli stoklarda sağ tık → seri girişi.
  - Satır bazında: işlem türü (giriş/çıkış), birim, hesap (döviz), işlem, depo. **Excel'den aktarma** var.
  - "Kopyala" ile evrak no ve tarih alt satırlara aktarılır. Sonunda "Hareketleri işle".
- Stok tanımı (genel özet): kod ve barkod otomatik verilebilir (barkod tipine göre sayaç: yetkili > sayaç tanımları > stok barkodu). ÖTV oran veya birim fiyat bazlı olabilir. KDV %0 ürünlerde e-Belge için istisna kodu girilir. 85 no'lu KDV işareti; vade günü; bonus oranı veya birim fiyatı (bonus tanımında hesaplama tipi "stoktan al" olmalı); prim. {50oGgAzv6NA}
- Birim işlem tipi "çarpan" veya "bölen" olabilir. Fiyatlarda alış fiyatı değişince kâr marjıyla satış fiyatı otomatik oluşturulabilir. Özel ayarlar 1'deki alış/satış iskontosunun kullanılması için modül ayarında "kaynak iskonto" = stok seçilmelidir. Eksi stoğu engellemek için stok ayarlarında "stok eksiye düşüyorsa işleme izin verme" işaretlenir. "Web'de görünsün" (Restoran/e-Ticaret), izleme tipi, özel ayarlar 2'de MRP minimum üretim miktarı ve ek özellik, alternatifler (stok aramada öneri için ayar "onay al"), tedarikçiler, stok durumu (şube bazında bakiye yenileme) ve depo bazında devir girişi. {50oGgAzv6NA}
- Birim tanımı: e-Belge için uluslararası birim kodu ve miktar hassasiyeti (ör. kg 2 hane, adet yok) tanımlanır. {dOfJw9ws7YI}
- Depo kaydı: aktif/pasif, terminal ve kullanıcı yetkileri. "Eşitle" butonu depo modülü öncesi yapılmış tüm stok hareketlerini seçili depoya bağlar. {29mI-j8oDxU}
- Depo transferi (tek ürün) ve toplu depo transferi: kaynak/hedef depo, miktar, birim, özel kod ve hesap (para birimi). {DsuFtsBPAl0}
- Hizmet tanımı: ad, yurt dışı adı, birim, KDV, ÖİV, fiyat ve döviz fiyatı, grup/ara/alt grup; pasife alınabilir. {e9Q9FmptapE}
- Lokasyon modülü: depo için kat/koridor/raf ağacı tanımlanır, depo krokisi üzerinde konum belirlenir. Lokasyon giriş/çıkışları stok veya depo miktarını etkilemez; yalnızca mevcut stoğun nerede durduğunu kaydeder. {HYkVSXCE7dU}
- Stok kartı birleştirme: kaynak stoğun tüm hareket ve belgeleri hedef stoğa aktarılır (mükerrer kartlar için). {WonDlh0T6U8}
- Stok sayım ve düzenleme: depo ve "envanter son tarih" (sayımın gerçekte yapıldığı tarih) seçilir. Sayım dosyadan okunabilir (TXT: barkod veya stok kodu + ayraç + miktar), mobil satış (PDA) sayımından alınabilir ya da elle girilir. Sayım tipi depo sayımı, stok girişi veya stok çıkışı olabilir. "Miktarı sıfır olmayan stokları aktar" ile sayılmayanlar eklenir. "Stok hareketleri işle" ile fark hareketi oluşur (maliyet fiyatı seçilir) veya "muhasebelendir" ile irsaliye/fatura yapılır. {prM-Aut4BeE}
- Asorti özet: renk ve beden tanımları stok yönetimi > tanımlardan yapılır; alt stok adı/koduna eklenecek bilgi seçilir; fiyat güncellemede eski fiyatları silme seçeneği var. {Ne-vM5Cr1K4}
- Toplu depo transferi: filtreyle ya da barkod okutarak, dosyadan (TXT/Excel), faturadan veya stok ek özelliklerinden ürün eklenir; seri/lot okutulabilir. "Transfer uygula" ile kaydedilir, transfer fişi ve etiket yazdırılır. {lw0IqUJRpdM}
- Toplu stok hareketi: birden fazla stoğa tek seferde giriş/çıkış; barkodla veya Excel'den (sütun eşleştirme) doldurulur. Döviz, hesap (KPB = kendi para birimi), depo ve seri/lot seçilir; "kopyala" ile evrak no/tarih alt satırlara çoğaltılır; "hareketleri işle" ile kaydedilir. {V8JrYrGSh-0}
- Argox etiket yazıcı: tasarım ArgoBar programında (PPLA 200 dpi) yapılır ve PRN dosyasına çevrilir. Sayfa (roll) ve tek etiket ölçüsü, yan yana etiket sayısı (per row) ve sol boşluk girilir. Metin alanına köşeli parantez içinde tablo alan adı yazılır (ad listesi seri etiket ekranında sağ tık > özelleştir). PRN dosyası not defterinde açılıp barkod değerinin yerine köşeli parantezle alan adı konur. WOLVOX/OctoPlus'ta "stok kartları seri etiket" ekranında bu PRN seçilip yazdırılır. {OQPf1qGhozo}
- Depo modülü ayrıca lisanslanır; stok ayarlarında "depo modülünü kullan" açılır. Depo adı "depo adı değiştir" ile değişir. "Eşitle" işleminden önce mutlaka yedek alınması önerilir. {C-xaNM9qf4A}
- Hizmet tanımında bonus oranı veya bonus birim fiyatı da girilir (oran girilirse birim fiyat dikkate alınmaz). {WkmdMH4fQEI}
- Paket tanımları (Stok 2 modülü gerekir): pakete stoklar miktar ve fiyat seçimiyle (veya elle fiyat + döviz) eklenir; faturada "stok paket arama" ile paket içeriği satırlara dökülür. İçeriğin satır satır görünmemesi için asorti/ana stok olarak açılmış bir stok pakete bağlanırsa faturaya yalnız ana stok gelir. {TU1PeQnX6Yg}
- Stok giriş/çıkış hareketi (fatura/irsaliye olmadan): miktar, birim, fiyat, döviz, cari (raporda görünmesi için), depo. "Maliyet ve satış istatistiklerinde kullan" işaretliyse maliyete etki eder. Hareket tipi iade veya devir olarak seçilebilir. {XnHTnRYuMCc}
- Birim/barkod sekmesinde varsayılan miktar girilmezse 1 kabul edilir; lotlu stokta lot bakiyesi aktarılır. {-jgZq6Uq2O0}
- İstatistikler sekmesi: her hesap (para birimi) için alış/satış son, ortalama, ağırlıklı ortalama, en ucuz ve en pahalı fiyatlar. {_DycYJ_ARfg}
- Stok limit kontrolleri: stok ayarlarında "stok eksiye düşerse uyar", engellemek için "eksiye düşüyorsa işleme izin verme". Sipariş/teklifteki bloke miktarlarının kontrole girmemesi için ilgili seçenek kaldırılır; stok kartı özel ayarlar 1'de de "eksiye düşerse uyar" işaretlenmelidir. {22P5771jTHU}
- Seri/lot: varsayılan izleme tipi genel ayarlar > stok ayarları > seri/lot'ta seçilir. Lot sistemi üretimde geriye dönük izlenebilirlik (hangi partiden kime satıldı) içindir. Seri no bir ürüne özeldir; lot no birden çok ürüne verilebilir. "Maliyetlerde eşleştirme yöntemi" açıkken satılan seri/lotun kendi alış fiyatı maliyet olur (ör. 10 ve 25 TL'lik seriler satıldıysa maliyet bu ikisi). {nO-F7tgUKj4} {sBjsXRCj0jc}
- Seri/lot giriş/çıkış hareketi (belge dışından): cari, miktar (seri no'da pasif, her hareket 1 adet; "toplu giriş" ile çoklu), depo, daha önce serisiz girilmiş stok hareketiyle eşleştirme, garanti ve son kullanma tarihi. "Bakiye" seri/lot bakiyelerini gösterir, "yazdır" etiket ekranına gider. {nO-F7tgUKj4}
- Otomatik sipariş listesi: stok ayarlarında "sipariş listesine ekle" işaretlenir. Stok kartı özel ayarlar 1'de de işaretlenip "şu miktarın altına düşünce" ve "şu miktara tamamla/şu kadar ekle" değerleri girilir. Verilen siparişte cari seçip "sipariş listesi" denince, o carinin tedarikçi olduğu ve listeye eklenmiş stoklar gelir. {5AducVphw6w}
- Paket tanımı (güncel anlatım): pakete barkod tipi seçilip barkod üretilebilir. İçerik yerine tek kalem görünmesi için paket, asorti ana stok olarak açılmış bir stoğa bağlanır. {ctFhkwl9HCI}

### Stok kartı sekmeleri
- Stok kodu ve barkod, stok ayarlarındaki şablonlara göre otomatik üretilebilir. {KZL9nLwJnD8} {0a8Slnl8plQ}
- Kartta uzun açıklama alanı (videoda yaklaşık 3000 karakter), satış elemanı için bonus ve prim alanları, ana stok / asorti (varyant) bağlantısı bulunur. {XR9f7i_pGwk} {2z-MznjN1bE}
- Seri no ve lot/parti izleme kart bazında açılır; "partiler parçalanabilir" seçeneği tek partinin birden fazla satışa bölünmesine izin verir. Maliyet hesabında "eşleştirme yöntemi" seçilir. {BSDpX8IAKrc} {9cwxLYL8Q2E}
- Minimum/maksimum ve kritik stok limitleri depo bazında tanımlanabilir; kritik seviyenin altına düşen ürün sipariş listesine otomatik eklenebilir. {rWhdt8QhGjc}
- Depozito ürünü (ör. damacana, kasa) karta bağlanabilir. {GxQ7RMfEqx8}
- Yazarkasa ile satılacak stokta "yazarkasa KDV departmanı" seçilmelidir. {6S8uKR123gY}
- Tedarikçi stok kodu alanı: e-Fatura gelen kutusunda tedarikçinin kodu ile kendi stok kartını eşleştirmek için kullanılır. {grNZQwSmkFQ}
- Kalite kontrol sekmesi MRP/üretim tarafında giriş kontrolü için kullanılır. {_JrPffOnGhA}

### Stok kartı, fiyat ve maliyet
- Toplu alış/satış fiyatı değişikliği: fiyat listesinde ürünler filtrelenir, işlemler > manuel fiyat değiştirme ekranında döviz hesabı ve fiyat no seçilir, yeni fiyatlar girilip uygulanır; artış yüzdesi gösterilir. {uZiPIjadhAY}
- Stok kartı fiyatlar sekmesi: fiyat başlıkları "fiyat tanımları"ndan yapılır, "varsayılan fiyat tanımlarını aktar" ile karta taşınır; fiyat sayısı sınırsızdır, her fiyat birime/barkoda bağlanabilir. Alış fiyatı değişince satış fiyatını kâr marjıyla yeniden oluşturmak için alış faturası ayarlarında "satış fiyatları oluşturma penceresini göster" işaretlenir. {sRfQESpznAs}
- Genel bilgiler sekmesi: stok kodu, genel ayarlardaki formata göre otomatik verilebilir. Barkodun otomatik verilmesi için sayaç tanımı gerekir; "sayaç yok" uyarısında sayaç tanımlarından barkod tipine sayaç eklenir. Tevkifatlı üründe e-Fatura için tevkifat kodu seçilir. Stok bazında vade günü ile prim oranı/tutarı girilebilir. Döviz fiyatı için "döviz hesabı kullan" işaretlenir. "Yerli üretim" işareti fatura çıktısında gösterilebilir. {euPXkkxF81g}
- Birim/barkod sekmesi: diğer birimler çarpan ile tanımlanır (ör. paket = 12 adet). Varsayılan birim, ek barkodlar, barkod okutulunca gelecek varsayılan miktar ve net/brüt ağırlık (çeki listesinde kullanılır) girilir. Hacim hesabı için sayısal özel alanlarla formül tanımı yapılıp karta bağlanır. {l4llGkRizGU}
- Asorti: önce renk ve beden tanımları yapılır, ana stok kartında "asorti sistemi kullan" işaretlenir, "alt stok" ekranında renk/beden seçilerek alt stoklar üretilir (resim kopyalama, marka/model aktarımı seçenekleri). Ana stok fiyatı değişince "fiyat güncelle" ile alt stoklara yansıtılır. Faturada ana stok seçilince asorti giriş ekranı açılır. {0D0IYdGOe9w}
- Ağırlıklı (terazi) ürün: genel ayarlar > stok ayarlarında elektronik terazi barkod tanımı yapılır: barkod tipi (ilk 2 hane, ör. 27/28/29), stok kodu uzunluğu, gramaj uzunluğu (ör. 5), gerekirse lot başlangıç/uzunluk. Faturada terazi barkodu okutulunca miktar ve fiyat otomatik hesaplanır. {n8wCyOQ-x9w}
- Depo bazlı stok limiti: stok ayarlarında "stok limit uyarıları depo bazında kullan" ve kartta "stok eksiye düşüyorsa uyar" işaretlenir; kontrol seçilen deponun kalanına göre yapılır. {d0upR6Kqo6Q}
- Seri/lot maliyet eşleştirme: kartta izleme tipi lot/parti, "partiler parçalanabilir" ve "maliyetlerde eşleştirme yöntemini kullan" işaretlenir. Bu durumda kâr-zarar gibi raporlar maliyeti çıkışın bağlandığı giriş lotundan hesaplar ve fiyatlandırma sekmesindeki seçenekler devre dışı kalır. Lot numarası formülle otomatik üretilebilir. Seri no için de aynı mantık. {9MJeIgkxTEU}
- Transfer irsaliyesinde FIFO: irsaliye ayarları > transfer irsaliyesinde stok fiyatı "FIFO" seçilince transfer eski girişlerden başlayarak kapatılır. {ABQ27Z1mboo}
- Ek maliyet dağıtımı: alış faturası ek bilgiler sekmesinde ek maliyet tutarı girilip stoklara dağıtılır (döviz ve dağıtım şekli seçilebilir). Maliyete yansıması için alış faturası ayarlarında "ek maliyetleri stok hareketlerine yansıt" işaretlenmelidir; sonra stok kâr-zarar ve envanter raporları bunu kullanır. {DnkkhlPGGKM}
- Miktar aralığına göre iskonto: stok ayarlarında "gelişmiş iskonto sistemi" ve "miktar aralığına göre iskonto" işaretlenir; iskonto tanımlarında cari/cari grup/il ile stok/grup/marka/model bazında, tarih aralıklı kademeler girilir (ör. 1-10 adet %10, 11-20 adet %15). {GFzsIJuQMHw}
- Toplu fiyat yenileme (fiyat değiştirme listesi → işlemler → fiyat yenileme):
  - Fiyat artırma: para birimi, alış/satış tipi, fiyat no; oran veya tutar kadar artır ya da düşür.
  - Fiyat çevirme: TL fiyatları dövize veya döviz fiyatları TL'ye, seçilen kur tarihiyle çevir.
  - Alış fiyatı değiştirme: son alış fiyatlarından güncelle (döviz seçeneği var).
  - Satış fiyatı oluşturma: kaynak fiyata yüzde ekleyerek (kâr marjı) veya düşürerek (ör. bayi fiyatı) yeni satış fiyatı üret; tüm listeye sabit fiyat da verilebilir.
  - Yuvarlama: küsurat kuralı (ör. 19,45 → 20).
  - Devir fiyatlarını değiştir: devir hareketlerinin fiyatlarını oranla güncelle (döviz devirleri dahil edilebilir). {4GySHhlMH0Q}

## Satın alma ve satış

### Belgeler: fatura, irsaliye, sipariş, teklif
- **Genel Ayarlar sekmesi (Özel Ayarlar) {Sz0D4VahKW8}:**
  - Program başlığı, mesaj tipi, form renkleri. Sağ alttaki uyarı penceresinin yenileme aralığı ve sesi. Açılışta kısayol çubuğu ya da yönetici ekranı. Tema.
  - Hesap tablosu uygulaması: Excel ya da OpenOffice.
  - Pencereleri ana ekrana sığdırma, otomatik sürüm kontrolü (gün).
  - Belge yazdırırken **stok tedarikçi bilgilerini** çekme.
  - Formlarda stok fiyatının para birimi.
  - Barkod aramasına **pasif stokları** dahil etme.
  - **Tarih değişince döviz kurlarını yeniden aktarmayı sorma.**
  - Resimleri kırpma.
- **İrsaliye formu sekmeleri** {ePQ_LpWALsY}{4kot5pxyTkU}{IxamE96wQxo}{0XEcGzq_qjM}{1_qLcNJaNCI}{lVlRDTC4iHA}{f0ZKlAPiYxo}{qL4rfxtSysI}{nPyjIiacrN8}{ytYuij522SE}:
  - **Genel:** sevk adresi (carinin fatura veya sevk adresi, başka carinin adresi de seçilebilir). Özel kod tüm satırlara aktarılabilir. İrsaliye no otomatik verilebilir ama resmi irsaliyede basılı seri no ile aynı olmalı. Sevk tarihi ve saati.
  - **İrsaliye Bilgileri:** fatura tarihi ve no (faturaya aktarınca dolar), grup, toplu KDV oranı ve dahil/hariç, irsaliye tipi.
    - Vade seçenekleri: manuel / varsayılan / cari vadesi / hareketlerdeki vade.
    - "Cari hareketlerine işlensin", "stok hareketlerine işlensin".
    - "Yazdırıldı", "İptal", "Faturalanacak", "Faturalandı".
  - **Ek Bilgiler 1:** ek bilgi 1–2 ve açıklama (raporda filtre olarak kullanılabilir), kargo firması, no ve tarihi, varsayılan depo, döviz (kurları ve birimi aktar), carinin hangi döviz hesabına işleneceği.
  - **Ek Bilgiler 2 (e-İrsaliye için zorunlu):** taşıyıcı (unvan, VKN/TCKN; cariyi taşıyıcı yapma butonu), şoför ve araç (İrsaliye Tanımları → Araç Tanımları).
  - **Fiyat Değiştirme:** yüzdeyle artırma/azaltma, cari vade oranını aktarma, stoktan alış 1–4 / satış 1–4 fiyatını aktarma.
  - **Bağlantılar:** kaynak belgenin modülü, tarihi ve numarası. Tasarımda tablo "İrsaliye Yazdırma Özel Değerler" → "dış modül bağlantı bilgileri/numaraları/tarihleri".
  - **Not:** tasarımda tablo "İrsaliye Yazdırma". Faturalanınca not faturaya da geçer.
  - **Pazarlama:** irsaliye bazında ya da satır bazında pazarlamacı ve prim oranları (üründen ve işçilikten). Pazarlama modülü gerekir.
  - **Özel Tanımlar:** kategori (sekme) ve alan. Veri tipleri: metin, tam sayı, ondalık, tarih-saat, var/yok, çoktan seçmeli.
  - **CRM:** bağlı proje/satış kodu. CRM modülü gerekir.
- **Sipariş formu sekmeleri** {RgpXHJqJ7Jc}{poziJ2SpNZ8}{HFr3uX2oLPc}{SbJetpxU0OQ}{JakjRNEd-Ic}{ytD0Kq2xbXQ}{B3usZHDs6XQ}{obg6ujfI2gs}{nmLfjop78Oc}{UsPDjP_Vxt8}:
  - Yurt içi/dışı alınan ve verilen siparişlerin işleyişi aynı.
  - Cari yetkilisi, özel kod, otomatik sipariş no, vade (gün/ay), grup, KDV, teslim tarihi, teklif no bağlantısı, durum.
  - **"Ön ödemeli satış":** Normalde sipariş cari ekstresine yansımaz. Bu seçenek açılırsa sipariş muhasebeleşmeden cari borçlanır. Taksit modülü varsa taksitlendirme penceresi açılır.
  - **Ek Bilgiler 1:**
    - Stok bloke (tüm satırlara aktarılabilir), faturalanınca muhasebe evrak tarihi ve no.
    - **Servis araç iş yükü:** araç ve teslim zamanı. Açmak için Genel Ayarlar → Servis Ayarları → Araç İş Yükü → "Araç iş yükü sistemini kullan" + stok montaj süresi alanlarının eşlenmesi.
  - **Ek Bilgiler 2:** e-Ticaret'ten gelen siparişin ayrıntıları, taşıyıcı, ödeme türü (diğer / ödeme aracısı).
  - **İskontolar:**
    - KDV öncesi: cari iskonto, iskonto 1–3 zincirleme, stok iskontosu **en son** uygulanır, özel iskonto.
    - KDV sonrası iskonto: oran ya da tutar.
  - CRM sekmesinde proje/satış kodu ve **kampanya kodu**.
- **Teklif formu {0ZyFklFKGgs}{MbAbjomV_ug}{dwHNkRD3B6o}:** Teklif Bilgileri 1–2 alanları tasarımda "Teklif Yazdırma Özel Değerler" tablosundadır. CRM'de bağlanan proje, proje raporunun "belgeler" kısmında görünür.
- **Sipariş durum tanımları {8RImIT-MpxQ}:** Satış Yönetimi → Tanımlar → Sipariş Tanımları. Her durum için ayrı ayrı seçilir:
  - renk, sıra, onay tarihi kontrolü
  - **alınan siparişte bloke sistemi**, **verilen siparişte termin sistemi**
  - uyarı sistemi ve uyarılacak personel
  - teslim raporunda kullanılsın, **muhasebeleştirilebilsin**
  - durum değiştirme yetkisi
- **Mal Kabul {dGbfx7P7n-Y}:** Satın Alma → İşlemler → İrsaliyeler → Mal Kabul.
  1. Ekle → tarih, sorumlu, araç bilgileri → kaydet.
  2. Kaynak seçilir: **Sipariş** (yalnız "onaylandı" durumdakiler, irsaliye oluşturmak için), İrsaliye ya da Fatura (sayım/kontrol için). Ctrl ile çoklu seçilip aktarılır.
  3. +/− butonları ya da barkodla sayılır.
  4. Durum "tamamlandı" → **İrsaliyeleri oluştur**.
- **Masraf faturası {ubA5BIQTFqg}:**
  - Satın Alma → Faturalar → Masraf Faturası. Hareket = gider işlemi.
  - Ödemeler sekmesinde kasa ya da kart; ödeme birden fazla türe bölünebilir; kartta erteleme.
  - **Zamanlı hesap:** her ay tekrarlayan gider için uyarı. Aylara kopyalanır. Otomatik talimat varsa kasa ya da banka hareketi olarak işlenir.
- **Fatura formu sekmeleri** {DvKeamDaS1o}{Q6IQm2a60E8}{Q5MlHZrY7eE}{xNbdaC4C3CM}{rYORU87sIsU}{GJneKauzLsE}{MT_Wunx1wNI}{Jbxn7pKvaew}{JEDQsxQnB2s}:
  - **İskontolar:** cari ve stok kartındaki iskontolar kutucuk işaretlenince gelir. Yeni faturada hangi kutucukların hazır işaretli geleceği Genel Ayarlar → Fatura Ayarları → Satış Faturası'nda belirlenir. Ok ile tüm satırlara aktarılır.
  - **Ek Bilgiler 1:**
    - Açıklamanın stok adlarından otomatik oluşması (Genel Ayarlar → Satış Faturası → açıklama "otomatik oluştur").
    - **ÖTV** ve **özel iletişim vergisi** durumu, **ihraç kaydı**, **bonus kazandır**.
    - **Limitli tevkifat kullan:** Genel Ayarlar'da belirlenen limitin üzerindeki KDV dahil tutarlarda tevkifat otomatik uygulanır.
    - Kargo firması, no ve tarihi; varsayılan depo; döviz birimi ve kuru; carinin hangi hesabına (KPB/döviz) yazılacağı; cari ve stokta döviz hesabına işleme.
  - **Fiyat Değiştirme:** Buradan seçilen stok fiyatı cari kartındaki fiyat seçimini geçersiz kılar.
  - **Not:** e-Arşivde not olarak gitmesi için e-Fatura ayarlarında "faturadaki not bilgisini … not olarak ekle" açılır. Matbu çıktıda tablo "Fatura Yazdırma", alan **"Açıklama 2"**.
  - **Pazarlama:** fatura bazında (yüzde ya da tutar) veya satır bazında (her satıra farklı pazarlamacı).
  - Bağlantılar (irsaliye, sipariş, teklif; elle de girilebilir), CRM (proje ve kampanya), Özel Tanımlar.
- **Teklif formu (ek)** {L7JaEoVL8oI}{JCGfpzQnTxQ}{i-W7ZOVq_hw}{T_W5ntA60Xc}{rSTVk8k6lJw}{EJVPo3EvHPw}{wzYcjZytsvY}{n1attLMJFus}:
  - Yurt içi/dışı alınan ve verilen teklifler. Birden fazla adres tanımı için **Cari 2** modülü gerekir.
  - Teklif Bilgileri: özel kod, otomatik no (Genel Ayarlar → Teklif), grup, KDV, muhasebe evrak tarihi ve no (sipariş, irsaliye ya da faturaya aktarınca dolar), **geçerlilik tarihi**, onay tarihi, teslim süresi (gün), durum, "özel tanım aktarma ayarları".
  - Kaynak iskonto Genel Ayarlar → Teklif Ayarları'ndan seçilir.
- Fatura türleri: alış, alıştan iade, yurt içi satış, yurt içi satıştan iade, yurt dışı satış, yurt dışı satıştan iade. Fatura no otomatik verilebilir (genel ayarlar > fatura ayarları). Fatura tipi (ör. konsinye, proforma) cari/stok hareket ayarlarını değiştirir. "Cari hareketler işlensin" ve "stok hareketleri işlensin" işaretleri bakiyeye etkiyi belirler; irsaliyeden gelen faturada stok hareketi irsaliyede işlendiğinden faturada tekrar işaretlenmez. {sTmfvj7d460}
- Fatura üst alanları: sevk adresi (başka cari adresinden de), ek bilgi 1-2, otomatik açıklama, ÖTV dahil/hariç, özel iletişim vergisi, ihraç kaydı, kargo no, varsayılan depo, döviz ve kurlar, cari/stok iskontosu, KDV sonrası (fatura altı) iskonto, pazarlamacı (fatura veya satır bazında prim), notlar, özel tanımlar, fiyat değiştirme (oranla artırma, cari vade oranı aktarma, stok fiyatından güncelleme), bağlantılar (teklif/sipariş evrakı) ve CRM (proje ve kampanya kodu). {sTmfvj7d460}
- Hareket satırı araçları: çoklu stok ekle, paket ekle, hizmet ekle, fiyat istatistiği, son satış/alış fiyatı, seri/lot girişi ve bakiyeleri (toplu seri girişi, Excel'den), asorti detayı, hareket özel alanları, tevkifat, ek tutarlar (navlun, sigorta, gümrük), ek kesintiler, 85 no'lu KDV matrahı, KDV ve iskonto detayları. {sTmfvj7d460}
- Fatura işlemleri: çeki listesi (ağırlıklar stok kartından), SMS, etiket yazdır, taksitlendir, vade farkı uygula (POS provizyon oranından), kâr-zarar, cari analiz, Excel'den bilgi al, karekoddan veri al, formül tanımları. Kapalı faturada birden fazla tahsilat türü (ör. nakit + POS) girilebilir; kapalı fatura tanımları ve kısayolları, "varsayılan tanıma göre otomatik kapat" seçeneği var. {sTmfvj7d460}
- "Kopyala 2": fatura/irsaliyeler seçilip dosyaya (.fkd) kopyalanır, başka şirkette aynı form > işlemler > kopyala 2 ile içeri alınır. Numara ve tarih yeniden verilebilir. Hedef şirkette olmayan cari ve stok kartları otomatik açılır. {co48wN76a1s}
- Toplu masraf faturası: satır satır masraf faturası girilir, "kopyala" / "satır kopyala" ile hızlanır; "ödeme tutarını ara tutardan otomatik al" seçilebilir; "faturaları işle" ile kaydedilir. {5WfMS00DRbY}
- Transfer talep: şube, eksik ürünleri başka şubeden talep eder. Karşı şube transfer irsaliyesinde hedef şubeyi seçip "talep ekranı"ndan kalemleri irsaliyeye aktarır. Talep eden şubenin cari olarak tanımlı olması gerekir. {WCLcnnGsbVI}
- Masraf faturası: gider carisi (ör. elektrik şirketi) seçilir, ödeme birden fazla türe bölünebilir (nakit + kredi kartı, erteleme). Düzenli giderler "zamanlı hesaplar" ile her ay hatırlatılır; seçilen aylara kopyalanır ve otomatik talimatla kasa/banka hareketi önerilir. {85Qf5TpvpFw}
- Satın alma talep ekranı: eksilen ürünler talep fişine eklenir (tedarikçi, termin, miktar). Verilen sipariş/teklifte "sipariş listesi" ile aktarılır; talepte tedarikçi seçildiyse listede yalnız o carinin tedarikçisi olduğu ürünler çıkar. Talep durumu "satın almada" olur. Talep listesinden "satın alma emri ver" ile doğrudan sipariş oluşturulabilir. {jJ3JfMl4q60}
- e-Teklif ve teklif değerlendirme: satın alma talep listesinden seçilen ürünler için tedarikçilere mail ile teklif linki gönderilir; tedarikçi web formunda fiyat, termin, ödeme günü ve açıklama girer, ERP'de yurt içi alınan teklif otomatik oluşur. Gereksinimler: WOLVOX vMobile kurulu ve portu modemde açık; KP'de mail sunucusu ve otomatik mail sistemi açık; mail şablonunda e-Teklif linki; tedarikçi carilerinde e-posta. Değerlendirme en uygun fiyat, en erken teslim ve en uzun ödeme günü kriterlerine verilen puanlarla sıralanır; seçilen teklif satın almaya aktarılır. {SkRcHKb3CqY}
- İrsaliye: gelen irsaliyeler satın alma, giden irsaliyeler satış yönetiminde. İrsaliye no otomatik verilebilir. "Faturalanacak" ve "faturalandı" işaretleri, cari/stok hareketi işleme seçenekleri, iskonto, pazarlamacı, özel tanımlar ve CRM bağlantısı fatura ile aynı mantıkta. İşlemler: faturaya aktar, Excel'den al, karekoddan al, faturadan aktar (fatura no ile), SMS, etiket, vade farkı, kopyala (gelen/giden/transfer olarak), kopyala 2 (başka şirkete), formül tanımları. {P1Wa4YXQSJ4}
- Sipariş: satın almada yurt içi/dışı verilen, satışta yurt içi/dışı alınan siparişler. Teslim tarihi ve teklif no alanları var. "Ön ödemeli satış" işaretlenirse sipariş toplamı cariye işlenir ve taksit ekranı açılır (mobilya, beyaz eşya gibi). "Stok bloke" ile kalemler bloke edilir. e-Ticaret'ten gelen siparişin ayrıntısı ek bilgiler 2'de. Sipariş faturaya, irsaliyeye veya basit üretime aktarılabilir. {VFAwjPQEfsU}
- Sipariş durum tanımları: sıra, onay tarihi kontrolü (genel ayarlar > program ayarları > "onay tarihi öncesine izin verme"). Alınan siparişte "bloke sistemi kullan", verilende "termin sistemi kullan"; uyarı sistemi ve uyarılacak personel, teslim raporunda kullan, "muhasebeleştirilebilsin" (fatura/irsaliyeye aktarılabilir), durum değiştirme yetkisi ve renk. {wYkpa1NE9ug}
- Teklif: alınan (satın alma) ve verilen (satış) teklifler aynı mantıkta. Geçerlilik tarihi, onay tarihi, teslim süresi, teklif durumu; siparişe aktarırken özel alan eşleştirmesi ("özel tanım aktarma ayarları"). Stok bakiyelerinde bloke = alınan teklif/siparişlerden, termin = verilen teklif/siparişlerden gelen miktar. "Otomatik stok kartı oluştur": seçilen özel alandaki koda göre stok yoksa kart açılır. Teklif faturaya, irsaliyeye veya servis formuna aktarılır. {V4N_3CozJ4Q}
- Toplu irsaliye faturalandırma: bir carinin birden fazla irsaliyesi tek faturada toplanır. Satır birleştirme seçenekleri: fiyatı farklı olanları ayır / aynı satıra topla / hepsi ayrı / farklı depoları ayır. Ortalama valör, döviz kuru kaynağı (irsaliye kuru veya günün kuru), özel alan eşleştirmesi ve farklı fatura carisi seçilebilir. {H5hTbOM6d-8}
- İrsaliye iskontoları: KDV öncesi iskonto 1-2-3 zincir halinde uygulanır. Cari iskontosu, stok iskontosu (alış ve satışta farklı olabilir) veya özel iskonto seçilir; tutar girişinde "önceki iskontoları sıfırla" ve "KDV dahil fiyatlara uygula" seçenekleri var. KDV sonrası iskonto oran veya tutar olabilir. {6hmhA3x2eI4}
- Teklif muhasebeleştirme (toplu teklif irsaliyelendirme/faturalandırma): yalnız durum tanımında "muhasebeleştirilebilsin" işaretli teklifler listelenir. Fatura tipi, satır birleştirme seçenekleri ("aynı stokları aynı satıra aktar" pahalı fiyatı alır) ve özel alan aktarma ayarları seçilir. {EOzK7YGElQ8}
- Fatura genel bilgileri: fatura seri (matbu seri veya sayaçtaki seri), otomatik no, özel kodun hareketlere aktarımı, grup. Vade durumu: manuel, varsayılan vade (genel ayar), cari vadesi veya hareketlerdeki (stok kartı) vade. e-Fatura/e-Arşiv işareti cariye göre gelir. "e-Belge" işaretli belgeler Ba/Bs bildirimlerine dahil edilmez. Senaryo, gönderim tipi, hesap, fatura tipi ve alıcı posta kutusu belgeden değiştirilebilir. {2ENJ8QfS8Bw}

### Cari limit, yaşlandırma ve belge araçları
- Cari limit: genel ayarlar > cari kart ayarlarında "limit aşımına izin verme" işaretliyse işlem engellenir, değilse yalnızca uyarı verilir. Tahsil edilmemiş çek/senetlerin limite dahil edilmesi ve yeni carilere varsayılan limit burada. Cari kartta açık hesap, irsaliye, sipariş ve çek/senet için ayrı kredi limiti girilir. {jujZb-X-1h0}
- Manuel yaşlandırma: cari kart ayarlarında "manuel yaşlandırma sistemi kullan" işaretlenir. Cari yaşlandırma raporunda borç hareketi seçilip "manuel kapat" ile hangi tahsilatla kapandığı belirtilir; kısmi kapama olabilir. Otomatik kapatma FIFO mantığıyla çalışır. Kapatmalar hareket sekmesinden iptal edilebilir. {wq-osWRFSfs}
- İrsaliye faturalanınca cari hareketin işlem türünü "fatura"ya çevirmek için fatura ayarlarında "irsaliyenin faturalanması sırasında cari hareket entegrasyonunu fatura ile ilişkilendir" işaretlenir. {Xravf0bkj4E}
- Karekod ile belge aktarımı: cari kartta karekod transfer alanı olarak stok kodu, barkod veya tedarikçi stok kodu seçilir; program ayarlarında karekod maksimum uzunluğu girilir. Tasarımda "DB bağlantılı karekod" eklenir (tablo: fatura raporları > fatura yazdırma karekodu). Karşı tarafta işlemler > "karekoddan veri al" ile okutulur. {9130LEuq5cw}
- Sevkiyat planlama: önce araç tanımları (plaka, şoför, kapasite); sevkiyat planlamada onaylı sipariş veya irsaliyelerden ürünler aktarılır, yükleme sekmesinde barkodla yükleme sayılır, durum "tamamlandı" yapılınca irsaliyeler oluşturulur. {Yi9sM9EB1IA}

### İthalat yönetimi
- Masraflar hizmet kartı olarak tanımlanır; "dağıtım anahtarları"nda her masrafın dağıtım şekli seçilir: tutar bazında, miktar bazında veya formülden (ör. hacim). Formül, stok kartındaki sayısal özel alanlar (ör. en × boy) ile formül tanımlarında kurulur ve stok kartının birim/barkod sekmesindeki "hacim hesaplama formülü"ne bağlanır. "Tüm ithalatı kapsıyor" işareti de burada. {aD5OymtyakY}
- İthalat dosyası: kod, durum, teslim ve ödeme şekli, menşei, taşıma, gümrük ve müşavir bilgileri; özel alanlar ve dosya eki eklenebilir. Belgelerde seçilebilmesi için dosya durumu "beklemede" veya "aktif" olmalıdır. Yurt dışı verilen sipariş, alış faturası, masraf faturası ve cari tediye fişi dosyaya bağlanır. {aD5OymtyakY}
- İthalat bağlı alış faturasında "stok hareketleri işlensin" pasif gelir; stok girişi "stok millileştirme" ekranında toplu ya da parça parça yapılır. Bu ekranda masraflar seçilip (gerekirse yalnız belirli stoklara) "hesapla" ile maliyete yansıtılır. Dosyaya bağlı tüm hareketler "hareket dökümü"nden izlenir. {aD5OymtyakY}

### Promosyon, sevkiyat, ek özellik ve ek kesinti
- Promosyon tanımları: geçerlilik tarihi, şube, gün/saat; müşteri (cari, grup, ülke/il/ilçe) kısıtı. Promosyon tipleri: toplam tutar genel (fatura genel toplamı limiti), toplam tutar marka/model/grup, toplam tutar stok bazında, miktar marka/model/grup, miktar stok bazında; maksimum promosyon adedi. İndirim sekmesinde promosyon ürünü ve oran/tutar verilir, uygulanan tutar hareketteki "promosyon iskonto tutarı"na yazılır. Ürün seçilmezse en ucuz ürüne uygulanır (ör. "3 al 2 öde"). Tek tanımda yalnız bir ürüne indirim uygulanır. Promosyon fatura ve Hızlı Satış'ta kayıt anında açılan ekrandan seçilir. {t4H8Qp-2tWs}
- Sevkiyat planlamada "taşıma bilgileri" araç kapasitesine göre kalan kapasiteyi gösterir; ağırlık/hacim stok kartının birim/barkod sekmesinden gelir. Kaynak olarak sipariş veya daha önce planlanmış irsaliye seçilebilir. Yüklemesi tamamlanan kalemler beyaza döner. {f2VhI6UgHBc}
- Stok ek özellik tanımları (lisansta Stok 2 modülü gerekir): başlık > detay > alt detay; tip çoktan seçmeli veya "stoktan seç" olabilir, "boş geçilemesin" seçeneği var. Stok kartında özel ayarlar 2 > ek özellikler alanından bağlanır; alınan sipariş ve verilen teklifte stok seçilince seçim ekranı açılır. {xBfxAjnVswU}
- Ek kesinti (ör. stopaj): genel ayarlar > fatura ayarları > ek kesintiler. Kaynak alan ara toplam, genel toplam veya formül olabilir; oran veya sabit tutar ile alış/satış muhasebe kodları girilir. Faturada "ek kesintiler" > "sabitlerden güncelle" ile uygulanır ve muhasebe fişine yansır. {VmulwJaLovY}

### Fiyat, iskonto ve formül
- Formül tanımları: hareket bazlı sayısal özel alanlar (tam sayı/ondalıklı) açılır; formül tanımlarında Shift+Space ile alan listesi açılıp örneğin en × boy = miktar tanımlanır. Sonuç miktar veya özel iskonto alanına yazılır. {Zflv7knhbfk}
- Gelişmiş fiyat sistemi: stok ayarları > genel > "gelişmiş fiyat sistemi kullan". Puanlama ile aynı cari birden fazla listeye giriyorsa hangi kriterin (grup, il vb.) öncelikli olduğu belirlenir; cari koduyla yapılmış liste her zaman önceliklidir. Sonrasında çakışmada "seçilecek fiyat" kuralı uygulanır. Program yeniden açılınca "satış fiyat liste tanımları" gelir: liste adı, hesap, durum aktif, tarih ve şube; cari kriterleri (kod, grup, ülke/il/ilçe) ve birim bazında stok fiyatları (Excel'den aktarım). {uoZ97FQG_ZI}
- Gelişmiş iskonto sistemi açılınca stok kartındaki iskonto oranları geçersiz olur. İskonto tanımları cari (kod/grup/il, boşsa tümü) ve stok gruplamasına (stok, grup, marka, model) göre yapılır; miktar aralıklı veya iskonto 1-2-3 şeklinde. {9-eyCakHmZU}
- İskonto kısıtlama: personel bazında, isteğe bağlı cari için. "Toplam tutar" tipinde belgedeki satır iskontolarının ortalaması sınırı geçemez; "hareket bazında" her satır için ayrı sınır. Stok, grup, marka veya modele göre azami oran verilir. {34FuQfUtetg}

## e-Belge (e-Fatura, e-Arşiv, e-Müstahsil)

- e-Fatura opsiyonel alanlar: UBL standardında olmayan alanlar (özel alanlar, iskonto 2 vb.) e-Fatura ayarlarında opsiyonel alanlara eklenir. Fatura seviyesindeki alanlar PDF'e yansır; hareket seviyesindekiler XML'de InvoiceLine altında görülür (gönderilen XML "fatura giden" klasöründe). Ondalık hassasiyet seçilebilir. Görselde nerede görüneceği için entegratöre örnek XML ile başvurulur. {WC_13JiQESY}
- e-Müstahsil: KP e-Devlet'te e-Müstahsil işaretlenir; fatura ayarlarında "varsayılan e-Müstahsil kesintilerini yükle" ile kesintiler gelir; cari kartta e-Müstahsil kullanımı "evet" yapılır; alış faturasında kesintiler güncellenip gönderilir. {P401ZLUnNJw}
- Kamu kurumuna e-Fatura: KP şirket kaydı özel bilgilerde banka hesabı (IBAN) TR ile başlayan 26 karakter, boşluk ve tiresiz yazılır; sonra ERP kapatılıp açılır. Kurumun cari kartında hesap bilgileri > "kamu kurumu" işaretli olmalı. Faturada harcama biriminin vergi numarası seçilir. {TrEQEX9TgpI}

### e-Fatura ayarları ve gönderim
- **Gönderim akışı {Sl7oFxxyac8}:**
  1. Kontrol Paneli → şirket → e-Devlet 1'de e-Fatura/e-Arşiv açılır, e-Adres doldurulur.
  2. ERP'de e-Fatura Ayarları → Kullanıcı Bilgileri'nde entegratör (Digital Planet, EDM, İzibiz, Süper Entegratör) ile portal ve web servis bilgileri girilir → **Bağlantı Testi Yap** ([4UssohVnT0Q]).
  3. Yurt İçi Satış Faturası'nda cari seçilir (mükellefiyet görünür). "?" ile senaryo ve tip (tevkifat, istisna) değiştirilir.
  4. Kaydedince "gönderilsin mi?" sorulur. Sonra göndermek için e-Fatura Gönderimi → Seçilenleri Gönder.
- **Varsayılan sekmesi {akQtt6sZsOo}:** Yeni cari için varsayılan senaryo, gönderim tipi (kağıt/elektronik) ve hesap (TL/döviz). Ticari senaryo yalnız e-Fatura mükelleflerine uygulanır.
- **Opsiyonel alanlar {gA4X9fo5Suc}:** Fatura, hareket, irsaliye ve stok alanları XML'e eklenir (ör. cari kodu, hareket açıklaması, seri/lot, garanti tarihi). Tasarımda görünmesi için entegratörle görüşülür.
- **Mail sekmesi {Xdcwnc_KtDU}:** e-Arşiv maili için önce Kontrol Paneli'nde mail sunucusu tanımlanır. Alıcı cari, yetkili ya da departman olabilir; şablon seçilir.
- **e-Müstahsil {mRY2tYZYOjg}:** Kontrol Paneli'nde e-Müstahsil açılır. Alış faturasında cari seçilince e-MM olarak gelir. Kesintiler "Ek Kesintiler"den eklenip "sabitleri güncelle" yapılır. Kesinti oranı ve uluslararası kodu Genel Ayarlar → Fatura Ayarları → Ek Kesintiler'de tanımlanır.
- e-Fatura ayarları (WOLVOX ERP):
  - Belge içeriği: ÖTV vergi kodu; not bilgisini e-Fatura/e-Müstahsile ekle; şahıs firmasında ticari unvanı ad-soyad alanına aktar; alıcı adresini carinin açık adresine aktar.
  - Numara ve ekler: gönderimden sonra fatura no'yu portal numarasıyla güncelle; gönderilen PDF'i belgenin dosyalarına ekle.
  - Gönderim: kayıtta otomatik gönderim (onaya bağlı); portala taslak kaydetme (yalnız EDM); gönderim bilgilerini cari kart yerine fatura kartından al; kapalı fatura bilgisini ekle; e-Arşiv mail sistemi (yalnız İzibiz); nota eklenecek kur (güncel kur veya belgedeki kur); şubeye göre gönderici posta kutusu.
  - Cari kaydında vergi no ve e-posta zorunlu tutma.
  - XML'e eklenebilen alanlar: yazıyla genel toplam, bağlı irsaliye/sipariş no, cari bakiyesi, vade, tedarikçi stok kodu. Tasarımda görünmeleri için entegratörle görüşülür.
  - Hareket fiyatları birim fiyat hassasiyetine göre yuvarlanabilir; hareket sıralaması (stok kodu/adı) seçilebilir. {yYkXg_TYA4k}

### e-Fatura tipleri
- **İstisna {jQVSl87eBi8}:** Satırda KDV 0 yapılıp istisna kodu seçilir. **Kod stok kartına kaydedilirse otomatik gelir.** Sonra "?" → İstisna Faturası.
- **Tevkifat {gwO4xkYSP9Y}:** Satırda oran ve kod girilir (görünmüyorsa butonla eklenir). **Stok kartında satış ve alış tevkifat kodu/oranı** girilirse otomatik gelir. "?" → Tevkifat Faturası.
- **e-İhracat {wrsf0qDMDtM}:**
  - Sayaç: "e-İhracat No", şablon kodu **IHR**.
  - Cari: ülke yurt dışı, **vergi no 2222222222 (on tane 2)**. Hesap bilgileri → e-Fatura kullan, senaryo **İhracat**, hesap döviz ve "döviz hesabı kullan".
  - Stok: Özel Ayarlar 2'de **GTİP no**.
  - Faturada teslim ve ödeme ülkesi/ili/ilçesi, **taşıma şekli** doldurulur.

## Üretim (basit üretim ve MRP II)

### Basit üretim
- **Eksiye düşen stokları otomatik üret {vxEmnAKVgwY}:** Üretim → Tanımlar'da reçete açılır. Üretim → İşlemler → "Eksiye düşen stokları otomatik üret" → depo → filtrele → Otomatik Üret. Arka planda sürekli çalışması için Özel Ayarlar → Üretim Modülü'nde açılır.
- Normal reçete: üretilecek ürün seçilir. Üretim kodu otomatik verilebilir (genel ayarlar > basit üretim). Maliyet tipi (hangi fiyat), planlama miktarı, diğer maliyetler, hesap türü, "stok bloke" (planlamada hammaddeyi bloke eder) ve "şubelerde ortak kullan" var. Hammaddeler 1 birim mamul için miktar ve fire ile girilir; işçilik/hizmet ve paket eklenebilir. {O-TQbDP99tY}
- Normal üretim: reçete seçilir, üretim miktarı girilir, "maliyet hesapla" ve "üretimi oluştur". Üretim planlamada reçete ve miktar seçilince hammaddeler bloke olur. {OumJTUAU-n0} {zq4PpRE5b-I}
- Parçalama reçetesi: bir ürünün parçalara ayrılması (ör. 1 kg buğday → %30 1. kalite, %30 2. kalite, %40 kepek). Tüketilen ve üretilen ürünler ile maliyet yüzdeleri girilir; parçalama üretimi tüketileni düşer, üretilenleri girer. {yhvsN97sz1g} {OEKV7irILH8}
- Eksiye düşen stokları otomatik üret: işlem tarihine kadarki envantere göre reçetesi olan eksi stoklar tek seferde üretilir. Hammadde deposu "reçete varsayılan" seçilirse depo kontrolü yapılmaz. {FT6o6rS-9d8}

### MRP II
- Tanımlar: mesai grupları (gün içi mesai saatleri, ileri tarihlere kopyalama), mola tanımları (yemek, çay), duruş tanımları (parça değişimi, elektrik/doğalgaz kesintisi), iş merkezleri (online iş merkezi için personel yetkisi), operasyonlar (tedarik, iç operasyon veya fason), makineler (mesai, elektrik tüketimi, personel, işlenebilen stoklar, periyodik bakım takibi). {he8joOQCcKE}
- Reçete: üretim emri altında mamul, yarı mamuller (başka reçeteden de) ve hammaddeler; miktar, fire oranı/miktarı, depo ve maliyet tipi. Operasyon ve makine seçilip birim işleme süresi girilir; operasyona teknik resim eklenebilir, sabit geri dönüşüm tanımlanabilir. Ürün ağacı ve birim maliyet görülür. {7RUG1Xth3Ps}
- Üretim planlama: reçete seçilir, başlama tarihi zorunludur; kaydedince satın alma ve diğer maliyetler aktarılır. Sipariş "sipariş bul" ile bağlanır. Durum beklemede → planlamada → üretimde; "üretimde" olunca iş emirleri otomatik oluşur. Satın alma sekmesinde tedarik edilecek ürünler görülür. {U-4aBMY3kPI}
- İş emirleri tüm üretim için tek, makine vardiyasına göre veya saatlik oluşturulabilir. Online İş Merkezi'nden kapatılabilir. Kısmi stok entegrasyonu yapılabilir; sonuçlandırmada üretilen, kalite onaylı ve onaysız (yan ürün) miktarlar girilir. Genel ayarlardaki "iş emrini operasyon bazında kapat" kaldırılırsa üretim tek adımda sonuçlandırılır. {yfPqY3_f-sI}
- Hammadde giriş kontrol: kontrol/geliş tarihleri, stok, tedarikçi, sipariş/gelen/ölçüm miktarı, maksimum red ve onaylanmayan miktar girilir; onaylanan miktar tolerans üstündeyse durum "parti kabul" olur. Hammadde giriş raporundan izlenir. {I45HDm0uRI8}
- Fason birleştirme: cari seçilir, yarı mamuller (1 mamul için miktar, fire, maliyet tipi) ve hedef stoklar girilir; durum "üretimde" yapılınca stoktan düşen irsaliye oluşturulur. Geliş bilgileri girilip durum "tamamlandı" yapılır, stok entegrasyonu ile mamul girişi yapılır. {c4Zbe-7W-f4}
- Fason parçalama: kaynak stok ve hedef stoklar, miktarlar ve maliyet yüzdeleri; üretimde → giriş bilgileri → irsaliye → geliş bilgileri → tamamlandı → stok entegrasyonu. {DEMZwon3epc}
- Kalite kontrol: stok kartındaki kalite kontrol sekmesinde tanım, ölçüm yöntemi ve ölçüm tipi girilir (toleranslı: standart ± değer; evet/hayır: gözle kontrol). İş emirlerinin kalite kontrol alanında "kalite kontrol oluştur" ile operasyonlar seçilir, "aktif kaydı düzenle" ile üretilen/ölçülen miktar ve sonuçlar girilir. Maksimum red miktarına göre parti kabul veya parti red olur. Kalite kontrol raporundan izlenir. {hEGnjwiG8gg}
- Online İş Merkezi: KP'de kullanıcıya "Online İş Merkezi operatör" yetkisi verilir; ERP'de iş merkezi tanımında personel (ve gerekirse makine) yetkisi verilir. KP → Diğer İşlemler → Online İş Merkezi'nde sistem açılır, web servis portu ve SQL Server portu girilir. Tarayıcıdan sunucu IP:port ile girilir, şirket ve çalışma yılı seçilir. Personel iş merkezini seçer; bekleyen/aktif/tamamlanan operasyonları görür, operasyonu başlatır, durdurur, bitirir. Ekran üretim yüzdesini gösteren izleme panosu olarak da kullanılabilir. {egaRIjwjkZ4}
- Fason (normal, bir ürüne karşılık bir ürün): bağlı üretim kodu, fason, nakliye ve diğer maliyetler; cari; gönderilecek stok ve 1 mamul için yarı mamul miktarı (ör. 50 gönderilir, 1 mamul için 2 gerekiyorsa 25 mamul çıkar), fire ve maliyet tipi. Hedef stok miktarı otomatik gelir. Durum "üretimde" yapılır, giriş bilgilerinden gönderim irsaliyesi oluşturulur. Dönüşte geliş bilgileri girilir, durum "tamamlandı" yapılır ve stok entegrasyonu ile mamul girişi yapılır. Toplam maliyet maliyetler bölümünde görünür. {vSTGeCrUuQ4}

## Servis yönetimi

- **Servis fişi {EFrG4A5NPfs}:**
  - Cari seçilir, servise gelen ürün eklenir. Cari ve stok hareketine işlenip işlenmeyeceği seçilir.
  - Fiş bilgileri: durum, özel kod, grup, KDV oranı, geçerlilik tarihi.
  - Geliş ve teslim bilgileri; muhasebeleşince evrak tarihi ve no otomatik dolar.
  - Seri no için **Seri Garanti Takip**'e (garantiye gönder/garantiden al) buradan geçilir.
  - Ek parça, bakım sözleşmesi, arıza ve sorumlu görüşü, özel alanlar.
- **Randevu kaydı {MQLNtWfRMiE}:** Yerinde servis planlaması için. İşlem, durum (yapılacak, yapıldı, iptal), tarih ve saat, ürün (carinin ürününden ya da stoktan), seri no, araç ve personel girilir. "Servise Aktar" ile fişe dönüşür.
- **Bakım sözleşmesi {MycA6zkgXEQ}:**
  - Başlangıç ve bitiş, periyot, ücret, sorumlu ve teknik personel, sözleşmeli ürünler, verilen hizmetler.
  - Otomatik randevu için Uyarıcı/Hatırlatıcı → Servis Bakım 1 → "Periyodik bakım için servis hatırlatma kaydını otomatik oluştur" (kaç gün önce).
- **Fiş faturalandırma ve irsaliyelendirme {BMS1HOeBaCc}{zSajm0L-hD0}:**
  - Fatura veya irsaliye modülü gerekir. Varsayılan filtre "teslim edildi"; Ctrl ile çoklu seçim yapılır.
  - Yurt içi ya da yurt dışı faturası, hareket aktarma seçenekleri, depolara ayırma, kur (fiş kuru ya da aktif kur), özel alan aktarımı, tarih (fiş tarihi, bugün ya da seçilen) ve "her fişe ayrı fatura" seçilir.
  - Cari filtrelenmediyse fatura carisi seçilmelidir.
- **Tanımlar:**
  - Araç tanımları {OXCTZoNfvVE}: plaka, özel kodlar, "irsaliyede varsayılan", araca bağlı servis personeli. Personel olabilmek için cari kartında Özel Bilgiler 2'de "servis personeli" işaretlenir.
  - Fiş durum tanımları {vDsfOd5GCvI}: "servis iş yükünde yer alsın", onay tarihi kontrolü, durum değiştirme yetkisi, sıra no.
- **Servis formu sekmeleri** {gh0HACvzL0Q}{t0Av8FsO4Vo}{S6rnTjAlTn0}{yMKp6f-8irk}{U4KHlFGKhlk}:
  - Arıza: tasarımda tablo "Servis Raporları → Fiş Yazdırma".
  - Bağlantılar: tekliften "teklifi servise aktar".
  - CRM: proje ve kampanya kodu.
  - **Dış Servis:** ürün başka firmada onarılıyorsa firma, gidiş ve dönüş tarihi ve evrak no, **ödenen ücret** ve **müşteriye yansıtılan ücret** (fark = kâr). Toplam harekete aktarılabilir.
- **Bakım sözleşmesi {C-KDp6zT7eE}:** Sözleşme no'nun otomatik verilmesi Genel Ayarlar → Servis Ayarları → Randevu ve Bakım'dadır. Periyot gün, hafta, ay ya da yıl olabilir. İşlem kodları Servis → Tanımlar → İşlem Tanımları'nda tanımlanır.
- **Servis formu** {lO4aHhQ6dEU}{uPNKYa9BXa4}{s4YA90Mcdnk}{qPseoRg-BgY}{LkoFSJYcUQM}:
  - Cari adres tanımı (birden fazla adres için Cari 2 gerekir). Cari ve stok hareketine işlenme; varsayılanı Genel Ayarlar → Servis Ayarları'ndadır.
  - Fiş Bilgileri: otomatik fiş no (Genel Ayarlar → Servis). Grup (Servis → Tanımlar → Servis Grubu). Durumlar: beklemede, işleme girdi, işlem tamam, teslim edildi, iptal ve özel durumlar. KDV, geçerlilik tarihi, geliş ve teslim bilgileri, döviz ve hesap, muhasebe evrak bilgisi, varsayılan depo.
  - **Ürün Bilgileri:** Cari kartındaki "Servis Bilgileri" otomatik dolar. **Aynı seri no'lu önceki fişler** listelenebilir. Seri no garanti takibi, garanti durumu, ürün tanımları (Servis → Ürün Tanımları), marka ve model, servis ve cari özel alanlarının eşleşmesi. 2. sekmede ek parçalar ve bakım sözleşmesi bağlantısı.
- **Randevu kaydı (ayrıntılı) {56AFDhnUg0s}:** Hatırlatma Uyarıcı/Hatırlatıcı Ayarları → Servis Randevu'dan (saat) açılır. Personel eklenirken **araç iş yükü** penceresi açılır. Kayıt "Servise Aktar" ile fişe gider.
- Servis randevu kaydı: gelişmiş cari aramada servis bilgilerine (cari karttaki ürünler) göre arama yapılır. İşlemler, arıza bilgisi ve sorumlu görüşü girilir; servis aracı/personel seçilebilir. "Servise aktar" ile servis fişine dönüşür, yazdırılabilir. {uWBjmtmOz-c}
- Bakım sözleşmesi: cari ve sözleşmeye konu ürünler, başlangıç/bitiş, periyot (gün/hafta/ay/yıl), bakım ücreti, sorumlu ve teknik personel. Sonraki bakım tarihi otomatik hesaplanır; sözleşme randevu kaydıyla eşleşip servis fişine aktarılır. Numara otomatik verilebilir (servis ayarları). {LPiA4SvhIjE}
- Servis fişi muhasebeleştirme: durumu "teslim edildi" olan fişler (başka durumlar da seçilebilir) toplu olarak irsaliye veya faturaya aktarılır. Fatura carisi, "farklı depoları ayır", kaynak döviz kuru ve özel alan eşleştirmesi ayarlanır. {BmWf46Rk1AU}
- Servis fişi ön tanımları: işlem tanımları (kod, açıklama, ücret), faturalama için hizmet kartları, ürün tanımları (veya mevcut stoklar), marka/model ve fiş durum tanımları ("servis iş yükünde yer alsın", onay tarihi kontrolü). {TiZeYiYYUm4}
- Servis fişinde cari/stok hareketi işleme seçenekleri, fiş no (servis ayarlarında otomatik), fiş durumu, geliş/teslim bilgileri (teslim alan, cari kartta "servis personeli" işaretli bir cari olmalı), ürün bilgisi (cari servis bilgisinden, stoktan veya seri no ile geçmiş fişler), ek parçalar ve bakım sözleşmesi bağlantısı. Diğer alanlar: arıza/sorumlu görüşü, yapılan işlemler ve personel (başlangıç/bitiş), servis aracı ve dış servis carisi. Giriş ve teslim tutanağı yazdırılır; durum değişince müşteriye otomatik SMS/e-posta gidebilir. {TiZeYiYYUm4}
- İşlem tanımları: kod, tanım, sabit ücret (değişkense boş bırakılır) ve hizmet kodu eşleşmesi. Servis grup tanımları ve ürün tanımları (cari kartın servis bilgilerinde de kullanılır). {WN2w42pOPZM} {9RwvRNre66w} {V1p19rPiLVk}
- Raporlar:
  - Araç iş yükü: servis ayarlarında "araç iş yükü sistemi kullan" ve özel alan seçimleri gerekir. Toplam saat = stok kartındaki montaj süresi özel alanı + siparişteki ek süre; siparişte ek bilgiler 1'de araç seçilmiş olmalıdır. {M2FwSIb8DqU}
  - Cari servis tanımlar listesi. {wkYrxsCsoUY}
  - Fiş raporu ve hareketli fiş raporu (işlemleriyle; SMS ve detaylı yazdırma). {vGaIDUSfJrE} {PH4CiTuLX4E}
  - Hizmet raporu: yalnız faturaya aktarılmış fişlerdeki hizmetleri sayar. {fBUJteNH9LY}
  - Personel iş yükü: servis işlemlerinde personel, süre ve ücret girilmiş olmalıdır. {NnI-tftIEts}
  - Servis analizi (cari bazında servis sayısı, son servis tarihi ve geçen gün; toplu SMS). {VCP2j-EjZuo}
  - Bakım sözleşme listesi (toplu mail/SMS). {UCC81Qx58wM}
  - Servis özel rapor (seçilen alanlara göre gruplayıp saat, ücret ve iş adedi toplamı). {99K1FoFs74g}
- Servis paket tanımları: bir pakete stoklar ve yapılacak işlemler eklenir (ör. asansör bakım paketi). Paket servis fişine eklenince stoklar stok kısmına, işlemler işlemler alanına düşer. Paket kopyalanabilir. {w56BobECxyc}
- Servis fişi İşlemler menüsünden "faturaya aktar / irsaliyeye aktar" ile tek tek faturalanabilir. {O8yW0kytArU}
- Servis işlemleri sekmesi: süre (saat), saatlik ücret veya işlem ücreti, açıklama, başlangıç/bitiş, hizmet kodu. Ücret toplamının harekete aktarımı özel ayarlar > servis ayarlarından (hizmet tanımı, bağımsız hareket veya işlem tanımı) belirlenir. Araç plakasındaki personel aktarılabilir. {TCE19-MblSE}
- Servis marka/model tanımları: marka eklenir, sağ tarafta o markaya modeller eklenir; "bul" ile aranıp düzenlenir. {UT2nSNJD4qc}

## CRM

- **Anket tanımları {dO4SL0WM1X4}:** Kod, ad, hangi şubelerde kullanılacağı, durum, sorular ve cevaplar. Toplu cevap analizi yapılabilir.
- **Kampanya tanımları {ziosPV3fc2s}:** Kod, ad, tip (ilan, direkt satış, seminer, konferans, fuar), tarih aralığı, durum. Tahmini ve gerçek bütçe, geri dönüş, gelir ve geri kazanım girilir. Kampanya satışlarda seçilip sonuçları izlenir.
- **Proje ve satış takibi {ANK5tT-4U-Y}:** Potansiyel müşteri ya da cari seçilir. Proje kodu, sorumlu personeller, durum, satış kanalı, tahmini tutar ve **satış olasılığı**, teslim tarihi girilir. Kampanyaya bağlanabilir. Bayi satışları bayi carisi üzerinden raporlanır.
- Aktivite kaydı: cari, konu, aktivite sahibi ve tipi, başlangıç/bitiş zamanı; "alarm aktif" ile belirtilen dakika önce uyarı; tekrarlamalı randevu. Ajandada gün/hafta/ay görünümü var; tarihe çift tıkla aktivite açılır. {Sn2n5nT7H_w}
- CRM ekranında cari kartlar, yetkililer, otel müşterisi (WOLVOX Otel destek kayıtları), kampanyalar (hedef kitleye cari ekleme), proje ve satış takip, destek kayıtları ve servis fişleri izlenir. {UF4SrvZjSwg}
- CRM özel ayarlarında "CRM ajandayı randevu paneli olarak kullan", "ajandada sadece aktif personeller", "grupları ağaç olarak göster" ve varsayılan aktivite tipi var. {UF4SrvZjSwg}
- CRM raporlarında (ör. en çok satılan ürünler) listeye cari/stok/fatura alanları eklenebilir; "kullanılan SQL cümlesi" sekmesi oluşan SQL'i gösterir. Filtre "özel tanım kaydet/yükle" ile saklanır, "CRM liste" ile sonuçtan CRM cari listesi yapılır; sağ tık ile Excel/HTML/XML'e aktarılır. {xKC3oeaib4g}
- Ajanda ekranı: gün/hafta/ay; saate çift tıklayınca aktivite açılır. Aktivite kodu, konu, öncelik, tip (ör. toplantı), durum (yapılacak, beklemede, tamamlandı, ertelendi, iptal), aktivite sahibi, tarih-saat, alarm, açıklama; ilgili cari, kampanya, proje/satış ve müşteri destek kaydı bağlanabilir. {tOHaqXaeDN4}

### CRM tanımları {K9yZNExMae8}
- **Müşteri listeleri:** kampanya, proje ve aktivitelerde kullanılacak cari grupları.
- **Aktivite tipi ve aktivite durumu** tanımları (ör. işyeri ziyareti: beklemede, planlandı, yapıldı).
- **Müşteri desteği için:** destek durumu (varsayılanlar çözüldü, cevaplandı, yeni mesaj), destek önceliği, destek tipi (soru, problem, diğer), bildirim şekli.
- **CRM sektör tanımları** (cari kartındaki CRM alanı için). **Proje ve satış durum tanımları.**

## Genel Muhasebe

- **Enflasyon muhasebesi {Fv6AbUuPSA0}:**
  - GM Genel Ayarlar → Ayarlar 2 → "Enflasyon muhasebe sistemi kullan".
  - Hesap planında enflasyon hesap tipi, düzeltme ve fark hesap kodları girilir; varsayılanlar "Enflasyon İşlemleri"nden aktarılabilir.
  - Düzeltmeden önce **522, 523, 524, 570, 580, 590 ve 591** hesapları sıfırlanır.
  - Yİ-ÜFE endeksi **"Webden Al"** ile alınır.
  - **Düzeltme tablosu:** hesap seçilir → "Düzeltme ekle" (esas, basit ortalama ya da hareketli ortalama yöntem) → **YMY fişi oluştur**.
  - Stoklar için "stok toplu enflasyon hesaplama" kullanılır.
  - Demirbaşta kayıt içinde "Enflasyon muhasebesi uygula" ve düzeltme, fark ve amortisman hesap kodları girilir. GM'de sabit kıymet düzeltmesi yapılır (toplu da yapılabilir; kayıtsız kıymetler için manuel).
  - Son adımda **698** hesabı "Hesapların kapatılması" ile kapatılır.
  - Bilançoda "Enflasyon fişleri dahil" seçilince düzeltilmiş bilanço alınır.

## Mobil Satış (PDA) ve Mobile Server

- **Kurulum ve bağlantı {HTy-Be8fxS8}:** Sunucu IP'si `ipconfig` ile öğrenilir. Cihaz tarayıcısında `IP:port` açılır, Mobil Satış APK'si indirilir ve kurulur. Uygulamada Host, Port ve **şirket kodu** girilir → pazarlamacı şifresi → "Merkezden Veri Al".
- **Anlık veri gönderimi {CsbTkRf-1iE}:** Mobil Server → PDA Ayarları → **Genel 2**'de hangi kayıtların gönderileceği seçilir: fatura, cari, irsaliye, sipariş, cari hareket, tahsilat, tediye. İnternet gerekir. **Merkeze gönderilen fatura cihazda artık düzenlenemez.**
- **Belge tarih kontrolü {Nze32eSGnzo}:** Genel 2 → "Belge tarihini günün tarihiyle sunucudan kontrol et". İleri ve geri tarihli belge girişini engeller.
- **e-Fatura/e-İrsaliye {YTYHeOGTNGU}:** Kontrol Paneli'ndeki otomatik gönderim ayarı aynı zamanda ERP'deki gönderim kuyruğunun sıklığını belirler. Cihazda gönderim tipi seçilir: yok / kuyruğa ekle / hemen / kullanıcı onaylı (Bilgi Bankası 3349).
- **Etiket {9W6CFIV4Xv0}:** İki yol var: Mobil Server'ın bağlı olduğu PC yazıcısı ya da mobil yazıcı. Mobil yazıcı için PRN dosyası cihaza kopyalanır. Stok → Fiyat Göster → etiket yazdır.
- **Rota {tTtMeCBkFto}:**
  - Rota grubu tanımlanır. Cari kartında Özel Bilgiler 1'e rota grubu ve sıklığı, Özel Bilgiler 2'ye pazarlamacı girilir.
  - Rota planına tarih, pazarlamacı, **araç plakası** ve müşteriler girilir.
  - Cihazda: rota başlat (**çıkış km**'si girilir) → müşteri seçmeden fatura kesilemez → ziyaret bitir → rota bitir → merkeze gönder.
  - Raporlar: Cari Rota Raporu, **Rota Sonuç Raporu**.
- **Sevkiyat planlama {HMIdmf1udyg}:** Pazarlamacıya yetki verilir. ERP'de "beklemede" durumlu plan açılır. Cihazda İrsaliye → Sevkiyat Planlama (Yükleme): barkodla ya da elle yükleme → kaydet → gönder. ERP'de yüklenen miktar görülür; durum "tamamlandı" yapılınca irsaliye oluşur.
- **Stok fiyatı değiştirme {7-06EcJsKPk}:** Kasa, POS ve Filtre Tanımları'nda "stok fiyatını görebilsin/değiştirebilsin" yetkisi verilir. Cihazda Stok Listesi → Stok fiyatı güncelle (TL ya da döviz) → gönder.
- **Sayım {zmuxPkfeJ94}:** ERP'de PDA Stok Sayım Listesi'nde görünür. Stok Sayım ve Düzenleme'de depo seçilir → Düzenlemeye Başla → **"Stok sayım listesinden aktar"** → hareketlere işle ya da muhasebeleştir.
- **Transfer irsaliyesi {iO6iHrYMJYI}:** Yetki verilir. Cihazda cari olarak şubenin carisi seçilir. Bilgiler → Transfer'de hedef şube, kaynak ve hedef depo girilir.
- Rota grupları tanımlanır; cari kartı özel bilgiler 1'de rota grubu, sırası, kodu ve ziyaret sıklığı girilir. Rota planında tarih, rota grubu, plasiyer ve araç plakası seçilip müşteriler aktarılır; plan kopyalanabilir. Mobile Server'da yetkili > kasa, POS ve filtre tanımlarında personelin rota grupları seçilir. Veri aktarımından sonra PDA'da "rota başlat/bitir" (kilometre) ve "rotam" menüleri açılır; başlangıç/bitiş bilgileri ERP'ye döner. {bOZ0TZxBC2A}
- Pazarlamacı tanımı: ERP'de cari kart açılır; ad-soyad ile özel bilgiler 2'de "pazarlama sistemini kullan" ve PDA şifresi zorunludur. Mobile Server'da yetkili > kasa, POS ve filtre tanımlarında pazarlamacı seçilip ayarlanır: şube, cari görünürlüğü (bakiye görsün/görmesin), kasa/banka/POS, işlem yetkileri, görebileceği stoklar ve depo, varsayılan depo ve eski kayıt gönderimi. Sonra pazarlamacı PDA'dan veri alır. {_DwSwNoOR8g}
- PDA ayarları (Mobile Server > yetkili > PDA ayarları): çoklu stok seçimi, ağırlıklı barkodu dikkate alma, aynı ürünü tek satırda birleştirme, ürün seçince miktar/fiyat penceresi, cari seçince bakiye gösterme, dövizli caride işlemleri dövizle yapma, barkod okutunca miktar sorma, kullanılabilir miktar (depo modülüyle), stok miktarı uyarısı, cari limit aşımını engelleme, GPS konum kontrolü. Fatura, cari, irsaliye, sipariş ve tahsilatta merkeze anında gönderim sorulabilir; ileri/geçmiş tarihli işlem kontrolü yapılabilir. {9bK0VwBVysM}
- PDA'da depo transferi: Mobile Server'da pazarlamacıya "depo transferi yapabilsin/silebilsin" yetkisi verilir, PDA merkezden veri alır; stok > depo transferinde kaynak/hedef depo seçilip barkod okutulur, kaydedilir ve senkronizasyonla merkeze gönderilir. {lpJN4IPO44M}

## vMobile / WebConnect

- WOLVOX vMobile (videoda WebConnect) Installer'dan kurulur, şirket seçilir; KP kullanıcısıyla tarayıcıdan girilir. Dışarıdan erişim için statik IP ve modemde port yönlendirme gerekir; adres "statikIP:port" şeklindedir, port programın port ayarlarından değiştirilir. Telefon/tablet tarayıcısından kullanılır. {9eZV-dvRMks}
- Kurulum: WOLVOX Installer'dan indirilir, yetkili kullanıcıyla şirket ve çalışma yılı seçilir. Dışarıdan erişim için modemde 8888 portu açılır (videodaki varsayılan; kurulumda farklı olabilir). Menüler: stok, satın alma, satış, servis, finans, CRM, Restoran, yetkili. {rkyoVI1db4A}

## Hızlı Satış

- **Özel ayarlar** (Yetkili → Özel Tanımlar → Özel Ayarlar):
  - Aktif kasa ve depo {4CskW6K1HtQ}.
  - Otomatik fiş yazdırma: yazdır / önizle / yok {JGGTO4QI-oE}.
  - Nakitte **para üstü hesaplama penceresi** {v958aC1KSU4}.
  - Sayaçlar: satış ve iade faturası, irsaliye, cari, stok, cari hareket {5UfLhBLnEVg}.
- **Basit görünüm tasarım modu:** Sağdaki üç çizgiyle açılır.
  - Ödeme butonlarına ödeme tanımı atanır {wn--m7oNSNg}.
  - "Öğe ekle" ile stok, cari, pazarlamacı, hizmet ya da program butonu kısayolu eklenir {rzlcHAU1zJE}.
- **Bekletme {zIjmOWkGqb4}:** Satış beklemeye alınır. "Bekleme listesini veritabanında sakla" açıksa liste online (veritabanında), kapalıysa offline (program klasöründe dosyada) tutulur.
- **İşlemler:**
  - Değişim {FMoDPi_uGZM}: günün satışlarından ürün seçilir, iade ödeme türü ve yeni ürün seçilir, fark tahsil edilir.
  - İade {jU_VrqPwQWs}.
  - Kasa menüsü {QLafQvn-TuQ}: gelir/gider, kasa-banka, kasadan kasaya, kasa toplamları ve sayım.
  - Stok menüsü {oWwBwdhlsSc}: stok ve hizmet tanımı, değişim fişi; etiket için Kartoteks modülü gerekir.
- **PAVO N86 ile:**
  - Cari tahsilat {p6uUUeu65cs}: İşlemler → Cari → Cari Tahsilat → tutar → **"ÖKC tahsilatı yap"** → fatura seçilir → cihaza gönderilir.
- PAVO N86: lisansta Hızlı Satış, stok, cari, kasa, fatura ve e-Fatura/e-Arşiv gerekir. KP e-Devlet 1'de (ve şube kaydında) "Android yeni nesil ÖKC entegrasyonu kullan" ve "PAVO N86 entegrasyonu kullan" açılır. Hızlı Satış → Yetkili → Özel Ayarlar → Entegrasyon Ayarları → PAVO N86'da şubeye cihaz tanımlanır (ad, seri no, IP) ve personel atanır. Cihazda harici entegrasyon REST seçilip "cihaz eşleştir" yapılır; nakit/POS ödemeleri cihaza gider. {vpL1TKWo-Yk}
- Veresiye: cari seçilip ödeme alınmadan "işlem tamamla" ile satış cariye borç olarak işlenir. {EIQmMiriqmU}
- Gün sonu raporu sekmeleri: fişler ve içerikleri, veresiye fişleri, cari borç/tahsilat dağılımı, kasa hareketleri, ürün satışları ve miktar toplamları, ürün gruplarına göre satışlar, satılmayan ürünler, iptal raporu, personel satış dağılımı, pazarlamacı satışları, kredi kartı/POS satışları, ürün grubuna göre iadeler. {I5wNClXVOpE}

### Genel ve özel ayarlar
- Online sunucu-istemci kurulumunda "fatura kayıtlarını sunucu üzerinde yap" seçeneği kayıtların istemcide değil sunucuda oluşmasını sağlar. {dbqhw7AdPoc}
- Diğer ayarlar: tam ekran kilidi (kasiyerin Windows'a çıkmasını engeller), detaylı gün sonu (vardiya bazlı), iskontonun KDV sonrası uygulanması. {dbqhw7AdPoc}
- Boştayken belli saniye sonra imleci barkod alanına götürme, varsayılan pazarlamacı, "fatura kayıtlarını sunucu üzerinde yap" (uzak bağlantıda hız), 3. döviz gösterimi, cari bakiyesi gösterimi, açılışta tam ekran ve kilitli. {phzNkwhsFPE}
- Kontroller: stok ve cari limit kontrolü (ERP'deki limitler), belirli cari grubunda borç bakiye kontrolü, kara liste kontrolü, fiyatsız ürün uyarısı, alış altı satış kontrolü, manuel birim girişini engelleme, veresiyede vade kontrolü. {phzNkwhsFPE}
- Açık hesaba satışları ERP'ye irsaliye olarak kaydetme; varsayılan depo/kasa ve genel müşteri cari kodu; miktar çarpan karakteri (ör. "5*" sonra barkod); elektronik ve online terazi; basit görünüm; tutar penceresi olmadan ilk ödeme türüyle kapatma; "hızlı ayar yükle"; müşteri ekranı; Hugin FLY385/485 dinamik POS ayarları; weblink/applink. {phzNkwhsFPE}
- Çekmece: Özel Ayarlar → Entegrasyon Ayarları → Çekmece Ayarları'nda "satış öncesi veya sonrası çekmece açma işlemini kullan" açılır ve çekmecenin bağlı olduğu yazıcı seçilir; satış tamamlanınca fiş yazıcısı üzerinden çekmece tetiklenir. {664L9v4KT3M}

### Genel kullanım ve görünümler
- Hızlı Satış, ERP ile aynı veritabanını kullanır; depo ve kasa önce ERP'de tanımlanmalıdır. Farklı satış ekranı görünümleri özel ayarlar > satış iade görünüm > "hızlı ayar yükle" ile seçilir. Genel müşteri carisi şube bazında ayrı atanabilir. {pZvrlnfqx1U}
- Ürün listesi (hızlı butonlar) sağ tık > dizayn ile gruplar ve ürünler eklenerek hazırlanır; ERP paketleri de eklenebilir. Ödeme butonları da sağ tık > dizayn > ödeme ekle ile tanımlanır; bankada birden fazla POS varsa ödeme sırasında POS seçtirilir. Diğer özellikler: fiyat gör, bekleme listesi, fiş bilgileri (manuel fatura no, KDV durumu, vade, not), veresiye hızlı kapatma, vade farkı tablosu, tablo yerleşimini kaydetme, KDV sonrası iskonto ile yuvarlama, birden fazla ödeme türüyle tahsilat. {pZvrlnfqx1U}
- Basit ekran: özel ayarlar > görünüm ayarlarında "basit görünüm" işaretlenir. Design modunda gruplara sağ tık > öğe ekle ile stok eklenir, grup adı ve sıra değiştirilir, ödeme kısayollarına işlem türü atanır. {KgoylAjaXdE}
- Tema seçimi (özel ayarlar > görünüm > tema ayarları) yalnızca basit görünümde çalışır; uygulanınca program yeniden başlar. {9q09cc_vwT4}

## Restoran

- **PAVO N86 entegrasyonu {ocpcRrD25nQ}:**
  - Lisans: Restoran (veya Lite), Stok, Cari, Kasa, Fatura ve e-Fatura/e-Arşiv. P2P entegrasyon için ayrıca **Restoran PDA**.
  - Kontrol Paneli → şirket (şube varsa şube kaydı da) → e-Devlet 1 → "Android yeni nesil yazarkasa entegrasyonu kullan" + "Pavo N86 entegrasyonu kullan".
  - Restoranda Menü → Program Ayarları → Yazarkasa Entegrasyonu → Pavo N86 (VUK 507) → Pavo cihaz tanımı:
    1. Şube seçilir, **access token** alınır.
    2. "+" ile cihaz eklenir: entegrasyon tipi **REST**, ad, seri no ve IP girilir.
    3. **Personel ataması** yapılır.
  - Cihazda Ayarlar → Satış Uygulamaları → Harici Entegrasyonlar → REST seçilir, sonra "Cihaz Eşleştir".
- **PAVO işlemleri:**
  - Veresiye/açık hesap/avans {NuzRY7Fxejw}: Pavo ayarlarındaki "veresiye hesap türü" (açık hesap ya da avans) seçilir. Adisyonda müşteri seçilip **borçlu kapat** yapılınca cihazda o türde fiş çıkar.
  - Cari tahsilat {rssHPESppr4}: Menü → Cari İşlemler → Cari Tahsilat → "ÖKC tahsilatı yap".
  - Satış iptali {wSms91uYNao}: Menü → Fatura İptal → "Pavo fatura iptal" → cihazda iade ve ödeme türü seçilir.
- Masa ve ürün: program ayarlarında masa grupları (kafe, bar, teras…), tek tek veya "toplu ekle" ile masalar (kişi sayısı, garson çağrı ID, süreli masa tarifesi, gizli, VIP). Adisyon ürün grupları oluşturulur. Ürünler ERP'de stok kartı olarak açılır (birimlere göre farklı fiyat, ör. yarım porsiyon = satış fiyatı 1). Restoran'da grup seçilip "dizayn" > "ürün ekle" ile butona bağlanır; resmi olmayan ürünler düz buton görünür. {RyetWPQ0BFA}
- Bağımsız bölümler: kafe ve restoran gibi bölümler tek veritabanında ayrılır. Program ayarları > kullanıcıya özel ayarlar > bağımsız bölümlerde bölümler tanımlanır; masa grupları, adisyon ürün grupları, personel ve garsonlar bölümlere eşlenir. Garson yalnız kendi bölümünü görür. {bjn2XZu6QKg}
- Hesap kapatma seçenekleri: program ayarları > adisyon kapatma seçenekleri; nakit, POS, evrak, dekont, bonus. Yemek/hediye çeki gibi türler ERP'de genel ayarlar > cari hareket ayarları > ek işlem türü olarak tanımlanır, Restoran yeniden açılınca gelir. "1. tanıma göre ödeme otomatik yapılsın", kasa ve POS/taksit tuşları tanımlanır (kasa/banka önce ERP'de tanımlı olmalı). Bölünmüş ödeme ve ara ödeme alınabilir. {XS6G5Vz27lg}
- Kredili ödeme / disko-bar-kulüp girişi: program ayarlarında birimler (kişi sayısı, ücret), kredili giriş fişi (barkod uzunluğu, kredi limiti, geçerlilik saati/günü, faturalama için özel kod), turnike geçiş adetleri (Veri Transferi'nin kartlı geçiş modülü lisansı gerekir; turnike ID'leri Veri Transferi'ndeki cihaz kodlarıyla aynı olmalı), ürün kredisi, raporlama grupları ve kombinasyon fiyat tablosu, paketler. Satış menü > ekranlar > disco bar kulüp giriş ekranından yapılır. {sA7HfOKjvaI}
- Kurye (paket) ekranı: masa dışı satışlar (self servis, eve servis). Caller ID entegrasyonunda arayan kayıtlıysa fiş açılır, değilse yeni cari açılır. Kullanıcıya KP'de Restoran > "kurye ekranı kullanımı" yetkisi verilir; kurye giriş/çıkışı izlenir. {IVb24QogO_k}
- Online sipariş entegrasyonları (program ayarları): QR Menü (restoran ID, e-posta/şifre, şube, ürün eşleştirme), MyFranchise (merkez cari kodu) ve MyRezzta (ödeme eşleştirme, siparişi vereni cari kaydetme, paket veya paket 2 sekmesine düşme, vale/hesap iste/garson çağır bildirimleri). Ortak ayarlar: yeni sipariş kontrol sıklığı, otomatik onayla ve mutfağa yazdır (ya da adisyon yazdır), kopya sayısı, sesli alarm. Veri transferi ayarlarında Migros Yemek IP adresi yer alıyor. {FWTzKCAwhLg}
- Hızlı adisyon ekranı düzenleme: vitrinde olmayan/olan ürünler, silinenler ve boş gruplar listelenir; toplu aktarım veya vitrinden çıkarma. Şube tanımları kopyala: kaynak şubeden hedef şube/depoya masa butonları ve grupları, masa krokisi, adisyon butonları, süreli masa tarifeleri, otomatik üretim ve tüketim ayarları kopyalanır ("kaynakta olmayanları sil" seçeneği var). {IwaBTDZLAAE}
- Adisyon ürün grupları: ana/alt grup, renk ve font, grup buton boyutu (sonra yeniden başlatma), "ürün butonlarını otomatik diz", "sayfa şeklinde göster". {2R222L-yvi0}
- Bağımsız bölümler (teras, bahçe, iç mekan): masa grubu, adisyon grubu ve personel/garson eşleştirmesiyle kullanıcıya yalnız kendi bölümü ve izinli ürün grupları gösterilir. {lJsyydr9PWY}
- Caller ID: genel ayarlarda arayan numara tanıma açılır, port Caller ID programındakiyle aynı olmalıdır. Kayıtlı numarada popup'tan adisyon açılır, kayıtsız numarada hızlı cari kaydı açılır; alan kodu ve popup süresi ayarlanır. Arama listesi ekranından fiş veya cari oluşturulur. {wlst8WvyZxk} {fRdePzYSCPQ}
- Stok detayları: menü tanımları (ana ürün + içindeki stoklar ve düşülecek miktarlar; fiş ve faturada yalnız ana ürün görünür, stok hareketlerinde içerik düşer), stok açıklama tanımları, dönüşüm tanımları (üründe "dönüşüm yap" ile alternatif ürünle değiştirme). {MZsz9d02vR0} {HcpCYgUvje4}
- Ekstra ve indirim: varsayılan ekstra (tutar/yüzde, masa geneli veya kişi başı, garson girişinde otomatik) ve yeni müşteri indirimi (varsayılan oran; kayıt günü uygulanmasın seçeneği). {B7hRKlHdlNk}
- Fiş tipleri: varsayılan müşteri, indirim oranı, para birimi, geçerli olduğu fişler (masa/paket), servis bedeli (tutar/yüzde, fiş geneli/kişi başı) ve renk (yalnız basit görünümde). Kullanım ayarlarında "adisyon açarken fiş tipi sor" işaretlenir. {qrpHpcqz7Zk}
- Hızlı stok tanımı: ERP'ye geçmeden Restoran içinden stok kartı açılır (kod/barkod otomatik, grup, birim, fiyatlar ve kâr oranı, KDV'ler, yazarkasa KDV departmanı veya "kasaya gönderme", döviz, yerli üretim). {9GCuDMsFaQ0}
- Otel entegrasyonu: genel ayarlar > Otel'de adisyon hesap kodu olarak WOLVOX Otel'de tanımlı gelir/ödeme tanımı seçilir (alkollü içecek için ayrı ya da KDV oranına göre departman). Hesap kapatırken "otel müşterisi" seçilirse tutar misafirin folyosuna aktarılır. {A0cSKU8YwQ4}
- Kurye ekranı ve avans: paket fişi kurye şifresiyle "kurye çıkışı" yapılır (paket çıktı), dönüşte teslim edildi (ödeme türü ve kasa), teslim edilemedi (adres bulunamadı, kabul edilmedi) veya iptal seçilir. Kuryeye avans, menü > ekranlar > kurye avans girişinden kasadan verilir. {DE7gEPYyqJM}
- Masa grupları ve toplu masa ekleme (ör. M2–M10). {EoDpVZQODo4}
- MyFranchise: program ayarları > AKINSOFT MyFranchise'da restoran ID (panelde firma profili), panelde "API kullanıcısı" olarak açılan kullanıcı adı/şifre, şube ve merkez cari kodu girilir. Stok aktarımı ile şablon şirketteki stoklar (yeni/güncellenen/silinen; stok tanımı, grup, fiyat, adisyon butonları, stok detayları) şubeye alınır. Şube "tedarikçi sipariş" ile merkezden ürün ister; merkez siparişi fatura/irsaliyeye aktarınca şubede "tedarikçi mal kabul"e düşer ve içe aktarılınca merkez cari adına alış faturası olur. Veriler şube tanımındaki periyotla otomatik, istenirse "verileri gönder" ile anında gönderilir. {hBqlX-mkPEg}
- Online tartı: genel ayarlarda "online tartı sistemini kullan"; asıl ayarlar Market Otomasyonu'nda yapılır, port iki tarafta aynı olmalıdır. Dara sistemi ve birden çok birim (virgülle) ayarlanır. {UHSqXfAYdCI}
- PDA Server: bu bilgisayar PDA sunucusu olarak işaretlenir; Android uygulama linki ayarın yanındaki soru işaretinde. Seçenekler: miktar sor, iptaller mutfağa hemen yazdırılsın, PDA'dan adisyon girilince otomatik fiş/mutfak çıktısı, garson yalnız kendi masalarını görsün, masa açarken kişi sayısı sor, ikinci fiş açarken numara sor, aynı masaya iki garsonun aynı anda müdahalesi. {D-eWKJ9i0Xo}
- Rezervasyon: başlangıç saati, standart rezervasyon saati, süre ve blokaj süresi, saatli/günlü gösterim, rezervasyon kişisini cari kaydetme, belirli dakika önce sesli uyarı ve tekrar, otomatik SMS hatırlatma. Rezervasyon ekranında masa atanınca süre boyunca bloke olur. {NqA-mE30ZFc}
- TSM (masada ödeme): genel ayarlar > TSM'de sistem açılır; "TSM ile birlikte ÖKC entegrasyonu" ve hesap kapanınca adisyon yazdırma seçilebilir. Cihaz (ör. VX680) seçilince cihazdaki ödeme tanımları gelir, programdaki nakit/POS/evrak türleriyle eşlenir. {uanrwXKZyHk}
- Yazıcı ayarları: adisyon yazıcısına Windows yazıcısı ve tasarım dosyası atanır; "PDA'larda adisyon yazıcı seçeneği olarak göster". Paket ve diğer sekmelere ayrı yazıcı seçilir. Yazdırma ayarlarında Türkçe karakter düzeltme, açıklamaları yazdırma, hesap kapatmada fatura/adisyon yazdır varsayılanı, garson modunda yazdırma sonrası ekranı kilitleme ve aynı ürünleri birleştirme var. Mutfak yazdırma ürün grubuna (departman) veya tek tek ürüne göre farklı yazıcılara gönderilir. {LyuS6TT5Lwg}
- Ön muhasebe / genel muhasebe entegrasyonu: sayaç ve kodlar (seçilmezse ERP varsayılanları), masa ve paket için varsayılan müşteri cari kodu, varsayılan depo veya adisyon ürün grubu / masa grubu bazında depo, tüm ürünlerin KDV'sini %20'ye çevirme. {fKskgpe0huU}
- Kartlı geçiş (Veri Transferi): disko-bar-kulüp giriş tanımları ve kredili kart işlemleri Restoran'da yapılır. Turnike bağlantısı WOLVOX Veri Transferi > Restoran > kartlı geçiş sisteminde cihaz tanımı (kod, IP, port) ile kurulur; cihaz kodu programdaki turnike koduyla aynı olmalıdır. Kartlı geçiş sistemi modülü lisansı gerekir. {ZbVH3-4VQYI}
- Adisyon kapatma seçenekleri: 10'a kadar ödeme seçeneği, varsayılan seçenek. Dekont/POS için banka modülü gerekir. "Diğer ödeme seçenekleri" butonunun içeriği seçilir. Paket ve paket 2 ödeme tanımları eşlenir. "İrsaliye cari grupları"na alınan gruptaki carilerin adisyonları kapanınca ERP'ye irsaliye olarak işlenir. {mZUH_LgYeRg}
- Görünüm ayarları: masa bölümü ve butonların gizlenmesi, masa yerleşimi (standart/basit), masa üstünde tutar gösterme, masa boyutları, masa durum renkleri (kapalı, açık, rezerve…), mutfağa yazdırılmamış ürün varsa farklı renk, garson/kullanıcı kilit ekranı görseli veya videosu ve yazısı. {SQOPXskcu6I}

### Online sipariş ve ÖKC entegrasyonları
- AKINSOFT QR Menü: web panelde kategori, ürün (birim, şube fiyatı, zamanlı indirim), ekstra seçenekler ve masalar tanımlanır. Restoran entegrasyonunda masa adları WOLVOX Restoran'daki ile birebir aynı olmalıdır. Her şubenin menü linki QR koda gömülür; siparişi hangi masanın verdiğini ayırmak için masaya özel sipariş şifresi üretilir. Restoran program ayarlarında panel kullanıcısı girilir, şube ve ürün eşleştirmesi yapılır. {68M9_Y8HRQA}
- Getir Yemek: önce Getir tarafında ürün ve opsiyonlar, Restoran'da stok açıklama tanımları hazır olmalıdır. WOLVOX Veri Transferi > Getir entegrasyonu ayarlarına API secret key ve restoran secret key girilir. Otomatik sipariş alma aralığı, restoran/kurye kapalıysa otomatik aç, genel müşteri cari kodu, normal siparişleri otomatik onay ve ileri tarihli siparişte ön onay ayarlanır. Ürün ve opsiyon eşleştirmesi Ctrl+Enter ile yapılır. Siparişler Restoran'ın online alanına sesli bildirimle düşer. {Q9S1OTn5o-4}
- Garson ekranı: garson ERP'de cari olarak açılır, özel bilgiler 2'de "garson" işaretlenir ve PDA şifresi verilir. KP'de kullanıcı açılıp Restoran yetkileri verilir; girişte garson PDA şifresiyle girer ve yalnız yetkili alanları görür. {a25iURgjxXQ}
- Disko/bar/kulüp giriş ekranı: birim tanımları satılır, kartlı sistemde karta yükleme/iade yapılır; "bakiye sıfırla" ile ön ödemeli satışlar birimlerin özel kodlarına göre gruplanıp faturalanır. {bOLVvdaC3K8}
- Yazarkasa POS entegrasyonları (Hugin T300, Olivetti MX915): Restoran'da hesap kapat veya Hızlı Satış'ta ödeme tipi seçilince işlem cihaza gider, ödeme cihazda tamamlanınca programda hesap kapanır. {8iVusSn3d-c} {mNXkuNaOhpc} {9IiceDD_q5Y}

## Yazarkasa ve terazi (Market Otomasyonu)

- **Ingenico/PAX entegrasyonu {oOnfPsNK49E}:**
  1. Lisansta Yazarkasa modülü olmalı. Cihazın yıllık kullanım ücreti **İKASA** üzerinden ödenir ve cihaza parametre yüklenir.
  2. Yazarkasa programında Ingenico seçilir → Ayarla: seri no ve IP girilir → "Uygulamayı çalıştır" (servis).
  3. "Cihazdan al" ile KDV, kısım, banka ve yemek kartı listeleri alınır. Ödeme eşleştirme yapılır.
  4. Kontrol Paneli'nde (şube varsa şubede de) "Android yeni nesil ÖKC kullan" + "yeni nesil ÖKC entegrasyonu kullan" açılır.
  5. Hızlı Satış veya Restoranda nakit/POS seçilince fiş cihaza gider.
- **Market Otomasyonu ayarları {Rss6pGPjWeA}:**
  - Ürün fiyatına KDV ekle; sıfır fiyatlı ürünleri gönderme.
  - **Gelişmiş fiyat sistemi kullan** (ERP'dekiyle birlikte açılır).
  - **Dosya sistemi kullan:** online server/client'ta gönderim dosyası sunucuda hazırlanır.
  - Terazilere stok yabancı adı gönderilebilir. Fatura, iade, e-Fatura ve e-Arşiv sayaçları seçilir.
  - Terazi PLU numarası barkoddan ya da özel kod 1/2/3'ten otomatik alınır. Cihaza gönderilecek fiyatın kaçıncı fiyat olduğu seçilir.
- **Online terazi {1zmZmwvFFpE}:**
  1. Lisansta Yazarkasa/Terazi modülü olmalı. Terazi PC'ye COM portundan bağlanır.
  2. Market Otomasyonu'nda Online Terazi → "Online tartı sistemini kullan" → COM ayarları → **"Gelen veriyi izle"** ile veri geldiği kontrol edilir.
  3. Veri geliyor ama satışa düşmüyorsa **veri deseni** ayarlanır: okuma yöntemi "özel okuma", başlangıç ve bitiş kodları (ör. `S`…`kg`, `U`…`kg`).
  4. Hızlı Satış: Özel Ayarlar → Entegrasyon → Tartım/Terazi → "Online tartı sistemini kullan" + **bildirim portu** (Market Otomasyonu'ndakiyle aynı, ör. **8891**). Restoran: Program Ayarları → Online Tartı.
  - "Test gramajı gönder" ile haberleşme denenir.
- Baster terazi: Market Otomasyonu'nda klasör seçilip "terazi ürünlerini oluştur" ile terazinin okuyacağı dosya üretilir. Stok kodu, barkod, fiyat ve yazarkasa KDV departmanı zorunludur. PLU, 27/28/29 barkod tipinden sonraki 5 hanedir. Dosya elle veya terazi firmasının ara yazılımıyla aktarılır. {j_TICrEcoSA}
- İnter MPOS 2001: dosya okuma yöntemiyle çalışır. POS kasa tanımları (yazarkasa firmasının kaydettiği kasa no, depo ve kasa), POS ve genel dizin girilir. "Ürün dosyası oluştur" / "cari dosyası oluştur" ile gönderilir (stok kodu, barkod, birim, fiyat, yazarkasa KDV departmanı zorunlu; PLU 27/28/29'dan sonraki 5 hane). "Satışları al" ile belirli tarihin satışları ERP'ye alınır. {oLZ4CgmhBog}

### Cihaz entegrasyonları
- Hugin FP300 ve FT202: cihaz seri no ve IP girilir, cihaz eşleştirme moduna alınır. "Cihazdan al" ile KDV oranları, kısımlar, kasiyerler, kredi tuşları ve fiş başlığı çekilir; ödeme tipleri eşleştirilir. Stoklarda yazarkasa KDV departmanı zorunludur. Videoya göre FT202 entegrasyonu için Hugin tarafına ayrı ücret ödeniyor (doğrulanmadı, güncelliği bilinmiyor). {C0PZv36dNiA} {f1r3puNLT38}
- BEKO 300TR: özel bağlantı kablosu için "AT" ile başlayan cihaz seri numarası AKINSOFT'a iletilir; COM port seçilir ve servis uygulaması çalıştırılır. {Dtxg9AOpXi8}
- ACLASS LS2X ve CAS LP1 v1.6 / LP1000N teraziler: yalnızca dosya ile ürün aktarımı yapılır; zorunlu alanlar stok kodu, barkod, birim, fiyat ve KDV departmanıdır. {Pge6mD-nEk0} {ar0JHD_FrZc}
- CAS CL5000: CL-Works yazılımının veritabanı kullanılır; terazi barkodunda PLU, 27/28/29 önekinden sonraki 5 hanedir. {0xxpuUN9pTo}
- Tüm yeni nesil ÖKC entegrasyonlarının ortak adımları: lisansta "yazarkasa terazi" modülü olmalı. Market Otomasyonu'nda yeni nesil ÖKC listesinden cihaz seçilir ve bağlantı (seri no, TCP/IP ya da COM/seri port) girilir. "Uygulamayı çalıştır" ile servis uygulaması açılır; "bağlantı kuruldu" logu görülünce KDV, kısım, ödeme, kasiyer, kredi tuşu ve fiş başlığı tanımları "cihazdan al" ile çekilir, ödeme türleri eşlenir. Stoklarda özel ayarlar 2 > "yazarkasa KDV departmanı" seçilmelidir; seçilmeyen stok yazarkasaya gönderilmez. KP şirket kaydı e-Devlet 1'de (şubeli ise şube kaydında da) "yeni nesil yazarkasa kullan" işaretlenir. Bundan sonra Restoran ve Hızlı Satış satışları cihaza gider. {glxhWNoAhOk} {t8wkfXqU40k} {B22Hd_pQJto} {6qjiZgD_2ng} {7vY2gkyBFEU}
- Cihaza özel notlar (videolara göre; ücret ve prosedürlerin güncelliği doğrulanmadı):
  - Hugin T300: cihaz için yıllık kullanım ücreti akinsoft.com.tr üzerinden ödenir; TCP/IP bağlantı. {glxhWNoAhOk}
  - Hugin VX675: COM port bağlantı (Aygıt Yöneticisi'ndeki port). {t8wkfXqU40k}
  - Ingenico iWE280/iDE280: ikasa.com.tr'den GMP-3 hizmeti alınır, cihaza parametre yüklenir; banka ve yemek kartı listeleri de cihazdan alınır. {B22Hd_pQJto}
  - Olivetti MX915: seri no AKINSOFT'a iletilir ve entegrasyon bedeli ödenir; servis şifresiyle cihazda IP ve GMP-3 eşleştirme yapılır; "uygulamayı çalıştır" öncesi cihaz GMP-3 eşleştirme ekranında olmalıdır. {6qjiZgD_2ng}
  - Profilo S900: entegrasyon formu doldurulup ücret yatırılır; TCP veya seri port; çalıştırmadan önce cihazda GMP-3 eşleştirme ekranı açık olmalıdır. {7vY2gkyBFEU}
- Perkon DIGI SM-100 terazi: doğrudan entegrasyon yok; "terazi ürünlerini oluştur" ile terazi yazılımına uygun ürün dosyası üretilir. Stok kodu, barkod, birim, fiyat ve yazarkasa KDV departmanı eksik olan ürün dosyaya girmez. {EQDCVJQgQjQ}

## Akaryakıt

- Akaryakıt vardiya kapama scripti: sayaç satışları, taşıt tanıma satışları ve cari satışlar listelenir; pompacıdan alınan nakit ve POS girişleri, gelir/gider, tahsilat/tediye, test satışı ve Z raporu girilir. Kapama pompacı bazındadır; fark oluşursa pompacıya yansıtılabilir. {R1WWyw2DHpk}

## İnsan Kaynakları

- **PDKS:**
  - Cihaz tanımları {_IhMgqxSewY}: işyeri, cihaz ID, tip, ad, IP ve port; aktarılan hareketleri cihazdan silme; "daha önce çekilmemiş kayıtlar / hafızadaki tüm kayıtlar"; bağlantı testi. **BioClock** tipinde Sistem bölümünden sürücü yüklenir.
  - Giriş/çıkış aktarımı {cfpxrApNGQw}: personel kartında çalışma planı ve **giriş kart numarası** girilir (bazı cihazlarda cihazdaki ID).
    - Entegre olmayan cihazda txt dosyasından alınır; Dosya Ayarları'nda kolon sıraları tanımlanır.
    - Entegre cihazda anlık alınır.
    - "İşlenmeden önce giriş/çıkış hareketlerine otomatik ayır" seçeneği, bütün okumaları "giriş" gönderen cihazlar içindir.
    - Sonunda "giriş çıkış tablosunu işle".
  - Vardiya tanımları {Tas4sUbRbY0}: başlangıç, yemek ve bitiş saatleri, ek mesai saatleri, normal ve ek mesai katsayıları, resmi tatil ve tatil vardiyası (ör. %200).
  - Mazeret izin tanımları {0CN8jma4hVg}: rapor, yıllık izin, görevlendirme, telafi… Puantaj cetvel kodu ve **ücretli/ücretsiz** bilgisi maaş hesabını etkiler.
- **Diğer İK işlemleri:**
  - İhbar ve kıdem tazminatı {1aF3ed6igVU}: son bordrodan hesaplanır ("bilgileri bordrodan al"). "Karşılıklar raporu"nda referans tarihiyle olası tazminat görülür.
  - İcra takibi {TsiYCc12NDg}: dosya ve kesinti bilgisi girilir. "Otomatik kesinti sistemini kullan" açıksa bordrolamada maaştan düşülür.
  - Görev takibi {od1p-wZXETI}.
  - Eğitim ve etkinlik takibi {EQIZ2jKnLl4}: katılımcı listesi ve katılım durumu.
- **ERP'den avans {RPcDO98FajE}:**
  - İK'da Yetkili → Genel Ayarlar → Entegrasyon → **"Avans hareketlerini ön muhasebeden çek"** açılır.
  - Personel kartında cari seçilir.
  - ERP'de bu cariye **cari tediye** girilir. Özel kod alanına avansın ait olduğu yıl ve ay yazılır. Avans personel kartına yansır.

### Muhasebe entegrasyonu ve çalışma planı
- İK'da iki ayrı muhasebe entegrasyon şablonu tanımlanabilir; SGK teşvik tutarı gelir hesabına yazılabilir. {NOrc87Ytm84} {YDI3O2HF7g4}
- Departman bazında borç/alacak muhasebe kodu verilebilir, böylece maaş gideri departmanlara ayrılır. {5sHQ0fgaQQ0}
- Ön muhasebe (ERP cari) entegrasyonunda personel carisi özel kod "maaş" gibi bir kodla ayrıştırılır. {8JAIo9AncWQ}
- Çalışma planında geç kalma/erken çıkma gibi durumlar için ceza kuralları tanımlanır. {B-ZyBZsjAQc}

### Personel takip, puantaj ve bordro
- Personel takip tanımları: vardiyalar (tatil vardiyası, resmi tatil vardiyası, fazla mesai katsayısı), çalışma planı ve yıllık çalışma takvimi, mazeret/izin tanımları (ücretli ise kesinti yüzdesi). Personel kartında varsayılan çalışma planı ve giriş kart numarası girilir. {SjQ9J-PFFUQ}
- Giriş-çıkışlar elle girilir, desteklenen cihazdan ya da dosyadan (offline) yüklenir. Online cihaz entegrasyonu için ilgili bilgisayara WOLVOX Kapı Ekranı kurulur (ayarlar F5). Aylık çalışma saati hesaplamasında genel ayarlarda 4 yöntemden biri seçilir. {SjQ9J-PFFUQ}
- Bordro sırası: yasal sabitler (iş yeri seçilip "web'den güncelle", her ay için) → personel kartında sigorta grubu, kanun no ve AGİ bilgileri → puantaj listesi (iş yerindeki tüm personele otomatik puantaj; kırmızı = o ay puantajı yok) → AGİ hesaplama (tüm aylar için bir kez) → bordro dökümünde "bordro hesapla". Bordro ve hesap pusulası yazdırılır, e-Bordro gönderilir. (Video AGİ döneminden; AGİ 2022'den itibaren kaldırıldı, bu adımı güncel sürümde doğrulayın.) {yDEUL2bnFDU}
- ERP'de verilen avansı İK'ya çekmek için İK genel ayarlar > entegrasyonda "avans hareketlerini ön muhasebeden çek" işaretlenir, personel kartı "bağlı cari kart" ile eşlenir. ERP'de cari tediyede avans girilir; hareket özel koduna ay ve yıl yazılır (ör. 01 ve 2017). {vcwFrOD4UJA}
- WOLVOX Kapı Ekranı: İK personel takip modülüyle entegre giriş-çıkış arayüzü. Giriş barkod okuyucu, klavye veya desteklenen cihazlarla (barkodlu/proximity kart, parmak izi, yüz tanıma; liste Bilgi Bankası'nda) yapılır. Ayarlar F5; içerideki personel listesi var. {B6r3t5jrDMc}
- Personel giriş-çıkış (güncel anlatım): vardiyalar, çalışma planı ve takvimi, mazeret izinleri; personel kartında varsayılan plan ve giriş kart numarası. Elle giriş, cihazdan yükleme veya anlık aktarım için Kapı Ekranı. Ücret hesabında 4 yöntem var. Gelmediği güne mazeret, giriş-çıkış raporundan çift tıklanarak atanır. {gtwFOy4M72Y}

### Online İK ve performans değerlendirme
- Online İK: İK ile entegre web arayüzü. Personel kendi kullanıcı adıyla girip giriş-çıkış, kesinti, çalışma saati ve maaş bilgisini, e-bordrosunu görür; sınav/ankete katılır, istek/öneri gönderir, belge ve duyuruları okur. Kullanıcı adı/parola personel kartı > personel takip > web arayüzü kullanıcı bilgisine girilir. KP > diğer işlemler > "Online İK personel paneli" ile açılır; internetten erişim için statik IP ve port yönlendirme gerekir. {ODyqUPTgVW8}
- Online İK giriş-çıkış sayfası ile personel bilgisayardan giriş/çıkış yapar; kayıt İK personel takibine düşer. Admin paneli (KP > diğer işlemler > Online İK admin paneli): varsayılan şirket, maaş görme ve şifre değiştirme yetkisi, yöneticilere bağlı personel yetkisi, bağlantılar, giriş-çıkış sayfasını kullanabilecek bilgisayarların IP'leri ve uzaktan erişim yetkileri. {ODyqUPTgVW8}
- 360 derece performans değerlendirme: durum aşamaları beklemede (tanım) → planlamada (personel Online İK'dan kimi değerlendireceğini seçer) → aktif (puanlama) → tamamlandı (pasif/iptal de var). Tanımda tarih, iş yeri, puan aralığı ve ağırlıklı puanlama katsayısı var. Kurallar (ör. aynı departman ve aynı statü) alan/karşılaştırma/"personel kartından al" ile kurulur; soru grupları hedef kitle kuralıyla belirli departmanlara yöneltilir; puan ağırlıkları tanımlanır. Online İK admin panelinde "performans değerlendirme personel seçimi/puanlama" yetkileri açılmalıdır. {hdS8cIQFK4Q}

## Otel

- **Özel ayarlar {XLrTShQM7KM}** (kullanıcı bazlı):
  - Hata gösterimi sistem mesajı mı özel mesaj mı; font; ekrana sığdırma.
  - **Kapı kilit entegrasyonu:** Kale, Makfa, Brasco.
  - Folyoda gizlenecek hesap departmanları.
  - Kayan alt bilgi şeridi: doğum günleri, check-in/out sayıları, kurlar.
  - AKBS; rezervasyon ve check-in'de otomatik SMS.
- **AKBS {E6XdPjBkzdg}{CI0UEPTj4es}:**
  1. Özel Ayarlar → Anlık Kimlik Bildirimi → "EGM/Jandarma AKBS kullan" → "AKBS uygulamasını çalıştır" → ayarlara EGM/Jandarma kullanıcı adı, şifre ve TCKN girilir.
  2. Rezervasyonda ad, soyad, TCKN, seri no, doğum tarihi, il ve ilçe dolu olmalı.
  3. Check-in sonrası İşlemler → **AKBS Giriş İşlemi**. Mobil uygulamadan gelen şifre girilir, bildirimler "aktarım logları"na düşer.
  4. Check-out'ta İşlemler → **AKBS Çıkış İşlemi**.
  - 9.02.01'den beri otomatik bildirim ayarı var (Bilgi Bankası 3820).
- **Gün sonu {vy12KzED4sw}:** Gün sonu raporu → önce **Room Posting** (oda ve folyo ücretleri işlenir, rezervasyon durumları kontrol edilir) → rapor → **Gün Sonu Yap**. Sistem tarihi bir gün ilerler. Ayar Genel Ayarlar → Rezervasyon sekmesindedir.
- **Forecast raporları {acfSanoxzQo}{94XQpF5y42I}:**
  - Oda, kişi ve oda geliri grafikleri; boş oda, yetişkin ve çocuk sayıları; günlük liste; uyruk raporu; genel forecast (toplam, dolu, arızalı, satılabilir oda).
  - Tarih bazında durum (departman geliri ve ödemeler), tarife/kontrat bazlı durum, konaklama özel raporu, oda tipi forecast, ülke bazlı forecast.
- **CRM {k_RMuA-eR5k}:** Anket kaydı (sorular ve cevaplar, yazdırılabilir) ve anket girişi (ERP carisine ya da otel müşterisine bağlanır). **Servis kaydı** ile havalimanı transferi gibi ulaşım personele atanır.
- Oda tanımları: oda kayıtları, oda tipi, yatak tipi, blok ve manzara tanımları. "Hızlı oda kayıt" ile numara aralığı toplu açılır. Arıza tarihleri arasında oda rezervasyona kapanır. {MxWUxVrwFJ8}
- Kontrat: para birimi, çocuk grupları ve dönem geçişinde fiyat hesabı (her dönem ayrı / giriş dönemi / çıkış dönemi). Dönemlerde oda başı veya kişi başı fiyat, pansiyon tipi, çocuk yaş grubu ve ek yatak fiyatı, kurallar (geçerli günler, KDV), ekstra/indirimler ve erken rezervasyon fiyatı tanımlanır. Dönem aksiyonları: ör. "10 gün kal 9 öde" veya belirli gün üzeri yüzde/tutar indirimi. {1pAuZpO3e7o}
- Ön büro: rezervasyon, konaklayanlar ve oda listesi. Oda sağ tık menüsünden folyo, rezervasyon kartı, oda kartı ve housekeeping talebi açılır. Oda değişikliği sürükle-bırak ile yapılır. Üç ödeme yolu var: folyo hareket ekle, genel ödeme (bölme) ve hızlı ödeme. Check-out'ta fatura kesilir. {Ul6dofzK6UA}
- Acenta kaydı: kısa ad, aktif/pasif, kara liste açıklaması, pazar/market, komisyoncu ve sorumluluk kapsamı (oda, ekstra, tümü). Kontenjan ve garanti oda sayısı tarih aralığıyla verilir; "stop sale" ile belirli tarihlerde acentadan rezervasyon durdurulur. {b0E3KmN40eU}
- Banket yönetimi: etkinlik (şirket, tarih, yetkili, acenta, sorumlu, sadece etkinlik / konaklama / ikisi, statü, katılımcı sayısı), salon ve oturma düzeni, ekipman, konaklamalı ise rezervasyon ve folyo. Salon tanımında kapasite, departman, salon birleştirme, oturma düzeni hazırlık/toplama süresi, tarih aralıklı veya saatlik fiyat, sabit ekipman ve bakım zamanları var. {_Al6dF_Y-YI}
- Otel genel ayarları:
  - Kasa ve bankalar: ERP'de tanımlı kasa ve kullanılabilir bankalar seçilir.
  - Otel sistem tarihi: gün sonu kullanılıyorsa her gün sonunda ilerler.
  - Rezervasyon: "oda sahibi kartını oluştur" (misafirden otomatik cari), gün sonunda çıkış yapılmayan rezervasyonları uzatma, pansiyon sistemi (aynı odaya çoklu rezervasyon), gün sonu kullanmadan hareketlerin anlık işlenmesi, mükerrer rezervasyonu ve rezervasyonda fiyat düzenlemeyi engelleme, check-in sonrası odayı kirliye alma, yalnız temiz odalara check-in.
  - Folyo: KDV oranları; oda ve kahvaltı ücretinin işleneceği gelir tanımları; konaklama vergisi (%2, oran değişince elle güncellenir; "oda ücretine dahil" seçeneği).
  - Uyarılar: kesilmeyen faturalar, doğum günü, evlilik yıl dönümü, sözleşmesi biten acentalar, kara listedeki misafir.
  - Misafir kaydı zorunlu alanları (TC vatandaşı / yabancı ayrı).
  - Log ayarları: eklenen, değiştirilen ve silinen kayıtlar. {JgSkypipS40}
- Ön kasa: kasalar arası transfer (TL/döviz), kasa toplamları, kasa devri (devralan personel ve devir belgesi), müşteri bakiye kapatma (otel müşterisi veya acenta; "aktar" ile bakiye tahsil edilip sıfırlanır), müşteri bakiye listesi, toplu folyo hareket girişi (oda → rezervasyon → hareket sahibi → hesap departmanı → tutar), toplu folyo ödeme (rezervasyon durumuna ve hareket sahibine göre filtreleyip toplu tahsil). {XdYllpIcBQ0}

### HotelRunner entegrasyonu
- HotelRunner panelinde özel uygulama oluşturulur; dönüş adresine WOLVOX Otel sunucusunun IP'si yazılır ve port modemde açılır. Üretilen kimlik doğrulama anahtarı ve HotelRunner no, WOLVOX Veri Transferi > HotelRunner entegrasyonu ayarlarına girilir (gerekli DLL'ler video açıklamasındaki yardım linkinde). Rezervasyon durumları (confirmed/reserved/cancel) Otel'deki karşılıklarıyla eşlenir. Oda tipleri ve acenteler aktarılıp eşleştirilir, oda tipi müsaitliği gönderilir. Rezervasyonlar oda tipi bazlıdır ve belirlenen periyotta Otel'e aktarılır. {Lzbu8FXMTmM}

## e-Ticaret ve Web Entegrasyon

- **ERP taksit entegrasyonu {86qscM7yBow}:** Bilgi Bankası 3473 ile aynı. Ticari Program Yönetimi'nde **"Carinin taksitli borçları görüntülenebilir ve ödeme yapabilir"** işaretlenir. Ödenen taksitler bir süre sonra ERP'de "ödendi" olur.
- **Kurulum {BvOAu0TGRd0}:** Ön muhasebe ve e-Ticaret lisansı gerekir. Installer'da "Wolvox Web Entegrasyon" → Yükle. "Hızlı kurulum" mevcut Wolvox dizinine kurar, "Sadece dosyaları indir" de seçilebilir. Kurulumda "Firebird veritabanını otomatik yükle" seçeneği var. Güncelleme de Installer'dan yapılır {oevPWa4krZo}.
- **Bağlantı {8AQHq5a6ARA}:**
  - Panele `site/panel` adresinden girilir.
  - Kullanıcılar → Yöneticiler → **Muhasebe kullanıcısı**: e-posta gerçek olmak zorunda değil. İstenirse **tek bir statik IP'ye kısıtlanabilir**. Tüm yetkiler verilir.
  - Tam ya da kısmi senkronizasyon seçilir. Kısmide miktar, fiyat, alış fiyatı ve gelişmiş iskontonun güncellenip güncellenmeyeceği ayrıca seçilir.
  - Web Entegrasyon → Ayarlar → Genel → site adresi (`/panel` olmadan) ve kullanıcı bilgileri → Test Et.
- **Genel ayarlar {VHpjO7nx900}{Mn5ehZlXjQk}:**
  - Otomatik işlemler: **periyot (dk)** ile stok gönder, cari gönder, sipariş al, cari al. Periyot sipariş yoğunluğuna göre seçilir.
  - Diğer: simge durumunda başlat, Windows'la açıl, **yalnız sipariş al** (veri göndermeden), belirli saatte otomatik yeniden başlat, N günde bir sürüm kontrolü.
- **Stok ayarları, numaralı seçenekler {eXa1iI8fVMk}** (Bilgi Bankası 3039'a ekler):
  - Açıklamada **HTML** varsa ayrı bir seçenek işaretlenir.
  - **İlk 4 fiyat** gider. 21 numaralı ayarla **5–10. fiyatlar** da gönderilir.
  - 22: "toptan satış KDV oranını kullan" (varsayılan perakende KDV).
  - 23: gelişmiş fiyat (ERP'de gelişmiş fiyatlama açık değilse pasif görünür).
  - 20: basit üretim reçeteleri.
  - Stok Ayarları 2:
    - Özel Kod 1/2/3 veya bir özel alanla ek filtre.
    - **Bakiyenin alınacağı depolar** (seçilmezse bütün depolar).
    - **"Resmi olmayan stoğu gönderme"**.
- **Cari ayarları {gzgnddEPL_Q}:**
  - Cari filtresi: yalnız belirli bir **grup adı** ya da **özel kod 1** değerini taşıyan cariler gönderilir.
  - Yeni gelen cariler için **varsayılan pazarlamacı** (pazarlamacının cari kodu) verilebilir.
  - "Cari kartından iskonto oranlarını gönder": özel iskonto ve iskonto 1 **tek bir birleşik oran** olarak gider (ör. %5 ve %10 → zincirleme hesaplanıp tek oran).
- **Kategori eşleştirme {_14Swgle0Dc}:** Kategori derinliği 10'a kadar çıkabilir.
  - Ör. kategori 1–3 = grup, ara grup, alt grup; kategori 4 = özel kod 1.
  - **Kategori yapısını baştan doğru kur.** Ürün linkleri (SEO URL'leri) ilk gönderilen kategorilere göre oluşur.
- **Stok alan eşleştirme {9fRMF9CG_Rc}:**
  - ERP stok kartında Özel Tanımlar → Ayar'dan bir kategori (ör. "e-Ticaret") ve alanlar açılır.
  - **Seçenekli alanlar** (ör. ücretsiz kargo) **Var/Yok** tipinde ya da 1/0 değerli Metin olarak açılır. Sepet min/max/artış miktarı ve ek alanlar Metin olur.
  - Yeni alanların görünmesi için Web Entegrasyon'dan çıkıp tekrar girilir.
  - Açıklama 2, barkod, renk, beden gibi kullanılmayan standart alanlar da eşlenebilir.
- **Genel Muhasebe ayarları {4QQnbhxv3IU}:** Yeni cari için muhasebe alış ve satış kodları. **Kargo satırı, vade farkı ve kapıda ödeme ücreti** muhasebe kodları.
- **Virman {MXo8L602S20}:** Her pazar ve e-Ticaret için bir cari açılıp kodu yazılır (Bilgi Bankası 3072).
- **Sipariş ödemelerini ERP'ye gönderme {GSnOOwQtnsY}:**
  1. Web Entegrasyon'da "yeni siparişi direkt fatura olarak kaydet" açılır, sayaçlar seçilir.
  2. Panelde Ödeme Ayarları → taksit tanımı → **Ticari Program Eşleştirme** yapılır.
  3. Entegrasyon Yönetimi'ne statik IP, kullanıcı ve **port 3056** girilir (modemde 3055 ve 3056 açık olmalı), şirket, şube ve yıl → Test.
  4. **"Gönderilen siparişlerde ödeme bilgisini gönder"** işaretlenir.
  - Ödemeler **Kontrol Paneli üzerinden** gönderilir. Kredi kartıyla ödenen sipariş **kapalı fatura** olarak düşer.
- Web Entegrasyon → Ayarlar → Sipariş Ayarları:
  - "Yeni siparişi direkt fatura olarak kaydet" (fatura sayacı seçilir). Kapalıysa sipariş olarak kaydedilir; "durumu beklemede düşsün" ayrıca seçilir.
  - "Sadece sipariş" özelliğindeki siparişlerin ödeme tiplerini dekont olarak aktarma; web siparişlerinin sipariş kodunu grup olarak kaydetme; sipariş sayacı ve depo.
  - Üründe ERP'de karşılığı yoksa: siparişi kaydetme ya da stok kartı açmadan kaydet.
  - "Üye bilgilerini sadece siparişte tut" açıksa üye cari olarak açılmaz.
  - Ek bilgiler (promosyon kodu, kanal/pazar sipariş kodu, kargo barkodu) ERP sipariş/faturasında açılan özel alana eşlenebilir. Özel alanı tanıdıktan sonra Web Entegrasyon'dan çıkıp tekrar girmek gerekir. {it2W-C0NwiI}
- Varsayılan birim sistemi: stok kartında iki özel alan açılır ("varsayılan birim" ve "diğer birimler"; birim adları birim/barkod sekmesindekiyle aynı yazılır). Web Entegrasyon stok ayarlarında "varsayılan ve diğer birim fiyat sistemini kullan" seçilir, stok alan eşleştirmede bu alanlar eşlenir. Böylece yalnız seçilen birimler e-Ticarete gider. {5e0HGJn4vA4}

## Veri Transferi

- **Getir Çarşı (Hızlı Satış) {E-vuN-9U2is}:**
  1. Getir'den **Chain ID** (şubeliyse her şube için ayrıca **Shop ID**) alınır → API testi → şube tanımları (her şubenin genel müşterisi ayrı).
  2. Seçenekler: sipariş kontrol süresi (sn), market veya kurye kapanırsa otomatik açma isteği (süre ya da saat aralığıyla), sipariş vereni cari olarak kaydetme.
  3. "Getir servisi otomatik açılsın" ve **Hızlı Satış çalışma portu** → Servisi Başlat.
  4. Hızlı Satış'ta Özel Ayarlar → Entegrasyon Ayarları → Online Sipariş → "Getir Çarşı online entegrasyon sistemini kullan". Aynı port ve **Veri Transferi bilgisayarının IP'si** girilir → Bağlantı Testi.
  5. Eşleştirmeler: birim, sipariş durumu (hazırlandı, kuryeye teslim…), sipariş alanı (Getir'in hareket ID ve product ID bilgileri sipariş özel alanlarına).
  - Siparişler Hızlı Satış'ta İşlemler → **Online Sipariş** ekranına düşer. "Satışa aktar" ile ödeme alınır ve ERP'ye sipariş olarak yazılır.

## OctoPlus

- e-Fatura/e-Arşiv: yetkili > şirket işlemleri > e-Devlet'te e-Fatura ve e-Arşiv işaretlenir, e-adres ve vergi no doğru girilir. Program yeniden açılınca e-Fatura ayarlarında entegratör, portal ve web servis bilgileri girilir; cariler mükellef listesine göre kontrol edilir. Ülke kayıtları ve uluslararası birim kodları tanımlanır. Seçenekler: taslak kaydet, kapalı fatura bilgisi, İzibiz için e-Arşiv mail gönderimi, döviz kurunu ekleme, varsayılan senaryo/tip, opsiyonel alanlar. Gönderim için caride ülke/il/ilçe ve VKN, stokta birim tanımı eksiksiz olmalıdır. {N1-tX6fKmsE}

## WolvoxCloud (WOLVOX 26 bulut sürümü)

### Genel
- WolvoxCloud videoları çoğunlukla ekranı tanıtan 30-90 saniyelik kısa anlatımlar. Menü yolları `menu-haritasi.md`'de; burada yalnız yeni bilgi var.
- Belge ekranlarının ortak düzeni: önce cari seçilir; üstte belge bilgileri, cari bilgileri, fiyatlandırma, ek bilgiler (irsaliyede taşıyıcı/şoför bilgileri); altta hareketler (stok/hizmet) ve kapalı fatura (ödeme); en altta alt toplam, döviz alt toplam ve KDV detayları. Kayıttan sonra "İşlemler" menüsünde etiket yazdırma, kopyalama ve (irsaliyede) faturalandırma var. {F3X4XqmTIQE} {co4nmrioerQ} {NIpPM1sGP6Y} {PoJIv-R8SLQ} {tgqb0MWc7e8} {zHE21ac_osM} {eSvpAzo_Onw}
- Dosya ekleri: bir kayda eklenen dosya en fazla 10 MB olabilir; ek düzenlenir, silinir, indirilir, resimse ön izlenir. {CO1rhPdEwSk}

### WolvoxCloud eğitimi (104 dk canlı bayi eğitimi, Temmuz 2026) {W0NOHUVbouA}
Kaynak: AKINSOFT kanalındaki kayıtlı canlı eğitim. Eğitmenin "şu an yok" dediği özellikler o tarihe aittir; sonradan eklenmiş olabilir.

**Hesap, şirket ve kullanıcı**
- İlk kayıtta örnek verili bir "tanıtım şirketi" açılır. Demoya geçmek için bu şirkette "kişiselleştirilmiş deneyimi başlat" seçilir ve bilgiler girilir. Kendi şirketiniz boş açılır, kalan demo süresi gösterilir. Lisans alınınca normal kullanıma geçilir.
- Menü, kullanıcılar alışmış olsun diye WOLVOX 26'ya benzer. Favoriler ve ana sayfa widget'ları var. Widget'lar tekli (tek toplam değer) veya çoklu olur; çokluda liste ya da bar/kolon/pasta grafik seçilir. Tema aydınlık veya karanlık.
- Kontrol Paneli yoktur. Kullanıcılar sistemde e-posta ile kayıtlı olmalıdır:
  1. Yetkili → Kullanıcı Davet: e-posta girilir, yetkiler davette veya sonra verilir.
  2. Davet edilen kişi aynı e-postayla "kayıt ol" yapar (demo talebi gerekmez) ve linkten daveti kabul eder.
  3. Lisans → Modül Eşleştirme: kullanıcı ancak davet kabul edildikten sonra listede görünür. Kullanıcı sayısı lisansla sınırlıdır.
- E-posta kişisel olmak zorunda değil; kurumsal adres de kullanılabilir. İşten ayrılan kullanıcının yetkileri kaldırılınca şirkete erişemez. Kullanıcı profilinde 2FA (e-posta veya Google Authenticator) açılabilir; güvenilir cihaz listesi var (eğitimde 5 cihaz).
- Rol tanımları isteğe bağlıdır: aynı yetkileri kullanan personel için rol kaydedilip seçilir. Yetkilendirmede widget ve rapor yetkileri de var.
- Aynı e-posta birden fazla şirkete davet edilebilir; üstteki "şirket adı: çalışma yılı" alanından şirket değiştirilir.
- Yeni şirket için tanıtım şirketine dönüp yeni demo talebi açılır ve ayrı lisans alınır. Şirketler arası otomatik veri aktarımı yoktur, yalnız Excel ile taşınır. Eğitmene göre bu yapı resmi/gayriresmi çift şirket kullanımına uygun değil.
- Genel ayarlardaki "destek personeline erişim izni ver" açıksa AKINSOFT desteği (LimonDesk kaydında) uzak bağlantı olmadan tarayıcıdan şirkete girebilir. OctoCloud'daki sistemle aynıdır; e-Defter açma yetkisiyle ilgisi yoktur.
- İnternet yoksa çalışmaz, çevrimdışı mod yok. Veriler sunucuda tutulur; WOLVOX 26'daki gibi kullanıcı tarafında yedek alma/geri yükleme işlemi anlatılmadı (eğitmen emin değildi).

**Genel ayarlarda açılması gerekenler**
- Genel muhasebe ve Demirbaş menüleri, "genel muhasebe kullan" açık değilse görünmez; demoda kapalı gelebilir.
- e-Beyanname bölümü (e-Beyan KDV1, KDV2, damga) yalnız Beyanname ayarlarına e-Beyanname API anahtarı girilince görünür. Normal beyanname ekranları (KDV1, KDV2, Muhtasar-SGK, damga vergisi) her zaman var; "hesapla" verilerden doldurur.
- Döviz: parasal ayarlar; depo: stok ayarları.
- e-Fatura/e-Arşiv/e-İrsaliye ayarları ayrı ekranda değil, Genel Ayarlar → e-Devlet'tedir. Eğitim tarihinde entegratör olarak EDM ve İzibiz destekleniyor (altyazıda "easy biz").
- e-Fatura sayaçları: seri, şablon kodu ve şablon dosyası. EDM'de şablon kodu boşsa entegratördeki varsayılan şablon kullanılır; İzibiz'de şablon kodu mutlaka seçilmelidir. Toplu sayaç ekleme yok, sayaçlar tek tek eklenir.
- Özel ayarlar kullanıcı bazlıdır, her kullanıcı için ayrı yapılır:
  - Belgelerde kullanılacak stok fiyatı ve para birimi.
  - Masraf faturasında döviz.
  - Gelen e-Fatura içeri alınırken "kaydettikten sonra PDF göster" ve "UBL'deki ürün adını hareketlere aktar".

**Stok**
- İlk iş stok birim tanımlarıdır. Birim tanımsızken açılan stoklara varsayılan "adet" gelir; bu, e-Faturadaki uluslararası birim koduyla uyuşmazlık çıkarır ve binlerce kartta düzeltmek zordur.
- Stok kartı sekmeleri: diğer vergiler, birim/barkod (ek barkod), fiyatlar, iskonto, muhasebe hesap kodu, varyant yönetimi (asorti, ana/alt stok, marka-renk-model-beden), izleme yöntemleri (seri/lot, bakiye limit uyarıları, otomatik sipariş için asgari miktar ve eklenecek miktar), e-Fatura için GTİP no ve üretim yeri, tedarikçiler, stok durumu, özel alan, dosyalar.
- Dosyalarda PDF/resim ön izlenir. "Resim olarak belirle" o dosyayı kartın ana resmi yapar; resim sayısı sınırı yok. Cari kartta da aynıdır.
- Alt stoklar kart içinden değil İşlemler → "alt stok işlemleri" ekranından üretilir (renk-beden oluştur → alt stokları oluştur).
- WOLVOX 26'daki ayarla açılan gelişmiş fiyat ve iskonto sisteminin yerini, ayar gerektirmeyen iki ekran aldı:
  - Stok fiyat kural tanımları: tarih aralığı, haftanın günleri ve saat aralığı (ör. happy hour, promosyon). Cari, cari grubu/ara/alt grup ya da ülke/il/ilçe seçilebilir; boş bırakılırsa tüm carilere uygulanır. Stoklar tek tek veya Excel'den eklenir (stok grubu toptan seçilemez). Kural, seçilen fiyat numarasının (ör. satış fiyatı 1) yerine geçer ve süre bitince eski fiyata döner. Cari farklı bir fiyat no kullanıyorsa bu kural o cariye uygulanmaz.
  - Stok iskonto kural ve kısıtlama tanımları: kural tipi kısıtlama (azami iskonto; tutar ya da oran) veya iskonto (miktar ya da oran bazında; asgari/azami miktar). Tarih, gün, saat ve cari filtreleri aynıdır.
- Rapor tasarımları DevExpress tabanlıdır. Varsayılan tasarımlar değiştirilemez; kopyalanıp kopya düzenlenir. Birden fazla detail bandı eklenebilir.

**Finans**
- Cari kartta "kişi/firma tipi" sabit değerlerdir: müşteri, tedarikçi, müşteri+tedarikçi, personel. Excel aktarımında kodları 1-4'tür ve cari koduyla birlikte zorunludur. Ek gruplama için cari grup tanımları kullanılır. e-Devlet ayarları cari kartta ayrı sekmededir.
- Banka tanımı tek ekrandadır: banka ve hesap bilgileri, "kredi kartı kullan / çek kullan / POS kullan" ile ilgili alt tablolar, şube yetkileri (satır olarak) ve muhasebe kodları.
- Cari tahsilat ekranında cari bakiyeler ayrı sekmede. Banka-kasa transferinde her satırda yön (bankadan kasaya / kasadan bankaya) seçilir; iki menüden de aynı ekran açılır.
- Raporlar: cari yaşlandırma (valörlü dahil), valörlü/hareketli/KPB esaslı bakiye listeleri.

**Satın alma ve satış**
- Teklif ve siparişte durum ve grup tanımı var; irsaliye ve faturada yalnız grup tanımı var.
- Fatura ve irsaliye türleri (konsinye, proforma, fiyat farkı, kur farkı…) belgenin içinden değil menüden seçilir. Tekliften siparişe geçiş "kopyala" ile yapılır.
- Teklif revize: kayıtlı teklifte revize tarihi ve açıklaması girilir, teklif kopyalanıp yeni teklif açılır. "Teklif revize raporu" eski ve yeni teklif no, tarih ve toplamları karşılaştırır.
- Diğer raporlar: sipariş teslim, stok bazlı sipariş/irsaliye, ihtiyaç listesi, transfer irsaliyesi, e-İrsaliye eşleştirme listesi, kâr-zarar, fatura analizi, fatura KDV analizi.
- Özel alanlar artık kartlardan değil Yetkili → Tanımlar → Özel Alan Tanımları'ndan tanımlanır:
  - Modül seçilir; belge geneli için "Fatura", satırlar için "Fatura Hareket" modülü.
  - Önce grup açılır, sonra alanlar eklenir. Alan türleri: metin, tam sayı, ondalıklı, tarih, saat, var/yok, çoktan seçmeli, çok seçimli.
  - "Filtrelenebilir = Evet" değilse raporlarda o alana göre filtreleme yapılamaz.
  - Belgeler arası aktarımda alan eşleştirmesi Genel Ayarlar'dadır.

**Lisans ve modüller**
- Modül eşleştirme kullanıcı bazlıdır. Cari tek modüldür (Cari 1/2 ayrımı yok). Stok, Stok 1 ve Stok 2 olarak ikiye ayrılır; sayım Stok 2'dedir. e-Fatura, e-Arşiv ve e-İrsaliye gelen kutuları için modül eşleştirmesi gerekmez.

**Demirbaş ve genel muhasebe**
- Demirbaş kartı: alış, amortisman, güncel değer, satış, hesaplamalar, zimmet, özel alan ve dosyalar. Demirbaş grupları var. Raporlar: demirbaş, dönem, yeniden değerleme ve zimmet raporu, amortisman kontrolü.
- Hesap planı "hesap planı oluştur" ile varsayılandan veya başka yıldan kurulur, Excel'e alınabilir.

**WOLVOX 26'dan geçiş (Bilgi Bankası 4056)**
1. Masaüstünde Kontrol Paneli → Upgrade → WolvoxCloud Aktarımı: şirket seçilir; istenirse stok/cari resimleri ve dokümanlar da dahil edilir; aktarım dosyası hazırlanır.
2. "WolvoxCloud upgrade yapmak istiyor musunuz?" sorusuna Evet denirse tarayıcı açılır; Hayır denirse dosya bekler.
3. WolvoxCloud'da Genel Ayarlar'daki "WolvoxCloud aktarım" alanı (yalnız lisanslı hesapta görünür, demoda yok): ön muhasebe veya genel muhasebe seçilir, dosya yüklenir, aktarılacak modül ve tablolar görülür.

**Eğitim tarihinde olmayanlar** (talep olarak toplandı)
- Açık bankacılık (FinCloudy) ve banka entegrasyonları.
- Mobil satış rotası, pazarlamacı.
- WhatsApp entegrasyonu.
- Ana cari / alt cari yapısı.
- CRM, script.
- Hızlı Satış, Restoran ve yazarkasa entegrasyonu.
- Stok fiyat kuralında grup seçimi.
- Şirketler arası belge aktarımı.
- Tahsilat/ödeme onay bildirimi. Belge onay mekanizması var ama bu ihtiyacı karşılamıyor.

### Başlangıç ve kullanıcı
- Kullanıcı profili: ad-soyad, aydınlık/karanlık tema, profil resmi ve iki adımlı doğrulama (2FA) türü: e-posta veya Google Authenticator. {SNAylZbJod8}
- Güvenilir cihazlar: 2FA açık kullanıcı doğrulamayla giriş yaptığı cihazı güvenilir olarak kaydedebilir. {EAn5klcBHiA}

### Sistem ve genel ayarlar
- Genel ayarlar (Sistem → Yetkili Tanımlar → Genel Ayarlar):
  - Şirket ayarları.
  - Cari ayarları: otomatik cari kodu, otomatik alış muhasebe kodu, ülke/il/vergi dairesini şirket bilgisinden alma, taksitli müşteri, cari döviz, manuel yaşlandırma.
  - Risk limitleri: aşıma izin vermeme ya da uyarı; açık hesap, irsaliye ve sipariş limitleri; vadesinde ödenmeyen bakiye kontrolü (limit ve tolerans günü).
  - Cari hareket ayarları: otomatik evrak no, "entegrasyon hareketlerine cariden müdahale edilebilsin", varsayılan tahsilat/tediye işlem türleri, dövizin seçili gelmesi.
  - Zincir pazarlama: prim verilecek azami üye sayısı, ilk satıştan sonra prim, başlangıç tarihi, asgari satış tutarı. {ZRA_FGu1ci8}
- Beyanname ayarları: e-Beyan entegrasyonu için e-Beyanname sitesinde profil → entegrasyon yönetimi sayfasından alınan API anahtarı girilir. {D7eEt9tDaUU}
- e-Defter ayarları: e-Defter veya envanter defteri için önce destek ekibine kayıt (ticket) açılır. Etkinleşince başlangıç tarihi ve şubeli defter/şube no seçilir. e-Defter yedekleme hizmeti için entegratör, kullanıcı adı ve şifre girilir. {UNFodX8Dlnc}
- Mail/SMS ayarları: otomatik mail ve SMS sistemleri açılır, mail ve SMS servisleri seçilir, "test et" ile deneme gönderimi yapılır. {bci4QLvkFbA}
- Excel transfer işlemleri: cari, stok, uyumlu stok marka/model, seri ve firma aktarımı. Çalışma sayfası ve başlangıç satırı seçilir. Mevcut kayıt için "güncelle / değiştirme", yeni kayıt için "ekle / ekleme" seçenekleri var. Sütunlar eşlenir (cari aktarımında cari kodu zorunlu), ön izlenip aktarılır. {gGyIkMt6Ee4}
- Metin özelleştirme: programdaki başlık metinleri (ör. "Muhasebeci" → "Muhasebeci Kayıt") değiştirilir. Toplu aktarım `.vmo` dosyasıyla yapılır (orijinal=özel satırları); orijinal metinde büyük/küçük harf önemlidir. {ejhCwRL2mmo}
- Sayaç tanımları: bir alan için birden fazla sayaç (basamak sayısıyla) tanımlanır. "Sayaç seçimi"nde hangisinin varsayılan olduğu belirlenir. {YhXICk6l46o} {8WOC6s3rhk4}
- Özel alan tanımları: modül seçilir → özel alan grubu → alanlar; kaydedince ilgili modülde görünür. {wDj982Na0mk}
- Diğer: belge onay tanımları listesi (modül ve durum filtresi) ve kullanıcı davet listesi (e-posta, davet gönderim ve geçerlilik tarihi). Kullanıcılar e-posta daveti ile eklenir. {zIZzLxnwtxw} {v1uu_SAUQJU}
- Fatura ayarları: satış faturası varsayılanları (iskonto 1 ve oranı, KDV oranı ve dahil/hariç, kaynak iskonto genel ayar mı cari/stok kartı mı, ÖTV kullanımı, vade manuel mi varsayılan ay/gün mü, otomatik açıklama, otomatik fatura no). Fatura sabitleri: cari/stok hareketleri işlensin seçili gelsin; entegrasyon faturalarında bu seçeneklere müdahale edilebilsin; irsaliye faturalanınca cari hareketi faturayla ilişkilendir. Masraf faturası: fiş no boş kaydedilsin veya otomatik verilsin, varsayılan cari. {FjnCPxYMuuc}
- Stok ayarları:
  - Stok kart ayarları: otomatik stok kodu/barkod, eksiye düşerse veya limit dışına çıkarsa uyar; limit kontrolüne bloke ve termin miktarlarını dahil et; eksiye düşüyorsa işleme izin verme.
  - Seri/lot: izleme tipi (seri no/lot), maliyetlerde eşleştirme yöntemi, alış/satış faturasında seri/lot girilmeden devam edilmesin, satış fatura ve irsaliyesinde seri/lot limiti ve son kullanma tarihi kontrolü, seri girişinde garanti tarihine eklenecek gün/ay/yıl.
  - Varsayılanlar: depo modülü ve varsayılan depo; stok belirli miktarın altına düşünce sipariş listesine otomatik ekleme.
  - Stok hareket ayarları: otomatik evrak no, entegrasyon hareketlerine stoktan müdahale, döviz.
  - Diğer: stok paket tanımına otomatik barkod; elektronik terazi barkod tanımı (barkod tipi, stok kodu ve gramaj uzunluğu, hassasiyet); karekod ayarları (grup, alan ve karakter sayısı). {684bD6zwRxo}
- e-Devlet ayarları:
  - Kullanım: e-Fatura, e-Arşiv ve e-İrsaliye açılır.
  - Kullanıcı bilgileri: entegratör (ör. EDM Bilişim) ile kullanıcı adı ve şifre.
  - e-Fatura ayarları: ÖTV vergi kodu; gönderimden sonra fatura no güncellensin; kayıtta otomatik gönderim; portala taslak kaydetme.
  - e-İrsaliye: not, vade ve cari bakiyesini belgeye ekleme.
  - Posta kutusu: şubeye göre gönderici posta kutusu.
  - Opsiyonel alanlar: fatura, fatura hareketi, irsaliye, irsaliye hareketi ve stok alanları e-Belgeye eklenir. {v9y3CBdpPFc}
- Şube ayarları: stok kartları tüm şubelerde ortaktır; cari kartlar ve döviz hareketleri isteğe bağlı ortak kullanılır ("cari kartları ortak kullan", "döviz hareketlerini ortak kullan"). {m_b6aW5YLMs}
- Kullanıcı daveti (Sistem → Yetkilendirme → Kullanıcı Davet): e-posta ve üst kullanıcı seçilir, rol veya yetkiler verilir (tam yetki, hızlı yetkilendirme; diğer yetkilerde kasa/depo kısıtı), "davet gönder" denir. Davet linki 5 gün geçerlidir, değiştirilemez; davet iptal edilebilir veya tekrar gönderilebilir. {InJvkRwVmpo}
- Kullanıcı yetkilendirme: rol yetkileri otomatik gelir; genel, rapor ve widget yetkileri ayrıdır. Kasa, depo ve şube kısıtları boş bırakılırsa kullanıcı hepsini görür. Hızlı yetkilendirmede ekleme/düzenleme/silme toplu verilir ya da "silme yetkilerini kaldır" denir. Rol tanımları listesi de var. {4ibqtwP7TzQ} {uVflaukcIKg}
- Genel muhasebe ayarları:
  - ERP entegrasyonu: fatura entegrasyonunda teklif kullanımı, satış faturası indirimlerini yansıtma, indirilecek KDV'de tevkifat ayrımı, otomatik maliyetlendirme.
  - Hesap kodları: ÖTV, vade farkı, sigorta/navlun.
  - Otomatik fiş açıklamaları.
  - Kontroller: günün tarihi kontrolü, açıklamasız hareket kaydetmeme, entegrasyon hareketlerine müdahale için onay.
  - Fiş kesinlik tarihi: bu tarihten önceye fiş girilemez, eski fişler düzenlenemez ve silinemez.
  - Otomatik firma kodu (basamak sayısı, ön/son ek). {gjC4bkfxnaE}
- Hareket tarih kontrolü ayarları: modül bazında çalışma yılı kontrolü (aktif yıl dışına izin verme / onay alarak / kontrol etme) ve tarih kontrolü (aktif ay öncesi, aktif gün öncesi, onay tarihi öncesi). Kullanıcıya "onay tarihi kontrolü yapma" yetkisi verilmişse bu ayar o kullanıcıya uygulanmaz. {tYhBZz2f6no}
- Parasal ayarlar: döviz sistemi ve varsayılan döviz, döviz tanımı ekleme, tutar ve kur ondalık basamakları. KPB'den döviz hesabına ve dövizden KPB'ye işlenirken alış mı satış kuru kullanılacağı ile kur tipi (döviz/efektif) seçilir. {HJkPR92iSc4}
- Özel alan aktarım eşleştirme: ör. irsaliye → fatura aktarımında hangi özel alanın hangisine taşınacağı modül çiftleri için tanımlanır. {fWdk7xb50Hg}
- Özel ayarlar (kullanıcı bazlı): cari seçilince kara liste kontrolü, stok paketi aktarılırken paket miktarını sorma, faturada okutulan barkod kayıtlı değilse stok kaydı sorma, aynı stok okutulunca satırları birleştirme, e-Fatura gelen kutusu içeri aktarma seçenekleri. {Q-DMNt1GKOw}
- Mail/SMS şablon tanımları: modül, durum (mail, SMS, ikisi, gönderme), onaylı ya da otomatik gönderim, tetikleyici durum değişikliği (ör. sipariş beklemede → onaylandı), alıcı (cari veya yetkili e-postası/cep telefonu) ve şablon metni. "Kullanılabilir alanlar" listesinden alan çift tıklanıp şablona yapıştırılır. {vZU0eooqD4I}
- Şube tanımları (Sistem → Diğer İşlemler → Şirket Ayarları → Tanımlar): şube kodu ve adı. e-Fatura/e-Arşiv kullanılıyorsa e-adres alanındaki il, ilçe, dış kapı ve iç kapı zorunludur. {qaBy3Dn3vfc} {OmUjgMZnWs4}
- Formül tanımları listesi ve formül hesaplama ekranı var. {rws3Y304zQI} {-oLhja5Yy8g}
- Çek/senet ayarları: evrak no ve bordro no otomatik verilsin; entegrasyon hareketlerine diğer modüllerden müdahale edilebilsin; kur farkında işlem yapma / evrak olarak işle / kur farkı faturalandırma sistemi. {jCAx_AHo9OI}
- Rol tanımları (Sistem → Yetkilendirme → Şirket Rol): rol adı, yetkiler, hızlı yetkilendirme ve kasa/depo/şube kısıtları. Kullanıcı yetkilendirmede rol seçilince yetkiler aktarılır. Kullanıcı listesinden yetki ekranına geçilir. {PfLuv4-etUw} {PPAmqFSz2V4}
- Sipariş ve teklif ayarları (alınan/verilen ayrı): iskonto 1-2-3 ve oranları otomatik işaretli gelsin, varsayılan KDV oranı ve dahil/hariç, kaynak iskonto (genel ayar veya cari/stok kartı), vade (manuel veya varsayılan ay/gün), otomatik açıklama, otomatik numara. Teklifte ayrıca "stok termin kullan" seçeneği var. {DF55ayzynCA} {30wJud-39L8}
- Formül tanımlarında detay bilgilere formül alanları eklenir; formül hesaplama ekranına kısayol var. {BXI3hEZEq4A}
- İrsaliye ayarları (satış ve alış ayrı): iskonto 1-2 varsayılanları, KDV oranı ve dahil/hariç, kaynak iskonto, varsayılan vade, otomatik açıklama (başlangıç karakteri ve karakter sayısı), otomatik numara. İrsaliye sabitleri: cari/stok hareketleri işlensin, stok maliyetlerini etkilesin, faturalandırmadan sonra stok hareket fiyatları güncellensin. {BIzdi1ESJic}
- Muhasebeci tanımları listesi (muhasebeci tipi, ad, unvan, e-posta, kimlik/vergi no). {IgxM4jkGnws}
- Lisans detay (Sistem → Lisans): aktif modüller, kullanıcı sayısı, **disk kullanımı**, lisans bitiş tarihi ve kalan gün. {EfqyYWH7BxE}
- Kasa hareket ayarları: otomatik evrak no, entegrasyon hareketlerine müdahale, döviz işlemi. Mail/SMS şablon listesi modül, durum ve onaya göre filtrelenir. {ACX4f6DDCTM} {c5Ia7izDjH0}
- Belge onay tanımları: modül (ör. sipariş, teklif), durum ve işlem yapan kullanıcılar seçilir. Tutar aralığına göre onaycı belirlenir (ör. verilen teklif 50.000-100.000 arasındaysa belirli yetkili kullanıcı onaylar). {bdEmS0BCwOs}
- Uyarıcı/hatırlatıcı ayarları: modül seçilir. Cari bakiyede "vade tarihi esaslı cari bakiye kontrolü" ve asgari bakiye; e-Fatura'da "gönderilmemiş e-Faturaları otomatik kontrol et". Uyarılacak kullanıcılar ve uyarı rengi belirlenir. {oyqg_ASgaT4}
- Mali dönem tanımları listesinden mali dönem değiştirilir. Stok tanımları listesinde "bilgi güncelle" ile toplu güncelleme yapılır. {9pWVCk08aJI} {LOY4X2skDBM}

### Finans
- Banka transfer fişi ve banka-kasa transfer fişinde tek fişe birden çok hareket satırı eklenebilir. {GXMEOeC0bSg} {p9olr7jbobA}
- Teminat çek/senet bordrosu: tahsilatta müşteri çeki/senedi/teminat mektubu, tediyede kendi çek/senet/teminat mektubu evrak tipleri. {y_u3YqingJ8} {2KfN3QtAaQI}
- Cari özel rapor: "gruplanacak alanlar" ile tablo sütunları seçilip kişisel rapor yapılır; toplam borç/alacak/bakiye altta. {OMybjkFHkLE}
- Toplu cari tediye fişi: tek fişte birden fazla cariye tediye. Cari toplu hareket fiş raporu toplu tahsilat/tediyeleri listeler. {tXoR73V84k8} {XDWp0hCHK1g}
- Çek/senet kısmi tediye ve bordro durum değiştirme (ör. bankaya takasa verme). {LX_dlG6UYzQ} {mk4-DJKXYT4}
- Raporlarda satır solundaki ok ile kayda gidilir; entegrasyon hareketinde "bağlantı" butonu kaynak belgeyi açar. Çek/senet valör hesaplı rapor ortalama vade ve valör tarihini gösterir. {SDKwN4TsQos} {JhTHTYNBEsI} {3ApBN71ZeUM} {8ceSZ_qduuY}
- Döviz kur listesi günlük kur girişlerini tarih ve saatiyle gösterir; "yeni ekle" ile tarih-saatli kur girilir. Cari yetkililer listesi de var. {w9MeVKjrH-g} {DELpd4_Md_c}
- TCMB kur indirme: ekran açılınca TCMB kurları otomatik gelir; "geçerli kurları aktar" ile sisteme kaydedilir. {i-72lP8JMrQ}
- Kredi kartı taksitlendirme: cari, işlem tipi, banka ve kredi kartı, toplam tutar, taksit sayısı, taksit aralığı (ay/gün), erteleme ve küsurat; ön izleme sonrası "taksit planını cariye işle". {lDmcvsp7xws}
- Banka hesap tanımı: kredi kartı / çek / kredi hesabı kullan işaretleri. Şube yetkileri satırlarında şubeye gelir-gider yetkisi verilir; kredi kartı, POS ve çek bilgileri alt tablolardadır. {wjMuvfiJ80o}
- Cari departman tanımları, cari yetkililerde departman seçimi için kullanılır. Cari tanımlar listesinden "bilgi güncelle" ile filtrelenen cariler toplu güncellenir. {_qpajZnWiPA} {ALEufCGP7RI}
- Diğer ekranlar: tahsilat/tediye girişi, toplu cari tahsilat fişi, çek/senet bordroları, çek/senet işlemler raporu, cari hareket analizi (aylık borç/alacak). {CH6WcC_NvHQ} {rEqc_1dn8b4} {B2haj539_qs} {p87S0P-8hnE} {v8jEAwMcPM8} {MBROixFldCw} {xgU1D3kL82w} {q_zLapl4xlQ}
- Cari tanımı sekmeleri: genel bilgiler, iletişim, e-Devlet (e-Fatura/e-Arşiv türü, senaryo, posta kutusu, "e-İrsaliye kullan"), banka hesap bilgileri, yetkililer (başka bir cari kartla bağlantı), kredi/bakiye, kredi limitleri (açık hesap, irsaliye, sipariş riskleri ve toplam risk; "kredi aşımında uyar"), dosyalar. {cH0T3GP4NH8}
- Gün sonu raporu 2: tarih, saat, şube, para birimi, kasa veya personel bazında o günün faturaları ve toplamları; diğer işlemlerde işlem gören cari/stoklar ve kasa hareketleri. {ZmZ8T7eOEYg}
- Döviz tanımları: listeden döviz seçilir, simge ve kod düzenlenir; kayıttan sonra kuru otomatik gelir. Günlük kur girişinde belirli tarihin kuru "girilen tarihteki kur bilgilerini getir" ile çekilir. {SUCKs6c-XgU} {Jia8ZTA9gWA}
- Toplu cari hareket fişi: tek fişte birden çok cariye borç veya alacak; işlem türüne göre kasa/banka. Cari virman fişi, teminat çek/senet durum değiştirme, kasa gelir girişi, cari grup (ana/ara/alt) ve kasa hareket grup tanımları da var. {TCWBK5edGUo} {5wPDSArr9pw} {pCEs7qX7iew} {fknaFIwFn6Y} {aJukMC7Xh6Q} {ZR4K80wpd3M}
- Cari analizi: risk limiti, kullanılabilir bakiye, açık hesap bakiyesi, irsaliye/sipariş riski, ödenmemiş çek/senet. Analiz detayında hareket, çek/senet, sipariş, irsaliye ve risk analizi sekmeleri var. Cari hareket analizi günlük, haftalık, aylık, 3/6 aylık veya yıllık, KPB ya da döviz bazında alınır. {NELLsfGCPaM} {QMumPo3uwTM}
- Dönemsel hareket raporu (taksitli): işlem görenler/görmeyenler, bakiye filtresi; "bilgi güncelle" ile listelenen cariler toplu güncellenir. {qFiVZ2KEXUY}
- Gün sonu raporu 3 transfer irsaliyelerini ve gelirleri gösterir. Kredi işlemlerinde dosya masrafı girilir, "ön izle" ile banka planı görülür, "krediyi kullan" banka bakiyelerine işler. {nr8hupNVpiU} {985nrxqpWUU}
- Diğer raporlar: cari yaşlandırma ve valör hesaplı rapor (vadeli toplam, ortalama vade günü, valör tarihi), çek/senet bordroları (bordro başına evrak toplamı, ortalama valör), cari virman fiş raporu, banka-kasa transfer raporu, döviz tanımları listesi. {_HUZHPdecHo} {zIDLgAyyRb0} {imTTfRMb25Y} {X6iwoOY1NKc} {1V4N2feNi7o}
- Finansal analiz raporları:
  - Detaylı: şube ve döviz seçimi; cari bakiyeleri, zamanlı hesaplar ve protestolu çek/senetler dahil edilebilir; banka opsiyon/kredi ve vadeli hesaplar dahil edilebilir. Kasa, banka ve cari bakiyeleri toplanır.
  - Kontrol: bugün, yarın ve sonraki günlerin borç/alacak toplamı ve farkı; gün seçilip "detaylı göster".
  - Periyodik: günlükten yıllığa; rotatif kredi seçeneği. {VyG_bl0wGac} {Kh0LsuJem4k} {HP-mcA9G-zk}
- Gün sonu raporu 1: günlük veya genel işlemler; bakiyeler için son işlem tarihi, stok envanterini fark hesaplarına dahil etme, fark hesaplarını gösterme. {GykbB-Fum_s}
- Hareketli bakiyeler listesi: cari hareketler için tarih aralığı verilerek çıktıda yalnız o aralığın hareketleri ve toplam bakiye basılır ("hareket yazdır"). Bakiyeler listesi ve dönemsel hareket raporunda "bilgi güncelle" ile toplu cari güncelleme yapılır. {L97frgZrSF8} {TLVC5_ZrdZ4} {L7CjcRm2IfQ}
- POS ve provizyon raporu (satış, iade, provizyon kesintisi, net tutar) ve banka likidite akışı (kredi limiti, kullanılabilir bakiye). Çek/senet analizi vadeye göre müşteri çeki/senedi portföy ve takas ile kendi çek/senetlerini ayırır. {vMDkLqfoOx4} {BpsGADLhiTY}
- Tatil tanımları (POS, kredi kartı ve ödeme vadelerinde kullanılır): tek tek veya "otomatik aktar" ile tarih aralığı ve tatil günleri seçilerek toplu oluşturulur. {0D41nVxflv8}
- Raporlar: işlem türü raporu (nakit, POS, çek, senet, tahakkuk, fatura, sipariş toplamları), KPB esaslı bakiyeler (dövizli cari bakiyeleri günün kuruyla TL'ye çevrilir), valörlü bakiyeler, kredi kullanım raporu (kredi yapılandırma/kapatma/düzenleme; POS hesap tablosunda provizyon ve vade oranları), kredi kartı raporu ve ekstreleri (hesap kesim günü, kart limiti, dönem sonu borcu), kasa hareket ve transfer raporları, teminat çek/senet bordroları. {-bBJKpUMdP0} {FvhlFywkfxw} {sqaT7d3XqUk} {Y_fvhuR9j1w} {etMp5QtQjGk} {_THcpoEEKSM} {JHsEI1ifdxQ} {G-YBlHBuuWE} {TF-tjSqzZVQ}
- Kasa-banka transfer fişinde her satırda yön (bankadan kasaya / kasadan bankaya) seçilir. {6iqB4hy9YUQ}
- Kasa hareket analizi: kasa gelir ve giderleri yıl ve ay bazında, kasa seçilerek incelenir. {WJBRKcnyOrU}

### Stok ve depo
- Depo raporları: yatay depo envanteri (depolar sütun olarak), depo hareket raporu, depo transfer fişi raporu, depo tanımları listesi. {gohmrBiaQnE} {txxN8Vfjx0E} {2UN17q08w9o} {98CGfE04Tg4}
- Demirbaş yeniden değerleme raporu: değerleme tarihi, oranı, önceki değer, artış ve yeni değer. {TVPuPOKvrL8}
- Seri/lot raporu renkleri: beyaz = girişi ve çıkışı yapılmış, yeşil = girişi yapılmış çıkmamış, kırmızı = giriş-çıkışında sorun olan seri. Seri/lot hareket raporu ve son kullanım tarihi izleme ekranı (giriş/çıkış kaydı) da var. {hKfUiYSeMD8} {FXqlJd4cNR4} {UfKawiYFcyI}
- Stok envanteri TL veya tanımlı döviz cinsinden alınabilir. Diğer ekranlar: stok bloke/termin raporu, hızlı stok arama (barkodla), beden tanımları (grup, beden, sıra). {MvbvQSS94YA} {zTmTPj36p6A} {IulXJieovCE} {OGq29BsnB4U}
- Fiyat listesi → işlemler: bilgi güncelleme, fiyat yenileme (artış/indirim, alış fiyatı değiştirme, satış fiyatı oluşturma, yuvarlama, devir fiyatı) ve manuel fiyat yenileme. Stok fiyat kural tanımları (tarih, şube, kural adı) ve stok iskonto kural/kısıtlama listesi var. {wet53zOBzII} {fILK0vrs4jU} {qwfwfwbPugg}
- Envanter raporları: birimli (her birim için giren/çıkan/kalan), depo bakiyeli (depo depo miktar). Kâr/zarar raporu (normal) ve basit (envanter birim fiyatı tipi seçilir; satış fiyatları üzerinden de hesaplanır). {jMrElyEAEpU} {WZAoh9I1XKM} {CVewZqWsV58} {JDS-9buw754}
- Stok yeterlilik raporu: planlama günü, tolerans ve yuvarlama verilir; satış ortalamasına göre stokun kaç gün yeteceği ve gereken miktar hesaplanır. Hizmet analizi (aylık) hizmet hareketlerini aylara yayar. {CgtNN9_MXxs} {lLJJStyUHsI}
- Tanımlar: stok/hizmet/paket grupları ağaç yapısında (ana → ara → alt grup, Excel'e aktarma), birim tanımı (uluslararası kod, miktar hassasiyeti), marka/model, depo tanımı, hızlı stok tanımı, stok paket tanımı (özel alan, dosya, asorti kullanımı). Stok tanım birleştirme, paket seri etiket yazdırma ve toplu stok giriş fiş raporu da var. {-BmwBdfYwSE} {QCq7qxZQzZE} {UzVN3QuTHYA} {B5Zpc_cs9Zs} {L-P38DsrDto} {rDEWJNIfOzY} {o5_bKD9ocIw} {Mo8BUYFPRGU} {_PGoAa38fAQ} {4PCaRzvdvSY} {SvsLbvOxhCY}
- İşlem görmeyen stoklar raporu: "hareketsiz stok gün sayısı" ve "ölü stok gün sayısı" girilerek hareketsiz ürünler ayrılır. Stok hareket analizi günlük, haftalık, aylık, 3 aylık, 6 aylık veya yıllık alınır. Stok özel raporu seçilen alanlara (ör. stok grubu) göre gruplanır. {-GNBz9zMCf8} {iYIF6I9LcvI} {zFrLyy-3DIk}
- Toplu seri no girişi ekranında seri ürünlerin giriş ve çıkışları yapılır. Hizmet tanımında genel muhasebe kullanılıyorsa muhasebe kodları seçilir. {CLzj_lKrjXk} {Gn-XJiQu4Eo}
- Demirbaş raporu: cins, grup, barkod, amortisman tipi/dönemi, alış/satış tarih ve fiyatına göre filtre; satır seçilince yıllara göre amortisman hesabı görülür. {fKbRNfsaFg0}
- Stok tanımı: genel bilgiler, döviz kullanımı, diğer vergiler (ÖTV, istisna kodu, tevkifat, alış/satış kodları), izleme yönetimi (limit uyarıları, seri). Varyantlı ürünlerde varyantlar "İşlemler" menüsünden oluşturulur; "stok resimleri" butonu var. {Dqq-ENLSt4E}
- Stok sayım ve düzenleme: "stok hareketleri işlensin" ve "genel muhasebe kullan" seçenekleri, işlem tipi (giriş, çıkış veya genel sayım), sayım miktarı ve birim; stok, paket ve seri eklenir; Excel'den aktarılabilir. {c5feOZXQin0}
- Fiyat ve iskonto kural tanımlarında kural adı, başlangıç/bitiş, geçerli şubeler ve gün bazlı zamanlama; iskonto kuralında kısıtlama şekli (oran/tutar) ve kural tipi var. {oAakKWLdYiI} {E9H18TQPPqE}
- Raporlar: stok kâr/zarar (özel; gruplama seçilmezse tek toplam satır), depo envanteri (birimli), stok tanımları seri etiket yazdırma. {NNU97eEAWlk} {1i8gGq-rqLg} {PvSNSGAtXZc} {OIE9lXxjFEA}
- Alt stok işlemleri: stok ana stok ve "asorti kullan" olarak kaydedilir, üstteki "alt stok işlemleri → alt stok ekle" açılır. Stok adı ana stoktan ya da elle; ada marka/model, koda renk/beden eklenip eklenmeyeceği seçilir. {7O_mhgO2Q-Q}
- Dönemsel giriş-çıkış raporu: negatif ve/veya sıfır miktarlı stokları dahil etme seçenekleri; toplam giren/çıkan miktar ve tutar. Renk tanımları (renk ve sıra no) asorti/varyantta kullanılır. {pRi7wv8nWSg} {YrPleVsm5Vc}

### Satın alma ve satış
- Toplu işlemler: sipariş ve irsaliye fiyat güncelleme (stok kartındaki seçilen fiyatı toplu aktarır), toplu alış/satış irsaliyesi (stok ve cari listesinden aktarılıp "irsaliyeleri işle"), toplu irsaliye faturalandırma (cari seçmeden de; depolara ayırma, kur, vade ve valör seçenekleri), toplu masraf faturası (gider kodu, fiyat, miktar). {c5Bnq1z5kTE} {hvDscXUn7cw} {AqEfP07Yyu4} {4nKx_WjIYKo} {hDV79_89FOc} {jKvHj11eCDI} {Nxra_WE_9VY} {T75Kr7zAy5o} {fERInIYDgQA} {fp95cpVIVp4}
- Tekliften siparişe geçiş "kopyala" menüsüyle yapılır (yurt içi alınan/verilen sipariş seçilerek); irsaliye ve faturaya aktarım "işlemler" menüsünden. Teklif irsaliyelendirmede irsaliye tipi ve satırların birleşip birleşmeyeceği seçilir. {1ECNSaZ0HD0} {oYvgBFv9DJs} {aaOCbbc-qSA} {UAuHztE8Z0M} {_yVWYesF3OM}
- Sipariş durumları (onaylandı, muhasebeleşti, beklemede) ve "stok bloke" işareti. Sipariş teslim raporunda yalnız "onaylandı" durumundaki siparişler görünür; buradan seçilenler faturaya veya irsaliyeye aktarılır (hepsi tek belge ya da her sipariş ayrı). {zbNFcVesr6w} {uyImnRBCpGw} {OVho0SOoTDM}
- Sipariş durum tanımlarında "uyarılacak personeller" oturum açılınca uyarı alır; "yetkili kullanıcılar" o durumu siparişte kullanabilir. {dzgJRiBCmvE}
- Transfer irsaliyesi: irsaliye detaylarında kaynak şube/depo ve hedef şube/depo seçilir. Kayıttan sonra yetkiye göre "onaylandı" veya "kabul edilmedi" durumu uygulanır. {4XpcoGUqEjc}
- Fiyat farkı faturasında "kaynak modül" ile hangi faturaya istinaden kesildiği seçilir. {7pmJLeZDSxQ} {ScmhPluM0UA}
- Masraf faturasına PDF veya görüntü eklenebilir. {nqJip-2QM7g}
- Raporlar: sipariş, teklif, irsaliye ve fatura raporları (hareketli sürümleri), stok bazlı teklif raporu, masraf faturası raporu, e-Fatura eşleştirme listesi ve fatura özel rapor (gruplanacak alanlar). {Qsej_cvY7lU} {Mh454BmXY8U} {jwK4H-v3gds} {VSfTSQCHMfs} {HGyRIsJnxW0} {m3c-2hcJRDM} {0YEhPFoc5BM} {YDHTlR81D4o} {TM2pxZhKojY} {ovQkkycBvW0}
- Teklif faturalandırma: aktarılacak tip (satış faturası, yurt içi/yurt dışı, iadeler) ve satır birleştirme seçenekleri. Teklif fiyat güncelleme, teklif ve sipariş durum tanımları (bloke/uyarı/muhasebeleştirilebilsin, uyarılacak ve yetkili kullanıcılar), teklif grup tanımları. Teklif değerlendirmeden satın alma talebine aktarım veya satın alma emri verilebilir. {0fO3cOSilws} {j_pzdctUbS4} {w2ApmwO6NNQ} {PCrP0gLQCtM} {Jmp3drkZNRc} {qeQ-GIppRtw} {v0By4KhUejQ}
- "Gönderilmiş e-Faturalar" yalnız gönderimi tamamlanmış faturaları listeler. {rW7tUeRDtZk}
- Satış faturasının üst bölümünde cari bilgileri, fiyatlandırma, toplu iskonto aktarımı, muhasebe entegrasyonu ve genel muhasebe özel alanı sekmeleri var. Toplu stok hareket fişi ile tek ekranda çok sayıda stok giriş/çıkışı kaydedilir. {hGXfZ4d-tlA} {c8qj9UdVjxw}
- Fatura, irsaliye ve sipariş grup tanımları Excel'e aktarılabilir; fatura özel raporu "gruplanacak alanlar" ile kurulur. Satın alma talep listesi stok, tedarikçi ve termin tarihine göre filtrelenir. {TJUZgGIFgAY} {CaroloyrCQk} {AWuhrnyASVY} {rKi-CtsOIRw} {ypjNKJynJOs}
- Teklif revize: teklifte İşlemler → "teklif revize işlemleri" ile yeni teklif formu oluşur; revize raporu eski ve yeni teklif no ile tarihlerini listeler. Cari bazlı sipariş raporunda üstte cari seçilince siparişleri altta listelenir. Hizmet raporunun hareketli sürümü hizmetin geçtiği belgeleri gösterir. {d8yG09Q4CqI} {guLJwWKvJ20} {cYdHq05_LPY}
- Ba/Bs formları ekranında forma girecek fatura tipleri seçilir ve fatura grubu, özel kod, unvana göre filtrelenir. {bUdhqgT9Ie4}
- Fatura raporu alt toplamları (satış/alış, KDV matrahı ve tutarı, iskonto, tevkifat), stok bazlı fatura raporu, masraf faturası özel raporu (gruplanacak alanlar), sipariş ihtiyaç listesi. {ZrulTG2OaJI} {W3ElAmS3CMI} {ZIQP9rEMeGg} {cu5PYjSogeE}
- Stok sipariş listesi (talep ekranı kayıtları: evrak no, talep ve termin tarihi) ve stok bazlı sipariş/irsaliye/teklif raporları; stok seçilince içinde geçtiği belgeler altta görünür. e-İrsaliye eşleştirme listesinden eşleştirme kaydı düzenlenebilir. {KQ_OwlAy8SY} {-2OVCm0fM-o} {D-FjMg5aOuM} {qNbeTax3ZTg} {d1dxNisptbA} {Nwuotmaosuo} {M3PnPyUT0Wk}
- Alış irsaliyesine stoklar Excel'den toplu aktarılabilir. Sipariş teslim raporunda "işlem miktarı" değiştirilerek sipariş kısmen (ör. 2 adetin 1'i) muhasebeleştirilebilir. {Btf14-QhTvc} {Gb6DDurnr4g}
- Araç tanımları: plaka, dorse plakası, tanım ve şoför; irsaliyenin taşıyıcı/şoför bilgilerine aktarılır. Transfer irsaliye raporu kaynak şube ve hedef duruma göre filtrelenir. {Pf0j-6VkZBo} {ki6xxDWPd34}
- Transfer talep ekranı ile şubeler arası transfer talebi oluşturulur. {VHsyhA79HdA}

### e-Belge
- e-Fatura / e-İrsaliye gelen kutusu eşleştirme: tedarikçi cari seçilir; gelen belge alış faturası mı masraf faturası mı olacak seçilir; hareket eşleştirme "özel" (tüm hareketleri tek satıra birleştirme veya kurala göre) ya da "stok bazında" (otomatik). Eşleştirme detayında adres karşılaştırma ve XML'de aranacak alan/veri kuralları; KDV oranı ve ek vergiler ayrıca eşlenir. {VvTLnm11ff8} {n_e2MemVLsg}
- e-İrsaliye durum sorgulama ekranı gönderilen belgelerin durumunu ve hatalarını gösterir. {hwwPtzeCO4Q}
- e-Fatura gönderimi ekranı: anlık hata yüzünden gönderilmemiş görünen faturalar elle onaylanır. Durum sorgulama portala gönderilmiş faturaların durumunu çeker. Durumu sorgulanan e-İrsaliyeler "gönderilmiş e-İrsaliyeler"e düşer. {XvSxJDb34H4} {SCw4eH0CmLE} {zG4-pXeUf8w}

### Genel Muhasebe
- Hesap planı: "varsayılan hesap planı" yalnız ana hesapları (100, 101, 102…) açar, alt/muavin hesaplar elle eklenir. Başka çalışma yılının hesap planı aktarılabilir. {6NL1wBmF8a4}
- Fişler: açılış, tahsil, tediye, mahsup ve kapanış. Ortak özellikler:
  - Otomatik KDV ayırma (aynı satıra / satır satır).
  - Satırlarda belge türü, fatura seri/no, e-Belge, Ba/Bs formu, firma, stok ve miktar, masraf merkezi, şube.
  - "Detay" ile satırın beyanname bilgileri (beyanname türü, KDV dönemi, tevkifat) girilir.
  - "Fiş bakiyesini / hesap bakiyesini / son satıra aktar", "KDV hesapla".
  - Kopyalama: kopyala, ters kopyala (borç/alacak yer değiştirir) ve özel kopyala (evrak no/açıklama korunsun, yenilensin ya da kopyalanmasın).
  - Kapanış fişi yıl sonu dışında kaydedilirse uyarı verir. {zKGlZwbAcRs} {g0K_3BNobXg} {Bc_OnCwP2_k} {HTGqw0SZ3dM}
- Hızlı fiş girişi tanımları: kod, fiş tipi, işlem tipi (alış/satış), KDV dahil/hariç, firma, KDV oranı, borç/alacak hesapları. Fişte şablon seçilip "aktar" ile tutar girilir ve "fiş oluştur" denir; tutar 0'dan büyük olmalıdır. {6_pDpSYbTKA}
- Z raporu girişi: ay seçilir, gün gün Z raporları (ör. kredi kartı + nakit tutarları) girilir; KDV tanımdaki orana göre hesaplanır. {1FMAgfZKekE}
- Zamanlanmış fiş: fişte "zamanlanmış fiş" işaretlenir; sonra işlemler > "zamanlanmış fişleri işleme koy" ile işaret kalkar ve fiş işlenir. {9xHUYB5JuzU}
- Hesap aktarma: bir hesabın bakiyesini tarih aralığıyla başka hesaba taşır (virman gibi). e-Defter kullanıcılarında beyan edilmiş aylar için yapılamaz; yalnız fiş kesinlik tarihinden sonraki kayıtlar aktarılır. {bs3AHe-_C98}
- Banka ekstresi aktarımı: tanımlı banka ekstre şablonu seçilir, Excel'den aktarılır (Excel'de formül olmamalı; videoya göre Excel lisanslı olmalı). Mevcut/yeni kayıt davranışı, tarih aralığı, döviz ve kur seçilir, ilk 10 kayıt ön izlenir. Hatalı satırlarda hata mesajı görünür; "fiş oluştur" ile muhasebe fişleri üretilir. {24Kd2LgwJSI}
- Tanımlar:
  - 7A sabitleri: "varsayılan yükle" ile 7/A yansıtma hesapları ve oranları gelir; oran bölünebilir (ör. %50 + %50). {UXVaDOKyc8Q}
  - KDV tanımları: orana göre alış/satış KDV hesapları, iade hesabı işareti. {EbXqadnKbqI}
  - Belge türü tanımları ("varsayılan yükle"), firma tanımları (beyanname ve raporlarda kullanılır), açıklama tanımları, fiş tipi tanımları (açılış, tahsil, tediye, mahsup, kapanış hazır gelir). {2WGPPW1MuJ0} {acAgToyG_BA} {Dc2h2j2Qw5I} {y-CcvoIMRss}
- Dönem işlemleri: kâr/zarar hesaplaması gelir ve gider hesaplarından kâr ve zarar fişlerini otomatik üretir. Maliyet hesaplaması envanter maliyet tipi ve maliyet hesabı seçilerek fiş oluşturur. {tlktBUo_oKQ} {7ypZydk0Oew}
- Raporlar: gelir tablosu (ayrıntılı/özet; satır formülleri "formül" ile düzenlenir: artı/eksi, net bakiye, borç/alacak bakiyesi veya toplamı; rapor kaydedilebilir), hesap durumu (aylık; birden fazla hesap virgülle), hesaplanan KDV listesi, stok envanter raporu, fiş listesi ve toplu fiş yazdırma. {YlhQBx8iq1M} {Gr90co4yrpk} {YLE2yyNhJOs} {1X7oghE_-bI} {KhFBw_qo8T8} {-QeBEy9coc8} {fDP2P_GTLT8}
- Hesap planı tablosu: alt hesap eklenirken bilanço grubu (aktif/pasif/yer almıyor) ve bilanço etkisi (+/−), özel kodlar, uluslararası birim kodu (envanter defteri için gerekli), KDV tanımı ve döviz birimi seçilir. Satırdan hesap hareketleri, hesap durumu, aylık/kesin mizan ve yardımcı deftere kısayol var. {HLH9VH8SWuc}
- Hesapların yansıtılması 7A/7B: 7A sabitlerindeki hesaplar (virgülle birden fazla, ör. 700,710) veya 7B hesapları ve dönem filtrelenir; tanımlı yansıtma oranlarıyla yansıtma fişi otomatik oluşturulur. {pKBXbrWWEPo} {gNtJCdgmxn8}
- Fiş işlemleri: fiş birleştirme (filtre + Ctrl/Shift ile seçim; "seçilenleri" veya "listelenen tümünü" birleştir; hareketleri gruplama seçeneği; birleştirilecek fiş sayısı uyarıda gösterilir), fiş sıralama (numaraları yeniden sıralar), fiş hareketleri raporu (satır bakiyesi, devirleri alt toplama ekleme). {7GzxusxRSWg} {C5j58yxvD_Y} {J_eZlgSPr0c}
- KDV tahakkuku (dönem sonu): ay, ödenecek vergi ve devreden KDV hesap kodları seçilerek tahakkuk fişi oluşturulur. Z raporu fiş oluştur: tanım ve ay seçilir; fiş günlük ya da aylık, numara otomatik veya belirli numaradan. {tah2Nr5j1UI} {UsXd3_uWVFA}
- Raporlar: kesin mizan (detay hesap seviyesi, bakiyesi olan hesaplar), nakit akım tablosu (satır formülleri; fiş tipine göre hesaplama), indirilecek KDV listesi, masraf merkezi durumu (aylık/kümülatif). Masraf merkezi tanımı: kod, ad, aktif durum, özel kodlar. {ffh8t28vKC8} {gHe039LdUjY} {Ky1l2skJaRU} {STzOc3u9raQ} {ZIuZO9w6SFw}
- Dönem sonu kapanış fişi: döviz bakiyeleri ve tarih filtresiyle hazırlanır. Hesap kartındaki "hesap bakiyesi" beklentisine (borç/alacak/sıfır; "−" ile dikkate alma) uymayan hesaplar bilgi mesajı olarak listelenir; bunlar hata değildir. Onaylanınca kapanış fişi aktif bakiyelere göre oluşur. {cY8VyKfKGC8}
- Bilanço (ayrıntılı): ters bakiye veren hesaplar için bilgi mesajı çıkar (ör. 119); hesap kartında bilanço grubu (aktif/pasif/yer almıyor) düzeltilince uyarı gider. {QnaEeYyWSsA}
- Fiş birleştirme (günlük): aynı tarihe ait fişleri tek fişte toplar. Entegrasyon fişleri birleştirilirse ön muhasebede yapılan sonraki düzeltmeler bu fişlere otomatik yansımaz. {k6boAwmEQP8}
- Fiş hareket sıra no güncelle (hareket sıra numaralarını yeniden verir; fiş sayısına göre uzun sürebilir) ve madde no sıralama (ay ve verilmeye hazır numara). {o6I1SEc10XM} {VWnVxw-0_lg}
- Virman hesabına aktarım: hesap kartında "virman hesabı" seçilir (ör. 100 → 142); dönem sonunda bakiye bu hesaba aktarılır. {xS6lBWMgo_w}
- Açılış ve kapanış mizanı: hesap aralığı, özel kodlar, listelenecek/dışlanacak hesaplar, detay seviyesi, hareketsiz ve bakiyesiz hesapları gösterme seçenekleri. {dstRqh6x7nY} {mDFqiaEFmxM}
- 7B sabitleri: hesap kodu, yansıtma hesabı ve oranı; "varsayılan yükle". {5o3GwOq9nwY}
- Masraf merkezi şablonu: şablon kodu ve adı, birden çok masraf merkezi ve yansıtma oranları; oranların toplamı %100 olmalıdır. Masraf merkezi hareket raporunda özel alanlara göre filtre eklenebilir. {9YjBcL6em6o} {F0a2oYWQm78}
- Fiş parçalama: seçilen fiş günlük, aylık, evrak no'ya göre veya günlük gruplanarak parçalanır. {IlReGv3_YNg}
- Z raporu tanımı: fiş ve satır açıklaması, yazarkasa no, KDV oranı ve hesap kodu, KDV dahil/hariç, borç/alacak hesapları. {FBuwv3rc9TA}
- Raporlar: aylık mizan (özel fiş tanımları dahil edilebilir), bilanço özet (ters bakiye uyarısı için hesap planındaki bilanço alanı kontrol edilir), yardımcı defter (devirleri al, dövizli yazdırma), basit yevmiye defteri (fiş toplamları, "son döküm" kaydı). Tediye fişi de diğer fişlerle aynı düzende. {WJCwFyZ0tag} {RkJn0UsfIv0} {CMas3-EJub8} {-7FTV7QHn0c} {E-JY1OcrPIg}
- Satışların maliyeti tablosu: satır seçilip "formüller"den hesap, hesap tipi (net bakiye, borç/alacak bakiyesi veya toplamı) ve isteğe bağlı fiş tipi tanımlanır; tanım sonraki dönemlerde de gelir. {0I1_-uNN9w4}
- Yevmiye defteri seçenekleri: fiş/satır açıklamaları, fiş no, borç/alacak bakiyeleri, madde numaralarını yeniden ver, miktarlar, tüm detay hesaplar, yalnız işlem görenler. {OrPkKlZLhb8}
- Genel muhasebe stok tanımı: stok kodu/adı, birim, grup, dönem sonu mal mevcudu, muhasebe ve maliyet muhasebe kodu. Defter-i kebir raporu, hareket sıralama, yansıtılan hesapların kapatılması 7B (önce "hesapların yansıtılması 7B" fişi oluşturulmuş olmalı) ekranları var. {afKSecqh_Q4} {y-IpBCaPnp4} {1ptOrPUJZkM} {sVMyZajSMqM}
- Mali tablolarda "önceki dönemleri aktar" ile daha önce kaydedilmiş rapor bilgileri önceki dönem sütunlarına çekilir. {aCaVICIqwpE}
- Yansıtılan hesapların kapatılması 7A: önce 7A yansıtması yapılmış olmalıdır; hesaplar virgülle girilir (ör. 700 ile 701'in kapatılması). {tpOjAEoCGs8}
- Hesap planı ekranında bilanço etkisi (+/−) ve hesap bakiyesi beklentisi (borç, alacak, sıfır veya etkilemiyor) seçilir; kapanış ve bilanço uyarıları bu alana göre çıkar. Uluslararası birim kodu seçimi önemlidir. Hesap planı Excel'e aktarılabilir. {Ar6tm9WUS7U}

### Beyanname
- WolvoxCloud'da beyanname ekranları var: damga vergisi, KDV 1, KDV 2 ve Muhtasar-SGK (MUHSGK). Her birinde idari bilgiler (vergi dairesi, dönem tipi, dönem, yıl), mükellef bilgileri, düzenleyen bilgileri ve dosya ekleri doldurulur. {CO1rhPdEwSk} {nTlM9xolmC8} {ee_KCv5WM5g}
- KDV 2: kesinti yapılan mükellefler ve tam/kısmi/isteğe bağlı tevkifat bildirimleri. Tutarlar formülden (işlem kodu + KDV oranı) veya "detay bilgi"den, yani genel muhasebe (YM) fişlerindeki detay bilgilerden hesaplanabilir. Eklerde ithalat bildirimleri ve isteğe bağlı tam tevkifat faturaları girilir. {nTlM9xolmC8}
- Muhtasar-SGK: vergiye tabi işlemler (vergi tür kodu, gayrisafi tutar, kesinti oranı; 5746 Ar-Ge ve teknoloji geliştirme bölgesi terkinleri), vergi bildirimi (çalışan sayısı, asgari ücret istisnaları), SGK bilgileri (personel satırları; "önceki beyanla aynı olduğunu beyan ederim" kutusu zorunlu; fazla mesai istihkaka/hak edilen ücrete dahil seçenekleri) ve ekler (iş yerleri, teknoloji geliştirme bölgesi stopaj teşviki, GVK 17 pay senedi). Hesaplama formülleri ekrandaki "notlar"da açıklanıyor. {ee_KCv5WM5g}
- KDV-1:
  - Beyan edilecek bilgi yoksa "beyan edilecek bilgim bulunmamaktadır" işaretlenir.
  - Matrah satırları elle, formülle (işlem türü + KDV oranı) veya "detay bilgilerden hesapla" (YM fiş detayları) ile doldurulur. Formüller sonraki beyannamelerde de geçerli kalır; elle eklenen satırlar yalnız o beyannameye aittir.
  - İndirimler yalnız elle veya formülle girilir. 7440 sayılı kanun ödemesi için "defaten / taksitle öde" seçeneği var.
  - İhraç kayıtlı teslimler, sonuç hesapları, ekler (sorumlu sıfatıyla ödenen KDV, 107/111 kodlu indirimler, 3065/13, teknoloji geliştirme bölgeleri, Hava Kuvvetleri katkı payı, tevkifat bildirimleri, 13. madde kapsamı) ve düzenleyen bilgileri doldurulur. {-wt-bsNTDHM}
- Muhtasar-SGK: vergi bildiriminde dönem tipi aylıksa yalnız 1. ay, 3 aylıksa üç ay doldurulur. Terkin tutarı alanları eklerden otomatik gelir; elle yazılan değer silinir. Ekler/işyeri bilgilerinde merkez veya mükellefiyetsiz şube kayıtları girilir; hesaplama kuralları "notlar"da. {QLQShfP6cLg}
- Beyanname listesi: beyanname türü, dönem, e-Beyan ve gönderim durumu; düzenleme ve silme. {N5B-puzxLwM}
- Beyanname vergi dairesi kodu: her beyanname türü için bir vergi dairesi kodu tanımlanır; aynı beyannameye ikinci kod eklenemez. {ZdcOXl72hUA}
- Muhtasar beyanname: vergiye tabi işlemlerde terkin tutarları kanuna göre (ör. 5084, 5225, 5746) ayrı gösterilir. Genel muhasebe entegrasyonunda satırlara hesap kodu ve isteğe bağlı fiş tipi (ör. yalnız mahsup fişleri) bağlanır. İşyeri bilgilerinde "diğer" seçilirse ticaret sicil numarasına 16 adet 9 yazılır. Ücret teşviki bildirimlerinde il kodu, ünite, işyeri sıra no ve aracı kodu girilir; "notlar"daki hesaplama açıklamalarına uyulmalıdır. {Szgr2rExaC4}

### Demirbaş
- Demirbaş tanımı: aktif/pasif, barkod, değer, hesap kodu, amortisman oranına göre otomatik bitiş yılı, güncel bilgiler (amortismanı alış fiyatından hesapla, güncel değer), KDV, miktar ve fiyat, satış bilgileri. Hesaplamalar yıl seçilince aylık amortismanı gösterir; amortisman tipi (ör. yıllık) değişirse "amortismanı yeniden hesapla" gerekir. Yeniden değerlemede tarih, artış oranı ve YM fiş tarihi girilir; "GM entegrasyonu yap" ile demirbaş ve birikmiş amortisman yeniden değerlenir ve "entegrasyon yap" ile muhasebeleşir. {dcwFj6vUW_c}
- Dönem raporu: cins, grup, barkod ve amortisman tipine göre filtrelenir. {UH9NDTjsd-Y}
- Demirbaş grup tanımları (ağaç yapısında, Excel'e aktarma) ve zimmet raporu (ad, departman, özel kod, kayıt tarihi, aktif/pasif). {A2GrteWW-GQ} {KjRP2MuZR40}
- Amortisman kontrol: filtrelenen demirbaşlar için açıklama ve YM fiş tarihiyle genel muhasebeye amortisman fişi oluşturulur; istenirse tek fişte birleştirilir. {cq5LdQPexTA}

## Tanıtım, duyuru ve içeriği kullanılamayan videolar

- {rVbBmPGZ4sk} (Cari kart birleştirme) videosunun otomatik altyazısı anlamsız (yanlış dil tanıma); içerik için {TsC-Xo23DcE} kullanıldı.
- {c1jUWqy0uoc} {z5Yer6joCss} {sHqFm63tpEc} {Sg8chIXDHKo} {JdOYnpolWWw} {Y2SKp3lYHLc} {oyLd99zKyhk}: tanıtım veya referans videoları; teknik bilgi yok. Hızlı Satış tanıtımında Android POS entegrasyonu, değişim kartı ve online terazi özellikleri sayılıyor.
- {avyXgcJLVVc} {GVo1tJJi4HQ}: otomatik altyazı anlamsız (yanlış dil). {g4Ik9imN-Pk} {mPkeXeRiUKg} {YAQ1uLLD_rI} {oV2jH1jvUq4} {fIQhJrlpzDs} {qLBwaD463dU} {xJfcI2A0yfU} {LmTaTIz3iJc} {jGUgFFLxg6Y} {wXGUfjP1hgE} {MwQ004As3DU} {sffYoceHBqY} {eZcwtAQHLcM} {0a410Lc5TqY} {WwtQraIqowk}: tanıtım, reklam, lansman ve röportajlar.
- Tanıtımlardan çıkan ürün bilgileri: Mobil Satış PDA ile sahada sipariş, fatura, tahsilat, yeni cari/stok kaydı, bluetooth yazıcıdan çıktı; gün sonunda veri merkeze aktarılır {mPkeXeRiUKg}. Garson çağrı sistemi: peçeteliklerde çağrı/hesap butonları, LED gösterge ve Restoran'da masa ikonları; Restoran PDA Android cihazlarla çalışır {qLBwaD463dU}. Yeni WOLVOX Otel özellikleri: A/B/C fiş yapısı (konaklama, ekstra ve özel ödeme kalemlerinin ayrılması), muhtelif gelir, odasız hesaplar (spa, salon, restoran) ve housekeeping görev atama {c8d6V3imeGg}. Restoran, AKINROBOTICS servis robotlarıyla entegre çalışabilir {wXGUfjP1hgE}.
- {JD_O450d0TI} {gstAP-hRCi8} {nEmYKxngKJg}: yalnız müzik, altyazıda içerik yok.
- WolvoxAI: ERP'de doğal dille (yazılı veya sesli) soru sorup rapor alma asistanı (ör. "bu ay hiç satılmayan ürünler"); SQL bilgisi gerekmez. {Q4mGGfq_sCg} {UgNSp7Mubfs}
- WOLVOX 9: modül ve kullanıcı sayısı ihtiyaca göre seçilir; güncelleme paketi bir yıl boyunca yeni sürümleri kapsar. {t0isSx9RXRE}
- WOLVOX Web Entegrasyon: e-ticaret sitesi ile ERP arasında sipariş, stok, fatura, cari, müşteriye özel fiyat/iskonto ve kategori senkronizasyonu. {sQFVRQRKHaQ}
- {7oLyqg39DdA}: Restoran tanıtımı (AKINROBOTICS servis robotu entegrasyonu).
- {XZukADbFg7o}: MRP II tanıtımı (anlık üretim panosu: aktif/geciken iş emirleri, ilerleme yüzdesi, makine durumu). {iqxbO73Qr3I}: Mobil Satış tanıtımı (Android telefon/tablet/PDA; Windows Mobile sürümü; Mobile Server; Bluetooth yazıcı).
- {8lRt98rQ7dg}: otomatik altyazı anlamsız (yanlış dil).
- {VkuF_3QQODQ}: WOLVOX Otel tanıtımı.
