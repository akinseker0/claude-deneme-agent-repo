# AKINSOFT / WOLVOX uzman agent'ı

Bu repo, AKINSOFT yazılımları ve WOLVOX ERP konusunda uzmanlaşmış bir **Claude Code agent'ı** ve onun **bilgi tabanını** içerir.

## İçerik

```
.claude/
├── agents/
│   └── wolvox-uzmani.md          # Agent tanımı (rol, çalışma yöntemi, güvenlik kuralları)
└── skills/
    └── wolvox/
        ├── SKILL.md              # Bilgi tabanı dizini ve kullanım kuralları
        └── references/           # Konu dosyaları
            ├── urunler.md
            ├── wolvox-erp-moduller.md
            ├── kurulum-ve-yonetim.md
            ├── veritabani-ve-sql.md
            ├── sdk-ve-entegrasyon.md
            ├── e-donusum.md
            ├── sektorel-programlar.md
            ├── sorun-giderme.md
            ├── bilgibankasi-ozetleri.md   # ~940 makalenin tam metninden kendi cümlelerimizle özetler
            ├── bilgibankasi-dizini.json   # 1411 makalenin no/başlık/kategori/adres dizini
            ├── menu-haritasi.md           # WOLVOX 26 / WolvoxCloud menü ağacı
            ├── video-dizini.md            # YouTube + Dailymotion eğitim videoları listesi
            ├── video-ozetleri.md          # Video altyazılarından çıkarılmış özetler
            └── kaynaklar.md               # Kaynaklar ve işlenme durumu
tools/
└── bilgibankasi.py               # Bilgi Bankası tam metinlerini yerel önbelleğe indirir/arar (stdlib)
```

## Yerel VS Code'da kullanım

1. Repoyu klonla ve klasörü VS Code'da aç (Claude Code eklentisi kurulu olmalı):
   ```bash
   git clone https://github.com/akinseker0/claude-deneme-agent-repo
   ```
2. Claude Code'da `/agents` komutuyla `wolvox-uzmani` agent'ını listede gör.
3. Kullanım:
   - Doğrudan sor: "Wolvox'ta yıl sonu devri nasıl yapılır?" Claude, agent'ın açıklamasına bakıp işi ona devreder.
   - Veya açıkça çağır: "wolvox-uzmani agent'ını kullanarak şu hatayı çöz: …"
4. Güncellemeler için `git pull` yeterli.

**Başka projelerde de kullanmak için:** `.claude/agents/wolvox-uzmani.md` dosyasını `~/.claude/agents/`, `.claude/skills/wolvox/` klasörünü `~/.claude/skills/` altına kopyala. Daha kalıcı bir çözüm istersen bu repo bir plugin marketplace'e çevrilebilir.

## Bilgi tabanı nasıl büyür?

Agent'ın kalıcı hafızası yok, bilgisi `references/` dosyalarından gelir. Yeni bir şey öğretmek için:

- Agent'a "bunu bilgi tabanına ekle" de. Doğrulanmış bilgiyi kaynağıyla birlikte ilgili dosyaya yazar.
- Ya da dosyaları kendin düzenle.
- Değişiklikleri commit'le ve push'la. Diğer bilgisayarlarda `git pull` ile gelir.

## Bilgi Bankası tam metinleri (yerel önbellek)

AKINSOFT makalelerinin tam metni telif nedeniyle repoya konmadı. Özetler `bilgibankasi-ozetleri.md` dosyasında. Tam metne ihtiyaç olursa kendi bilgisayarında şunları çalıştır (Python 3, ek paket gerekmez, internet gerekir):

```bash
python tools/bilgibankasi.py indir               # 1411 makaleyi .cache/bilgibankasi/ altına indirir (~15 dk, bir kez)
python tools/bilgibankasi.py oku 3845            # tek makaleyi göster
python tools/bilgibankasi.py baslik "e-fatura"   # başlıkta ara
python tools/bilgibankasi.py ara "sysas.ask"     # tam metinlerde ara
python tools/bilgibankasi.py dizin               # yeni makaleler için dizini yenile
```

`.cache/` klasörü `.gitignore`'da, commit'lenmez.

## Durum ve bilinen eksikler (2026-09-24)

- **Bilgi Bankası:** 1411 makaleden 1410'unun tam metni okundu. Yaklaşık 940'ı özetlere işlendi; geri kalanlar e-Ticaret tema şablonları, pazaryeri ayar ekranları, CafePlus gibi Wolvox dışı ya da tekrar eden konular ve başlık dizininden bulunabiliyor.
- **SDK:** Wolvox 9 SDK PDF'i ve resmi Delphi demo kaynağı okundu (`sdk-ve-entegrasyon.md`). SDK kullanmak için SDK lisansı ve AKINSOFT'tan alınan geliştirici kodu (devCode) gerekir.
- **Videolar:** Wolvox ile ilgili 946 Türkçe YouTube videosunun 906'sının Türkçe altyazısı okundu, özetler `video-ozetleri.md` dosyasında. Kalan 40 videonun altyazısı yok. Açıklamalar bilgi içermiyor. Otomatik altyazıda ses tanıma hataları olabileceği için kesin menü yolu programdan doğrulanmalı.
- **Ekran görüntüleri:** Repoya konmadı. Adresleri araç çıktısında var; agent gerektiğinde indirip okuyabilir.
- **Veritabanı şeması:** Yaklaşık 15 tablo ve bir kısım alan makalelerden doğrulandı. **Tam şema kullanıcının yerelindeki `wolvox.fdb` / `sirket.fdb` kopyasından çıkarılmalı.** Yerel oturumda agent'a şöyle diyebilirsin: "wolvox.fdb'nin bir kopyasından isql ile şemayı çıkar ve veritabani-ve-sql.md'yi güncelle, veriyi yazma."

## Gizlilik notu

Bu repo şu anda **herkese açık (public)**.
- Veritabanı dosyaları `.gitignore` ile dışlanıyor (`*.fdb`, `*.fbk`, `*.mdb`…).
- Yine de şirket verisi, şifre veya lisans bilgisi içeren hiçbir şeyi commit'leme.
- Repoya kendi notlarını ya da şema dökümlerini ekleyeceksen repoyu **private** yapmayı düşün (GitHub → Settings → General → Danger Zone → Change visibility).
