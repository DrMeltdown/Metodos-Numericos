import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True
labels = '$Option\;1$', '$Option\;2$', '$Option\;3$', '$Option\;4$'
sizes = [27,13,34,26]
explode = (0.01, 0.1, 0.01, 0.01)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig, ax = plt.subplots(dpi=300)
fig.patch.set_facecolor('gray')
plt.title("$Truly\;interesting$",color="black")
def autopct_format(percent):
    return r'${{{:.1f}\%}}$'.format(percent)


wedges, texts, autotexts = ax.pie(
    sizes, explode=explode, labels=None, autopct=autopct_format, startangle=90,
    colors=['darkkhaki', 'plum', 'chocolate', 'blueviolet'],
    wedgeprops=dict(edgecolor='k', linewidth=0.5))
for autotext in autotexts:
    autotext.set_color('black')  # Change color to white

# Fix legend to display the correct labels
legend = ax.legend(wedges, labels,
          title="$Options$",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
legend.get_frame().set_facecolor('lightgray')
legend.get_frame().set_edgecolor('black')
for text in legend.get_texts():
    text.set_color("black")  # Cambia 'white' por el color que desees
plt.show()
ax.pie(sizes, labels=labels)

