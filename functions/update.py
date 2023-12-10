import pandas as pd
from functions.check import save_current_action

def update(df):
    answer = input("Do you want to update the Data Base (Yes/No)?: ").capitalize()

    OPTIONS = ("Yes", "No")
    while answer not in OPTIONS:
        answer= input("Please just input 'Yes' or 'No': ").capitalize()
    
    match answer:
        case "Yes":
            new_df= input("Please input the new CSV's folder: ")
            
            try:
                new_df= pd.read_csv(new_df)
                new_df.set_index("id", inplace=True)

                new_df_copy= new_df.copy()

                column_names = df.columns.tolist()

                new_df = pd.merge(df, new_df, how='outer', on=column_names)
                new_df = new_df.combine_first(new_df_copy)
                df= new_df
                print("The Data Base was updated")
                return df
            except:
                print("The folder doesn't exist, please verify it, verify the Data Base's name or the back-slashes")
            
        case "No":
            return df