# variable is a object that could contain value
# Role in write name variable can't start use symbol (! @ , etc) and number/numaric, except underscore (_)
my_name: str = "putra"
_my_address: str = "jln. banyu"
My_age: int = 23
my_bodyweight: float = 59.12
my_languages: list = ["python", "R", "julia",]
my_fav: dict = {"language": "python"}

my_own_languages = ", ".join(my_languages)
my_own_fav = my_fav["language"]

print(f"saya adalah {my_name} berusia {My_age} dengan berat badan {my_bodyweight}, saya tinggal {_my_address}dan saya menguasi bahasa {my_own_languages}, tapi favorit saya adalah {my_own_fav}")

print("---Data Type---")
print(f"my_name:{type(my_name)}")
print(f"_my_address:{type(_my_address)}")
print(f"My_age:{type(My_age)}")
print(f"my_languages:{type(my_languages)}")
print(f"my_bodyweight:{type(my_bodyweight)}")
print(f"my_own_fav{type(my_fav)}")
