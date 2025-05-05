import pandas as pd

# 1. Cargar base de datos
df = pd.read_csv("c:/DocumentosDeRAIZ/Ingenierìa/LenguajesProgramación/Python/PythonDeveloper/Sesion7/archivo7.csv")

# 2. Palabras clave relacionadas a contraseñas
posibles_nombres = ["passw", "passwd", "password", "passwords", "clave", "contraseña", "contraseñas"]

# 3. Buscar columnas que coincidan parcialmente con las palabras clave
coincidencias = [col for col in df.columns if any(p in col.lower() for p in posibles_nombres)]

# 4. Mostrar columnas sospechosas
if coincidencias:
    print("🔍 Columnas que podrían contener contraseñas:")
    for col in coincidencias:
        print(f"- {col}")

    # 5. Mostrar contenido parcial de cada columna
    for col in coincidencias:
        print(f"\n📂 Contenido de la columna '{col}':")
        print(df[col].head())

    # 6. Exportar a nuevo archivo
    df[coincidencias].to_csv("posibles_contraseñas.csv", index=False)
    print("\n📁 Archivo 'posibles_contraseñas.csv' creado con columnas filtradas.")
else:
    print("❌ No se encontró ninguna columna sospechosa.")
