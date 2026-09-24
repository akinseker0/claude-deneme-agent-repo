# AKINSOFT / WOLVOX uzman agent'ı

Bu repo, AKINSOFT yazılımları ve WOLVOX ERP konusunda uzmanlaşmış bir **Claude Code agent'ı** ve onun **bilgi tabanını** içerir. FDB dosyalarını localden kullandığım için buraya eklenmemiştir.

## İçerik

```
.claude-plugin/
└── marketplace.json              # Plugin olarak kurulum için (kaynak: .claude klasörü)
.claude/
├── agents/
│   └── wolvox-uzmani.md          # Agent tanımı (rol, çalışma yöntemi, güvenlik kuralları)
└── skills/
    └── wolvox/
        ├── SKILL.md              # Bilgi tabanı dizini ve kullanım kuralları
        ├── scripts/
        │   └── bilgibankasi.py   # Bilgi Bankası tam metinlerini yerel önbelleğe indirir/arar (stdlib)
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
└── bilgibankasi.py               # Kısayol: skill içindeki scripts/bilgibankasi.py'yi çalıştırır
```

Agent, bilgi tabanını `skills: [wolvox]` ile başlangıçta yükler ve dosyaları skill klasörüne göre bulur. Bu yüzden repo başka bir projeye bağlandığında da çalışır.

## Kullanım

### En kolayı: plugin olarak tek komutla kurmak

Klonlamaya gerek yok. Herhangi bir terminalde (Claude Code kurulu olmalı):

```bash
claude plugin marketplace add akinseker0/claude-deneme-agent-repo
claude plugin install wolvox@wolvox-uzmani
```

Aynı şey Claude Code oturumunun içinden de yapılabilir:

```
/plugin marketplace add akinseker0/claude-deneme-agent-repo
/plugin install wolvox@wolvox-uzmani
```

