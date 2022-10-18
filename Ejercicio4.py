edad = int(input("introduce tu edad: \n"))
ingresos = float(input("introduce tus ingresos mensuales: \n"))
if edad > 16 and ingresos >= 1000:
    print("Puedes tributar")
else:
    print("No puedes tributar")