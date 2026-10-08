import random
import csv

random.seed(42)  # para que siempre salgan los mismos datos

estaciones = ["Portal Norte", "Calle 100", "Av. Chile", "Av. Jiménez", "Portal Sur"]
franjas = ["pico_manana", "valle", "pico_tarde", "noche"]

filas = []
for _ in range(300):
    estacion = random.choice(estaciones)
    franja = random.choice(franjas)
    lluvia = random.choice([0, 1])
    pasajeros = random.randint(50, 400)

    # entre más cosas "malas" juntas, más chance de retraso
    prob = 0.1
    if franja in ("pico_manana", "pico_tarde"):
        prob += 0.4  # hora pico
    if lluvia == 1:
        prob += 0.2
    if pasajeros > 300:
        prob += 0.2  # bus muy lleno

    retraso = 1 if random.random() < prob else 0
    filas.append([estacion, franja, lluvia, pasajeros, retraso])

# guardo todo en un csv
with open("datos_transmilenio.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["estacion", "franja", "lluvia", "pasajeros", "retraso"])
    w.writerows(filas)

print("Listo, dataset creado")