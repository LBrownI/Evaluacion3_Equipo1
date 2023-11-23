from datetime import datetime

# This is an example for the check function using the datatime library
now = datetime.now()
time = now.strftime("%d/%m/%Y %H:%M:%S")

def check(action: str):
    with open("logs.txt", "a") as f:
        f.write(f"{time}: {action}")
        
def restock():
    # ...
    check("Product 'id of the product''name of the product' has been restocked \n")

restock()