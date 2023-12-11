from functions.check import save_current_action
import pandas as pd
from functions.graphic_cards import Nvidia, Amd, Intel, Ati, Matrox

df = pd.read_csv('database\\techpowerup_gpus.csv')
df.set_index("id", inplace=True)



def br():
    global brand
    brands = ["Nvidia", "Amd", "Intel", "Matrox", "Ati", "None"]
    brand = input(f"Select one of these brands or type 'None' for FULL database download: \n {brands}\nSelected: ").capitalize()
    while brand not in brands:
        brand = input(f"Please just select one of these brands: \n{brands}\n").capitalize()
    return brand

def locate_brand(brand, df):
    if brand == "None":
        rows = df
    else:
        rows = df[df["gpu_name"].str.match(brand, case=False)]
        
        if rows.empty:
            print(f"No GPUs matching brand '{brand}' were found.")

    return rows

def filters():
    global selected_filters
    selected_filters = {"series": False,
            "gen": False,
            "ram": False}
    if brand == "None":
        selected_filters = selected_filters
    else:
        series_reply = input(f"\nDo you want to filter by {"series"}? (yes/no): ").lower()
        if series_reply == 'yes':
            selected_filters["series"] = True
        if selected_filters.get("series"):
            gen_reply = input(f"Do you want to filter by {"gen"}? (yes/no): ").lower()
            if gen_reply == 'yes':
                selected_filters["gen"] = True
            ram_reply = input(f"Do you want to filter by {"ram"}? (yes/no): ").lower()
            if ram_reply == 'yes':
                selected_filters["ram"] = True

def ram(df):
    answer = input("Please put the GPU's RAM size(s) (comma-separated, Example: 4 GB, 8 GB): \n")
    ram_sizes_to_search = [ram.strip().lower() for ram in answer.split(',')]

    lines_ram = df[df["memory_memory_size"].str.lower().isin(ram_sizes_to_search)]

    if lines_ram.empty:
        print(f"GPUs with the specified RAM sizes weren't found.")
        lines_ram = df
    return lines_ram

def csv_to_excel(df):
    try:
        excel_file = input("\nEnter the  file name for the download: ")
        sheet_name = input("\nEnter the sheet name for the Excel file (press Enter for default 'Sheet1'): ")
        if not sheet_name:
            sheet_name = 'Sheet1'
        df.to_excel(f"{excel_file}.xlsx", index=False, sheet_name=sheet_name)
        print(f"Excel file '{excel_file}.xlsx' downloaded successfully.")
        save_current_action(f"[DOWNLOAD] An Excel with the name '{excel_file}.xlsx' has been downloaded with the following criteria active: brand = {brand}, {selected_filters}")
    except Exception as e:
        print(f"Error: {e}")
    
def download(df):
    download_option = input("\nDownload as Excel or CSV?\n").upper()
    while (download_option!="EXCEL")and(download_option!="CSV"):
        download_option = input("Please just select 'Excel' or 'CSV': \n").upper()
    if download_option == "CSV":
        file_name = input("\nEnter the CSV file name for the download: ")
        try:
            df.to_csv(f"{file_name}.csv", index=False)
            print(f"CSV file '{file_name}.csv' downloaded successfully.")
            save_current_action(f"[DOWNLOAD] An Excel with the name '{file_name}.csv' has been downloaded with the following criteria active: brand = {brand}, {selected_filters}")
        except Exception as e:
            print(f"Error: {e}")
    elif download_option == "EXCEL":
        csv_to_excel(df)

def applied_filters():
    brand = br()
    filters()
    filtered_df = locate_brand(brand, df)
   
    if selected_filters.get("series"):
        if brand == "Nvidia":
            a = Nvidia(df)
            a.series()
            if selected_filters.get("gen"):
                a.gen()
            filtered_df = a.get_filtered_df()
            if selected_filters.get("ram"):
                filtered_df = ram(filtered_df)           

        if brand == "Amd":
            a = Amd(df)
            a.series()
            if selected_filters.get("gen"):
                a.gen()
            filtered_df = a.get_filtered_df()
            if selected_filters.get("ram"):
                filtered_df = ram(filtered_df)

        if brand == "Matrox":
            a = Matrox(df)
            a.series()
            if selected_filters.get("gen"):
                a.gen()
            filtered_df = a.get_filtered_df()
            if selected_filters.get("ram"):
                filtered_df = ram(filtered_df)
        
        if brand == "Intel":
            a = Intel(df)
            a.series()
            if selected_filters.get("gen"):
                a.gen()
            filtered_df = a.get_filtered_df()
            if selected_filters.get("ram"):
                filtered_df = ram(filtered_df)
        
        if brand == "Ati":
            a = Ati(df)
            a.series()
            if selected_filters.get("gen"):
                a.gen()
            filtered_df = a.get_filtered_df()
            if selected_filters.get("ram"):
                filtered_df = ram(filtered_df)
                
        if brand == "None":
            filtered_df = df
    download(filtered_df)