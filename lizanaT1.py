categoria = int(input("Ingresa la categoría (1 al 4): "))
sueldo = float(input("Ingresa el sueldo: "))

if categoria == 1:
    aumento = sueldo * 0.20
elif categoria == 2:
    aumento = sueldo * 0.15
elif categoria == 3:
    aumento = sueldo * 0.10
elif categoria == 4:
    aumento = sueldo * 0.05
else:
    aumento = 0

nuevo_sueldo = sueldo + aumento
print("Nuevo sueldo:", nuevo_sueldo)