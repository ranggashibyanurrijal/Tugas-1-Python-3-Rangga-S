print("=======================================================")
print("\t\tIndex Massa Tubuh (IMT)\nadalah nilai yang diambil dari perhitungan hasil bagi\nantara berat badan (BB) dalam kilogram dengan kuadrat\ndari tinggi badan (TB) dalam meter.")
print("=======================================================")

Berat_Badan = int(input("Masukan Berat Badan Anda : "))
Tinggi_Badan = int(input("Masukan Tinggi Badan Anda : "))

Tinggi_Badan = Tinggi_Badan / 100

IMT = Berat_Badan / (Tinggi_Badan ** 2)

print("Nilai IMT anda :", IMT)

if IMT < 18.5:
    print("Status Gizi : Underweight")
elif 18.5 <= IMT < 24.99:
    print("Status Gizi : Normal range")
elif 25 <= IMT < 29.99:
    print("Status Gizi : Overweight")
elif 30 <= IMT < 34.99:
    print("Status Gizi : Obese class 1")
elif 35 <= IMT < 39.99:
    print("Status Gizi : Obese class 2")
else:
    print("Status Gizi : Obese class 3")