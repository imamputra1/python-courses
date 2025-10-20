print("=== Perkenalan Pemerograman dengan Python ===")
"""
gua akan mendokumentasikan pengetahuan gua seputar Python
dalam directory ini. gua harap ini bisa membantu untuk
kalian yang ingin belajar. pendekatan yang gua pakai juga
menggunakan annotasi type hint untuk membiasakan membuat code yang
robust
"""
# 1. Pintu Gerbang, katanya gitu sih
print("\n --- Statement paling sakral ---")
print("Hello World")    # String teks
print("1234567890")     # Numerik sebagai String
print("!@$%^&*,.:(){}") # Symbol atau karakter khusus

# 2. Apa itu variable dan data type?
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

# 3. Operasi aritmatika dasar
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

# 4. kita tes fungsi build-in python  type() dengan type hint
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

# 5. kita tes fungsi dengan type hint
print("\n --- ")


