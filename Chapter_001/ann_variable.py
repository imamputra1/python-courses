"""
Pada file ini kita akan membahas tentang variable tentu dengan penggunakan typing style
Typi Hints yang mudah mudah komperhensif. mencakup deklarasi, scope, lifetime, dan 
best practice.
"""

print("=" * 5, "VARIABLE", "=" * 5)

# --- Konsep dasar sebuah variable ---
"""
variable adalah named storege location didalam sebuah memori yang menyimpan sebuah nilai.
python menggunakan dynamic type dengan duck type. namun disini kita menggunakan static type type
untuk mempermudah identfikasi tipe data dan type checking untuk reliability yang lebih baik.
"""
print("--- 1. konsep dasar variable ---")
# kita akan mencoba mendeklarasikan dengan type Hints
nama: str = "Putra"
_alamat_kos: str = "jln. banyu no. 123"
usia: int = 23
tinggi_badan: float = 168.99
_status_mahasiswa: bool = True

print("deklarasi tipe data\n",
      f"nama: {nama} (type: {type(nama).__name__})\n",
      f"alamat kos: {_alamat_kos} (type: {type(_alamat_kos).__name__})\n",
      f"usia: {usia} (type: {type(usia).__name__})\n",
      f"tinggi: {tinggi_badan} (type: {type(tinggi_badan).__name__})\n",
      f"status mahasiswa: {_status_mahasiswa} (type: {type(_status_mahasiswa).__name__})\n")

