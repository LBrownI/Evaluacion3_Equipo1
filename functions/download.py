def download(df):
    file_name = input("\nEnter the file name (including extension) for the download: ")
    
    try:
        #Saves the DataFrame to a CSV file
        df.to_csv(file_name, index=False)
        print(f"CSV file '{file_name}' downloaded successfully.")
    except Exception as e:
        print(f"Error: {e}")

