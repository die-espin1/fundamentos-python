import numpy as np

consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

print("Dimensiones:", consumo.ndim)    # 2 (filas y columnas)
print("Forma:", consumo.shape)    # (10, 7) → 10 filas y 7 columnas
print("Tipo de datos:", consumo.dtype)    # float64 (números decimales)
print("Consumo primer hogar:", consumo[0])    # Todos los datos de la fila 0
print("Consumo el miércoles (día 3):", consumo[:, 2])    # Todos los datos de la columna 2

# Promedio de consumo por hogar (calcula la media por filas)
promedio_por_hogar = np.mean(consumo, axis=1)

# Promedio de consumo diario de todos los hogares (calcula la media por columnas)
promedio_por_dia = np.mean(consumo, axis=0)

# Suma total de consumo en la semana de los 10 hogares
total_consumo = np.sum(consumo)

print(promedio_por_hogar)
print(promedio_por_dia)
print(total_consumo)

# Máximo consumo por hogar (valor máximo en cada fila)
maximos = np.max(consumo, axis=1)

# Mínimo consumo por día (valor mínimo en cada columna) 
minimos = np.min(consumo, axis=0)

# Desviación estándar global de todos los datos
desviacion = np.std(consumo)

print(maximos)
print(minimos)
print(desviacion)

# Suma de consumo por hogar durante toda la semana
consumo_total_hogar = np.sum(consumo, axis=1)

# Índice del hogar con mayor consumo total (menos eficiente)
hogar_mayor_consumo = np.argmax(consumo_total_hogar)

# Índice del hogar con menor consumo total (más eficiente) 
hogar_mas_eficiente = np.argmin(consumo_total_hogar)

print("Consumo total por hogar:", consumo_total_hogar)
print("Hogar con mayor consumo (índice):", hogar_mayor_consumo)
print("Hogar más eficiente (índice):", hogar_mas_eficiente)

# Suma de consumo semanal por hogar
consumo_total_hogar = np.sum(consumo, axis=1)
print(f"\nConsumo total de cada hogar durante la semana: {consumo_total_hogar}")

# Identificación de hogares con consumo mayor a 100
altos = consumo_total_hogar > 100  # Crea máscara booleana
consumo_mayor_100 = np.where(altos)[0]  # Obtiene índices de los que cumplen

print(f"\nÍndices de hogares con consumo mayor a 100: {consumo_mayor_100}")


# 1. Consumo del hogar 5 el viernes (día 5)
consumo_hogar5_viernes = consumo[4, 4]  
print(f"1. Consumo hogar 5 el viernes: {consumo_hogar5_viernes}")

# 2. 
consumo_ultimos3_domingo = consumo[-3:, 6]  
print(f"\n2. Consumo últimos 3 hogares el domingo:\n{consumo_ultimos3_domingo}")

#3.
promedio_finde = np.mean(consumo[:, [5,6]])
print(f"\n3. Promedio consumo fines de semana: {promedio_finde:.2f}")

# 4.
desviaciones_dias = np.std(consumo, axis=0)
dia_mayor_desviacion = np.argmax(desviaciones_dias)
print(f"\n4. Día con mayor desviación estándar: Día {dia_mayor_desviacion + 1} (índice {dia_mayor_desviacion})")
print("   Esto indica que ese día los hogares muestran mayor variabilidad en sus patrones de consumo")

# 5. 
consumo_total = np.sum(consumo, axis=1)
indices_menores = np.argsort(consumo_total)[:3]
print(f"\n5. 3 hogares con menor consumo total:")
for i, idx in enumerate(indices_menores, 1):
    print(f"   Hogar {idx}: {consumo_total[idx]:.2f}")

# 6. 
hogar3_original = consumo[2]
hogar3_aumentado = hogar3_original * 1.10
nuevo_total_hogar3 = np.sum(hogar3_aumentado)
print(f"\n6. Nuevo consumo total semanal del hogar 3 (con 10% de aumento): {nuevo_total_hogar3:.2f}")