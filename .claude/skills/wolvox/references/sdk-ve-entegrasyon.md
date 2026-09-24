# SDK ve entegrasyonlar

## WOLVOX SDK

Kaynaklar (2026-09-24'te tam okundu):
- Resmi "AKINSOFT Wolvox9 SDK Doküman" v1.02.01 (2024, 25 sayfa). WOLVOX 26 için yayımlanan "Wolvox SDK Doküman" (Aralık 2025, 26 sayfa) içerik olarak aynı, komutlar ve XML yapısı değişmemiş.
- Bilgi Bankası 257 (Wolvox 8/9) ve 3994 (WOLVOX 26+).
- AKINSOFT'un Delphi (W8, W9, WOLVOX 26) ve C# (W8) demo projeleri, makalelerin ekinde.

Doküman AKINSOFT'un izni olmadan çoğaltılamaz; burada sadece kendi cümlelerimizle teknik özet var. Ayrıntı için PDF'leri oku:
- Wolvox 9: `https://akinsoft.net/bilgibankasi/data/upload/257/wolvox9_sdk_dokuman1734088631.pdf` veya `https://bilgibankasi.akinsoft.net/tr/home/dosyaindir?blkodu=1034`
- WOLVOX 26: `https://bilgibankasi.akinsoft.net/tr/home/dosyaindir?blkodu=1046` (Delphi demo: `blkodu=1047`)

### Ön koşullar
- SDK **çözüm ortaklarına** yönelik. Kullanmadan önce AKINSOFT **Lisans departmanından SDK lisansı** açtırılmalı.
- Girişte AKINSOFT'un verdiği **geliştirici kodu (`devCode`) ve geliştirici parolası (`devPass`)** gerekir.
- AKINSOFT SDK için **teknik destek vermiyor**. Doküman ve demo projeler esas.

### Mimari ve bağlantı
- **Kontrol Paneli'ne gömülü bir HTTP servisi.** Adres: `http://<KontrolPaneli-IP>:<güncelleme portu>/getdata.html`. Güncelleme portu varsayılan olarak **3056**.
- **GET:** Parametre dizisinin tamamı (`command=...&tpwd=...` kısmı) **Base64 (UTF-8) ile kodlanıp** `getdata.html?` sonrasına eklenir.
- **POST:** Adres `http://<ip>:3056/` olur. Gövdeye `DATA=<base64(parametre dizisi)>` gönderilir.
- **Yanıtın tamamı Base64 kodludur.** Çözünce düz metin veya XML çıkar.
- **Oturum:**
  1. `command=wlogin&username=<kullanıcı>&password=<MD5(parola)>&devCode=..&devPass=..&timeOut=<dakika>` gönderilir. Parola **MD5 hash** olarak gider, kullanıcının Wolvox yetkileri aynen geçerli olur. Oturum varsayılan olarak 60 dakika sürer.
  2. Başarılı yanıt `1&<geçici parola>`, hatalı yanıt `0&<hata mesajı>` biçimindedir.
  3. Sonraki her istekte **`tpwd=<geçici parola>`** gönderilir.
  4. İş bitince `command=wlogout&tpwd=..`.
- Çoğu komut **`sirketKodu`** ve **`calismaYili`** ister. Önce `get_sirketliste` ile yetkili olunan şirket, yıl ve şubeler alınır.

### Veri okuma komutları (`get_*`, dönüş XML)
| Komut | Ne döndürür | Önemli ek parametreler |
|---|---|---|
| `get_sirketliste` | Yetkili şirketler, çalışma yılları, şubeler | — |
| `get_carilist` / `get_carihrklist` | Cari kartları / cari hareketleri | `ekSart`, `fieldList` |
| `get_caribakiyeler` / `get_caribakiye` | Cari bakiyeleri (toplu / tek cari) | `ekSart` / `blCrKodu` |
| `get_carivadesigecenborc` | Vadesi geçen borç | `blcrkodu`, `paraBirimi` |
| `get_caritaksitdetay`, `get_carikredilist` | Cari taksitleri, kredi bilgileri | `blCrKodu` |
| `get_stoklist` | Stoklar ve fiyatları | `ekSart`, `fieldList` |
| `get_stokbarkodbul`, `get_stokpaketbul` | Barkoddan stok veya paket bulma | `barcode` |
| `get_stokenvanter` / `get_depoenvanter` | Stok / depo envanteri | `envHesabi`, `maliyetTipi`, `tarih1`, `tarih2`, `doviziDahilEt`, `sadeceMikEnv`, `stokEkSart`, `envSubeSart`, (`depoEkSart`) |
| `get_serilotbakiye` | Seri/lot bakiyeleri | `ekSart`, `fieldList` |
| `get_faturalist` / `get_faturadetay` | Fatura listesi / tek fatura | `ekSart`, `fieldList` / `blftkodu` |
| `get_irsaliyelist` / `get_irsaliyedetay` | İrsaliye listesi / detayı | / `blirkodu` |
| `get_siparislist` / `get_siparisdetay` / `get_siparisdurumtanim` | Sipariş listesi / detayı / durum tanımları | / `blmaskodu` |
| `get_kasalist`, `get_depolist`, `get_dovizlist`, `get_parabirimleri`, `get_bankaposliste` | Tanım listeleri | `ekSart`, `fieldList` |
| `get_dovizkur` | Bir dövizin belirli tarihteki kuru | `dovizBirimi`, `tarih`, `subeKodu` |
| `get_faturaanalizi`, `get_ceksenetanalizi`, `get_kasahrkanalizi`, `get_carihrkanalizi` | ERP'deki analiz raporları | `analizTipi`, `KPBDVZ`, `analizHesap`, `subeSart`, `ekSart` |
| `get_gunsonuraporu1` | Gün sonu raporu (günlük ve genel) | Çok sayıda `Gun*`/`Gnl*` parametresi (tarih aralıkları, şube, para birimi, dahil edilecek işlem türleri) |
| `get_kisitlialandegerleri` | Sınırlı (enum) alanların değer-metin listesi | — |
| `get_ozelalantanimlistesi` | Özel alan tanımları | — |
| `get_yoneticiekrani` | Yönetici ekranı verisi | — |
| `get_hotelcheckinlist` | Otel check-in listesi | `subeSart`, `ekSart` |

**Ortak parametreler:**
- **`ekSart`:** `AND` ile başlayan SQL koşulu, ör. ` AND CARI.ILI = 'KONYA'`.
- **`subeSart`:** Şube filtresi, ör. ` AND CARI.SUBE_KODU IN ('MERKEZ','SUBE')`.
- **`fieldList`:** Dönecek alanlar, virgülle ayrılır, ör. `CARIKODU,TICARI_UNVANI`.
- **`analizTipi`:** 1 günlük, 2 haftalık, 3 aylık, 4 üç aylık, 5 altı aylık, 6 yıllık.
- **`KPBDVZ`:** 1 = KPB (kendi para birimi), 0 = döviz. Döviz seçilirse `analizHesap` alanına döviz birimi yazılır.
- **Tarih formatı:** `gg.aa.yyyy` veya `gg.aa.yyyy sa:dk:sn`.
- **`maliyetTipi`:**
  - 1–4: Alış Fiyatı 1–4
  - 5: En Son Alış
  - 6: Ortalama Alış
  - 7: Ortalama Ağırlıklı Alış
  - 8: En Ucuz Alış
  - 9: En Pahalı Alış
  - 10: LIFO
  - 11: FIFO

### Veri yazma komutları (`postxml_*`)
- Komut `command=postxml_<tür>&tpwd=..&sirketKodu=..&calismaYili=..&xmlValue=<XML>` biçiminde gönderilir. Resmi demo, `get_sirketliste` dışındaki her komutta şirket kodu ve çalışma yılını ekliyor.
- Başarılı yanıt `BLKODU=<yeni kayıt no>`, hatalı yanıt `Error : <mesaj>`. SDK test programı başarıyı `XML_POST_OK^MBLKODU=339` gibi gösteriyor.
- Türler: `cari`, `carihrk`, `stok`, `stokhrk`, `fatura`, `faturaiptal`, `irsaliye`, `siparis`, `teklif`, `kasahrk`, `kasatransfer`, `ceksenet`, `servisfis`, `stoksayimi`.

**XML kuralları:**
1. Yapı dokümandaki örneklerle **birebir aynı** olmalı. Alan eklenip çıkarılabilir; alan adları veritabanındaki tablo alanlarıyla aynıdır.
2. Değerler `<![CDATA[...]]>` içinde yazılır.
3. XML içindeki her **`&` karakteri `|*` ile değiştirilir**, çünkü `&` HTTP parametre ayracı.
4. Fatura, irsaliye ve siparişte iskonto istenmiyorsa iskonto alanları **açıkça 0** gönderilir. Aksi halde carinin veya stoğun tanımlı iskontoları otomatik uygulanır.
5. Ondalıklar **virgülle** yazılır (`5,00`). Belge içi tarih alanları (ör. `VADESI`, `TARIHI`) örneklerde **Delphi TDateTime sayısı** olarak geçiyor (ör. `40826` gün sayısı; 30.12.1899'dan itibaren).
6. `<AYAR>` bloğunda **`TRSVER`** (işlem DLL sürümü) zorunlu. Ayrıca veritabanı (`DBFILENAME` = tam `.FDB` yolu veya `DBNAME`), kaydeden kullanıcı (`PERSUSER`) ve şube (`SUBE_KODU`) yer alır.

**Kök etiketler ve `TRSVER` değerleri (doküman v1.02.01):**
| Kayıt | Kök | Ana blok | Alt bloklar | TRSVER |
|---|---|---|---|---|
| Fatura | `WFT` | `FATURA` | `FATURAHAREKET/HAREKET`, `FATURAKUR/HAREKET`, `KAPALIFATURA/HAREKET` (ödemeler) | `ASWFT1.02.03` |
| Cari | `WCR` | `CARI` | — | `ASWCR1.02.03` |
| Cari hareket | `WCH` | `CARIHAREKET/HAREKET` | — | `ASWCH1.02.03` |
| Stok | `WST` | `STOK` | `STOKFIYAT/FIYATLAR` | `ASWST1.02.03` |
| Stok hareket | `WSH` | `STOKHAREKET/HAREKET` | — | `ASWSH1.02.03` |
| İrsaliye | `WIR` | `IRSALIYE` | `IRSALIYEHAREKET`, `IRSALIYEKUR` | `ASWIR1.02.03` |
| Sipariş | `WSP` | `SIPARIS` | `SIPARISHAREKET`, `SIPARISKUR` | `ASWSP1.02.03` |
| Teklif | `WTK` | `TEKLIF` | `TEKLIFHAREKET`, `TEKLIFKUR` | `ASWTEK1.02.01` |
| Servis fişi | `WSRFS` | `SERVISFIS` | `FISHAREKET`, `FISISLEMLER/ISLEMLER/PERSONELLER`, `FISKUR` | `ASWSF1.02.01` |
| Stok/depo sayımı | `WSTSY` | `STOCKTAKING/ROW` | — | `ASWSTDPSY1.02.01` |
| Kasa transferi | `WKH` | `TRANSFER` | — | `ASWKSTRS1.02.01` |
| Kasa hareket, çek/senet | — | — | — | `ASWKH1.02.03`, `ASWCS1.02.03` |

**Sık kullanılan alanlar:**
- **Fatura başlığı:** `FATURA_DURUMU`, `BLCRKODU` (+ carinin unvan/vergi/adres alanları), `KDV_DURUMU` (1 = KDV dahil), `KPBDVZ_CARI`, `ISK_KUL_*` / `ISK_ORAN_*` / `ISK_TUTAR_*`, `FATURA_NO` veya `SAYAC_TANIMI` (sayaç verilirse numara otomatik), `VADESI`, `ACIKLAMA`, `DOVIZ_KULLAN`, `PAZ_*` (pazarlama personeli).
- **Fatura satırı:** `BLSTKODU`, `STOK_ADI`, `BARKODU`, `MIKTARI`/`BIRIMI` (+ `_2` ikinci birim), `KDV_ORANI`, `KPB_FIYATI`, `DEPO_ADI`, `DVZ_FIYATI`/`DOVIZ_BIRIMI`/`DOVIZ_ALIS`/`DOVIZ_SATIS`, `MUH_KODU_GENEL`.
- **Kapalı fatura (ödeme):** `ISLEM_TURU` (cari hareket türü), `KASA_ADI`, `KPB_ATUT`.
- **Stok fiyatı:** `FIYAT_NO` (kaçıncı fiyat), `FIYATI`, `HESAP` (para birimi), `ALIS_SATIS` (1 alış, 2 satış), `TANIMI`.
- **Stok hareketi:** `BLSTKODU`, `DEPO_ADI`, `KPB_FIYATI`, `MIKTAR_2`, `TUTAR_TURU` (1 giriş, 0 çıkış).
- **Cari hareketi:** `BLCRKODU`, `ISLEM_TURU`, `TARIHI`, `KPB_ATUT` (alacak) / `KPB_BTUT` (borç), `KASA_ADI`, `GM_ENTEGRASYON` (1 = Genel Muhasebe'ye işle).

### Sabit kod tabloları (enum değerleri)
Bunlar veritabanında da aynı kodlarla tutulur, SQL yazarken de kullanılır.

- **`FATURA.FATURA_DURUMU`:**
  - 1 Yurt içi satış
  - 2 Yurt içi satıştan iade
  - 3 Yurt dışı satış
  - 4 Yurt dışı satıştan iade
  - 5 Alış
  - 6 Alıştan iade
  - 7 Masraf faturası
- **`CARIHR.ISLEM_TURU`:**
  - 1 Devir, 2 Evrak, 3 Nakit, 4 Dekont
  - 5 Kredi kartı, 6 POS, 7 Çek, 8 Senet
  - 9 Fatura, 10 İrsaliye
  - 12 Virman, 13 Tahakkuk, 14 Bonus, 15 Servis, 16 Sipariş
  - 101–105: 1.–5. özel tanım
- **`IRSALIYE.IRSALIYE_DURUMU`:** 1 Giden, 2 Gelen, 3 Transfer.
- **`SIPARIS.SIPARIS_DURUMU`:** 1 Beklemede, 2 Muhasebelendi, 3 Arşiv, 4 İptal, 5 Onaylandı, 6 Kısmi muhasebelendi.
- **`SIPARIS.SIPARIS_TURU`:** 1 Yurt içi alınan, 2 Yurt içi verilen, 3 Yurt dışı alınan, 4 Yurt dışı verilen.
- Diğer enum alanların değerleri için `get_kisitlialandegerleri` komutunu çağır.

### SDK ile entegrasyon yazarken önerilen yaklaşım
1. Test şirketinde çalış. Önce `wlogin` → `get_sirketliste` → `get_carilist` (küçük `fieldList` ile) zincirini doğrula.
2. İstek ve yanıtı Base64 kodlama/çözme katmanı yaz, parolayı MD5'le. Demo projeler (Delphi, C#) referans.
3. Yazma için dokümandaki XML örneğinden başla, `&` → `|*` dönüşümünü ve CDATA'yı unutma. Yanıtı ayrıştır: `BLKODU=` ile başlıyorsa başarılı, `Error :` ile başlıyorsa hata.
4. Kimlik bilgilerini (Wolvox kullanıcısı, devCode/devPass) ortam değişkeninde tut. 3056 portunu internete açma; gerekiyorsa VPN kullan.

## Script paketleri

- WOLVOX ERP hazır **script paketleri** yükleyerek genişletilebiliyor: **Yetkili → Tanımlar → Script Paketi İşlemleri** → indirilen dosyayı seç, yükle, parametre değerlerini girip kaydet.
- Örnek: **Konaklama vergisiyle fatura kesme scripti** (Bilgi Bankası 3561). Asgari sürümler: Kontrol Paneli s8.04.12, ERP s8.24.02, Otel s8.08.15. Parametreler: konaklama vergisi oda fiyatına dahil mi (Evet/Hayır), satış ve alış için konaklama vergisi muhasebe kodları. Genel Muhasebe kullanılıyorsa kodlar zorunlu.
  - Ön koşul: ERP genel ayarlar → fatura ayarları → satış faturasında **KDV kullanımı** seçili olmalı. Konaklama vergisi işaretlenince "Döviz Kullan" pasifleşir.
- Hızlı Satış'ta desteklenmeyen teraziler için script yazılıyor. Özel raporlarda da script sekmesi var (`veritabani-ve-sql.md`).

## AKINSOFT e-Ticaret ↔ WOLVOX ERP (Web Entegrasyon, WWB9)

- **WOLVOX Web Entegrasyon programı**, AKINSOFT e-Ticaret sunucusuyla otomatik haberleşir. Siparişleri ERP'ye aktarır. Stok, sipariş, fatura ve cari verileri senkronize edilir.
- e-Ticaret yönetim panelinde: **Entegrasyonlar → Ticari Program Yönetimi → "Tam Senkronizasyon"** seçili olmalı. Böylece ERP'deki tüm stok işlemleri e-Ticaret paneline yansır (Bilgi Bankası 492).

### Bağlantı kurulumu (Bilgi Bankası 2207)
1. **e-Ticaret panelinde:** **Kullanıcılar → Yöneticiler → Yeni Ekle** → tür olarak **"Muhasebe Kullanıcısı"** seçilip kullanıcı oluşturulur.
2. **Web Entegrasyon programında:** **Ayarlar** → **Genel** sekmesi → **Web Sitesi Ayarları**:
   - **Site Adresi:** e-ticaret sitesinin adresi, **`http://` ile** yazılır (`https`'deki "s" olmadan), ör. `http://test.com`.
   - **Kullanıcı Adı / Şifre:** 1. adımdaki muhasebe kullanıcısı.
   - **Test Et** → başarılıysa bağlantı kuruldu.

### Diğer ayarlar
- **Sipariş kayıt ayarları** (3065, 3907):
  - Üye olmadan alışveriş yapan müşteriler, siparişteki bilgilerle ERP'de cari olarak açılabiliyor.
  - e-Ticaret'teki Ek Bilgi, Promosyon Kodu ve Kargo Barkodu alanları, ERP'deki alınan sipariş ekranının özel tanım başlıklarıyla eşleştirilebiliyor.
  - Siparişler aynı anda **iki şirkete** kaydedilebiliyor. 2. şirket için sabit bir cari kodu verilebilir veya boş bırakılırsa her siparişten cari oluşturulur.
- **Cari ayarları** (3068):
  - Müşteri e-Ticaret'te adresini değiştirince ERP'deki cari adresinin otomatik güncellenmesi seçilebiliyor.
  - e-Ticaret'e hangi carilerin aktarılacağı özel kod alanı değerine göre filtrelenebiliyor.
- **Stok ayarları** (3039), **sanal pazar virman hesapları** (3072).
- **Taksit entegrasyonu** (3473; video `86qscM7yBow`, `JJXK_VkTPqk`):
  - ERP'de cariye oluşturulan taksitler e-Ticaret'e aktarılır, müşteri sitede görüp ödeyebilir. Ödenen taksit bir süre sonra ERP'de "Ödendi" olur.
  - Gereksinim: e-Ticaret'te **Online Tahsilat** modülü, ERP'de **Banka** ve **Taksit Takip** modülleri, Kontrol Paneli **s.8.03.96+**, ERP **s.8.22.12+**.
  - e-Ticaret'te Ticari Program Yönetimi ekranında **"Carinin taksit borçları görüntülenebilsin ve ödeme yapılabilsin"** seçeneği işaretlenir.
- **B2B/B2C/müşteri tipine göre ürün gösterimi** (2680):
  1. ERP'de stok tanımlarındaki **Özel Alan Tanımı** ile **veri tipi "Metin"** olan bir alan açılır.
  2. e-Ticaret panelinde **"Gösterilecek Üye Tipi"** bu alanla eşleştirilir. Böylece bir ürün bayilere görünüp üyelere gizlenebilir.
- **e-Ticaret + ERP + Genel Muhasebe** (3119): Web Entegrasyon'un Genel Muhasebe bölümünde **"Yeni Cariler İçin Varsayılan Muhasebe Kodları"** (Alış Kodu, Satış Kodu) tanımlanır. e-Ticaret'ten gelen yeni cariler ERP'ye bu kodlarla kaydolur.
- e-Ticaret tarafında gelişmiş fiyat listesi de var (3510).

### Üçüncü taraf e-ticaret ve pazaryeri entegratörleri
T-Soft, Sentos, Entegra Bilişim, Ayen Software ve Projesoft (B2B) Wolvox entegrasyonu sunuyor. Genelde gereken bilgiler: Wolvox bağlantı/API bilgileri, firma ve ambar/depo tanımları, ürün-varyant kod yapısı, fatura seri/sıra şeması, e-Fatura/e-Arşiv yetkileri.

## WebConnect (IWM9)

- ERP'ye tarayıcıdan (masaüstü, telefon, tablet) erişim sağlayan web uygulaması.
- Cari, Kasa, Stok, Fatura, Sipariş, Servis, İrsaliye, Günsonu ve Restoran raporları. Veri girişi de yapılabiliyor.
- **Kurulum ve bağlantı** (Bilgi Bankası 1526; eski makale 537):
  1. WebConnect'i aç → **Port Ayarları**. Varsayılan çalışma portu **8888**. Başka program kullanıyorsa değiştir.
  2. Bu portu modemden WebConnect bilgisayarına yönlendir.
  3. Kontrol Paneli → **Kullanıcı İşlemleri → Kullanıcı Yetkilendirme** → personeli ve şirketi seç → **Program Kullanım Yetkileri**'nde **WebConnect**'i işaretle → Yetkileri Kaydet.
  4. Tarayıcıdan `http://<sabit-dış-IP>:8888` adresine gir.
- MSSQL kullanılıyorsa **SQL Server 2012+** gerekir.

## WOLVOX Reporter (ARP2) ve mobil uygulamalar

- Android'den ERP'ye bağlanıp rapor alma.
- Mobil Satış (APD9) sahada senkronize çalışıyor (`sektorel-programlar.md`).
- Mobil uygulamalarda güncelleme paketi (WOL UP/GP) kontrolü var (Bilgi Bankası 3868).

## WOLVOX ERP ↔ Genel Muhasebe

Entegrasyon iki yolla yapılır:
1. **Anlık entegrasyon:** ERP'de **"Genel Muhasebe Sistemi Kullan"** işaretlenir ve **Anlık Entegrasyon** seçilir. ERP'deki işlemler anında Genel Muhasebe'ye yansır.
2. **Toplu entegrasyon:** Aynı ayarda **Toplu Entegrasyon** seçilir. Sonra:
   - ERP'de: **Diğer İşlemler → G.Muhasebe → Entegrasyon Dosyası Oluştur** (XML üretir).
   - Genel Muhasebe'de: **Fiş İşlemleri → Fiş Oluşturma → Transfer Dosyasından Fiş Oluştur** → XML'i seç → "Toplu Fiş Oluşturma" ekranı açılır.
- **Hesap kodu eşleştirme:** Carileri tek bir muhasebe koduyla izlemek için cari kartında **"Muh. Alış Kodu"** ve **"Muh. Satış Kodu"** alanlarına kod yazılır. Çek/senet hesap kodları ayrıca ayarlanır.
- Genel Muhasebe e-Defter ile entegre çalışıyor (WDF9). Demirbaş amortismanları da Genel Muhasebe'ye aktarılabiliyor.
- Kaynak: Bilgi Bankası 969. Video: Ufuk Aydın, "Wolvox Genel Muhasebe Nasıl Kullanılır? Entegrasyon ve Örnekli Anlatım" (`E4VGhPMoRcQ`).
