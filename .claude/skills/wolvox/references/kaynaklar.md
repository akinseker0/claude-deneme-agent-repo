# Kaynaklar: dokümanlar, videolar, siteler

**Tarihçe:**
- 2026-09-24 ilk sürüm: ağ kısıtlıyken web arama özetlerinden derlendi.
- Aynı gün ağ erişimi açıldıktan sonra:
  - Bilgi Bankası'nın `sitemap.xml`'indeki **1411 Türkçe makaleden 1410'unun tam metni indirildi ve okundu**. Eksik olan tek makale 3690, 3683'ün Azerice sürümü.
  - Wolvox 9 **SDK PDF'i** ve resmi Delphi demo kaynağı okundu.
  - YouTube ve Dailymotion **video başlıkları** listelendi.
  - Ardından Wolvox videolarının **Türkçe altyazıları ve açıklamaları** okundu; özetler `video-ozetleri.md` dosyasında.

**Nerede ne var:**
- Makale özetleri `bilgibankasi-ozetleri.md` dosyasında. Telif nedeniyle tam metinler repoda yok; `python tools/bilgibankasi.py oku <no>` ile yerelde açılır.
- Makalelerin tam listesi (numara, başlık, kategori, adres) `bilgibankasi-dizini.json` dosyasında.

**Durum anahtarı:**
- **okundu:** tam metin okundu ve bilgi tabanına işlendi.
- **indirildi (özetlenmedi):** tam metin önbellekte var ama özetlere ayrıca yazılmadı. Konu büyük ölçüde başka makalelerle kapsanıyor ya da ürün Wolvox dışında.

## Resmi Bilgi Bankası (bilgibankasi.akinsoft.net)

Adres biçimi: `https://bilgibankasi.akinsoft.net/tr/home/makale/<no>-<slug>`. İngilizce makaleler `/en/home/makale/...`. Kategori listesi: `/tr/home/makalelistesi?kat=<no>`.

### Kurulum, sürüm, lisans
| No | Başlık | Durum |
|---|---|---|
| 221 | WOLVOX Programı Kurulum Talimatı | okundu |
| 3655 | WOLVOX 8 Programı İndirme ve Kurulum Talimatı | okundu |
| 3832 / 3839 | WOLVOX (9) Programı İndirme ve Kurulum Talimatı | okundu |
| 2799 / 4004 | Wolvox setup / download & installation (İngilizce) | okundu |
| 1302 | Eski sürümlerden program indirme | okundu |
| 3831 | Önceki sürümlerden Wolvox 9'a upgrade | okundu |
| 1145 | Önceki sürümlerden Wolvox 8'e upgrade | okundu |
| 3852 | WOLVOX 9 Upgrade Processes (İngilizce) | okundu |
| 3864 | Wolvox 9 Client Upgrade | okundu |
| 3829 | Wolvox 9'da online lisans alma | okundu |
| 697 | "Lisanslanan client sayısı aşılmış" uyarısı | okundu |
| 351 / 3863 | Sürüm güncelleme işlemleri (8 / 9) | okundu |
| 3817, 3732, 1586 | Sürüm notları (ERP 9.02.01, Kontrol Panel 8.04.24, İK 8.07.01) | okundu |
| 3868 | Mobil uygulamalarda güncelleme paketi kontrolü | okundu |

### Bağlantı, kullanıcı, yetki
| No | Başlık | Durum |
|---|---|---|
| 308 | Server/client bağlantı ayarları | okundu |
| 1894 | SQL Server kullanıcıları için server/client ayarları | okundu |
| 211 | MSSQL ile uzaktan erişim için açılması gereken portlar | okundu |
| 1673 | Kontrol Paneli kullanıcı kayıt ve yetkilendirme | okundu |
| 1802 | Hızlı kullanıcı yetkilendirme | okundu |
| 3287 | Wolvox ERP admin panel access (İngilizce) | okundu |

