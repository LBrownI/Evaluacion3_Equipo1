import pandas as pd
from functions import check, restock

df = pd.read_csv("database\\techpowerup_gpus.csv")
df.set_index("id", inplace=True)

OPTIONS = ("Distribute","Restock","Check","Download","Exit")

def menu():
    option = input(f"*Welcome to inventory System*\nPlease choose one option:\n{OPTIONS}\n").capitalize()
    while option not in OPTIONS:
        option = input(f"Please choose only one of these options:\n{OPTIONS}\n").capitalize()
    return option


option=menu()
print(option)

match option:
    case "Distribute":
        # call distribute
        print("placeholder")
    case "Restock":
        restock.restock(df)
    case "Check":
        check.print_logs()
    case "Download":
        print("placeholder")
        # call download
    case "Exit":
        print("Saving files... (not realy xd)")
        exit(0)


# This is an example for the filter function
def filter():
    gpu_name = df.loc[df['graphics_processor.gpu_name'] == "Auburn"]
    print(gpu_name)
