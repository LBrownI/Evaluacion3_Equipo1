import pandas as pd
from functions import check

df = pd.read_csv("database\\techpowerup_gpus.csv")

options=["Distribute","Restock","Check","Download","Exit"]
def menu():
    option= input(f"*Welcome to inventory System*\nPlease choose one option:\n{options}\n")
    option=option.capitalize()
    while option not in options:
        option= input(f"Please choose only one of these options:\n{options}\n")
        option=option.capitalize()
    return option
option=menu()
print(option)

match option:
    case "Distribute":
        # call distribute
        print("placeholder")
    case "Restock":
        # call restrock
        print("placeholder")
    case "Check":
        # call check
        print("placeholder")
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

def restock():
    # ...
    # At the end of the function, it will call to the check function to save the executed action in the logs.txt file
    check.save_current_action("Product 'id of the product''name of the product' has been restocked")

filter()