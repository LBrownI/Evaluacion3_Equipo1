import pandas as pd
from functions import check, restock, distribute, filter, graphic, update
import os

df = pd.read_csv("database\\techpowerup_gpus.csv")
df.set_index("id", inplace=True)

OPTIONS = ("Restock","Distribute","Check","Graphic","Download","Update","Exit")

def menu():
    option = input(f"\n -----> MAIN MENU <-----\nPlease choose one action:\n{OPTIONS}\n").capitalize()
    while option not in OPTIONS:
        option = input(f"\nPlease choose only one of the following options:\n{OPTIONS}\n").capitalize()
    return option

while True:
    option=menu()
    print(f"You chose: {option}\n")

    match option:
        case "Graphic":
            graphic.brand_pie_chart()
        case "Distribute":
            distribute.distribute(df)
        case "Restock":
            restock.restock(df)
        case "Check":
            check.print_logs()
        case "Download":
            filter.applied_filters(df)
        case "Update":
            df = update.update(df)
        case "Exit":
            exit(0)
        

