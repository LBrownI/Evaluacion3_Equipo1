import pandas as pd

df = pd.read_csv('techpowerup_gpus2.csv')

def br(df):
    brands = ["Nvidia", "Amd", "Intel", "Matrox", "Ati"]
    brand = input(f"What brand are you looking for? Please select one of these brands: \n {brands}\n").capitalize()
    while brand not in brands:
        brand = input(f"Please just select one of these brands: \n{brands}\n").capitalize()
    return locate_brand(brand, df)

def locate_brand(brand, df):
    filas = df[df["gpu_name"].str.contains(brand, case=False)]
    
    if filas.empty:
        print(f"No GPUs matching brand '{brand}' were found.")
    else:
        print(f"The GPUs with brand '{brand}' in stock are these: \n", filas)
    
    return filas

def models(filas):
    model_input = input("Enter the models you are looking for (comma-separated): \n")
    models_to_search = [model.strip().lower() for model in model_input.split(',')]

    filas_model = filas[filas["gpu_name"].str.lower().isin(models_to_search)]

    if filas_model.empty:
        print(f"No GPUs matching the specified models were found.")
    else:
        print(f"The GPUs with the specified models in stock are these: \n", filas_model)

    return filas_model


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
    type_filter = ["brand", "model", "ram"]
    chosen_filters = []

    for filter_type in type_filter:
        response = input(f"Do you want to filter by {filter_type}? (yes/no): ").lower()
        if response == 'yes':
            chosen_filters.append(filter_type)

    filtered_df = df.copy()

    for chosen_filter in chosen_filters:
        if chosen_filter == 'brand':
            filtered_df = br(filtered_df)
        elif chosen_filter == 'model':
            filtered_df = models(filtered_df)
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
