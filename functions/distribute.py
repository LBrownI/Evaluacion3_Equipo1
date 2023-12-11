from functions.check import save_current_action

def distribute(df):
    id = int(input("Enter the id of the product you want to distribute: "))

    product = df.filter(items=[id], axis=0)
    gpu_name = product.iloc[0]["gpu_name"]
    current_stock = product.iloc[0]["stock"]

    print(f"The product (id: {id}) {gpu_name} currently has {current_stock} units available.")

    distribution_location = input("Enter the location where the product will be distributed: ")
    distribution_amount = int(input("Enter the amount of units to distribute to the location: "))

    if distribution_amount > current_stock:
        print("ERROR: Distribution amount exceeds current stock.")
        return

    df.at[id, 'stock'] = current_stock - distribution_amount
    print(f"{distribution_amount} units of {gpu_name} distributed to {distribution_location} successfully.")

    save_current_action(f"[DISTRIBUTE] The product (id: {id}) {gpu_name} has been distributed. {distribution_amount} units were sent to {distribution_location}. Remaining stock: {current_stock - distribution_amount}")
    df.to_csv("database\\techpowerup_gpus.csv")


