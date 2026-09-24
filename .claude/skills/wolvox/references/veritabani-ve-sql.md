# Veritabanı, tablolar ve SQL

## Veritabanı motorları

- **Firebird** (varsayılan, en yaygın). Kullanıcı `SYSDBA`, varsayılan parola `masterkey` (değiştirilmediyse). Port **3050**.
  - **Sürüm:** AKINSOFT, Wolvox için **Firebird 2.1.7 veya 2.5.4, 32 bit (win32)** öneriyor (Bilgi Bankası 460, 2856). İşletim sistemi 64 bit olsa bile AKINSOFT programları genelde 32 bit Firebird ile çalışır.
  - Veritabanı dosyası ODS 11 yapısında (Firebird 2.x). **Firebird 3/4/5 bu dosyayı doğrudan açamaz**, "unsupported on-disk structure" hatası verir. Modern Firebird'de açmak için önce Firebird 2.5'in `gbak` aracıyla yedek (`.fbk`) alıp sonra yeni sürümde geri yüklemek gerekir. **Bunu sadece kopya üzerinde yap**, Wolvox'un kullandığı dosyayı asla yükseltme.
  - **Unicode yok:** Latin dışı karakterler (Arapça, Kiril) `?` olur (Bilgi Bankası 3592). Türkçe karakterler için bağlantı charset'i büyük olasılıkla `WIN1254`. Bu doğrulanmadı; bozuk gelirse `NONE` ile dene.
- **MSSQL** destekleniyor. Firebird'den MSSQL'e geçiş "Veritabanı Transfer İşlemi" ile yapılır (MSSQL Server 2008+, WebConnect varsa 2012+). Unicode ihtiyacı varsa MSSQL Unicode collation seçilir. Ayrıntılar `kurulum-ve-yonetim.md` dosyasında. Bazı bayiler, uzman desteğin yoksa Firebird'de kalmanı öneriyor.
  - MSSQL tarafında Wolvox bir **CLR assembly** (`Wolvox7Udf_mssql`) kullanıyor. SQL Server 2017+'da `clr strict security` açık olduğu için "CREATE or ALTER ASSEMBLY" hatası çıkabilir (`sorun-giderme.md`).
- Yedekleme tarafında MySQL de destekleniyor.
- Firebird veritabanı dosyası, Firebird servisinin çalıştığı makinenin **yerel diskinde** olmalı. Ağ sürücüsü (paylaşımlı klasör) üzerinden çalışmaz.

## Dosya yerleşimi

- **Firebird:** Program kurulum dizinindeki **`DATABASE_FB`** klasörü (ör. `C:\AKINSOFT\Wolvox9\DATABASE_FB`, eski sürümlerde `...\AKINSOFT\WOLVOX8\DATABASE_FB`).
- **MSSQL:** **`DATABASE_MSSQL`** klasörü.
- Bilinen dosya adları:

| Dosya | İçerik |
|---|---|
| `wolvox.fdb` | Sistem / Kontrol Paneli veritabanı: şirket tanımları, kullanıcılar, yetkiler, lisans/client tanımları. **Hassas** |
| `sirket.fdb` | Şirketin ticari verisi (cari, stok, fatura…). Geri yükleme ekranında bu adla listelenir, MSSQL karşılığı `sirket.mdb`. Kullanıcı kurulumunda iki dosyanın varlığı doğrulandı (2026-09) |
| `gmuhasebe.fdb` | Genel Muhasebe |
| `ikaynak.fdb` | İnsan Kaynakları |
| `imuhasebe.fdb`, `dosya.fdb` | Kaynaklarda geçiyor, içeriği doğrulanmadı |

- Birden fazla şirket veya çalışma yılında dosyaların klasörlere nasıl dağıldığı doğrulanmadı. Kesin yol için kullanıcının `DATABASE_FB` klasörüne veya Kontrol Paneli'ndeki şirket/veritabanı ayarlarına bak. **Tahmin etme.**
- Wolvox 9 için hazır boş veritabanları ve etiket dizaynları (Argox raf etiketi vb.) Bilgi Bankası 3836'da indirilebiliyor. MRP II için ayrı veritabanı var.

## Anahtar yapısı: BLKODU

- **`BLKODU`** her tablonun benzersiz kayıt numarası (primary key).
- İlişkiler `BL<kısaltma>KODU` biçimindeki yabancı anahtarlarla kurulur:

