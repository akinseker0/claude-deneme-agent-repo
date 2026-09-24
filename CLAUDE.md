# Bu repo hakkında

Bu repo kod değil, bir Claude Code agent'ı ve onun bilgi tabanını barındırır. Konu: AKINSOFT yazılımları ve WOLVOX ERP.

- Agent: `.claude/agents/wolvox-uzmani.md`
- Bilgi tabanı (skill): `.claude/skills/wolvox/SKILL.md` ve `.claude/skills/wolvox/references/*.md`

## Kurallar

- AKINSOFT veya Wolvox ile ilgili sorularda `wolvox-uzmani` agent'ını kullan ya da `wolvox` skill'ini yükle.
- Bilgi tabanı dosyaları Türkçe yazılır. Her yeni bilgiye kaynağını ekle (Bilgi Bankası makale no veya URL).
- Doğrulanmamış bilgiyi "doğrulanmadı" veya "bayi kaynağına göre" diye işaretle. Tablo adı, SDK fonksiyonu veya menü yolu uydurma.
- Bir kaynağı okuyup işlediğinde `.claude/skills/wolvox/references/kaynaklar.md` içindeki durumunu güncelle.
- AKINSOFT dokümanlarını birebir kopyalama; kendi cümlelerinle özetle ve linkini ver.
