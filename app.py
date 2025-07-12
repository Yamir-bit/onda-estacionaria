import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# 🧾 Configuración inicial
st.set_page_config(page_title="Simulación de Onda Estacionaria", layout="centered")
st.title("Simulación de Onda Estacionaria en Cuerda Vibrante")
st.markdown("**Autor:** Yamir Bermudo Reyes 23190004.")
st.write("Esta app simula una onda estacionaria en una cuerda fija por ambos extremos. "
         "Puedes cambiar el modo armónico y la amplitud para observar cómo varía la forma de la onda.")

# 🎛️ Sliders de control
modo = st.slider("Modo armónico (n)", min_value=1, max_value=6, value=1)
amplitud = st.slider("Amplitud (A)", min_value=0.1, max_value=1.0, value=1.0, step=0.1)
frecuencia = st.slider("Frecuencia (Hz)", min_value=0.5, max_value=5.0, value=1.0, step=0.1)

# 📏 Parámetros fijos
L = 1.0  # longitud de la cuerda
x = np.linspace(0, L, 1000)
omega = 2 * np.pi * frecuencia

# 📌 Función para nodos y antinodos
def nodos_antinodos(n):
    nodos = [i * L / n for i in range(n + 1)]
    antinodos = [(i + 0.5) * L / n for i in range(n)]
    return nodos, antinodos

# ⏱️ Contenedor de gráfico para animación
plot_area = st.empty()

# 🔁 Bucle de animación
for _ in range(200):  # Puedes cambiar la cantidad de ciclos
    t = time.time() % 1
    y = 2 * amplitud * np.sin(modo * np.pi * x / L) * np.cos(omega * t)

    nodos, antinodos = nodos_antinodos(modo)
    antinodo_y = [2 * amplitud * np.sin(modo * np.pi * xi / L) * np.cos(omega * t) for xi in antinodos]

    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(x, y, color="crimson", label="Onda estacionaria")
    ax.plot(nodos, [0]*len(nodos), 'ko', label="Nodos")
    ax.plot(antinodos, antinodo_y, 'bo', label="Antinodos")
    ax.set_xlabel("Posición (m)")
    ax.set_ylabel("Amplitud")
    ax.set_ylim(-1.2, 1.2)
    ax.grid(True)
    ax.set_title("Animación de Onda Estacionaria")
    ax.legend()

    plot_area.pyplot(fig)
    time.sleep(0.05)  # pausa de 50 ms


