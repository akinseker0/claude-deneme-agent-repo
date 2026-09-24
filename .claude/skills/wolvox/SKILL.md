---
name: wolvox
description: AKINSOFT ve WOLVOX bilgi tabanı (WOLVOX ERP, Kontrol Paneli, Genel Muhasebe, Hızlı Satış, Restoran, Otel, İnsan Kaynakları, e-Fatura/e-Dönüşüm, SDK, Firebird/MSSQL veritabanı ve SQL, OctoPlus, OctoCloud, CafePlus). Menü yolları, kurulum, server/client, lisans, yedekleme, yıl sonu devri, Excel aktarımı, özel rapor, entegrasyon ve hata çözümleri için kullan. Kullanıcı Akınsoft, Wolvox veya bu ürünlerden birini andığında yükle.
---

# AKINSOFT / WOLVOX bilgi tabanı

Bu skill `references/` klasöründeki konu dosyalarından oluşur. Soruya uyan dosyayı oku, gereksiz dosyaları yükleme.

| Dosya | İçerik |
|---|---|
| `references/urunler.md` | Şirket bilgisi, ürün ailesi, program kodları (WOO9, WOG9…), sürüm geçmişi (7/8/9/26), lisans modeli |
| `references/wolvox-erp-moduller.md` | ERP modülleri, satış akışı (teklif→sipariş→irsaliye→fatura), fatura tasarımı, stok, finans, çek/senet, üretim/MRP II, servis, CRM |
| `references/kurulum-ve-yonetim.md` | Kurulum, Kontrol Paneli, server/client ve portlar, kullanıcı/yetki, lisans ve client sayısı, sürüm güncelleme, yedekleme, yıl sonu devri, Excel transfer |
| `references/veritabani-ve-sql.md` | Firebird/MSSQL, `DATABASE_FB`, BLKODU anahtar yapısı, bilinen tablolar/alanlar, örnek SQL, SQL Monitör, özel raporlar, Python ile okuma, güvenlik kuralları |
| `references/sdk-ve-entegrasyon.md` | WOLVOX SDK (HTTP+XML), e-Ticaret/Web Entegrasyon, pazaryeri entegratörleri, WebConnect, Genel Muhasebe entegrasyonu |
| `references/e-donusum.md` | e-Fatura, e-Arşiv, e-İrsaliye, e-Defter, özel entegratörler, ayarlar, sık hatalar |
| `references/sektorel-programlar.md` | Hızlı Satış, Restoran, Otel, İK/Bordro, Mobil Satış, Genel Muhasebe, OctoPlus/OctoCloud, e-Ticaret, CafePlus |
| `references/sorun-giderme.md` | Bağlantı, lisans, SQL ve veritabanı hataları, genel tanı kontrol listesi |
| `references/kaynaklar.md` | Bilgi Bankası makale numaraları, PDF'ler, video listeleri, bayi kaynakları ve hangisinin işlendiği |

## Kullanım kuralları

1. **Sürümü netleştir.** Menü yolları Wolvox 7, 8, 9 ve 26 arasında farklılaşabilir. Kullanıcının sürümünü ve veritabanını (Firebird/MSSQL) bilmeden kesin menü yolu verme.
2. **Kaynağı belirt.** Yanıtta dayandığın Bilgi Bankası makale numarasını veya kaynağı söyle, kullanıcı doğrulayabilsin.
3. **Bilmediğini uydurma.** Bu tabanda olmayan bilgi (SDK fonksiyon adları, doğrulanmamış tablo adları, paket içerikleri) için web araştırması yap (bilgibankasi.akinsoft.net öncelikli) veya bilmediğini açıkça söyle.
4. **Riskli işlemlerde önce yedek.** Devir, geri yükleme, Excel toplu aktarım, veritabanı transferi ve sürüm güncellemesinden önce yedek almayı hatırlat.
5. **Veritabanına doğrudan yazma önerme.** Okuma SQL'i tamam; yazma için SDK, Excel Transfer veya program arayüzünü öner.
6. **Bilgi tabanını büyüt.** Doğrulanmış yeni bir bilgi öğrendiğinde (kullanıcı onayıyla) ilgili referans dosyasına kaynağıyla ekle ve `kaynaklar.md` içindeki durumu güncelle.
