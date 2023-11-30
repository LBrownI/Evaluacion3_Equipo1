def br(df):
    brands = ["Nvidia", "Amd", "Intel", "Matrox", "Ati"]
    brand = input(f"what brand are you looking for?, please only select one of these brands: \n {brands}\n").capitalize()
    while brand not in brands:
        brand = input(f"Please just select one of these brands: \n{brands}\n").capitalize()
    match brand:
        case "Nvidia":
            brand = brand.upper()
            filas_nvidia = df.loc[df["gpu_name"].str.startswith(brand)]
            print(f"The GPUs {brand} on stock are these: \n", filas_nvidia)
        case "Amd":
            brand = brand.upper()
            filas_amd = df.loc[df["gpu_name"].str.startswith(brand)]
            print(f"The GPUs {brand} on stock are these: \n", filas_amd)
        case "Intel":
            filas_intel = df.loc[df["gpu_name"].str.startswith(brand)]
            print(f"The GPUs {brand} on stock are these: \n", filas_intel)
        case "Matrox":
            filas_matrox = df.loc[df["gpu_name"].str.startswith(brand)]
            print(f"The GPUs {brand} on stock are these: \n", filas_matrox)
        case "Ati":
            brand = brand.upper()
            filas_ati = df.loc[df["gpu_name"].str.startswith(brand)]
            print(f"The GPUs {brand} on stock are these: \n", filas_ati)

def ram(df):
    answer= input("Please put the Gpu's ram size: \n")
    lines_ram= df.loc[df["memory.memory_size"]==answer]
    print(f"The GPUs on stock with {answer} ram are these: \n", lines_ram)
def filters(df):
    type_filter=["brand","ram"]
    t_filter= input(f"Please select one of these filters: \n {type_filter}\n")
    t_filter=t_filter.lower()
    while t_filter not in type_filter:
        t_filter= input(f"Please just choose one of these options: \n {type_filter}\n")
        t_filter=t_filter.lower()
    if t_filter==type_filter[0]:
        br(df)
    else:
        ram(df)

def download(df):
    file_name = input("\nEnter the file name (including extension) for the download: ")
    
    try:
        #Saves the DataFrame to a CSV file
        df.to_csv(file_name, index=False)
        print(f"CSV file '{file_name}' downloaded successfully.")
    except Exception as e:
        print(f"Error: {e}")