import pandas as pd


# jugamos coon el codigo
def bubble_sort_basico(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

valores = [5, 2, 9, 1, 5, 6]
print("Original:", valores)
print("Ordenado:", bubble_sort_basico(valores.copy()))

def insertion_sort(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista

valores = [9, 3, 7, 1, 5]
print("Original:", valores)
print("Ordenado:", insertion_sort(valores.copy()))

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

