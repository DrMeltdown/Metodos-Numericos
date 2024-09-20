import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
caja = dict(boxstyle='round', facecolor=(0, 0, 0.1), alpha=0.5, edgecolor=((1, 1, 1)))

plt.figure(dpi=350, figsize=(10, 6))
ax = plt.subplot(polar=True)
ax.spines['polar'].set_color((0.5, 0.5, 0.8))
ax.grid(color=(0.5, 0.5, 0.8), linestyle='-', linewidth=1)
ax.set_facecolor((0, 0, 0.2))
plt.gcf().set_facecolor((0, 0, 0.1))  # Cambia este color por el que prefieras

subjects = ["$One$","$Two$","$Three$","$Four$",
            "$Five$","$Six$","$Seven$","$Eight$",
            "$Nine$","$Ten$"]  # Ajusta según necesites

# Calificaciones (puedes agregar más valores aquí)
mid_grades = [1,1,1,1,1,1,1,1,1,1]

# Añadir el primer valor al final de las calificaciones para cerrar el ciclo
mid_grades.append(mid_grades[0])

# Ajustar los delimitadores para el ciclo cerrado
delimitadores = [max(mid_grades) * 1.2 for _ in range(len(mid_grades))]

# Ajustar theta para que tenga el mismo número de puntos que mid_grades
theta = np.linspace(0, 2 * np.pi, len(mid_grades))

# Establecer el grid de ángulos para los sujetos
lines, labels = plt.thetagrids(range(0, 360, int(360 / len(subjects))), (subjects))
plt.setp(labels, color=((1, 1, 1)))

# Aumentar la distancia de las etiquetas del borde de la circunferencia
ax.tick_params(colors=((1, 1, 1)), pad=20)  # Ajusta el valor de 'pad' para más o menos distancia

# Añadir las etiquetas de calificaciones en el gráfico
for i in range(len(mid_grades)):
    ax.text(theta[i], mid_grades[i] + (mid_grades[i]*.1), str(mid_grades[i]), 
            color=((1, 1, 1)), fontsize=10, ha='center', va='center', bbox=caja)

# Dibujar el gráfico
ax.plot(theta, mid_grades, color=(1, 1, 1), alpha=0.5)
ax.fill(theta, mid_grades, (0, 0, 0), alpha=0.7)
ax.plot(theta, delimitadores, alpha=0)

# Título del gráfico
plt.title("$Title$", fontsize=14, color=((1, 1, 1)))
plt.show()
