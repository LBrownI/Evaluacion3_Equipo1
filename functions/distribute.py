from functions.check import save_current_action

def distribute(df):
    id = int(input("\nEnter the id of the product you want to distribute: "))

    product = df.filter(items=[id], axis=0)
    gpu_name = product.iloc[0]["gpu_name"]
    current_stock = product.iloc[0]["stock"]

    print(f"The product (id: {id}) {gpu_name} currently has {current_stock} units available.")

    distribution_amount = int(input("How much do you want to distribute to other stores: "))

    if distribution_amount > current_stock:
        print("Error: Distribution amount exceeds current stock.")
        return

    # Deduct stock for distribution
    df.at[id, 'stock'] = current_stock - distribution_amount
    print(f"{distribution_amount} units of {gpu_name} distributed to other stores successfully.")

    save_current_action(f"The product (id: {id}) {gpu_name} has been distributed. {distribution_amount} units were sent to other stores. Remaining stock: {current_stock - distribution_amount}")
    df.to_csv("database\\techpowerup_gpus.csv")

