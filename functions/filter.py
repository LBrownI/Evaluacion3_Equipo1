import pandas as pd
from functions.graphic_cards import Nvidia

df = pd.read_csv('database\\techpowerup_gpus.csv')
df.set_index("id", inplace=True)



def br():
    brands = ["Nvidia", "Amd", "Intel", "Matrox", "Ati"]
    brand = input(f"What brand are you looking for? Please select one of these brands: \n {brands}\n").capitalize()
    while brand not in brands:
        brand = input(f"Please just select one of these brands: \n{brands}\n").capitalize()
    return brand


def filters():
    global selected_filters
    selected_filters = {"series": False,
            "gen": False,
            "ram": False}
    
    response = input(f"Do you want to filter by {"series"}? (yes/no): ").lower()
    if response == 'yes':
        selected_filters["series"] = True
    if selected_filters.get("series"):
        response = input(f"Do you want to filter by {"gen"}? (yes/no): ").lower()
        if response == 'yes':
            selected_filters["gen"] = True
    response = input(f"Do you want to filter by {"ram"}? (yes/no): ").lower()
    if response == 'yes':
        selected_filters["ram"] = True

def ram(df):
    answer = input("Please put the GPU's RAM size(s) (comma-separated, Example: 4 GB, 8 GB): \n")
    ram_sizes_to_search = [ram.strip().lower() for ram in answer.split(',')]

    lines_ram = df[df["memory_memory_size"].str.lower().isin(ram_sizes_to_search)]

    if lines_ram.empty:
        print(f"GPUs with the specified RAM sizes weren't found.")
    else:
        print(f"The GPUs in stock with the specified RAM sizes are these: \n", lines_ram)

    return lines_ram

def download(df):
    file_name = input("\nEnter the file name (including extension) for the download: ")

    try:
        df.to_csv(file_name, index=False)
        print(f"CSV file '{file_name}' downloaded successfully.")
    except Exception as e:
        print(f"Error: {e}")


brand = br()
filters()
print(selected_filters)

if selected_filters.get("series"):
    if brand == "Nvidia":
        a = Nvidia(df)
        a.series()
        if selected_filters.get("gen"):
            a.gen()
        filtered_df = a.get_filtered_df()
        if selected_filters.get("ram"):
            filtered_df = ram(filtered_df)

download(filtered_df)