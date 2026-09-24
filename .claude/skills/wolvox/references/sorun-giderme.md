# Sorun giderme

Her sorunda önce şunu sor: **Wolvox sürümü nedir (7/8/9/26), veritabanı Firebird mi MSSQL mi, tek bilgisayar mı çok kullanıcılı mı, hata mesajının tam metni ne?**

## Bağlantı sorunları

### "Unable to complete network request to host '...'"
Firebird istemcisi veritabanı sunucusuna ulaşamıyor (Firebird'ün genel hata mesajı).
1. Sunucuda Firebird servisi çalışıyor mu? (Windows Hizmetler → Firebird Server)
2. Kontrol Paneli sunucuda açık mı?
3. İstemcideki **Sunucu Ayarları** doğru mu (IP ve port 3055)? Sunucu IP'si DHCP ile değişmiş olabilir. Sunucuya sabit IP verilmesini öner.
4. Güvenlik duvarı/antivirüste **3050, 3054, 3055, 3056** açık mı?
5. Host `127.0.0.1` ise yerel servis kapalıdır. Örneğin e-İrsaliye gönderirken bu hatayı alıyorsan yerel Firebird/Kontrol Paneli bağlantısını kontrol et.

### İstemci sunucuya bağlanamıyor
- `kurulum-ve-yonetim.md` dosyasındaki "Server/client bağlantısı" adımlarını izle.
- İstemciden `ping <sunucu-ip>` ve `Test-NetConnection <sunucu-ip> -Port 3055` (PowerShell) ile ağı test et.

### Uzaktan erişim çalışmıyor
- Modemde port yönlendirme: Firebird için 3050, 3054, 3055, 3056, 80. MSSQL için 3055, 3056.
- Mümkünse port açmak yerine **VPN** öner. Açılacaksa önce `masterkey` parolasını değiştir.

## Lisans

### "Lisanslanan client sayısı aşılmış. Veritabanı yöneticinize başvurunuz."
- Sebep: Lisans, bağlanan makine isimleriyle sayılıyor. Makine değişince veya makine kodu değişince sayı dolmuş görünür.
- Çözüm: Kontrol Paneli → **Yetkili → WOLVOX Lisans → Client Tanımları** → ilgili programı seç → eski kayıtları sil (Bilgi Bankası 697). PDA/el terminali için de aynısı.

## Veritabanı ve SQL hataları

### "Dynamic SQL Error"
- AKINSOFT'a göre bu hatalar **veritabanıyla ilgili değil**. Girilen veriden (geçersiz karakter, alan uzunluğu, hatalı tarih) veya işletim sisteminden (bölgesel ayarlar, tarih/ondalık ayırıcı) kaynaklanır (Bilgi Bankası 1976).
- Kendi özel raporunda/SQL'inde alıyorsan sorgu sözdizimi, tablo veya alan adı hatalıdır.
- Kontrol et: Windows bölge ayarı Türkçe mi, tarih/ondalık ayırıcı standart mı, son girilen kayıtta alışılmadık karakter var mı.

### Kontrol Paneli güncellemesinden sonra "Field not found"
- Genelde **sürüm uyuşmazlığından** olur (bu bir çıkarım): Kontrol Paneli ve veritabanı güncellenmiş, istemcideki program eski kalmış (veya tersi).
- Tüm bilgisayarlardaki programları aynı sürüme güncelle. Veritabanı güncellemesinin tamamlandığından emin ol.

### Hareket işlerken "PRIMARY KEY" hatası
- Aynı anahtarla ikinci kayıt eklenmeye çalışılıyor. Genelde sayaç/generator ile tablo verisi uyumsuz olduğunda, ör. dışarıdan elle kayıt eklendikten veya eksik bir geri yüklemeden sonra.
- Kalıcı çözüm için bayi veya AKINSOFT destekle çalış. Veritabanında elle generator değiştirme riskli, önce yedek al.

### İstemcilerin bağlantısı sık sık kopuyor (Firebird kopma sorunu)
- AKINSOFT'un çözümü (Bilgi Bankası 460; İngilizce 2856):
  1. Önce yedek al.
  2. Kurulu Firebird'ü kaldır.
  3. **Firebird 2.1.7 veya 2.5.4, 32 bit (win32)** sürümünü kur.
- Aynı sürümler, sorun yaşanan diğer AKINSOFT programlarında da kullanılabiliyor.

### "Uyumsuz Firebird sürümü" uyarısı
Bilgisayardaki Firebird sunucusu programın beklediği sürüm değil (Bilgi Bankası 373).
1. `C:\Windows\System32` (64 bit sistemde `SysWOW64`) içinde `GDS32.DLL` var mı kontrol et. Yoksa Firebird servisini durdurup kurulu sürümün aynısını yeniden kur.
2. Sorun sürüyorsa:
   1. **Denetim Masası → Programlar ve Özellikler**'den Firebird'ü kaldır.
   2. `C:\Program Files\Firebird` klasörünü sil (64 bit sistemde `Program Files (x86)` altında).
   3. Gerekli sürümü indirip **hiçbir seçeneği değiştirmeden** kur.
- Firebird kaldırılıp kurulunca AKINSOFT programının veritabanı parolası **`masterkey`**'e döner.
- Ayrıntılı kaldırma rehberi: "Firebird Silmek ve Yeniden Kurmak" (Bilgi Bankası 3306).

### "Unsupported on-disk structure for file ..."
- Veritabanı dosyasının yapısı (ODS) kurulu Firebird sürümüyle uyumsuz. Genelde dosya Firebird 2.x ile oluşturulmuş, makinede başka bir sürüm (ör. 3.0+) var, ya da Kontrol Paneli'nde DBUpdate sırasında yanlış sürüm devrede.
- Çözüm:
  1. Önce `.fdb` dosyasının kopyasını al.
  2. Firebird'ü durdurup kaldır. `System32`/`SysWOW64` altındaki `fbclient.dll` ve `gds32.dll` dosyalarını sil.
  3. Firebird 2.5 (32 bit) kur, bilgisayarı yeniden başlat, DBUpdate'i tekrar dene.
- Kaynak bayi rehberi (akinsoft.bireysel.com.tr). Firebird SSS: firebirdfaq.org/faq80.
- Wolvox dosyasını kendi aracınla (Python, DBeaver) açarken de bu hatayı alırsın. Firebird 2.5 istemcisi kullan (`veritabani-ve-sql.md`).

### Latin dışı karakterler "?" olarak kaydediliyor
- Firebird veritabanında Unicode desteği yok. Arapça, Kiril gibi karakterler gerekiyorsa MSSQL Unicode veritabanına geç (Bilgi Bankası 3592, `kurulum-ve-yonetim.md`).

### MSSQL: "CREATE or ALTER ASSEMBLY for assembly 'Wolvox7Udf_mssql' ..."
- SQL Server'da `clr strict security` seçeneği 1 olduğunda çıkar (SQL Server 2017+ varsayılanı). Wolvox'un CLR fonksiyon assembly'si yüklenemiyor.
- AKINSOFT'un çözümü (Bilgi Bankası 3187): AKINSOFT programlarını kapat, SQL Server Management Studio'da **her veritabanı için** makaledeki kodları çalıştır.
- Microsoft'un genel önerisi: assembly'yi sertifikayla imzalamak veya `sp_add_trusted_assembly` ile güvenilir yapmak.
- `clr strict security`'yi sunucu genelinde kapatmak güvenlik riskidir. Makaledeki yöntemi tercih et.

### Veritabanı bozulması şüphesi
- Önce **dosyanın kopyasını** al, orijinali değiştirme.
- Kontrol Paneli yedek/geri yükleme veya Firebird `gbak -b` / `gbak -c` ile yedekten yeniden oluştur. Onarım için `gfix` kullanılır; risklidir, uzman desteği öner.

## e-Dönüşüm hataları
`e-donusum.md` dosyasındaki "Sık hatalar" bölümüne bak ("Tutamaç yanlış durumda", "Invalid InvoiceId", kamu faturası, firma kontrolü).

## Genel tanı kontrol listesi

1. Hatanın tam metni ve ekran görüntüsü.
2. Sürüm: program "Hakkında" ekranı ve Kontrol Paneli sürümü aynı mı?
3. Sorun tek bilgisayarda mı, hepsinde mi? Tek bilgisayardaysa istemci/ağ, hepsindeyse sunucu/veritabanı.
4. Son yapılan değişiklik: güncelleme, Windows güncellemesi, antivirüs, IP değişikliği, devir, geri yükleme?
5. Herhangi bir düzeltme denemeden önce **yedek**.
6. Çözülemezse: yetkili bölge bayisi veya AKINSOFT destek hattı (444 40 80).
