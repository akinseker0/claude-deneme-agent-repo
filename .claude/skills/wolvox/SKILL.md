---
name: wolvox
description: AKINSOFT ve WOLVOX bilgi tabanı (WOLVOX ERP, Kontrol Paneli, Genel Muhasebe, Hızlı Satış, Restoran, Otel, İnsan Kaynakları, e-Fatura/e-Dönüşüm, SDK, Firebird/MSSQL veritabanı ve SQL, OctoPlus, OctoCloud, CafePlus). Menü yolları, kurulum, server/client, lisans, yedekleme, yıl sonu devri, Excel aktarımı, özel rapor, entegrasyon ve hata çözümleri için kullan. Kullanıcı Akınsoft, Wolvox veya bu ürünlerden birini andığında yükle.
---

# AKINSOFT / WOLVOX bilgi tabanı

Bu skill `references/` klasöründeki konu dosyalarından oluşur. Soruya uyan dosyayı oku, gereksiz dosyaları yükleme.

**Dosyaların yeri.** Bu skill'in klasörü: `${CLAUDE_SKILL_DIR}`. Aşağıdaki `references/...` ve `scripts/...` yolları bu klasöre göredir, çalışma dizinine göre değil. Skill başka bir projeden (`--add-dir`, `~/.claude/skills/` bağlantısı veya plugin) kullanılıyorsa Read ve Grep'e tam yolu ver. Yukarıdaki yol boş ya da `${...}` olarak görünüyorsa klasörü Glob ile bul (`**/skills/wolvox/SKILL.md`) veya `~/.claude/skills/wolvox/` ve `~/.claude/plugins/cache/wolvox-uzmani/` konumlarına bak.

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
| `references/bilgibankasi-ozetleri.md` | **Bilgi Bankası makalelerinin tam metinlerinden çıkarılmış özetler** (~900 makale): ERP ayarları ve ipuçları, hatalar, sürüm geçmişi (8.25 → 26.04), WebConnect, Web Entegrasyon, Veri Transferi, Mobil Satış, e-Dönüşüm, yazarkasa/POS uyumluluğu, donanım, Octo, bulut ürünleri, e-Ticaret. Önce `Grep` ile ara (makale numarası `[no]` biçiminde) |
| `references/bilgibankasi-dizini.json` | 1411 Bilgi Bankası makalesinin numarası, başlığı, kategorisi ve adresi. Konu ararken başlık araması için |
| `references/menu-haritasi.md` | WOLVOX 26 / WolvoxCloud menü ağacı (eğitim videosu başlıklarından) |
| `references/video-dizini.md` | AKINSOFT YouTube ve Dailymotion eğitim videolarının listesi (başlık ve ID) |
| `references/video-ozetleri.md` | **Eğitim videolarının altyazılarından çıkarılmış özetler**: Kontrol Paneli, ERP modülleri, Hızlı Satış, Restoran, yazarkasa/terazi entegrasyonları, İK, Otel, MRP II, Mobil Satış, WolvoxCloud (104 dakikalık resmi eğitim dahil). Kaynak `{YouTube ID}`. Önce `Grep` ile ara |
| `references/kaynaklar.md` | Kaynak listesi, PDF'ler, bayi kaynakları ve işlenme durumu |

**Tam metin aracı** (`scripts/bilgibankasi.py`, yalnız Python 3 standart kütüphanesi). Özette ayrıntı yoksa makalenin tamamını oku. Ağ erişimi gerekir. Metin repo kökündeki `.cache/` klasörüne (skill kopyalanarak kurulduysa `~/.cache/`) iner ve repoya girmez:

```bash
python "${CLAUDE_SKILL_DIR}/scripts/bilgibankasi.py" baslik "devir"   # başlıkta ara (dizinden, ağ gerekmez)
python "${CLAUDE_SKILL_DIR}/scripts/bilgibankasi.py" oku 3845         # tek makale (yoksa indirir)
python "${CLAUDE_SKILL_DIR}/scripts/bilgibankasi.py" indir            # tüm makaleleri önbelleğe indir (~15 dk)
python "${CLAUDE_SKILL_DIR}/scripts/bilgibankasi.py" ara "GETVALUE"   # önbellekteki tam metinlerde regex ara
```

Linux/macOS'ta `python` yoksa `python3` kullan. Bu repo açıkken `python tools/bilgibankasi.py ...` kısayolu da aynı işi yapar.

## Kullanım kuralları

1. **Sürümü netleştir.** Menü yolları Wolvox 7, 8, 9 ve 26 arasında farklılaşabilir (26.02.01'den itibaren program dosyası `werp.exe`; öncesinde `werp9.exe`). Kullanıcının sürümünü ve veritabanını (Firebird/MSSQL) bilmeden kesin menü yolu verme.
2. **Önce özetlere bak.** Konu için `Grep` ile `bilgibankasi-ozetleri.md` ve diğer referans dosyalarını ara. Gerekirse `scripts/bilgibankasi.py oku <no>` ile tam metni aç.
3. **Kaynağı belirt.** Yanıtta dayandığın Bilgi Bankası makale numarasını veya kaynağı söyle, kullanıcı doğrulayabilsin.
4. **Bilmediğini uydurma.** Bu tabanda olmayan bilgi (SDK fonksiyon adları, doğrulanmamış tablo adları, paket içerikleri) için web araştırması yap (bilgibankasi.akinsoft.net öncelikli) veya bilmediğini açıkça söyle.
5. **Riskli işlemlerde önce yedek.** Devir, geri yükleme, Excel toplu aktarım, veritabanı transferi ve sürüm güncellemesinden önce yedek almayı hatırlat.
6. **Veritabanına doğrudan yazma önerme.** Okuma SQL'i tamam; yazma için SDK, Excel Transfer veya program arayüzünü öner.
7. **Bilgi tabanını büyüt.** Doğrulanmış yeni bir bilgi öğrendiğinde (kullanıcı onayıyla) ilgili referans dosyasına kaynağıyla ekle ve `kaynaklar.md` içindeki durumu güncelle.
