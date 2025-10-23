"""
Pada file ini kita akan membahas tentang variable tentu dengan penggunakan typing style
Typi Hints yang mudah mudah komperhensif. mencakup deklarasi, scope, lifetime, dan 
best practice.
"""

from typing import Any, Dict, List, Set, Tuple, Union


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

# --- Aturan Penamaan Variable ---
"""
1. Harus dimulai dengan huruf (A-Z, a-z) dan Underscore (_)
2. Dapat diikuti dengan huruf, angka, dan Underscore
3. Case Sensitive (nama != Nama != NAMA)
4. Tidak boleh menggunakan Reserve Keyword (def, return, if, dan 30 lainnya)
5. Menggunakan snack_case convention (PEP8):
        PEP8:
        1. style guide yang menjelaskan bagaimana code python harus diformat.
        2. tujuannya adalah untuk keterbacaan dan konsistensi.
        
        snack_case:
        1. konvensi penamaan (naming convention) dimana variable ditulis dengan huruf kecil 
        dan dipisahkan dengan Underscore (_)
        2. contoh -> nama_pengguna, total_score_tertinggi, def hitung_utang(self)

        saran: selalu gunakan snack_case kecuali pada fungsi (diluar class) dan method(fugsi didalm class)
"""
print("\n --- 2. aturan penamaan yang valid")
# contoh penamaan berdasarkan PEP8
valid_variable: dict[str, Any] ={
    "nama": "putra",
    "nama_lengka": "imam putra",
    "_alamat_kos": "jln. banyu",
    "usia23": 23,
    "ipk_3": 3.79,
    "is_active": True,
}
# Contoh nama yang tidak valid
"""
2nama = "salah" --> tidak boleh mulai dengan angka
nama-lengkap = "salah" --> tidak boleh menggunkan dash/hypen
class = "salah" --> tidak boleh menggunakan Reserve Keyword
nilai total = "salah" --> tidak ada menggunakan spasi
"""

print("Contoh penamaan valid:")
for k, v in valid_variable.items():
    print(f"{k}: {v}")

# --- type Hints dasar ---
print("\n --- 3. Type Hints dasar ---")

# primitive type dengan explicit type Hints
nama_lengkap: str = "imam putra"
tahun_lahir: int = 2003
skor_ipk: float = 3.79
is_verified: bool = True
empty_date: None = None

print("Type Hints Primitive\n",
      f"String: {nama_lengkap} --> {type(nama_lengkap).__name__}\n",
      f"integer: {tahun_lahir} --> {type(tahun_lahir).__name__}\n",
      f"float: {skor_ipk} -- > {type(skor_ipk).__name__}\n",
      f"bolean value: {is_verified} --> {type(is_verified).__name__}\n",
      f"None: {empty_date} -- > {type(empty_date).__name__}\n")

# --- Variable Collactions dengan Type Hints ---
print("\n --- 4. Variable Collactions dengan Type Hints")

# List 
programming_languages: List[str] = ["python", "R", "Julia"]
nilai_ip: List[Union[int, float]] = [4, 3.8, 37.9]

# Tuple
koordinat_3d: Tuple[float, float, float] = (10.5, 20.3, 40.0)
data_mahasiswa: Tuple[str, int, float] = ("Nino", 23, 168.1)

# Dictionary
profile_user: Dict[str, Union[str, int, bool]] = {
    "username": "putra_dev",
    "email": "a.i.syahputra415@gmai.com",
    "usia": 22,
    "interdis_learn": True
}

# Set
angka_unik: Set[int] = {1, 2, 3, 4, 2, 6, 1, 8} # duplikat otomatis dihapus
kategori: Set[str] = {"Math", "AI", "Philosophy", "Economics"}

print("Collactions:\n",
      f"List: {programming_languages}\n",
      f"Tuple: {koordinat_3d}\n",
      f"Dictionary: {profile_user}\n",
      f"Set: {angka_unik}")
