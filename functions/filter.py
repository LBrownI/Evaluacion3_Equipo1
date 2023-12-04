import pandas as pd
from graphic_cards import nvidia

df = pd.read_csv('database\\techpowerup_gpus.csv')

global brand

def br(df):
    brands = ["Nvidia", "Amd", "Intel", "Matrox", "Ati"]
    brand = input(f"What brand are you looking for? Please select one of these brands: \n {brands}\n").capitalize()
    while brand not in brands:
        brand = input(f"Please just select one of these brands: \n{brands}\n").capitalize()
    return locate_brand(brand, df)

def locate_brand(brand, df):
    filas = df[df["gpu_name"].str.contains(f"{brand} ", case=False)]
    
    if filas.empty:
        print(f"No GPUs matching brand '{brand}' were found.")
    else:
        print(f"The GPUs with brand '{brand}' in stock are these: \n", filas)
    
    return filas

nvidia = nvidia(df)

def ram(df):
    answer = input("Please put the GPU's RAM size(s) (comma-separated, Example: 4 GB, 8 GB): \n")
    ram_sizes_to_search = [ram.strip().lower() for ram in answer.split(',')]

    lines_ram = df[df["memory.memory_size"].str.lower().isin(ram_sizes_to_search)]

    if lines_ram.empty:
        print(f"GPUs with the specified RAM sizes weren't found.")
    else:
        print(f"The GPUs in stock with the specified RAM sizes are these: \n", lines_ram)

    return lines_ram

def filters(df):
    type_filter = ["brand","series","gen", "ram"]
    chosen_filters = []

    for filter_type in type_filter:
        response = input(f"Do you want to filter by {filter_type}? (yes/no): ").lower()
        if response == 'yes':
            chosen_filters.append(filter_type)

    filtered_df = df.copy()

    for chosen_filter in chosen_filters:
        if chosen_filter == 'brand':
            filtered_df = br(filtered_df)
        elif chosen_filter == 'series':
        elif chosen_filter == 'ram':
            filtered_df = ram(filtered_df)

    download(filtered_df)


def download(df):
    file_name = input("\nEnter the file name (including extension) for the download: ")

    try:
        df.to_csv(file_name, index=False)
        print(f"CSV file '{file_name}' downloaded successfully.")
    except Exception as e:
        print(f"Error: {e}")

filtered_data = filters(df)
download(filtered_data)
