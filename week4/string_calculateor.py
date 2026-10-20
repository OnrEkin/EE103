s = "abcabc"

unique_letters = ""

for char in s:
    # Karakter daha önce biriktiriciye eklenmediyse ekle
    if char not in unique_letters:
        unique_letters += char

print(len(unique_letters))  # Çıktı: 3