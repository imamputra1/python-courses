from typing import Any, Callable, Dict, List, Tuple, Set, Optional, Union

print("=== Perkenalan Pemerograman dengan Python ===")
"""
gua akan mendokumentasikan pengetahuan gua seputar Python
dalam directory ini. gua harap ini bisa membantu untuk
kalian yang ingin belajar. pendekatan yang gua pakai menggunakan
annotasi type hint untuk membiasakan membuat code yang robust
"""
# 1. Pintu Gerbang kita, katanya gitu sih
print("\n --- Statement paling sakral ---")
print("Hello World")    # String literal teks/karakter
print("1234567890")     # string literal Numerik sebagai String
print("!@$%^&*,.:(){}") # String literal Symbol atau karakter khusus

# 2. sekarang kita tes variable dan data type
print("\n--- Apa itu variable dan data type? ---")
# variable String 
my_name: str = "Putra"
My_massage: str = "semoga code dan penjelasannya ga buat bingungin"
# variable numarik
age: int = 22
body_height: float = 168.72
# variable boolean
was_married: bool = False
student: bool = True

print(My_massage)
print(f"\nHallo, nama saya: {my_name}")
print(f"Umur: {age} tahun")
print(f"Tinggi badan: {body_height}")
print(f"Status Pernikahan: {was_married}")
print(f"Status mahasiswa: {student}")

# 3. kita akan mencoba operasi aritmatika dasar
print("\n --- Contoh Syntax operasi aritmatika ---")
a: int = 18
b: float = 20.02
print(f" a = {a}, b = {b}")
print(f"penjumlahan: {a} + {b} = {a+b}")
print(f"pengurangan: {a} - {b} = {a-b}")
print(f"perkalian: {a} - {b} = {a*b}")
print(f"pembagian: {a} / {b} = {a/b}")
print(f"pembagian bulat: {a} // {b} = {a//b}")
print(f"modulus atau sisa bagi: {a} % {b} = {a%b}")
print(f"pangkat/exponensial: {a}**{b} = {a**b}")

# 4. kita coba fungsi build-in python  type() dengan type hint
print("\n --- kita tes melakukan pengecekan primitive data type dengan fungsi build-in type() ---")
string_kosong: str = ""
string_isi: str = "Gas"
bilangan_natural: int = 8
bilangan_bulat: int = -1
bilangan_rasional: float = 2.1
boolean_value: bool = True
none_value: None = None

print(f"primitive data type string kosong: {type(string_kosong)}")
print(f"primitive data type string isi: {type(string_isi)}")
print(f"primitive data type natural int: {type(bilangan_natural)}")
print(f"primitive data type rasional int: {type(bilangan_rasional)}")
print(f"primitive data type bilangan bulat: {type(bilangan_bulat)}")
print(f"primitive data type bolean value: {type(boolean_value)}")
print(f"primitive data type none value: {type(none_value)}")

# 5. kita coba fungsi dengan type hint
print("\n --- Fungsi Dengan Type Hints ---")
def sapa(my_name: str) -> str:
    """fungsi menyapa dengan type hints."""
    return f"helo, {my_name}!"
def hitung_luas_persegi_Panjang(length: float, width: float) -> float:
    """fungsi menghitung luas persegi panjang"""
    return length * width
def cek_status(age: int, was_married: bool) -> Tuple[str, bool]:
    """
    Melakuakan pengecekan status berdasarkan umur dan status pernikahan.
    kita coba Return:
        Tuple kita aka berisi status dan apakah ini eligible untuk program tertentu
    """
    if age >= 21 and not was_married:
        return "Dewasa belum menikah", True
    elif age >= 21 and was_married:
        return "Dewas sudah menikah", False
    else:
        return "Remaja", False
# Kita coba menggunakan fungsi diatas
print(sapa("Nino"))
luas: float = hitung_luas_persegi_Panjang(5.2, 3.2)
print(f"luas: {luas}")

status, eligible = cek_status(23, False)
print(f"status: {status}, eligible: {eligible}")

# 6. COLLECTIONS dengan Type hints
print("\n --- 6. Collections dengan Type Hints ---")
# List dengan type hints
expertis: List[str] = ["AI-Ethics", "Econimic", "Computer science", "Philosophy"]
angka: List[Union[int, float]] = [1, 2, 3, 4.2, 5.12]
# Dictionary dengan type hints
students: Dict[str, Union[str, int]] = {
    "my_name": "Imam",
    "student_id": "476713",
    "age": 23
}
# Tuple dengan type hints
koordinat: Tuple[float, float, float] = (10.5, 20.3, 5.0)
# Set dengan type hints
unique_numbers: Set[int] = {1, 2, 3, 4, 5}
print(f"List expertis: {expertis}")
print(f"List angka: {angka}")
print(f"Dictionary Student: {student}")
print(f"Tuple Koordinat: {koordinat}")
print(f"Set numbers: {unique_numbers}")

# 7. OPTIONAL DAN UNION TYPES
print("\n ---7. Optinal dan union types")
# Optional berarti bisa berupa tipe tertentu atau None
optional_name: Optional[str] = None  # kita bisa menggunakan string atau None
optional_age: Optional[int] = 25
# Union berarti bisa berupa salah satu dari beberapa tipe
id_user: Union[int, str] = 1234567890    # bisa int dan string
id_user = "ABC123"    #Valid

