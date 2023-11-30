import pandas as pd
from functions import check, restock, distribute, filter

df = pd.read_csv("database\\techpowerup_gpus.csv")
df.set_index("id", inplace=True)

OPTIONS = ("Distribute","Restock","Check", "Filter","Exit")

def menu():
    option = input(f"\n*Welcome to inventory System*\nPlease choose one option:\n{OPTIONS}\n").capitalize()
    while option not in OPTIONS:
        option = input(f"\nPlease choose only one of the following options:\n{OPTIONS}\n").capitalize()
    return option

while True:
    option=menu()
    print("You chose:",option)

    match option:
        case "Distribute":
            distribute.distribute(df)
        case "Restock":
            restock.restock(df)
        case "Check":
            check.print_logs()
        case "Filter":
            filter.filters(df)
        case "Exit":
            print("Saving files... (not really xd)")
            exit(0)
        

