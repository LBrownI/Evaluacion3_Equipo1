import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patheffects import withStroke

df = pd.read_csv('database\\techpowerup_gpus.csv')
df.set_index("id", inplace=True)

def create_brand_pie_chart():
    brands = ["Nvidia", "Amd", "Intel", "Matrox", "Ati"]

    brand_stocks = [df[df["gpu_name"].str.contains(f"{brand} ", case=False)]["stock"].sum() for brand in brands]

    # Creating explode data
    explode = (0.1, 0.0, 0.2, 0.3, 0.0)
    
    # Creating color parameters
    colors = ("yellowgreen", "crimson", "turquoise", "mediumblue", "black")
    
    # Wedge properties
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

    # Show plot
    plt.show()

# Call the create_brand_pie_chart function
create_brand_pie_chart()
