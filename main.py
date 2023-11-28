import pandas as pd
from functions import check, restock, distribute, download, Filter

df = pd.read_csv("database\\techpowerup_gpus.csv")
df.set_index("id", inplace=True)

OPTIONS = ("Distribute","Restock","Check","Download","Filter","Exit")

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
        case "Download":
            download.download(df)
            # call download
        case "Filter":
            Filter.filters(df)
        case "Exit":
            print("Saving files... (not really xd)")
            exit(0)
        


# This is an example for the filter function
def filter():
    gpu_name = df.loc[df['graphics_processor.gpu_name'] == "Auburn"]
    print(gpu_name)
