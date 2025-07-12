import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# Configuración inicial
st.set_page_config(page_title="Simulación de Onda Estacionaria", layout="centered")
st.title("🌊 Simulación de Onda Estacionaria en Cuerda Vibrante")
st.markdown("**Autor:** Yamir Bermudo Reyes 23190004.")

# Parámetros de usuario
modo = st.slider("Modo armónico (n)", 1, 6, 1)
amplitud = st.slider("Amplitud (A)", 0.1, 1.0, 1.0, 0.1)
frecuencia = st.slider("Frecuencia (Hz)", 0.5, 5.0, 1.0, 0.1)

# Tiempo actual (simula animación)
t = time.time() % 1
omega = 2 * np.pi * frecuencia
L = 1.0
x = np.linspace(0, L, 1000)
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
ax.plot(x, y, color="crimson", label="Onda estacionaria")
ax.plot(nodos, [0]*len(nodos), 'ko', label="Nodos")
ax.plot(antinodos, antinodo_y, 'bo', label="Antinodos")
ax.set_ylim(-1.2, 1.2)
ax.set_xlabel("Posición (m)")
ax.set_ylabel("Amplitud")
ax.set_title("Simulación de un Frame (refrescar para animar)")
ax.grid(True)
ax.legend()

st.pyplot(fig)
st.markdown("⏱️ *Cada vez que recargues la página, verás un nuevo instante de tiempo.*")

# Opcional: botón para recargar
if st.button("🔄 Ver siguiente instante"):
    st.experimental_rerun()


