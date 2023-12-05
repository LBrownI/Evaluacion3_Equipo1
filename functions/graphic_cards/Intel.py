import pandas as pd

df = pd.read_csv("database\\techpowerup_gpus.csv")
df.set_index("id", inplace=True)

class Intel:
    def __init__(self, df):
        self.df = df
        
        self.df_with_filters = ""
        self.selected_series = ""
        
        # This doesn't include all of the generations of each series (and not all graphics cards series either)
        self.series_and_gen = {
            "Alchemist": [],
            "Extreme Graphics": [],
            "GMA Graphics": [],
            #many issues here
            "Graphics ": [],
            "H3C Graphics": [],
            "HD Graphics": [],
            "Knights Corner": [],
            "Knights Ferry": [],
            "Xe Graphics": [],
            }

    def series(self):
        intel_series = list(self.series_and_gen.keys())
        print("-----> INTEL SERIES SELECT MENU <-----\n")
        for i, series in enumerate(intel_series):
            print(f"  [{i+1}] {series}")

        selected_series = int(input("\nSelected series: "))-1
        self.selected_series = intel_series[selected_series]
        
        self.df_with_filters = self.df[self.df.graphics_card_generation.str.contains(intel_series[selected_series])]

    def gen(self):
        intel_gen = self.series_and_gen.get(self.selected_series)
        
        if intel_gen == []:
            self.df_with_filters = self.df[self.df.graphics_card_generation.str.contains(self.selected_series)]
        else:
            print("-----> INTEL GEN SELECT MENU <-----\n")
            for i, gen in enumerate(intel_gen):
                print(f"  [{i+1}] {gen}")
            selected_gen = int(input("\nSelected gen: "))-1

            self.df_with_filters = self.df[self.df.graphics_card_generation.str.contains(self.series_and_gen.get(self.selected_series)[selected_gen])]
    
    
    def get_filtered_df(self):
        return self.df_with_filters

if __name__ == "__main__":
    a = Intel(df)
    a.series()
    a.gen()