| Alan | Gösterdiği tablo |
|---|---|
| `BLCRKODU` | `CARI.BLKODU` |
| `BLSTKODU` | `STOK.BLKODU` |
| `BLFTKODU` | `FATURA.BLKODU` |
| `BLMASKODU` | Ana (master) kaydın `BLKODU`'su. Detay tablolarında kullanılır (ör. `STOK_FIYAT_LISTE_DT`) |

- SDK kayıt fonksiyonları başarılı olunca yeni kaydın BLKODU'sunu döndürür (`BLKODU=1234`).

## Bilinen tablolar ve alanlar

Kaynaklarda doğrulanmış olanlar:

| Tablo | Açıklama | Bilinen alanlar |
|---|---|---|
| `CARI` | Cari kartları | `BLKODU`, `CARIKODU`, `TICARI_UNVANI`, `ADI`, `SOYADI`, `GRUBU`, `ARA_GRUBU`, `ALT_GRUBU`, `DOVIZ_KULLAN`, `DOVIZ_BIRIMI` |
| `CARIHR` | Cari hareketleri | `BLCRKODU` |
| `STOK` | Stok kartları | `BLKODU`, `STOKKODU`, `STOK_ADI`, fiyat alanları |
| `STOKHR` | Stok hareketleri | `BLSTKODU` |
| `FATURA` | Fatura başlıkları | `BLKODU` |
| `FATURAHR` | Fatura satırları | `BLFTKODU`, `BLSTKODU`, `MIKTARI`, `KPB_ARA_TUTAR` |
| `STOK_FIYAT_LISTE` | Fiyat listesi başlığı | `BLKODU`, `FIYAT_TANIMI` |
| `STOK_FIYAT_LISTE_DT` | Fiyat listesi detayı | `BLMASKODU`, `BLSTKODU`, `STOK_TANIMI` |

> Sipariş, irsaliye, kasa, banka ve çek/senet tablolarının aynı adlandırmayı izlemesi muhtemel (`SIPARIS`/`SIPARISHR` gibi) ama **kaynakta doğrulanmadı**. Gerçek şemayı öğrenmek için Firebird sistem tablolarını sorgula:
>
> ```sql
> -- Kullanıcı tabloları
> SELECT TRIM(RDB$RELATION_NAME) FROM RDB$RELATIONS
> WHERE COALESCE(RDB$SYSTEM_FLAG, 0) = 0 ORDER BY 1;
>
> -- Bir tablonun alanları
> SELECT TRIM(RDB$FIELD_NAME) FROM RDB$RELATION_FIELDS
> WHERE RDB$RELATION_NAME = 'FATURA' ORDER BY RDB$FIELD_POSITION;
> ```
>
> MSSQL'de `INFORMATION_SCHEMA.TABLES` ve `INFORMATION_SCHEMA.COLUMNS` kullanılır.

## Örnek sorgular

```sql
-- Tüm cariler / stoklar (Excel'e aktarmak için SQL Monitör'de)
SELECT * FROM CARI;
SELECT * FROM STOK;

-- Cari ve hareketleri
SELECT *
FROM CARI CR1
LEFT JOIN CARIHR CRHR1 ON (CRHR1.BLCRKODU = CR1.BLKODU);

-- Fiyat listesine göre satış miktarı/tutarı
SELECT STOK_FIYAT_LISTE.FIYAT_TANIMI,
       STOK_FIYAT_LISTE_DT.STOK_TANIMI,
       SUM(FATURAHR.MIKTARI)       AS "MIKTAR TOPLAM",
       SUM(FATURAHR.KPB_ARA_TUTAR) AS "TUTAR TOPLAM"
FROM STOK_FIYAT_LISTE_DT
INNER JOIN STOK_FIYAT_LISTE ON STOK_FIYAT_LISTE.BLKODU = STOK_FIYAT_LISTE_DT.BLMASKODU
INNER JOIN FATURAHR        ON FATURAHR.BLSTKODU        = STOK_FIYAT_LISTE_DT.BLSTKODU
INNER JOIN FATURA          ON FATURA.BLKODU            = FATURAHR.BLFTKODU
GROUP BY STOK_FIYAT_LISTE.FIYAT_TANIMI, STOK_FIYAT_LISTE_DT.STOK_TANIMI;
```

## Program içinden SQL çalıştırma

### SQL Monitör
- WOLVOX programlarında yerleşik. Yazılan sorgular raporlanabilir ve Excel'e aktarılabilir (tabloda sağ tık → Aktar).

