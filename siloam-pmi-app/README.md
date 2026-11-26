# PMI Radiologi - Siloam Hospitals Lippo Village

Aplikasi Streamlit: monitoring suhu & kelembapan (3 shift), checklist QC peralatan (✓ / ✗), dashboard, QR per ruangan, dan form PDF.

## Isi folder
| File | Fungsi |
|---|---|
| `app.py` | aplikasi utama |
| `Siloam Logo.png`, `Siloam Logo White.png` | logo (putih dipakai otomatis di header biru) |
| `requirements.txt` | library Python |
| `schema.sql` | 3 tabel Supabase (jalankan sekali di project Supabase **baru**) |
| `get_fonts.py` | unduh `Lexend-Regular.ttf` + `Lexend-Bold.ttf` (opsional, lihat bawah) |
| `.streamlit/config.toml` | tema warna |
| `.streamlit/secrets.toml.example` | contoh isi Secrets |

## Langkah deploy
1. Buat project Supabase baru -> SQL Editor -> jalankan isi `schema.sql`.
2. Jalankan `python get_fonts.py`, lalu upload semua file di folder ini ke repo GitHub baru
   (`app.py`, logo, font, `requirements.txt`, folder `.streamlit/config.toml`; **jangan** upload secrets asli).
3. Streamlit Cloud -> New app -> pilih repo, file `app.py`.
4. App -> Settings -> Secrets: isi `SUPABASE_URL`, `SUPABASE_KEY`, `AUTHOR_PASSWORD` (lihat `secrets.toml.example`).
5. Login Author (sidebar) -> menu **Download & QR** -> isi alamat app yang benar -> *Simpan alamat* -> unduh & cetak QR.

Catatan font: tanpa file `.ttf`, app mencoba mengunduhnya sendiri saat pertama membuat PDF; bila gagal, PDF memakai Helvetica.

## Format form (mengikuti formulir resmi Siloam)
- **Suhu & Kelembaban**: `FORM-SHG-KL-11 Rev02` - pembacaan jam **08 / 14 / 22**, suhu **20-24 °C**, pita merah muda = di dalam batas normal, kode dokumen `SHKL 2205.11.x/2`.
- **Batas kelembaban per ruang** (`ROOM_HUM` di `app.py`): MRI 30-70 %, Digital Diagnost & Duo Diagnost 20-75 %, Panoramik CBCT 40-55 %, CT Scan 50-60 %.
  **BMD** tidak ada di workbook Siloam -> sementara 20-75 % (sama seperti X-Ray); ubah bila ada batas resmi.
- **QC Harian**: `Form_QC_Harian_LV.xlsx` (checklist ✓ / ✗ per shift).

## Yang perlu disesuaikan
- Inisial staff (`DEFAULT_CFG["staff"]`, saat ini `AA..EE`) atau lewat sidebar Author.
- Batas suhu/kelembapan (`SUHU_NORMAL`, `HUM_NORMAL`) dan jam shift (`SHIFT_HOUR`).
- Daftar item QC ada di bagian `DAFTAR PERIKSA QC` pada `app.py`.
