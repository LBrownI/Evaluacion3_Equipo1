from functions.check import save_current_action

def restock(df):
    id = int(input("Enter the id of the product you want to restock: "))

    product = df.filter(items= [id], axis = 0)
    gpu_name = product.iloc[0]["gpu_name"]
    current_stock = product.iloc[0]["stock"]
    print(f"The product (id: {id}) {gpu_name} currently has {current_stock} units available.")
    
    origin_location = input("Enter the location where the product came from: ")
    new_stock = int(input("Enter the amount of units to restock: "))

    df.at[id, 'stock'] = current_stock + new_stock
    print("Product stock updated succesfully")
    
    save_current_action(f"[RESTOCK] The product (id: {id}) {gpu_name} has been restocked. {new_stock} new units were received from {origin_location}. Now it has {current_stock+new_stock} units")
    df.to_csv("database\\techpowerup_gpus.csv")