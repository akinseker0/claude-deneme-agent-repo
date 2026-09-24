#!/usr/bin/env python3
"""AKINSOFT Bilgi Bankası yerel önbellek aracı (sadece Python standart kütüphanesi).

Makalelerin tam metni telif nedeniyle repoya konmaz. Bu araç onları kullanıcının
kendi bilgisayarında ~/.cache/wolvox-bilgibankasi/ altına indirir (repo dışında).
Klasör kullanıcı başına tektir: repo klonu, --add-dir, ~/.claude bağlantısı veya
plugin, hangi yolla çalıştırılırsa çalıştırılsın aynı önbellek kullanılır.
Makale listesi: skill klasöründeki references/bilgibankasi-dizini.json

Araç skill klasöründe durur ki skill başka bir projeye bağlandığında da çalışsın.
Repo kökünden `python tools/bilgibankasi.py ...` kısayolu da aynı işi yapar.

Kullanım:
  python bilgibankasi.py oku 257                       # tek makale (önbellekte yoksa indirir)
  python bilgibankasi.py ara "devir"                   # önbellekteki makalelerde ara (regex)
  python bilgibankasi.py baslik "e-fatura"             # dizinde başlık ara (indirme gerekmez)
  python bilgibankasi.py indir                         # tüm makaleleri indir (eksik olanları)
  python bilgibankasi.py indir --kategori "e-Fatura"   # sadece bir kategori
  python bilgibankasi.py dizin                         # sitemap.xml'den dizini yenile
"""
import argparse
import html
import json
import re
import sys
import time
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

BASE = "https://bilgibankasi.akinsoft.net"
SKILL_DIR = Path(__file__).resolve().parent.parent  # .claude/skills/wolvox
# Kurulum yolundan bağımsız, kullanıcı başına tek önbellek (plugin güncellemesinde de silinmez).
CACHE = Path.home() / ".cache" / "wolvox-bilgibankasi"
INDEX_JSON = SKILL_DIR / "references" / "bilgibankasi-dizini.json"
DELAY = 0.5  # sunucuyu yormamak için istekler arası bekleme (sn)

if hasattr(sys.stdout, "reconfigure"):  # Windows konsolunda Türkçe karakterler için
    sys.stdout.reconfigure(encoding="utf-8")


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (bilgibankasi-onbellek)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "ignore")


class ArticleParser(HTMLParser):
    """`knowledge-single` bloğunun metnini, resim ve bağlantılarını toplar."""

    BLOCK = {"p", "div", "li", "tr", "h1", "h2", "h3", "h4", "h5", "br", "table"}

    def __init__(self):
        super().__init__()
        self.depth = 0
        self.inside = False
        self.parts, self.images, self.links = [], [], []
        self.title = ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self._in_title = True
        if not self.inside and tag == "div" and "knowledge-single" in (a.get("class") or "").split():
            self.inside, self.depth = True, 1
            return
        if not self.inside:
            return
        if tag == "div":
            self.depth += 1
        if tag in self.BLOCK:
            self.parts.append("\n")
        if tag == "img" and a.get("src"):
            self.images.append(a["src"])
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if self.inside and tag == "div":
            self.depth -= 1
            if self.depth == 0:
                self.inside = False
        if self.inside and tag in self.BLOCK:
            self.parts.append("\n")

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self.inside:
            self.parts.append(data)

    def result(self):
        text = html.unescape("".join(self.parts))
        text = re.sub(r"[ \t\r\f\v]+", " ", text)
        text = re.sub(r"\n\s*\n+", "\n\n", text).strip()
        title = self.title.replace(" - AKINSOFT Bilgi Bankası", "").strip()
        return title, text


def load_index():
    if not INDEX_JSON.exists():
        sys.exit(f"Dizin bulunamadı: {INDEX_JSON}. Önce 'dizin' komutunu çalıştırın.")
    return json.loads(INDEX_JSON.read_text(encoding="utf-8"))["makaleler"]


def article_url(no):
    for a in load_index():
        if a["no"] == no:
            return a["url"]
    sys.exit(f"{no} numaralı makale dizinde yok. 'dizin' komutuyla dizini yenileyin.")


def download(no, url):
    p = ArticleParser()
    p.feed(fetch(url))
    title, text = p.result()
    CACHE.mkdir(parents=True, exist_ok=True)
    body = (f"# {title}\nURL: {url}\nRESIMLER: {json.dumps(p.images)}\n"
            f"BAGLANTILAR: {json.dumps(p.links)}\n\n{text}\n")
    (CACHE / f"{no}.md").write_text(body, encoding="utf-8")
    return title, len(text)


