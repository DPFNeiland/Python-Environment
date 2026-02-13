import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Configurações do núcleo e órbitas
nucleus_radius = 0.2  # Raio do núcleo
orbit_radii = [1, 2, 3]  # Raio das órbitas
electron_speeds = [0.05, 0.03, 0.02]  # Velocidade angular dos elétrons

# Inicializa a figura
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.axis('off')

# Desenha o núcleo
nucleus = plt.Circle((0, 0), nucleus_radius, color='orange', label='Núcleo')
ax.add_artist(nucleus)

# Desenha as órbitas
orbits = [plt.Circle((0, 0), r, color='blue', fill=False) for r in orbit_radii]
for orbit in orbits:
    ax.add_artist(orbit)

# Inicializa os elétrons
electrons = [plt.Circle((r, 0), 0.1, color='red') for r in orbit_radii]
for electron in electrons:
    ax.add_artist(electron)

# Função de atualização para animação
def update(frame):
    for i, electron in enumerate(electrons):
        angle = frame * electron_speeds[i]
        x = orbit_radii[i] * np.cos(angle)
        y = orbit_radii[i] * np.sin(angle)
        electron.set_center((x, y))
    return electrons

# Configura a animação
ani = animation.FuncAnimation(fig, update, frames=360, interval=20, blit=True)

# Exibe a simulação
plt.legend()
plt.show()
