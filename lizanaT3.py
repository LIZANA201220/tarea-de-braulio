temporada = input("Temporada (baja, media o alta): ").lower()
salario = float(input("Salario: "))
gastos = float(input("Gastos: "))
presupuesto = salario - gastos

if temporada == "baja" and presupuesto >= 1300:
    print("Puedes hacer un viaje internacional")
elif temporada == "media" and presupuesto >= 800:
    print("Puedes hacer un viaje nacional")
elif temporada == "alta" and presupuesto >= 400:
    print("Puedes hacer un viaje local")
else:
    print("No alcanza, mejor quédate en casa a dormir ")