def cmd_oku(args):
    f = CACHE / f"{args.no}.md"
    if not f.exists():
        download(args.no, article_url(args.no))
    print(f.read_text(encoding="utf-8"))


def cmd_ara(args):
    files = sorted(CACHE.glob("*.md"), key=lambda x: int(x.stem)) if CACHE.exists() else []
    if not files:
        sys.exit("Önbellek boş. Önce: python bilgibankasi.py indir")
    pat = re.compile(args.ifade, re.IGNORECASE)
    for f in files:
        lines = f.read_text(encoding="utf-8").splitlines()
        hits = [l.strip() for l in lines[4:] if pat.search(l)]
        if hits or pat.search(lines[0]):
            print(f"[{f.stem}] {lines[0].lstrip('# ')}")
            for h in hits[: args.satir]:
                print("    " + h[:200])


def cmd_baslik(args):
    pat = re.compile(args.ifade, re.IGNORECASE)
    for a in load_index():
        if pat.search(a["baslik"]) or pat.search(a.get("kategori") or ""):
            print(f"[{a['no']}] {a['baslik']}  ({a.get('kategori') or '-'})")


def cmd_indir(args):
    arts = load_index()
    if args.kategori:
        arts = [a for a in arts if args.kategori.lower() in (a.get("kategori") or "").lower()]
    todo = [a for a in arts if args.yenile or not (CACHE / f"{a['no']}.md").exists()]
    print(f"{len(todo)} makale indirilecek -> {CACHE}")
    for i, a in enumerate(todo, 1):
        try:
            title, n = download(a["no"], a["url"])
            print(f"[{i}/{len(todo)}] {a['no']} {title[:70]} ({n} karakter)")
        except Exception as e:  # ağ hatasında devam et
            print(f"[{i}/{len(todo)}] {a['no']} HATA: {e}")
        time.sleep(DELAY)


def cmd_dizin(args):
    """sitemap.xml'den tüm Türkçe makaleleri alıp dizini yeniler (bilinen başlık/kategori korunur)."""
    old = {a["no"]: a for a in load_index()} if INDEX_JSON.exists() else {}
    xml = fetch(f"{BASE}/sitemap.xml")
    arts = []
    for url in re.findall(r"<loc>(.*?)</loc>", xml):
        m = re.search(r"/tr/home/makale/(\d+)-([^/?]+)", url, re.I)
        if not m:
            continue
        no = int(m.group(1))
        prev = old.get(no, {})
        arts.append({"no": no,
                     "baslik": prev.get("baslik") or m.group(2).replace("-", " "),
                     "kategori": prev.get("kategori", ""),
                     "url": url})
    arts.sort(key=lambda a: a["no"])
    # Önbellekte tam metni olan makalelerin gerçek başlığını ve kategorisini kullan
    for a in arts:
        f = CACHE / f"{a['no']}.md"
        if f.exists():
            t = f.read_text(encoding="utf-8")
            a["baslik"] = re.sub(r"\s+", " ", t.splitlines()[0].lstrip("# ")).strip() or a["baslik"]
            k = re.search(r"Kategori\s*\n\s*(.+)", t)
            if k:
                a["kategori"] = k.group(1).strip()
    lines = ",\n".join("  " + json.dumps(a, ensure_ascii=False) for a in arts)
    INDEX_JSON.write_text(
        '{\n "kaynak": %s,\n "guncelleme": %s,\n "makaleler": [\n%s\n ]\n}\n'
        % (json.dumps(f"{BASE}/sitemap.xml"), json.dumps(time.strftime("%Y-%m-%d")), lines),
        encoding="utf-8")
    print(f"Dizin yazıldı: {INDEX_JSON} ({len(arts)} makale). Önbellekte olmayan yeni makalelerin başlığı adresinden türetildi.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="komut", required=True)
    p = sub.add_parser("oku"); p.add_argument("no", type=int); p.set_defaults(f=cmd_oku)
    p = sub.add_parser("ara"); p.add_argument("ifade"); p.add_argument("--satir", type=int, default=3); p.set_defaults(f=cmd_ara)
    p = sub.add_parser("baslik"); p.add_argument("ifade"); p.set_defaults(f=cmd_baslik)
    p = sub.add_parser("indir"); p.add_argument("--kategori"); p.add_argument("--yenile", action="store_true"); p.set_defaults(f=cmd_indir)
    p = sub.add_parser("dizin"); p.set_defaults(f=cmd_dizin)
    args = ap.parse_args()
    args.f(args)


if __name__ == "__main__":
    main()