### Özel raporlar
1. **Özel Raporlar → Özel Rapor İşlemleri → Yeni Rapor Ekle**.
2. "SQL Rapor Adı" alanına rapor adını yaz, SQL kodu alanına sorguyu yaz.
3. **SQL Kodunu Çalıştır (F9)** ile test et. "SQL Kodu Başarıyla Çalıştı" mesajı gelmeli.
4. **Kaydet**. Sonra "Seçili Raporu Düzenle / Sil / Aç" ile yönetilir. Açınca filtrelenebilir.
- **Script sekmesi:** Özel rapor tanımında bir **Script** sekmesi var. Buradaki **"Çift Tıklama"** sayfasına kod yazılırsa, rapor grid'inde bir satıra çift tıklanınca ilgili kart açılır (ör. fatura numarasına çift tıklayınca o fatura). Kod önce seçili alanın boş olmadığını kontrol eder, sonra örneklerdeki "kartı aç" komutlarını çağırır (Bilgi Bankası 739). Komutların tam sözdizimi için makaleyi oku.

### Dış araçlarla okuma
- **Excel + ODBC** (Bilgi Bankası 704):
  - Firebird: **Firebird ODBC sürücüsünü** kur, sonra **Denetim Masası → Yönetimsel Araçlar → Veri Kaynakları (ODBC)** üzerinden DSN ekle. Excel'den bu DSN ile bağlanıp kendi raporunu tasarla.
  - SQL Server: **SQL Server Native Client** kur. Kurulumdan sonra WOLVOX ERP'yi kapatıp açınca raporlama kesintisiz çalışır.
- **Genel Firebird araçları:** `isql` (Firebird ile gelir), FlameRobin, IBExpert, DBeaver.
- **Python (Firebird 2.5 dosyası):**

  ```python
  # pip install fdb   (Firebird 2.5 istemcisiyle çalışır)
  # DİKKAT: Python'un bit sayısı fbclient.dll'in bit sayısıyla aynı olmalı.
  # Wolvox 32 bit Firebird kurar; 64 bit Python kullanıyorsan 64 bit Firebird 2.5 istemcisi (fbclient.dll) gerekir.
  import os
  import fdb

  con = fdb.connect(
      dsn="localhost:C:/wolvox-kopya/sirket.fdb",  # her zaman KOPYA dosya
      user="SYSDBA",
      password=os.environ["WOLVOX_FB_PASSWORD"],     # koda gömme
      charset="WIN1254",                             # bozuk gelirse "NONE" dene
  )
  cur = con.cursor()
  cur.execute("SELECT CARIKODU, TICARI_UNVANI FROM CARI")
  for row in cur.fetchall():
      print(row)
  con.close()
  ```

  Firebird 3+ istemcisiyle çalışan `firebird-driver` paketi ODS 11 dosyasını doğrudan açamaz (yukarıdaki sürüm notuna bak).

- **isql ile şema dökümü (Windows, kopya dosyada):**

  ```bat
  "C:\Program Files (x86)\Firebird\Firebird_2_5\bin\isql.exe" -user SYSDBA -password <parola> "localhost:C:\wolvox-kopya\sirket.fdb"
  SQL> SHOW TABLES;
  SQL> SHOW TABLE CARI;
  ```

  Tam DDL dökümü için: `isql -x -user SYSDBA -password <parola> "localhost:C:\wolvox-kopya\sirket.fdb" -o sirket_sema.sql`. Bu sadece yapıyı yazar, veriyi yazmaz. Firebird'ün kurulu olduğu yol makineye göre değişir.

## Güvenlik ve veri bütünlüğü kuralları

1. **Doğrudan veritabanına yazma** (`INSERT`/`UPDATE`/`DELETE`). Program iş kuralları, bakiyeler, hareket bağlantıları ve BLKODU üretimi atlanır, veri tutarsızlaşır. Veri eklemek için **SDK**, **Excel Transfer** veya **Web Entegrasyon** kullan.
2. Okuma sorgularını mümkünse **yedek veya kopya veritabanında** çalıştır. Canlıda uzun süren sorgular kullanıcıları yavaşlatır.
3. Canlı Firebird dosyasını servis çalışırken dosya olarak kopyalama. Önce servisleri durdur (`kurulum-ve-yonetim.md`, Bilgi Bankası 942) ya da `gbak`/Kontrol Paneli yedeklemesini kullan.
4. Parolaları koda veya repoya yazma. `.fdb`, `.fbk`, `.mdb` dosyalarını git'e ekleme (repodaki `.gitignore` bunları dışlıyor).
5. `wolvox.fdb` içinde kullanıcı ve yetki bilgileri var. Şemasını çıkarmak serbest, **verisini okuma veya paylaşma**.
