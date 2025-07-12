import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# Configuración
st.set_page_config(page_title="Onda Estacionaria", layout="centered")
st.title("🌊 Onda Estacionaria en una Cuerda")
st.markdown("**Autor:** Yamir Bermudo Reyes 23190004.")

# Controles
modo = st.slider("Modo armónico (n)", 1, 6, 1)
amplitud = st.slider("Amplitud (A)", 0.1, 1.0, 1.0, 0.1)
frecuencia = st.slider("Frecuencia (Hz)", 0.5, 5.0, 1.0, 0.1)

# Tiempo variable para simular movimiento
t = time.time() % 1
L = 1.0
x = np.linspace(0, L, 1000)
omega = 2 * np.pi * frecuencia
y = 2 * amplitud * np.sin(modo * np.pi * x / L) * np.cos(omega * t)

# Nodos y antinodos
def nodos_antinodos(n):
    nodos = [i * L / n for i in range(n + 1)]
    antinodos = [(i + 0.5) * L / n for i in range(n)]
    return nodos, antinodos

nodos, antinodos = nodos_antinodos(modo)
antinodo_y = [2 * amplitud * np.sin(modo * np.pi * xi / L) * np.cos(omega * t) for xi in antinodos]

# Gráfico
fig, ax = plt.subplots(figsize=(8, 3))
ax.plot(x, y, "crimson", label="Onda estacionaria")
ax.plot(nodos, [0]*len(nodos), "ko", label="Nodos")
ax.plot(antinodos, antinodo_y, "bo", label="Antinodos")
ax.set_ylim(-1.2, 1.2)
ax.set_xlabel("Posición (m)")
ax.set_ylabel("Amplitud")
ax.set_title("Frame actual de la onda")
ax.grid(True)
ax.legend()

st.pyplot(fig)



