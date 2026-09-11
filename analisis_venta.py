import pandas as pd
import io

# 1. Datos simulados en formato CSV (Insumo de la práctica)
csv_data = """Fecha,ID_Transaccion,Producto,Categoria,Precio_Unitario,Cantidad,Metodo_Pago
2023-10-01,1001,Laptop Pro 15,Electronica,1200.50,1,Tarjeta
2023-10-01,1002,Raton Inalambrico,Accesorios,25.00,2,Efectivo
2023-10-02,1003,Monitor 27in,,250.00,1,Tarjeta
2023-10-02,1004,Teclado Mecanico,Accesorios,85.50,1,
2023-10-03,1005,Laptop Pro 15,Electronica,1200.50,2,Transferencia
2023-10-03,1006,Raton Inalambrico,Accesorios,25.00,5,Tarjeta
2023-10-04,1007,Auriculares Bluetooth,Electronica,,1,Efectivo
2023-10-04,1008,Soporte para Laptop,Accesorios,30.00,3,Tarjeta
"""

# 2. Carga del conjunto de datos
df = pd.read_csv(io.StringIO(csv_data))

# 3. Exploración inicial
print("--- Exploración Inicial ---")
print(df.info())
print("\nValores nulos por columna:\n", df.isnull().sum())

# 4. Limpieza de datos (Manejo de nulos)
# Se rellena la categoría faltante con la etiqueta 'Desconocido'
df['Categoria'] = df['Categoria'].fillna('Desconocido')

# Se rellena el precio unitario faltante con el promedio de dicha columna
promedio_precio = df['Precio_Unitario'].mean()
df['Precio_Unitario'] = df['Precio_Unitario'].fillna(promedio_precio)

# 5. Creación de nuevas variables
df['Ingreso_Total'] = df['Precio_Unitario'] * df['Cantidad']

# 6. Análisis descriptivo básico
ingresos_por_categoria = df.groupby('Categoria')['Ingreso_Total'].sum().reset_index()

print("\n--- Resultados del Análisis ---")
print("Ingresos totales por categoría:")
print(ingresos_por_categoria)
