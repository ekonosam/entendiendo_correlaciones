#%%
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import itertools
import os
# Datos de ejemplo
x = [1, 2, 3, 4]
y = [1, 3, 2, 4]

# Todas las combinaciones posibles (pares únicos i < j)
pairs = list(itertools.combinations(range(len(x)), 2))

# Crear la figura
fig, ax = plt.subplots()
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Conexiones entre todas las muestras (xᵢ, yᵢ)")

# Dibujar los puntos
points = ax.scatter(x, y, color="blue")
texts = [ax.text(xi+0.1, yi+0.1, f"({{x}}_{i+1}, {{y}}_{i+1})", fontsize=9) for i, (xi, yi) in enumerate(zip(x, y))]

# Lista para las líneas
lines = []

# Función de actualización por frame
def update(frame):
    i, j = pairs[frame]
    line, = ax.plot([x[i], x[j]], [y[i], y[j]], color="gray", linewidth=1)
    lines.append(line)
    return lines

# Crear la animación
ani = animation.FuncAnimation(
    fig, update, frames=len(pairs), interval=500, blit=True, repeat=False
)

plt.show()

if not os.path.exists("videos"):
    os.makedirs("videos")
    
    
# Guardar el archivo como GIF en la carpeta "animacion"
output_path = "videos/conexiones.gif"
ani.save(output_path, writer="pillow", fps=2)


#%%