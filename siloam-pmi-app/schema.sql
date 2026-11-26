-- Jalankan di Supabase: SQL Editor -> New query (project BARU khusus Siloam Lippo Village)
create table if not exists entries (
  id bigserial primary key,
  dibuat text, ruang text not null, tanggal text not null, shift text not null,
  suhu text, kelembapan text, petugas text, status text, temuan text, tindakan text,
  unique (ruang, tanggal, shift)
);
-- checklist QC: 1 baris per alat x tanggal x shift (P/S/M, atau H = harian untuk Duo Diagnost Kamar 5)
create table if not exists qc_entries (
  id bigserial primary key,
  dibuat text, alat text not null, tanggal text not null, shift text not null default 'P',
  petugas text, hasil text, catatan text,
  unique (alat, tanggal, shift)
);
create table if not exists app_config (
  key text primary key,
  value text
);