Kurulum kullanıcı düzeyindedir, yani bu bilgisayardaki tüm projelerde ve VS Code'daki oturumlarda geçerlidir. Claude Code'u (veya VS Code'u) yeniden başlat. Agent `wolvox:wolvox-uzmani`, bilgi tabanı `/wolvox:wolvox` adıyla görünür.

- **Güncelleme:** Claude Code repodaki yeni commit'leri kendisi kontrol edip kurar. Hemen almak için: `claude plugin marketplace update wolvox-uzmani`.
- **Kaldırma:** `claude plugin uninstall wolvox@wolvox-uzmani`.
- **npm gerekmez.** Claude Code agent ve skill'leri npm paketi olarak değil, plugin olarak dağıtır. Plugin GitHub'dan doğrudan indirilir.
- **Not:** Plugin salt okunur bir kopyadır. Agent'ın "bilgi tabanına ekle" dediği yeni bilgiler kalıcı olsun istiyorsan repoyu klonlayıp aşağıdaki 1. yöntemle çalış ve değişikliği commit'le.
- Bu repoyu açtığında hem proje agent'ı (`wolvox-uzmani`) hem plugin agent'ı (`wolvox:wolvox-uzmani`) listede görünür. İkisi aynı dosyadır, hangisi çağrılırsa çağrılsın aynı sonucu verir.

### Diğer yollar (repoyu klonlayarak)

Önce repoyu bilgisayarına klonla (Claude Code CLI veya VS Code eklentisi kurulu olmalı):

```bash
git clone https://github.com/akinseker0/claude-deneme-agent-repo
```

Güncellemeler için klon klasöründe `git pull` yeterli.

Agent'ı nasıl çağırırsın (her yöntemde aynı):
- Doğrudan sor: "Wolvox'ta yıl sonu devri nasıl yapılır?" Claude, agent'ın açıklamasına bakıp işi ona devreder.
- Veya açıkça çağır: "wolvox-uzmani agent'ını kullanarak şu hatayı çöz: …"
- `/agents` listesinde `wolvox-uzmani`, `/wolvox` yazınca bilgi tabanı skill'i görünmeli.

#### 1. Bu klasörü açarak

Klasörü VS Code'da aç (veya bu klasörde `claude` çalıştır). Agent ve skill kendiliğinden yüklenir.

#### 2. Başka bir projede, o oturumluk: `--add-dir`

```bash
cd C:\projeler\baska-proje
claude --add-dir C:\projeler\claude-deneme-agent-repo
```

Açık bir oturumda `/add-dir C:\projeler\claude-deneme-agent-repo` de olur. Eklenen klasörün `.claude/agents` ve `.claude/skills` içerikleri yüklenir. Agent dosyasını değiştirirsen oturumu yeniden başlat. `settings.json` içindeki `permissions.additionalDirectories` yalnız dosya izni verir, agent veya skill yüklemez.

#### 3. Tüm projelerde kalıcı: `~/.claude` altına bağlantı

Plugin yerine bunu seçersen agent'ın öğrendikleri doğrudan klondaki dosyalara yazılır. Kopyalamak yerine **bağlantı** kur. Böylece `git pull` ile gelen güncellemeler her projede görünür, agent'ın öğrendikleri de repoya yazılır.

Windows (PowerShell):

```powershell
$REPO = "C:\projeler\claude-deneme-agent-repo"   # kendi klon yolun
New-Item -ItemType Directory -Force "$HOME\.claude\agents", "$HOME\.claude\skills" | Out-Null
New-Item -ItemType Junction -Path "$HOME\.claude\skills\wolvox" -Target "$REPO\.claude\skills\wolvox"
Copy-Item "$REPO\.claude\agents\wolvox-uzmani.md" "$HOME\.claude\agents\"
```

Klasör bağlantısı (junction) yönetici izni istemez. Agent tek bir dosya olduğu için kopyalanır; agent dosyası değişirse `Copy-Item` satırını yeniden çalıştır. Kopya yerine dosya bağlantısı istersen yönetici PowerShell'inde: `New-Item -ItemType SymbolicLink -Path "$HOME\.claude\agents\wolvox-uzmani.md" -Target "$REPO\.claude\agents\wolvox-uzmani.md"`.

macOS / Linux:

```bash
REPO=~/projeler/claude-deneme-agent-repo   # kendi klon yolun
mkdir -p ~/.claude/agents ~/.claude/skills
ln -s "$REPO/.claude/skills/wolvox" ~/.claude/skills/wolvox
ln -s "$REPO/.claude/agents/wolvox-uzmani.md" ~/.claude/agents/wolvox-uzmani.md
```

Sonra herhangi bir projede Claude Code'u yeniden başlat. Bu repoyu açtığında aynı adlı proje agent'ı öncelik alır, çakışma olmaz. Plugin'i de kurduysan ikisinden birini kullan. Agent veya skill görünmüyorsa bağlantı yerine klasörü kopyalamayı dene.

#### 4. Bulut oturumları (claude.ai/code)

Bulut oturumları bilgisayarındaki `~/.claude` klasörünü okumaz. Oturumu bu repo seçili olarak başlat; agent ve skill repodan yüklenir. Başka bir repoda bulut oturumu açacaksan ya `.claude/agents/wolvox-uzmani.md` ve `.claude/skills/wolvox/` klasörünü o repoya da koy, ya da skill'i claude.ai hesabının skill ayarlarından etkinleştir (bu yol yalnız skill'i getirir, agent'ı getirmez).

## Bilgi tabanı nasıl büyür?

Agent'ın kalıcı hafızası yok, bilgisi `references/` dosyalarından gelir. Yeni bir şey öğretmek için:

- Agent'a "bunu bilgi tabanına ekle" de. Doğrulanmış bilgiyi kaynağıyla birlikte ilgili dosyaya yazar.
- Ya da dosyaları kendin düzenle.
- Değişiklikleri commit'le ve push'la. Diğer bilgisayarlarda `git pull` ile gelir.

## Bilgi Bankası tam metinleri (yerel önbellek)

AKINSOFT makalelerinin tam metni telif nedeniyle repoya konmadı. Özetler `bilgibankasi-ozetleri.md` dosyasında. Tam metne ihtiyaç olursa kendi bilgisayarında şunları çalıştır (Python 3, ek paket gerekmez, internet gerekir). `tools/bilgibankasi.py` bir kısayoldur; asıl araç `.claude/skills/wolvox/scripts/bilgibankasi.py`:

```bash
python tools/bilgibankasi.py indir               # 1411 makaleyi ~/.cache/wolvox-bilgibankasi/ altına indirir (~15 dk, bir kez)
python tools/bilgibankasi.py oku 3845            # tek makaleyi göster
python tools/bilgibankasi.py baslik "e-fatura"   # başlıkta ara
python tools/bilgibankasi.py ara "sysas.ask"     # tam metinlerde ara
python tools/bilgibankasi.py dizin               # yeni makaleler için dizini yenile
```

Önbellek repo dışında, kullanıcının `~/.cache/wolvox-bilgibankasi/` klasöründedir (Windows'ta `C:\Users\<ad>\.cache\wolvox-bilgibankasi`). Tüm makaleler yaklaşık 25-30 MB tutar. Klasör kullanıcı başına tektir: repo klonundan, başka bir projeden ya da plugin'den hangi oturumda çalıştırılırsa çalıştırılsın aynı yer kullanılır. Bu yüzden bir kez indirmek yeterli. `oku` yalnız istenen makaleyi indirir; `ara` yalnız inmiş makalelerde arar, tam metin araması için önce bir kez `indir` çalıştır. Bulut oturumları (claude.ai/code) başka bir makinede çalıştığı için bu önbelleği görmez.

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
