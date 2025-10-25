"""
Pada file ini kita akan membahas tentang variable tentu dengan penggunakan typing style
Typi Hints yang mudah mudah komperhensif. mencakup deklarasi, scope, lifetime, dan 
best practice.
"""

from typing import Any, Callable, ClassVar, Dict, Final, List, Optional, Set, Tuple, Union, TypeAlias
from dataclasses import dataclass

print("=" * 5, "VARIABLE", "=" * 5)

# --- KONSEP DASAR SEBUAH VARIABLE ---
"""
variable adalah named storege location didalam sebuah memori yang menyimpan sebuah nilai.
python menggunakan dynamic type dengan duck type. namun disini kita menggunakan static type type
untuk mempermudah identfikasi tipe data dan type checking untuk reliability yang lebih baik.
"""
print("--- 1. konsep dasar variable ---")
# kita akan mencoba mendeklarasikan dengan type Hints:
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

# --- ATURAN PENAAMAAN VARIABLE ---
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
# contoh penamaan berdasarkan PEP8:
valid_variable: dict[str, Any] ={
    "nama": "putra",
    "nama_lengka": "imam putra",
    "_alamat_kos": "jln. banyu",
    "usia23": 23,
    "ipk_3": 3.79,
    "is_active": True,
}
# Contoh nama yang tidak valid:
"""
2nama = "salah" --> tidak boleh mulai dengan angka
nama-lengkap = "salah" --> tidak boleh menggunkan dash/hypen
class = "salah" --> tidak boleh menggunakan Reserve Keyword
nilai total = "salah" --> tidak ada menggunakan spasi
"""

print("Contoh penamaan valid:")
for k, v in valid_variable.items():
    print(f"{k}: {v}")

# --- TYPE HINTS DASAR---
print("\n --- 3. Type Hints dasar ---")

# primitive type dengan explicit type Hints:
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

# --- VARIABLE COLLACTIONS DAN TYPE HINTS ---
print("\n --- 4. Variable Collactions dengan Type Hints")

# Type countainer list:
programming_languages: List[str] = ["python", "R", "Julia"]
nilai_ip: List[Union[int, float]] = [4, 3.8, 37.9]

# Type countainer Tuple:
koordinat_3d: Tuple[float, float, float] = (10.5, 20.3, 40.0)
data_mahasiswa: Tuple[str, int, float] = ("Nino", 23, 168.1)

# Type countainer Dictionary:
profile_user: Dict[str, Union[str, int, bool]] = {
    "username": "putra_dev",
    "email": "a.i.syahputra415@gmai.com",
    "usia": 22,
    "interdis_learn": True
}

# Type countainer Set:
angka_unik: Set[int] = {1, 2, 3, 4, 2, 6, 1, 8} # duplikat otomatis dihapus
kategori: Set[str] = {"Math", "AI", "Philosophy", "Economics"}

print("Collactions:\n",
      f"List: {programming_languages}\n",
      f"Tuple: {koordinat_3d}\n",
      f"Dictionary: {profile_user}\n",
      f"Set: {angka_unik}")

# --- TYPE ALIASES ---
print("\n --- 5. Type Aliases ---")
# kita coba menaikan kompleksitas code kita, untuk menghandlenya kita menggunkan Aliases:
Vector3D: TypeAlias = Tuple[float, float, float]
Person: TypeAlias = Dict[str, Union[str, int, float, bool]]
Matrix: TypeAlias = List[List[float]]

posisi: Vector3D = (1.0, 2.5, 3.7)
user_data: Person = {
    "nama": "Nino Reysa",
    "usia": 23,
    "tinggi": 169.1,
    "is_active": True
}
matrix: Matrix = [
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0]
]
print("Type Aliases\n",
      f"Vector3D: {posisi} ->\n"
      f"User Value: {user_data}\n",
      f"Matrix: {matrix}\n")


# --- OPTIONAL DAN UNION ---
print("---  6. Union and Option Type ---")
# Optional String artinya bisa string atau None:
name_middle: Optional[str] = None
nomor_telpon: Optional[str] = "+628 1234567890"

# Union type untuk multiple possible type:
identifier: Union[str, int] = 1234567890
identifier = "USER_123"

# complex union type:
config_value: Union[str, int, float, bool, None] = "enable"
config_value = 43
config_value = None

print("Optional  and Union Type")
print(f"Middle name: {name_middle}")
print(f"Telepon: {nomor_telpon}")
print(f"Identifier: {identifier}")
print(f"config_value: {config_value}")

# --- CONSTANTS DAN VARIABLE ---
print("\n --- 7. Konstanta dan Final Variable ---")
#Konvensi: UPPERCASE untuk Konstanta:
PI: Final[float] = 3.14159
MAX_CONNECTIONS: Final[float] = 1000
DATABASE_URL_: Final[str] = "postgresql://localhost:5432/app_db"
DEFAULT_TIMEOUT: Final[int] = 30

