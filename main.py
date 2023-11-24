from datetime import datetime
import pandas as pd

df = pd.read_csv("database\\techpowerup_gpus.csv")


# This is an example for the check function using the datatime library
def check(action: str):
    now = datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M:%S")
    
    with open("logs\\logs.txt", "a") as f:
        f.write(f"{time}: {action}\n")
        
# This is an example for the filter function
def filter():
    gpu_name = df.loc[df['graphics_processor.gpu_name'] == "Auburn"]
    print(gpu_name)

def restock():
    # ...
    # At the end of the function, it will call to the check function to save the executed action in the logs.txt file
    check("Product 'id of the product''name of the product' has been restocked")

filter()