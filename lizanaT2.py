t1 = float(input("Temperatura día 1: "))
t2 = float(input("Temperatura día 2: "))
t3 = float(input("Temperatura día 3: "))
humedad = float(input("Humedad actual (%): "))

promedio = (t1 + t2 + t3) / 3

if promedio > 30 and humedad < 40:
    print("Riego alto: usar 10 litros")
elif promedio > 25 and humedad < 60:
    print("Riego medio: usar 5 litros")
else:
    print("Riego bajo: usar 2 litros")