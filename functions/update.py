import pandas as pd
from functions.check import save_current_action

def update(df):
    new_df = input("Please input the new CSV's folder location (path): ")

    try:
        new_df = pd.read_csv(new_df)
        new_df.set_index("id", inplace=True)

        new_df_copy = new_df.copy()

        column_names = df.columns.tolist()

        new_df = pd.merge(df, new_df, how='outer', on=column_names)
        new_df = new_df.combine_first(new_df_copy)
        df = new_df
        df.to_csv("database\\techpowerup_gpus.csv", index=False)
        print("The Data Base has been updated")
    except:
        print("The folder doesn't exist, please verify it, verify the Data Base's name or the back-slashes")

    save_current_action("[UPDATE] The working database has been updated")