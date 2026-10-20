target = 0.1
f = target

result = 0.0
power = 0.5  # İlk basamağın ikilik değeri: 2^(-1) = 0.5
binary_fraction = "0."

# Gerçek değerle yaklaşım arasındaki fark 0.00001'den büyük olduğu sürece devam et
while abs(result - target) >= 0.00001:
    f = f * 2
    integer_part = int(f)
    binary_fraction += str(integer_part)
    
    if integer_part == 1:
        result += power
        
    power /= 2                        # Sıradaki basamağın ondalık değeri (0.25, 0.125, ...)
    f = f - integer_part

print(f"0.1 sayısının ikilik yaklaşımı: {binary_fraction}")
print(f"Elde edilen yaklaşık ondalık değer: {result}")
print(f"Hata payı: {abs(result - target)}")