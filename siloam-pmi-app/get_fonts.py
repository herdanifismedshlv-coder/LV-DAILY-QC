# -*- coding: utf-8 -*-
"""Unduh font Lexend (Regular + Bold) ke folder ini. Jalankan sekali:  python get_fonts.py
Lalu commit kedua file .ttf ke GitHub (sejajar dengan app.py) supaya PDF memakai font Lexend."""
import os
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
FILES = {
    "Lexend-Regular.ttf": ["https://github.com/google/fonts/raw/main/ofl/lexend/static/Lexend-Regular.ttf",
                           "https://raw.githubusercontent.com/google/fonts/main/ofl/lexend/static/Lexend-Regular.ttf"],
    "Lexend-Bold.ttf": ["https://github.com/google/fonts/raw/main/ofl/lexend/static/Lexend-Bold.ttf",
                        "https://raw.githubusercontent.com/google/fonts/main/ofl/lexend/static/Lexend-Bold.ttf"],
}
for name, urls in FILES.items():
    dest = os.path.join(HERE, name)
    if os.path.exists(dest):
        print("sudah ada:", name)
        continue
    for u in urls:
        try:
            req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as r, open(dest, "wb") as f:
                f.write(r.read())
            print("diunduh:", name)
            break
        except Exception as e:
            print("gagal", u, e)
    else:
        print("TIDAK BISA mengunduh", name, "- unduh manual dari https://fonts.google.com/specimen/Lexend")