# Class variables (shared across instances):
class AppConfig:
    VERSION: ClassVar[str] = "1.0.0"
    DEBUG_MODE: ClassVar[bool] = False
    SUPPORTED_LANGUAGES: ClassVar[List[str]] =["en", "id", "ja"]

print("Constanta dan Final Variable")
print(f"PI: {PI}")
print(f"MAX_CONNECTIONS: {MAX_CONNECTIONS}")
print(f"App Version: {AppConfig.VERSION}")
print(f"Debug Mode: {AppConfig.DEBUG_MODE}")

# --- VARIABLE SCOPE DAN LIFETIME ---
print("\n --- 8. Variable scope dan Lifetime ---")
# global scope:
counter_global: int = 0

def increment_counter() -> int:
    """Fungsi dengan variable local dan variable global"""
    # local variable:
    counter_local: int = 0
    counter_local += 1
    # Mengakses dan modify global variable:
    global counter_global
    counter_global += 1

    return counter_local

def outer_function() -> Callable[[], int]:
    """Contoh Clouser dengan nonlocal variable."""
    count: int = 0
    
    def inner_function() -> int:
        nonlocal count # Mengacu ke variable di outer finction
        count += 1
        return count
    
    return inner_function
# Test scope:
print("Variable Scope:")
local_result = increment_counter()
print(f"Local Counter: {local_result}")
print(f"Global Counter: {counter_global}")

# Test closure:
closure_func = outer_function()
print(f"Closure call 1: {closure_func()}")
print(f"Closure call 2: {closure_func()}")
print(f"Closure call 3: {closure_func()}")

# --- TYPE CONVERSION (CASTING) ---
print("\n --- 9. Type Convention (Casting) ---")
# Explicit type convention:
angka_string: str = "123"
angka_integer: int = int(angka_string)
angka_float: float = float(angka_string)

float_string: str = "45.67"
float_value: float = float(float_string)
int_from_float: int = int(float_value) # Truncate, Not Round

# Bolean Convention:
truthy_value: bool = bool(1) # True
falsy_value: bool = bool(0) # False
falsy_string: bool = bool("") #False

# Collaction convention:
list_from_tuple: List[int] = list ((1, 2, 3))
tuple_from_list: Tuple[int, ...] = tuple([1, 2, 3])
set_from_list: Set[int] = set ([1, 2, 3, 3])

print("Type Convention")
print(f"String '123' --> int: {angka_integer}\n",
    f"String '123' --> float: {float_value}\n",
    f"Float 45.67 --> int: {int_from_float}")
print(f"Bool converstion: 1 --> {truthy_value}, 0 --> {falsy_value}, and '' -> {falsy_string}")
print(f"Tuple type --> List: {list_from_tuple}")
print(f"List type --> tuple: {tuple_from_list}")
print(f"List type --> set: {set_from_list}")

# --- VARIABLE OPERATIONS ---
print("\n --- 10. Variable Operations ---")

# Multi Assignment:
x: int = 10
y: int = 20
z: int = 30

# Swap values
print(f"Sebelum swap: x = {x}, y = {y}")
x, y = y, x # kita coba penulisan yang sedikit berbeda
print(f"Sesudah Swap: x = {x}, y = {y}")

# Chained Assignment
a = b = c = 0 # semua variable mendapatkan value 0

# Extended Unpacking
numbers: List[int] = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(f"Unpacking: First = {first}, middle = {middle}, last = {last}")

# Walrus Operator (Python 3.8+)
if (n := len(numbers)) > 3:
    print(f"List memiliki {n}, elements (lebih dari 3)")

# --- DATACLASS UNTUK STRUCTRED DATA ---
print("\n --- 11. Dataclass untuk structured data ---")

# Membuat dataclass dari module dataclasses:
@dataclass
class PersonData:
    """Dataclass untuk merepresentasikan data person"""
    name: str
    usia: int
    email: str
    is_verified: bool = False
    skills: List[str] = None

    def __post_init__(self) -> None:
        """Initialize default values after init."""
        if self.skills is None:
            self.skills = []

    @property
    def tahun_lahir(self) -> int:
        """Calculate birthday year from age."""
        current_year: int = 2024
        return current_year - self.usia

    def tambah_skill(self, skill: str) -> None:
        """Add new Skills"""
        self.skills.append(skill)

# Menggunakan dataclass:
person1: PersonData = PersonData(
    name = "putra",
    usia = 23,
    email = "putra@mail.test",
    skills = ["Python", "Data analysis"]
)
person1.tambah_skill("Machine learning")

print("DataClass Example:")
print(f"Person: {person1.name}, usia: {person1.usia}")
print(f"Tahun lahir: {person1.tahun_lahir}")
print(f"Skills: {', '.join(person1.skills)}")

