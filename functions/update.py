import pandas as pd
from functions.check import save_current_action

def update(df):
    new_df_location = input("Please input the new CSV's folder location (path): ")
    df = pd.read_csv("database\\techpowerup_gpus.csv")
    try:
        new_df = pd.read_csv(new_df_location)
        if df is None or 'id' not in df.columns or 'id' not in new_df.columns:
            raise ValueError("Both DataFrames must have the 'id' column.")
        df.set_index("id", inplace=True)
        new_df.set_index("id", inplace=True)
        df.update(new_df)
        df = pd.concat([df, new_df[~new_df.index.isin(df.index)]])
        df.reset_index(inplace=True)
        output_csv = input("Enter the output CSV file path (including file name and extension): ")
        df.to_csv(output_csv, index=False)
        print("The Database has been updated")
    except Exception as e:
        print(f"Error: {e}")

    save_current_action("[UPDATE] The working database has been updated")