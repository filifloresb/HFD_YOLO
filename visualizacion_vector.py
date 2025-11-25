import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

# --- Vector fijo vertical (desde el origen) ---
v_vert = np.array([0, -1])

# Figura y ejes
fig, ax = plt.subplots(figsize=(5, 6))
plt.subplots_adjust(left=0.1, bottom=0.30)  # Dejamos espacio para más sliders

# Ejes base
ax.axhline(0, linewidth=1)
ax.axvline(0, linewidth=1)
ax.set_xlim(-3, 3)
ax.set_ylim(2, -3)      # Eje Y invertido tipo imagen
ax.set_aspect('equal', 'box')
ax.grid(True)

# Vector vertical fijo desde (0,0)
vert_arrow = ax.quiver(0, 0, v_vert[0], v_vert[1],
                       angles='xy', scale_units='xy', scale=1, linewidth=3)

# Vector variable inicial
ox0, oy0 = 0.5, 0.5   # origen inicial
vx0, vy0 = 1.0, -0.5  # componentes iniciales
v_var = np.array([vx0, vy0])

var_arrow = ax.quiver(ox0, oy0, v_var[0], v_var[1],
                      angles='xy', scale_units='xy', scale=1, linewidth=3)

# Texto para mostrar ángulo
angle_text = ax.text(-2.8, 1.6, "", fontsize=10)

def calcular_angulo(v1, v2):
    """Devuelve el ángulo entre v1 y v2 en grados."""
    n1 = np.linalg.norm(v1)
    n2 = np.linalg.norm(v2)
    if n1 == 0 or n2 == 0:
        return None
    cos_theta = np.dot(v1, v2) / (n1 * n2)
    cos_theta = np.clip(cos_theta, -1.0, 1.0)   # Evitar errores numéricos
    return np.degrees(np.arccos(cos_theta))

# Sliders: origen (ox, oy) y componentes (vx, vy)
ax_ox = plt.axes([0.1, 0.22, 0.8, 0.03])
ax_oy = plt.axes([0.1, 0.18, 0.8, 0.03])
ax_vx = plt.axes([0.1, 0.14, 0.8, 0.03])
ax_vy = plt.axes([0.1, 0.10, 0.8, 0.03])

slider_ox = Slider(ax_ox, 'ox', -2, 2, valinit=ox0)
slider_oy = Slider(ax_oy, 'oy', -2, 2, valinit=oy0)
slider_vx = Slider(ax_vx, 'vx', -2, 2, valinit=vx0)
slider_vy = Slider(ax_vy, 'vy', -2, 2, valinit=vy0)

def update(val):
    ox = slider_ox.val
    oy = slider_oy.val
    vx = slider_vx.val
    vy = slider_vy.val

    # Actualizar origen y componentes del vector variable
    var_arrow.set_offsets([[ox, oy]])
    var_arrow.set_UVC(vx, vy)

    # Calcular ángulo entre el vector vertical y el vector variable
    v_var = np.array([vx, vy])
    ang = calcular_angulo(v_vert, v_var)

    if ang is None:
        angle_text.set_text("Ángulo: indefinido (vector nulo)")
    else:
        angle_text.set_text(f"Ángulo entre vertical y variable: {ang:.2f}°")

    fig.canvas.draw_idle()

# Conectar sliders con la función update
slider_ox.on_changed(update)
slider_oy.on_changed(update)
slider_vx.on_changed(update)
slider_vy.on_changed(update)

ax.set_title("Vector vertical fijo y vector variable (origen móvil)")
plt.xlabel("Eje X → derecha")
plt.ylabel("Eje Y → abajo")

# Primera actualización para que muestre ángulo inicial
update(None)

plt.show()
