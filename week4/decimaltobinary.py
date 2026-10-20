decimal_number = 13
num = decimal_number

if num == 0:
    binary_result = "0"
else:
    remainders = ""
    while num > 0:
        remainder = num % 2           # 2'ye bölümden kalan (0 veya 1)
        remainders += str(remainder)  # Kalanı kaydet
        num = num // 2                # Bölümü güncelle
    
    binary_result = remainders[::-1]  # Kalanları tersine çevir

print(f"{decimal_number} sayısının ikilik karşılığı: {binary_result}")  # Çıktı: 1101
#Mantık: $13 \div 2 = 6$ (kalan 1), $6 \div 2 = 3$ (kalan 0), $3 \div 2 = 1$ (kalan 1), $1 \div 2 = 0$ (kalan 1). Kalanlar tersten okunduğunda "1101" elde edilir.