### Veritabanı, yedekleme
| No | Başlık | Durum |
|---|---|---|
| 798 | Yedekleri geri yükleme | okundu |
| 942 | Firebird tabanlı programlarda datadan yedek alma/geri yükleme | okundu |
| 943 | MSSQL tabanlı programlarda datadan yedek alma/geri yükleme | okundu |
| 1893 | Tüm detayları ile AKINSOFT Yedekleme programı | okundu |
| 3177 | AKINSOFT Yedekleme programı ile SQL yedekleme/geri yükleme | okundu |
| 1655 | OctoPlus'ta yedek alma ve geri yükleme | okundu |
| 1684 | Veritabanı transfer işlemi (Firebird → MSSQL) | okundu |
| 3592 | Firebird'ü SQL Unicode veritabanına dönüştürme | okundu |
| 3836 | Wolvox 9 hazır database ve dizaynlar | okundu |
| 460 / 2856 | Firebird veritabanında kopma sorunu (TR / EN) | okundu |
| 373 | Uyumsuz Firebird sorunu | okundu |
| 3306 | Firebird silmek ve yeniden kurmak | okundu |
| 3187 | 'Wolvox7Udf_mssql' assembly hatası çözümü | okundu |
| 441 | Excel'den cari ve stok kart aktarımı | okundu |
| 1124 | Cari ve stok kayıtlarının tüm alanlarını Excel'e aktarma | okundu |
| 704 | ODBC (Firebird/MSSQL) ile dinamik Excel raporlama | okundu |
| 739 | Özel raporda grid'e çift tıklayıp kart açma (script) | okundu |
| 1976 | "Dynamic SQL Error" hatası | okundu |

### SDK ve entegrasyon
| No | Başlık | Durum |
|---|---|---|
| 257 | WOLVOX ERP Programı SDK İşlemleri | okundu |
| 3994 | WOLVOX SDK İşlemleri (WOLVOX 26+) | okundu |
| 969 | ERP ile Genel Muhasebe entegrasyonu | okundu |
| 492 | AKINSOFT e-Ticaret ile ERP entegrasyon ayarları | okundu |
| 2207 | Web Entegrasyon genel ayarlar (e-Ticaret bağlantısı) | okundu |
| 3065 / 3907 | Web Entegrasyon sipariş kayıt ayarları / 2. şirket | okundu |
| 3068 | Web Entegrasyon cari ayarları | okundu |
| 3039 | Web Entegrasyon stok ayarları | okundu |
| 3072 | Web Entegrasyon sanal pazar virman hesapları | okundu |
| 3473 | e-Ticaret & ERP taksit entegrasyonu | okundu |
| 2680 | Ürünlerin B2B/B2C/müşteri tipine göre gösterimi | okundu |
| 3119 | e-Ticaret + ERP + Genel Muhasebe entegrasyonu | okundu |
| 3510 | e-Ticaret'te gelişmiş fiyat listesi | okundu |
| 1526 / 537 | WebConnect bağlantı ayarları | okundu |
| 3561 | Konaklama vergisi ile fatura kesme script çalışması | okundu |

### e-Dönüşüm
| No | Başlık | Durum |
|---|---|---|
| 1801 | Tüm detayları ile Wolvox e-Fatura işlemleri | okundu |
| 3199 | e-Faturada dış modül bağlantı bilgileri | okundu |
| 2146 | Kamu kurumlarına e-Fatura nasıl düzenlenir | okundu |
| 3042 | Kamu faturası gönderim hatası kontrol listesi | okundu |
| 3713 / 3715 | Gelen e-Faturayı irsaliye / sipariş ile eşleştirme | okundu |
| 719 | ERP'den e-İhracat faturası gönderimi | okundu |
| 2686 | Restoran programı otomatik e-Fatura gönderimi | okundu |

### ERP kullanımı
| No | Başlık | Durum |
|---|---|---|
| 655 | Wolvox ERP Servis modülü | okundu |
| 1060 | Mal fazlası çalışma sistemi | okundu |
| 311 | Gelişmiş satış fiyat listesi | okundu |
| 626 | Satış fiyat listesi oluşturma | okundu |
| 1276 | Alış ve satış fiyatlarını otomatik oluşturma | okundu |
| 3538 | Wolvox Maliyet Muhasebesi | okundu |

### Sektörel programlar ve yardım dosyaları
| No | Başlık | Durum |
|---|---|---|
| 651 | Wolvox Restoran kullanımı | okundu |
| 706 | Restoran ve Restoran Lite farkları | okundu |
| 2266 | Restoran masa kroki sistemi | okundu |
| 3680 | Restoran otomatik üretim | okundu |
| 3657 | Restoran şubelere tanım kopyalama | okundu |
| 3687 / 3841 | Restoran Android PDA kurulumu / PDA yardım dosyası | okundu |
| 3543 | Hızlı Satış fiş tasarımına para üstü vb. ekleme | okundu |
| 1487 / 2418 | Hızlı Satış yardım dosyası / dokümanı | okundu |
| 1433 / 3844 | Otel yardım dosyası | okundu |
| 3549 | Otel konaklama vergisini aktif etme | okundu |
| 1458 | İnsan Kaynakları yardım dosyası (8) | okundu |
| 1672 / 3851 | Genel Muhasebe yardım dosyası | okundu |
| 1527 / 578 | Beyanname yardım dosyası | okundu |
| 1508 / 3853 | Demirbaş yardım dosyası | okundu |
| 2657 | CafePlus yardım dosyası | okundu |

