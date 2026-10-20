fraction = 0.375
f = fraction

binary_fraction = "0."

while f > 0:
    f = f * 2
    integer_part = int(f)             # Virgülün solundaki tam kısmı al (0 veya 1)
    binary_fraction += str(integer_part)
    f = f - integer_part              # Yeni kesirli kısmı sakla

print(f"{fraction} kesrinin ikilik karşılığı: {binary_fraction}")  # Çıktı: 0.011