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
            └── kaynaklar.md      # Bilgi Bankası makaleleri, PDF'ler, videolar ve işlenme durumu
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

## Bilinen eksikler (ilk sürüm, 2026-09-24)

İlk sürüm web arama sonuçlarından derlendi. Oluşturulduğu ortamın ağ politikası akinsoft.com.tr, bilgibankasi.akinsoft.net ve youtube.com'u doğrudan açmaya izin vermedi. Bu yüzden:

- **Videolar izlenmedi.** Sadece başlıklar ve linkler var (`kaynaklar.md`).
- **Ekran görüntüleri toplanamadı.**
- **Bilgi Bankası makalelerinin çoğu tam okunmadı.** Arama özetleri işlendi, hangisinin ne kadar işlendiği `kaynaklar.md` içinde işaretli.
- **SDK PDF'i okunmadı.** Fonksiyon adları ve XML şemaları eksik.

Yerel VS Code oturumunda (ağ erişimi olan bir ortamda) agent'a şunu söyleyebilirsin: "`kaynaklar.md` içindeki 'başlık' durumundaki Bilgi Bankası makalelerini ve SDK PDF'ini oku, bilgi tabanını güncelle."
