from abc import ABC, abstractmethod

# ==============================================================================
# JAWABAN NOMOR 1: ABSTRAKSI
# ==============================================================================
# Penjelasan: 
# Abstraksi diterapkan dengan membuat kelas `RekeningBank` mewarisi `ABC` 
# (Abstract Base Class) dari modul `abc`. Hal ini mencegah pembuatan objek 
# langsung dari `RekeningBank`. Regulasi BI mengharuskan prosedur standar 
# perhitungan biaya admin dan pencetakan laporan. Oleh karena itu, kita 
# mendefinisikan `hitung_biaya_admin` dan `cetak_laporan` dengan dekorator 
# `@abstractmethod`. Ini memaksa setiap kelas anak (jenis rekening spesifik) 
# untuk mengimplementasikan (meng-*override*) fungsi-fungsi tersebut sesuai 
# dengan rumusnya masing-masing.

class RekeningBank(ABC):
    @abstractmethod
    def hitung_biaya_admin(self):
        """Method abstrak untuk menghitung biaya administrasi bulanan."""
        pass
    
    @abstractmethod
    def cetak_laporan(self):
        """Method abstrak untuk mencetak laporan ringkas."""
        pass

# ==============================================================================
# JAWABAN NOMOR 2: ENKAPSULASI
# ==============================================================================
# Penjelasan:
# - `__limit_overdraft` dan `__pin_transaksi` menggunakan dua underscore (__),
#   yang merupakan *private access modifier* (Name Mangling). Atribut ini
#   tidak bisa diakses langsung dari luar kelas untuk mencegah manipulasi fraud.
# - `_saldo` menggunakan satu underscore (_), yang secara konvensi adalah 
#   *protected access modifier*. Ini menandakan atribut ini ditujukan untuk 
#   penggunaan internal dan subclass, namun bisa dibaca menggunakan properti.
# - Getter/Setter diimplementasikan menggunakan dekorator `@property` dan 
#   `@nama_property.setter`. Setter untuk saldo divalidasi agar tidak bisa 
#   diisi dengan nilai negatif (minus).

class RekeningGiro(RekeningBank):
    def __init__(self, limit_overdraft, pin_transaksi):
        # Enkapsulasi menggunakan Private Modifier (__)
        self.__limit_overdraft = limit_overdraft
        self.__pin_transaksi = pin_transaksi
        self._saldo = 0
        
    def hitung_biaya_admin(self):
        return 25000  # Contoh implementasi biaya admin giro
    
    def cetak_laporan(self):
        print("Laporan Rekening Giro")

    # Setter dan Getter untuk limit (jika diperlukan dengan validasi)
    # PIN tidak memiliki getter/setter publik demi keamanan murni.

class RekeningTabunganBiasa(RekeningBank):
    def __init__(self, saldo_awal):
        # Enkapsulasi menggunakan Protected Modifier (_) untuk saldo
        self._saldo = saldo_awal
        
    @property
    def saldo(self):
        # Getter: Saldo boleh dibaca bebas
        return self._saldo
    
    @saldo.setter
    def saldo(self, nilai_baru):
        # Setter: Validasi ketat (tidak boleh minus)
        if nilai_baru < 0:
            raise ValueError("Saldo tidak boleh negatif!")
        self._saldo = nilai_baru

    def hitung_biaya_admin(self):
        return 10000  # Contoh implementasi biaya admin tabungan
    
    def cetak_laporan(self):
        print(f"Laporan Tabungan Biasa: Saldo saat ini Rp {self.saldo}")

# ==============================================================================
# JAWABAN NOMOR 3: OVERLOADING DAN OVERRIDING (POLIMORFISME)
# ==============================================================================
# Penjelasan Pemilihan Fungsi berdasarkan Jumlah Argumen:
# Di Python sejati, *Method Overloading* murni (membuat nama method yang sama
# dengan parameter berbeda) tidak didukung langsung. Namun, ini dapat 
# diwujudkan menggunakan *Default Arguments* atau `*args`. Pada kelas 
# `PemutarAudio` di bawah, kita mendefinisikan metode `putar` dengan parameter 
# opsional `kualitas_bitrate=None`. Saat dipanggil dengan 1 argumen, fungsi 
# mengeksekusi blok tanpa bitrate. Jika dipanggil dengan 2 argumen, ia 
# menangani logika bitrate khusus tersebut.
#
# Penjelasan Titik Resolusi Overriding (Polimorfisme):
# Meskipun objek `pemutar` bertipe deklarasi (tipe induk) `PemutarAudio`, saat
# diinisialisasi ia menunjuk ke instansiasi kelas anak `PemutarAudioPremium`.
# Konsep *Dynamic Dispatch* di Python menyebabkan sistem akan mencari 
# implementasi metode `putar` di kelas aktual objek tersebut, yaitu 
# `PemutarAudioPremium` terlebih dahulu (dari bawah ke atas di *Method 
# Resolution Order* / MRO). Sehingga perintah kedua mengeksekusi metode yang
# sudah di-*override* (mengaktifkan Dolby Atmos).

class PemutarAudio:
    def putar(self, judul_lagu, kualitas_bitrate=None):
        if kualitas_bitrate is None:
            # Fungsi 1 Parameter: Putar standar
            print(f"[Standar] Memutar '{judul_lagu}' dari penyimpanan lokal.")
        else:
            # Fungsi 2 Parameter: Putar dengan kualitas spesifik
            print(f"[Kualitas] Memutar '{judul_lagu}' dengan bitrate {kualitas_bitrate}.")

class PemutarAudioPremium(PemutarAudio):
    # Method Overriding untuk pengguna premium
    def putar(self, judul_lagu, kualitas_bitrate=None):
        if kualitas_bitrate is not None:
            # Mengoverride fungsi 2 parameter untuk mengaktifkan Dolby Atmos
            print(f"[Premium Dolby Atmos] Memutar '{judul_lagu}' pada {kualitas_bitrate} (Fitur Spatial Audio Aktif).")
        else:
            # Jika hanya 1 parameter, gunakan metode asli induk
            super().putar(judul_lagu)

# ==============================================================================
# MAIN PROGRAM (SIMULASI DAN OUTPUT)
# ==============================================================================
if __name__ == "__main__":
    print("-" * 50)
    print("SIMULASI KUIS 3 PBO - FRANSISCUS ASISI KANANDA H.D.")
    print("-" * 50)
    
    # Simulasi Enkapsulasi Tabungan
    print("\n--- Uji Enkapsulasi Tabungan ---")
    tabungan = RekeningTabunganBiasa(50000)
    print(f"Saldo Awal: Rp {tabungan.saldo}")
    tabungan.saldo = 100000
    print(f"Saldo Setelah Ubah Valid: Rp {tabungan.saldo}")
    try:
        tabungan.saldo = -20000
    except ValueError as e:
        print(f"Validasi Berhasil: {e}")

    # Simulasi Polimorfisme Audio
    print("\n--- Uji Polimorfisme & Overriding (Audio) ---")
    # Deklarasi Polimorfik (Tipe Induk, Objek Anak)
    pemutar: PemutarAudio = PemutarAudioPremium()

    # Eksekusi Perintah
    pemutar.putar("Bohemian Rhapsody")              # Perintah ke-1
    pemutar.putar("Stairway to Heaven", "320kbps")  # Perintah ke-2
    
    print("-" * 50)
