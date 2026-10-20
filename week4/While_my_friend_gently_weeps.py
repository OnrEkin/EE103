number1 = input("FROM WHERE? ")

# Girilen değerin tam sayı olup olmadığını kontrol etme (negatif sayılar dahil)
if number1.lstrip('-').isdigit():
    number1 = int(number1)  # İşlem yapabilmek için tam sayıya çeviriyoruz
else:
    print("Please choose a number not a string.")
    exit()

number2 = input("TO WHERE? ")

# Önce ikinci değerin de sayı olup olmadığını kontrol ediyoruz
if number2.lstrip('-').isdigit():
    number2 = int(number2)
else:
    print("Please choose a number not a string.")
    exit()

# İkinci sayı birinci sayıdan büyük değilse uyar ve çık
if number1 >= number2:
    print("Please pick second number to be bigger than first number")
    exit()

# Aradaki sayı adedini hesaplama ve döngüye sokma
carpim = 1

# number1'den number2'ye kadar (number2 dahil) döngü kuruyoruz
for i in range(number1, number2 + 1):
    carpim = carpim * i  # veya kısaca: carpim *= i

print(f"Sonuç (Çarpım): {carpim}")