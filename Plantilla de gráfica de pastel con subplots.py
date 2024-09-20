import matplotlib.pyplot as plt

def autopct_format(percent):
    return r'${{{:.1f}\%}}$'.format(percent)

pietext=0
uselabeling=False
if uselabeling==False:
    pietext=""
elif uselabeling==True:
    pietext=autopct_format
plt.rcParams['text.usetex'] = True
# Configuración de datos
labels = ['$Option\;1(30\%)$', '$Option\;2(80\%)$', 
          '$Option\;3(15\%)$', '$Option\;4(5\%)$']
sizes = [30, 80, 15, 5]
explode = (0.05, 0.05, 0.05, 0.05)
colors = ['saddlebrown', 'rosybrown', 'pink', 'olivedrab']

labels2 = ['$Option\;1(27\%)$', '$Option\;2(13\%)$', 
           '$Option\;3(34\%)$', '$Option\;4(26\%)$']
sizes2 = [27, 13, 34, 26]
explode2 = (0.05, 0.05, 0.05, 0.05)
colors2 = ['olivedrab', 'rosybrown', 'pink', 'saddlebrown']



# Crear la figura y ejes
fig, axs = plt.subplots(2,2, dpi=300)
fig.patch.set_facecolor('gray')
plt.subplots_adjust(wspace=1.5, hspace=0.5)
# Primera gráfica de pastel
axs[0,0].set_title("$Pie\;1$", color="black")
wedges, texts, autotexts = axs[0,0].pie(
    sizes, explode=explode, labels=None, autopct=pietext, startangle=90,
    colors=colors, wedgeprops=dict(edgecolor='k', linewidth=0.5))

for autotext in autotexts:
    autotext.set_color('black')

legend = axs[0,0].legend(wedges, labels, title="$Options$", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
legend.get_frame().set_facecolor('lightgray')
legend.get_frame().set_edgecolor('black')
for text in legend.get_texts():
    text.set_color("black")

# Segunda gráfica de pastel
axs[0,1].set_title("$Pie\;2$", color="black")
wedges, texts, autotexts = axs[0,1].pie(
    sizes2, explode=explode2, labels=None, autopct=pietext, startangle=90,
    colors=colors2, wedgeprops=dict(edgecolor='k', linewidth=0.5))

for autotext in autotexts:
    autotext.set_color('black')

legend = axs[0,1].legend(wedges, labels2, title="$Options$", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
legend.get_frame().set_facecolor('lightgray')
legend.get_frame().set_edgecolor('black')
for text in legend.get_texts():
    text.set_color("black")

# Primera gráfica de pastel
axs[1,0].set_title("$Pie\;3$", color="black")
wedges, texts, autotexts = axs[1,0].pie(
    sizes, explode=explode, labels=None, autopct=pietext, startangle=90,
    colors=colors, wedgeprops=dict(edgecolor='k', linewidth=0.5))

for autotext in autotexts:
    autotext.set_color('black')

legend = axs[1,0].legend(wedges, labels, title="$Options$", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
legend.get_frame().set_facecolor('lightgray')
legend.get_frame().set_edgecolor('black')
for text in legend.get_texts():
    text.set_color("black")

# Segunda gráfica de pastel
axs[1,1].set_title("$Pie\;4$", color="black")
wedges, texts, autotexts = axs[1,1].pie(
    sizes2, explode=explode2, labels=None, autopct=pietext, startangle=90,
    colors=colors2, wedgeprops=dict(edgecolor='k', linewidth=0.5))

for autotext in autotexts:
    autotext.set_color('black')

legend = axs[1,1].legend(wedges, labels2, title="$Options$", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
legend.get_frame().set_facecolor('lightgray')
legend.get_frame().set_edgecolor('black')
for text in legend.get_texts():
    text.set_color("black")


# Mostrar las gráficas
plt.tight_layout()
plt.show()
