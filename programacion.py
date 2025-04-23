import pandas as pd

data = {
    "ID_Reporte": [1, 2, 3, 4],
    "Descripción": [
        "Bache en Av. Colón",
        "Alumbrado roto en Cerro",
        "Basura en Plaza San Martín",
        "Bache en Av. Vélez Sarsfield"
    ],
    "Barrio": ["Centro", "Cerro de las Rosas", "Centro", "Alberdi"],
    "Prioridad": ["Alta", "Media", "Baja", "Alta"]
}

df = pd.DataFrame(data)

# Buscar palabras clave según el contenido de la descripción
df["Tipo"] = df["Descripción"].apply(
    lambda x: "Bache" if "Bache" in x else
              "Alumbrado" if "Alumbrado" in x else
              "Basura" if "Basura" in x else "Otro"
)

reportes_centro_alta = df[(df["Barrio"] == "Centro") & (df["Prioridad"] == "Alta")]
print(reportes_centro_alta)

conteo_tipo_barrio = df.groupby(["Tipo", "Barrio"]).size().reset_index(name="Cantidad")
print(conteo_tipo_barrio)

df["Código"] = df["Barrio"] + "-" + df["ID_Reporte"].astype(str)

print(df)

