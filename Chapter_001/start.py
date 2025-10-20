from typing import Dict, List, Tuple, Set, Optional, Union


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
print(f"\n Hallo, nama saya: {my_name}")
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
def hitung_luas_persegi(length: float, width: float) -> float:
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
luas: float = hitung_luas_persegi(5.2, 3.2)
print(f"luas: {luas}")

status, eligible = cek_status(23, False)
print(f"status: {status}, eligible: {eligible}")

# 6. COLLECTIONS dengan Type hints
print("\n --- 6. Collections dengan Type Hints ---")
# List dengan type hints
expertis: List[str] = ["AI-Ethics", "Econimic", "Computer science", "Philosophy"]
angka: List[Union[int, float]] = [1, 2, 3, 4.2, 5.12]
# Dictionary dengan type hints
student: Dict[str, Union[str, int]] = {
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
