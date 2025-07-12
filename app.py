import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_autorefresh import st_autorefresh
import time

# Recargar la página automáticamente cada 100ms (10 FPS aprox.)
st_autorefresh(interval=100, limit=1000, key="refresh")

# Configuración de la app
st.set_page_config(page_title="Simulación de Onda Estacionaria", layout="centered")
st.title(" Simulación de Onda Estacionaria en Cuerda Vibrante")
st.markdown("**Autor:** Yamir Bermudo Reyes 23190004")
st.write("Esta app simula una onda estacionaria en una cuerda fija por ambos extremos. "
         "Puedes cambiar el modo armónico y la amplitud para observar cómo varía la forma de la onda.")

# Parámetros ajustables
modo = st.slider("Modo armónico (n)", min_value=1, max_value=6, value=1)
amplitud = st.slider("Amplitud (A)", min_value=0.1, max_value=1.0, value=1.0, step=0.1)

# Tiempo: se genera automáticamente
t = time.time() % 1  # valor entre 0 y 1 que cambia constantemente

# Dominio espacial
L = 1.0
x = np.linspace(0, L, 1000)
omega = 2 * np.pi * 1
y = 2 * amplitud * np.sin(modo * np.pi * x / L) * np.cos(omega * t)

# Nodos y antinodos
def nodos_antinodos(n):
    nodos = [i * L / n for i in range(n + 1)]
    antinodos = [(i + 0.5) * L / n for i in range(n)]
    return nodos, antinodos

nodos, antinodos = nodos_antinodos(modo)
antinodo_y = [2 * amplitud * np.sin(modo * np.pi * xi / L) * np.cos(omega * t) for xi in antinodos]

# Graficar
fig, ax = plt.subplots(figsize=(8, 3))
ax.plot(x, y, color="crimson", label="Onda estacionaria")
ax.plot(nodos, [0]*len(nodos), 'ko', label="Nodos")
ax.plot(antinodos, antinodo_y, 'bo', label="Antinodos")
ax.set_xlabel("Posición (m)")
ax.set_ylabel("Amplitud")
ax.set_ylim(-1.2, 1.2)
ax.grid(True)
ax.set_title("Onda estacionaria (auto-actualizada)")
ax.legend()

# Mostrar en Streamlit
st.pyplot(fig)