print(f"Nama Optional: {optional_name}")
print(f"Umur optional: {optional_age}")
print(f"ID user: {id_user}")

def proses_data(data: Union[str, int, List[int]]) -> str:
    """Kita akan memproses data yang bisa berupa string, integers, atau list of int"""
    if isinstance(data, str):
        return f"Sting: {data.upper()}"
    elif isinstance(data, int):
        return f"Int: {data * 2}"
    else:
        return f"List: {sum(data)}"
print(proses_data("hello"))
print(proses_data(10))
print(proses_data([1, 2, 3]))

# 8. Type Aliases
print("\n --- 8. Type Aliases --- ")
# Kita akan membuat sebuah code yang lebih bersih
Vector = Tuple[float, float, float]
Person = Dict[str, Union[str, int, bool]]

# kita akan membuat sebuah Aliases
posisi: Vector = (1.2, 2.3, 3.4)
orang: Person = {
    "name": "Agus",
    "age": 23,
    "aktif": True
}
print(f"posisi:{posisi}")
print(f"saya: {orang}\n")
print("-" * 10, "memeriksa rincian tipe data didalam tuple", "-" * 10)
data_type_posisi = [] #Objek/wadah untuk memuat hasil looping
for element in posisi:
    data_type_posisi.append(type(element))
    print(f"element: {element}, tipe data: {type(element)}")
    print("-" * 40)# loping untuk memeriksa masing masing tipe data didalam tuple
set_tipe_tuple = set(type(element) for element in posisi) # memeriksa dengan fungsi build-in set() tipe data yang uniq
print("\n", "-" * 10, "memeriksa rincian tipe data didalam disc", "-" * 10)

for key, value in orang.items(): 
    print(f"key: '{key}': tipe data --> {type(key)}")
    print(f"value: '{value}': tipe data --> {type(value)}")
    print("-" * 40)
key_type_orang = [type(k) for k in orang.keys()]
value_type_orang = [type(v) for v in orang.values()]
set_tipe_dict = all(isinstance(v, str) for v in orang.values())
print("Data Type dari Vector, posisi, Person, dan orang \n",
      type(Vector), type(posisi), type(Person), type(orang),"\n",
      "-" * 40,f"\n Ini adalah ringkasan tipe data tuple yang bertipe data sama: {len(set_tipe_tuple) == 1}\n tipe data: {data_type_posisi}"
)
print("-"* 40)
print(f"\n ini adalah ringkasan tipe data yang ada didalam Dictionary:\n key --> {key_type_orang}\n value --> {value_type_orang}")

# class dengan type hints
print("\n --- 9. Class dengan Type Hints ---")

class Mahasiswa:
    """class mahasiswa dengan type hints"""
    def __init__(self, name: str, nim: str, ipk: float) -> None:
        self.name: str = name
        self.nim: str = nim
        self.ipk: float = ipk
        self.mata_kuliah: List[str] = []

    def tambah_matkul(self, matkul: str) -> None:
        """Menambah mata kuliah"""
        self.mata_kuliah.append(matkul)

    def update_ipk(self, ipk_baru: float) -> None:
        self.ipk = ipk_baru
        print(f"IPK {self.name} berhasil diperbaharui {self.ipk}")

    def get_info(self) -> Dict[str, Union[str, float, List[str]]]:
        """mengembalikan (return) informasi mahasiswa"""
        return{
            "nama": self.name,
            "nim": self.nim,
            "ipk": self.ipk,
            "mata_kuliah": self.mata_kuliah
        }
# Menggunakan Class
mhs: Mahasiswa = Mahasiswa("Dea", "001100", 3.21)
mhs.tambah_matkul("programan python")
mhs.tambah_matkul("algoritma")
mhs.tambah_matkul("struktur data")

info: Dict[str,Union[str, float, List[str]]] = mhs.get_info()
print(f"Info mahasiswa: {info}\n")

# 10. Advanced Type Hints
print("\n --- 10. Advanced Type Hints ---")
# Callable type untuk fingsi
math_opertion = Callable[[float, float], float]

def apply_operation(a: float, b: float, operation: math_opertion) -> float:
    """Menarapkan operasi matematika pada dua angka."""
    return operation(a, b)

def tambah(x: float, y: float) -> float:
    return x + y
def kali(x: float, y: float) -> float:
    return x * y
add: float = tambah(5, 2)
multiple: float = kali(20.02, 20.25)

print(f"5 + 2 = {apply_operation(5, 2, tambah)}")
print(f"20.25 + 20.02 = {apply_operation(20.02, 20.25, kali)}")
print("diatas kita langsung mengakases value yang ada didalam return dari fingsi tambah dan kurang tanpa menyimpan di variable")

print(f"kita coba untuk memanggil dari value yang sudah disimpan di varable add: {add} dan multiple: {multiple}")

# 11. Type Hint untuk memeriksa Runtime
print("--- 11. type hint untuk memeriksa runtime ---")

def validasi_data(data: Any, expected_type: type) -> bool:
    """Validasi tipe data pada runtime"""
    if isinstance(data, expected_type):
        print(f"data {data} bertipe {expected_type.__name__} - VALID")
        return True
    else:
        print(f"data {data} bertipe {type(data).__name__}, expected {expected_type.__name__} - INVALID")
        return False
# Testing Validasi
validasi_data("hello", str)
validasi_data(123, str)
validasi_data([1, 2, 3], list)
validasi_data(3.14, float)
