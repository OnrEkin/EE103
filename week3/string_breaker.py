#unbroken=str("onoeWoUiEKIN284jnf2mfds")
#broken= unbroken[8:12]
#print("My name is",broken)

#----------------------------------------#

unbroken = "onoeWoUiEKIN284jnf2mfds"
name = "EKIN"

# unbroken içindeki ismi boş karakterle ("") değiştirerek siliyoruz:
junk = unbroken.replace(name, "")

print(f"junk={junk} name={name}")

#----------------------------------------#

#unbroken = "onoeWoUiEKIN284jnf2mfds"
#target = "EKIN"

# İsmin başladığı indeksi bulur
#start = unbroken.find(target)
#end = start + len(target)

# İsmi metinden çeker
#name = unbroken[start:end]

# İsmin öncesini ve sonrasını birleştirir
#junk = unbroken[:start] + unbroken[end:]

#print(f"junk={junk} name={name}")
