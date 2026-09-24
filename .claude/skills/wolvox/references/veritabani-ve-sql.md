# Veritabanı, tablolar ve SQL

## Veritabanı motorları

- **Firebird** (varsayılan, en yaygın). Kullanıcı `SYSDBA`, varsayılan parola `masterkey` (değiştirilmediyse). Port **3050**.
- **MSSQL** destekleniyor. Firebird'den MSSQL'e geçiş "Veritabanı Transfer İşlemi" ile yapılır (MSSQL Server 2008+). Bazı bayiler, uzman desteğin yoksa Firebird'de kalmanı öneriyor.
- Yedekleme tarafında MySQL de destekleniyor.
- Firebird veritabanı dosyası, Firebird servisinin çalıştığı makinenin **yerel diskinde** olmalı. Ağ sürücüsü (paylaşımlı klasör) üzerinden çalışmaz.

## Dosya yerleşimi (Firebird)

- Veritabanları program kurulum dizinindeki **`DATABASE_FB`** klasöründe durur (ör. `...\AKINSOFT\WOLVOX8\DATABASE_FB`).
- Bilinen dosya adları: `wolvox.fdb` (sistem/Kontrol Paneli), `gmuhasebe.fdb` (Genel Muhasebe), `imuhasebe.fdb`, `ikaynak.fdb` (İnsan Kaynakları), `dosya.fdb`, ayrıca her şirketin kendi veritabanı dosyası.
- Kesin dosya adı ve yolu için kullanıcının kendi `DATABASE_FB` klasörüne veya Kontrol Paneli'ndeki şirket/veritabanı ayarlarına bakılmalı. **Tahmin etme.**

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
- Özel raporda grid'e çift tıklayınca ilgili kartı açtırmak mümkün (Bilgi Bankası 739).

### Dış araçlarla okuma
- **Excel + ODBC:** Firebird ODBC sürücüsü veya MSSQL ile Excel'den dinamik bağlantı kurulup raporlanabilir (Bilgi Bankası 704).
- **Genel Firebird araçları:** `isql` (Firebird ile gelir), FlameRobin, IBExpert, DBeaver.
- **Python (Firebird):**

  ```python
  # Firebird 3+ istemcisi için: pip install firebird-driver
  # Firebird 2.5 için: pip install fdb (API benzer: fdb.connect(...))
  from firebird.driver import connect

  con = connect(
      "192.168.0.10/3050:C:/AKINSOFT/WOLVOX8/DATABASE_FB/<SIRKET_DOSYASI>.FDB",  # gerçek yolu doğrula
      user="SYSDBA",
      password="<parola>",   # koda gömme; ortam değişkeninden oku
      charset="WIN1254",     # Türkçe karakterler bozuksa UTF8 dene
  )
  cur = con.cursor()
  cur.execute("SELECT CARIKODU, TICARI_UNVANI FROM CARI")
  for row in cur.fetchall():
      print(row)
  con.close()
  ```

  Kurulu Firebird sürümü (2.5 / 3 / 4) ve karakter seti kurulumdan kuruluma değişebilir. Bağlanmadan önce kontrol et.

## Güvenlik ve veri bütünlüğü kuralları

1. **Doğrudan veritabanına yazma** (`INSERT`/`UPDATE`/`DELETE`). Program iş kuralları, bakiyeler, hareket bağlantıları ve BLKODU üretimi atlanır, veri tutarsızlaşır. Veri eklemek için **SDK**, **Excel Transfer** veya **Web Entegrasyon** kullan.
2. Okuma sorgularını mümkünse **yedek veya kopya veritabanında** çalıştır. Canlıda uzun süren sorgular kullanıcıları yavaşlatır.
3. Canlı Firebird dosyasını, servis çalışırken dosya olarak kopyalama. `gbak` veya Kontrol Paneli yedeklemesini kullan.
4. Parolaları koda veya repoya yazma.
