# 🎓 Amikom-Tugas-Kuis_3_PBO

![Python Badge](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![LaTeX Badge](https://img.shields.io/badge/LaTeX-Document-teal?style=for-the-badge&logo=latex&logoColor=white)

Tugas Kuis 3 Pemrograman Berorientasi Objek (PBO). Proyek ini merupakan implementasi studi kasus sistem Perbankan dan Pemutar Audio menggunakan pilar-pilar OOP di Python: Abstraksi, Enkapsulasi, Inheritance, Overloading, dan Overriding/Polimorfisme.

## 🚀 Fitur Utama (Key Features)

- **🏛️ Abstraksi (ABC):** Implementasi *Abstract Base Class* pada entitas `RekeningBank` dengan *abstract methods* yang mewajibkan subclass mengimplementasikannya.
- **🔒 Enkapsulasi Ketat:** Pengamanan data sensitif (`__pin`, `__limit`) pada `RekeningGiro` serta validasi modifikasi `_saldo` pada `RekeningTabunganBiasa` dengan mekanisme *Getter/Setter*.
- **🎛️ Method Overloading:** Simulasi overloading metode di Python menggunakan *default arguments* untuk fungsi pemutaran musik 1 parameter dan 2 parameter.
- **🎭 Polimorfisme (Dynamic Dispatch):** Resolusi *method overriding* dinamis dari instansiasi `PemutarAudioPremium` meskipun dideklarasikan sebagai induk.

## ⚙️ Cara Kerja Program (How It Works)

Logika program terbagi menjadi dua bagian simulasi:
1. **Sistem Rekening:** Menginisialisasi objek `RekeningTabunganBiasa`, mengekstrak saldonya secara aman menggunakan getter, mengujinya dengan setter validasi (mencoba minus), lalu menangkap error (*exception handling*).
2. **Sistem Pemutar Audio:** Mendeklarasikan objek bertipe `PemutarAudioPremium` secara polimorfik, lalu memutar dua variasi lagu menggunakan fungsi *overloading* yang otomatis ter-*override* berkat fitur Dolby Atmos Premium.

```mermaid
flowchart TD
    A[Mulai Program] --> B[Inisialisasi Tabungan]
    B --> C{Ubah Saldo Negatif?}
    C -->|Ya| D[Bangkitkan ValueError]
    C -->|Tidak| E[Update Saldo]
    D --> F[Inisialisasi Pemutar Audio Polimorfik]
    E --> F
    F --> G[Panggil putar(1 argumen)]
    G --> H[Panggil putar(2 argumen)]
    H --> I[Sistem Resolve ke Kelas Anak: Dolby Atmos]
    I --> J[Selesai]
```

## 📋 Prasyarat & Instalasi

Proyek ini hanya membutuhkan Python 3.x dan modul standar. Untuk render LaTeX dibutuhkan TeX Live (atau bisa diunggah ke Overleaf).
Untuk instalasi dependensi jika ingin mere-render gambar output:
```bash
git clone https://github.com/diondharmawan/Amikom-Tugas-Kuis_3_PBO.git
cd Amikom-Tugas-Kuis_3_PBO
# Buat Virtual Environment (opsional)
python3 -m venv .venv
source .venv/bin/activate
# Install dependensi render image (hanya untuk utils)
pip install Pillow
```

## 🎮 Cara Penggunaan (Usage)

Jalankan script utama di terminal/CLI:
```bash
python3 hasil/kuis3.py
```
**Contoh Output Terminal:**
```text
--------------------------------------------------
SIMULASI KUIS 3 PBO - FRANSISCUS ASISI KANANDA H.D.
--------------------------------------------------

--- Uji Enkapsulasi Tabungan ---
Saldo Awal: Rp 50000
Saldo Setelah Ubah Valid: Rp 100000
Validasi Berhasil: Saldo tidak boleh negatif!

--- Uji Polimorfisme & Overriding (Audio) ---
[Standar] Memutar 'Bohemian Rhapsody' dari penyimpanan lokal.
[Premium Dolby Atmos] Memutar 'Stairway to Heaven' pada 320kbps (Fitur Spatial Audio Aktif).
--------------------------------------------------
```

## 📂 Struktur Direktori

```text
.
├── .gitignore
├── hasil/
│   ├── kuis3.py               # Source code OOP utama
│   ├── render_image.py        # Utilitas render teks ke gambar
│   ├── sc_code.png            # Screenshot kode
│   ├── sc_output.png          # Screenshot hasil terminal
│   ├── main.tex               # Dokumen LaTeX laporan
│   └── Laporan_Tugas_Kuis_3_PBO.zip # Berkas rilis kumpul
└── README.md                  # Dokumentasi repo
```

## 👨‍🎓 Identitas Kontributor

| Keterangan | Detail |
| :--- | :--- |
| **Nama** | Fransiscus Asisi Kananda Herdion Dharmawan |
| **NIM** | 24.83.1107 |
| **Program Studi** | Teknik Komputer |
| **Institusi** | Universitas Amikom Yogyakarta |
| **Repositori** | [Amikom-Tugas-Kuis_3_PBO](https://github.com/diondharmawan/Amikom-Tugas-Kuis_3_PBO) |
