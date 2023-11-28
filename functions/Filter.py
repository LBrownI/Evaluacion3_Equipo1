
def filters(df):
    brands = ["Nvidia", "Amd", "Intel", "Matrox", "Ati"]
    brand = input(f"what brand are you looking for?, please only select one of these brands: \n {brands}\n")
    brand = brand.capitalize()
    while brand not in brands:
        brand = input(f"Please just select one of these brands: \n{brands}\n")
        brand = brand.capitalize()

    match brand:
        case "Nvidia":
            brand= brand.upper()
            filas_nvidia = df.loc[df["gpu_name"].str.startswith(brand)]
            print(f"Las tarjetas marca {brand} disponibles son las siguientes: \n", filas_nvidia)
        case "Amd":
            brand=brand.upper()
            filas_amd = df.loc[df["gpu_name"].str.startswith(brand)]
            print(f"Las tarjetas marca {brand} disponibles son las siguientes: \n", filas_amd)
        case "Intel":
            filas_intel = df.loc[df["gpu_name"].str.startswith(brand)]
            print(f"Las tarjetas marca {brand} disponibles son las siguientes: \n", filas_intel)
        case "Matrox":
            filas_matrox = df.loc[df["gpu_name"].str.startswith(brand)]
            print(f"Las tarjetas marca {brand} disponibles son las siguientes: \n", filas_matrox)
        case "Ati":
            brand=brand.upper()
            filas_ati = df.loc[df["gpu_name"].str.startswith(brand)]
            print(f"Las tarjetas marca {brand} disponibles son las siguientes: \n", filas_ati)