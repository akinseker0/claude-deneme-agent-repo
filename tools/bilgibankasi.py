#!/usr/bin/env python3
"""Kısayol. Asıl araç .claude/skills/wolvox/scripts/bilgibankasi.py dosyasında
(skill ile birlikte taşınsın diye orada). Kullanım için o dosyanın başına bakın."""
import runpy
from pathlib import Path

ARAC = Path(__file__).resolve().parent.parent / ".claude" / "skills" / "wolvox" / "scripts" / "bilgibankasi.py"
runpy.run_path(str(ARAC), run_name="__main__")
