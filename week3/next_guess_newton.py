x = float(input("What x to find the cube root of? "))
g = float(input("What guess to start with? "))

# Kabul edilebilir hata payı (tolerans)
epsilon = 0.0001
iteration = 1

# Tahminin küpü ile x arasındaki fark toleranstan büyük olduğu sürece devam et
while abs(g**3 - x) >= epsilon:
    print(f"Adım {iteration}: Tahmin = {g:.6f}, Küpü = {g**3:.6f}")
    
    # Newton formülü ile sonraki tahmini hesapla
    next_guess = g - (g**3 - x) / (3 * (g**2))
    
    # Yeni tahmini bir sonraki adımın başlangıcı yap
    g = next_guess
    iteration += 1

print("-" * 40)
print(f"Sonuç: {x} sayısının yaklaşık küpkökü = {g:.6f}")
print(f"Kontrol (tahminin küpü): {g**3:.6f}")