## PDF dokümanlar

- Wolvox9 SDK Dokümanı (2024): `https://akinsoft.net/bilgibankasi/data/upload/257/wolvox9_sdk_dokuman1734088631.pdf`. **Okundu**. İşlenmiş hali `sdk-ve-entegrasyon.md` dosyasında. Kopyalanması ve dağıtılması yasak olduğu için metni repoda yok.
- WOLVOX ERP e-katalog: `https://www.akinsoft.com.tr/programlar/e-katalog/pdf/erp_v4.pdf`, `erp_v5.pdf`
- Genel Muhasebe e-katalog: `https://www.akinsoft.com.tr/programlar/e-katalog/pdf/genel-muhasebe_v6.pdf`
- e-Ticaret e-katalog: `https://www.akinsoft.com.tr/programlar/e-katalog/pdf/e-ticaret-v7.pdf`
- Kontrol Paneli tanıtım PDF'i (bayi): `https://www.akinsoft.istanbul/tanitim/wolvox/kontrolpaneli/wolvox_kontrolpaneli.pdf`
- Restaurant yardım dosyası PDF'i (bayi): `https://www.akinsoft.istanbul/tanitim/wolvox/adisyon/restaurant.pdf`
- Eski çevrimiçi yardım (Wolvox ön muhasebe): `https://www.akinsoft.com.tr/program_w/wolvox_yardim/wolvox_on_muh_yardim/...`

## Videolar

**Başlıkların tam listesi** (WolvoxCloud 408, WOLVOX ERP 355, Restoran 61, e-Ticaret 100, Octo 33… ve 94 Dailymotion videosu) `video-dizini.md` dosyasında. WolvoxCloud başlıklarından çıkarılan menü ağacı `menu-haritasi.md` dosyasında.

**Altyazılar okundu (2026-09-24):** Wolvox ile ilgili Türkçe YouTube videolarının otomatik Türkçe altyazıları indirildi (yt-dlp, `web_embedded` istemcisi) ve okundu. İşe yarayan bilgi `video-ozetleri.md` dosyasına kaynak `{video ID}` ile yazıldı. Ayrıntı:
- Wolvox ile ilgili 946 Türkçe videonun (538 WOLVOX ERP ve diğer ürünler, 408 WolvoxCloud) 906'sının altyazısı alındı ve okundu. 40 videonun Türkçe altyazısı yok (istek sınırına takılanlar yeniden denendi).
- WolvoxCloud videoları kısa ekran tanıtımları olduğu için yalnız yeni bilgiler not alındı. En değerlisi 104 dakikalık resmi WolvoxCloud eğitimi (`W0NOHUVbouA`, Temmuz 2026).
- **Video açıklamaları** okundu ama neredeyse hepsi yalnız başlığı tekrarlıyor, ek bilgi yok. **Dailymotion** açıklamaları da yalnız eski `akinsoft.net/programlar/prg.php?id=…` ürün sayfası bağlantılarından ibaret.
- Tanıtım, röportaj ve reklam videoları içerik açısından boş; `video-ozetleri.md` dosyasının son bölümünde listelendi. Birkaç videonun otomatik altyazısı yanlış dil tanıması yüzünden anlamsız.
- Otomatik altyazıda ses tanıma hataları var ("volvoks", "wallbox" = Wolvox gibi). Kesin menü yolu ve ayar adı için programın kendisi veya Bilgi Bankası esas alınmalı.
- Ham altyazılar telif nedeniyle repoya konmadı.

