from functions.check import save_current_action
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patheffects import withStroke

df = pd.read_csv('database\\techpowerup_gpus.csv')
df.set_index("id", inplace=True)

def brand_pie_chart():
    brands = ["Nvidia", "Amd", "Intel", "Matrox", "Ati"]

    brand_stocks = [df[df["gpu_name"].str.contains(f"{brand} ", case=False)]["stock"].sum() for brand in brands]

    # Explotar gráfica
    explode = (0.1, 0.0, 0.2, 0.3, 0.0)
    
    # Colores
    colors = ("yellowgreen", "crimson", "turquoise", "mediumblue", "black")
    
    # Separación de piezas
    wp = {'linewidth': 1, 'edgecolor': "green"}
    
    # Creating autocpt arguments
    def func(pct, allvalues):
        absolute = int(pct / 100. * np.sum(allvalues))
        return "{:.1f}%\n({:d} units)".format(pct, absolute)

    # Creating plot
    fig, ax = plt.subplots(figsize=(10, 7))
    wedges, texts, autotexts = ax.pie(brand_stocks,
                                  autopct=lambda pct: func(pct, brand_stocks),
                                  explode=explode,
                                  labels=brands,
                                  shadow=True,
                                  colors=colors,
                                  startangle=90,
                                  wedgeprops=wp,
                                  textprops=dict(color="white", path_effects=[withStroke(linewidth=2.5, foreground='black')]))

    # Adding legend
    ax.legend(wedges, brands,
              title="Brands",
              loc="upper left",
              bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight="bold")
    ax.set_title("Stock Distribution by Brand")

    plt.show()

    save_current_action(f"[GRAPHIC] A graphical representation of the stock has been acquired")
