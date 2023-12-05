import pandas as pd
from functions import check, restock, distribute, filter, graphic, update

df = pd.read_csv("database\\techpowerup_gpus.csv")
df.set_index("id", inplace=True)

OPTIONS = ("Graphic","Distribute","Restock","Check", "Filter","Exit", "Update")

def menu():
    option = input(f"\n*Welcome to inventory System*\nPlease choose one option:\n{OPTIONS}\n").capitalize()
    while option not in OPTIONS:
        option = input(f"\nPlease choose only one of the following options:\n{OPTIONS}\n").capitalize()
    return option

while True:
    option=menu()
    print("You chose:",option)

    match option:
        case "Graphic":
            graphic.brand_pie_chart()
        case "Distribute":
            distribute.distribute(df)
        case "Restock":
            restock.restock(df)
        case "Check":
            check.print_logs()
        case "Filter":
            filter.asjdiojasdjoiasd()
        case "Update":
            df = update.update(df)
        case "Exit":
            print("Saving files... (not really xd)")
            exit(0)
        