**Kanallar ve oynatma listeleri**
- AKINSOFT Eğitim (YouTube): `https://www.youtube.com/user/AKINSOFTEgitim` (kaynaklara göre 180'i aşkın Wolvox eğitim videosu)
- AKINSOFT Eğitim (Dailymotion): `https://www.dailymotion.com/akinsoftegitim`. Örnekler: "WOLVOX ERP Stok Kart Kaydı" (`x1nkxun`), "WOLVOX ERP Özel Rapor İşlemleri" (`x221t2f`), "WOLVOX ERP Fatura Tasarımı" (`x1nc924`)
- Oynatma listesi "Akınsoft Wolvox 9 Eğitimleri": `PLHhZkXOqwqsBpyQN62OXBC7BTAAldMrD7`
- Oynatma listesi "WOLVOX ERP": `PLn1dufQyGqvtpK2lGVMxm9MAyN32mjViK`
- Eski AKINSOFT video yardım sayfası: `http://www.akinsoft.net/programlar/video-yardim/index.php`

**Tekil videolar (YouTube ID)**
| ID | Başlık |
|---|---|
| `-06N6myRruk` | AKINSOFT Wolvox 8 Cari, Fatura, Stok Eğitimi 1 |
| `YdlVzsc4f5w` | AKINSOFT Wolvox 8 Cari, Fatura, Stok Eğitimi 2 |
| `J_DvbS7Igeg` | AKINSOFT Wolvox 8 Cari, Fatura, Stok Eğitimi 3 |
| `XdI8wx-rbg0` | Wolvox Temel Eğitim |
| `IG18WtMpHxo` | AKINSOFT WOLVOX ERP 9 |
| `WNwN67gI4PY` | Akınsoft Wolvox ERP 9 Çıktı |
| `0K4JlV1Cz1Y` | WOLVOX ERP Fatura Tasarımı (Fatura Dizayn) İşlemleri |
| `GrlugoZA0ew` | WOLVOX 8 ERP e-Fatura, e-Arşiv ve e-İrsaliye İşlemleri |
| `BvOAu0TGRd0` | Wolvox Web Entegrasyon Programı Nedir? Nasıl Kurulur? |
| `86qscM7yBow` | AKINSOFT e-Ticaret ve Wolvox 9 ERP Taksit Entegrasyonu |
| `JJXK_VkTPqk` | AKINSOFT e-Ticaret ve Wolvox ERP Taksit Entegrasyon İşlemleri |
| `E4VGhPMoRcQ` | Wolvox Genel Muhasebe Nasıl Kullanılır? Entegrasyon ve Örnekli Anlatım (Ufuk Aydın) |
| `v-RNfIKvKe0` | Akınsoft Wolvox 8'de Kullanıcı Tanımlama ve Yetkilendirme |
| `bsJd2E6hebQ` | WOLVOX 8 "Lisanslanan Client Sayısı Aşılmış" hatasının çözümü |
| `4UbVWP4pmF0` | Wolvox PDA cihazlar için lisanslanan client sayısı aşılmış |

**Ücretli kurs:** Udemy, "Akınsoft Wolvox ERP ve Cari Stok Yönetimi Eğitimi".

## Ekran görüntüleri

Ekran görüntüleri repoya **konmadı** (telif ve boyut nedeniyle). Her makalenin görsel adresleri `tools/bilgibankasi.py oku <no>` çıktısının `RESIMLER:` satırında yer alır. Gerektiğinde agent görseli indirip okuyabilir; bu yöntemle [4081] makalesinin GIF'indeki SQL örneği okundu. Kullanıcı kendi ekran görüntüsünü paylaşırsa agent onu da okuyabilir.

## Üçüncü taraf ve bayi kaynakları

Resmi değiller. Çapraz kontrol için kullan.
- ufukaydin.net: Wolvox hata ve çözümleri, SQL Monitör, Excel transferi, port ayarları, e-Fatura hataları
- netprogramlama.com: özel rapor, SQL örnekleri, kurulum, devir
- blog.medyadizayn.com.tr: e-Fatura/e-Arşiv, lisans, hata çözümleri
- akinsoft.bireysel.com.tr: 2026 tarihli rehberler (Unsupported ODS, MSSQL yedekleme, kamu e-Fatura, eski sürüm indirme)
- akinsoftistanbul.net (bilgi kütüphanesi), akinsoftizmir.com.tr, akinsoftistanbulbb.com, akinsoftkurumsal.com.tr, blog.dijitalkobi.com.tr: Bilgi Bankası makalelerinin kopyaları ve rehberler
- musteri.akinsoftizmir.com.tr/knowledge-base: Bilgi Bankası makalelerinin kopyaları (resmi site erişilemezse alternatif)
- ercsoft.com.tr, akinsoftcekmekoy.com.tr: yıl sonu devir rehberleri
- Entegratörler: tsoft.com.tr, sentos.com.tr, entegrabilisim.com, ayensoftware.com, teknik.projesoft.com.tr
