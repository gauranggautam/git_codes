
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata
# === Charger le fichier brut ===
fichier = r"C:\Data\MultiHarpData\Imaging Atto\25_09_11\Data_250911_6_16.txt"  # <-- Mets le chemin de ton fichier
df = pd.read_csv(
        fichier,
        sep=r"\s+",
        header=None,
        skiprows=35,
        engine="python",
        on_bad_lines="skip",
        encoding="ISO-8859-1"
    )
# Vérification des colonnes
print(df.columns)
# Sélection colonnes 2 (index 1) et 5 (index 4)
df = df.iloc[:, [1, 3, 7]]
df.columns = ["AttoX.DetPos(um)","AttoY.DetPos(um)", "IdusCam.Integral(Cnt)"]
# Extraire les colonnes utiles
x = df["AttoX.DetPos(um)"].values
y = df["AttoY.DetPos(um)"].values
z = df["IdusCam.Integral(Cnt)"].values

plt.figure(figsize=(8,6))
sc = plt.scatter(x, y, c=z, cmap="inferno", s=300, marker="s")
plt.colorbar(sc, label="Intensité (Cnt)")
plt.xlabel("Position X (µm)")
plt.ylabel("Position Y (µm)")
plt.title("Heatmap brute (sans interpolation)")
plt.show()
plt.clf()
# === Créer une grille régulière ===
xi = np.linspace(x.min(), x.max(), 200)
yi = np.linspace(y.min(), y.max(), 200)
Xi, Yi = np.meshgrid(xi, yi)

# Interpolation des intensités

Zi = griddata((x, y), z, (Xi, Yi), method='cubic')

# === Affichage Heatmap ===
plt.figure(figsize=(8,6))
plt.imshow(Zi, extent=[x.min(), x.max(), y.min(), y.max()],
           origin='lower', aspect='auto', cmap='inferno')
plt.colorbar(label="Intensité (Cnt)")
plt.xlabel("Position X (µm)")
plt.ylabel("Position Y (µm)")
plt.title("Heatmap Intensité")
plt.show()