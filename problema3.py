# Datos de emisiones (toneladas) para los años 2003 y 2004
datos = {
    "Panamá": [21024.83, 22144.32],
    "Costa Rica": [24131.78, 24656.78],
    "Honduras": [12058.75, 13290.85],
    "Nicaragua": [17565.62, 18715.30],
    "El Salvador": [20324.50, 21132.30],
    "Guatemala": [12197.00, 12714.35]
}

# Calcular el porcentaje de diferencia y crear la matriz
matriz = [["País", "2003", "2004", "Diferencia (%)"]]

for pais, (anio_2003, anio_2004) in datos.items():
    diferencia = ((anio_2004 - anio_2003) / anio_2003) * 100 if anio_2003 > 0 else None
    matriz.append([pais, round(anio_2003, 2), round(anio_2004, 2), round(diferencia, 2) if diferencia is not None else "N/A"])

# Imprimir la matriz
for fila in matriz:
    print(f"{fila[0]:<15} {fila[1]:<10} {fila[2]:<10} {fila[3]:<15}")

# Proyección de emisiones
años_proyeccion = int(input("\nIngrese la cantidad de años de proyección (1 a 5): "))

for pais in datos:
    ultimo_dato = datos[pais][1]
    print(f"\nProyección de emisiones para {pais}:")
    for año in range(1, años_proyeccion + 1):
        proyeccion = ultimo_dato * 1.02  # Asumir un crecimiento del 2%
        print(f"Año 2004 + {año}: {round(proyeccion, 2)} toneladas")
        ultimo_dato = proyeccion
