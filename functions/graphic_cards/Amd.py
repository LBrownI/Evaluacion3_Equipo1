import pandas as pd

df = pd.read_csv("database\\techpowerup_gpus.csv")
df.set_index("id", inplace=True)

class Amd:
    def __init__(self, df):
        self.df = df
        self.df_with_filters = ""
        self.selected_series = ""
        
        # This doesn't include all of the generations of each series (and not all graphics cards series either)
        self.series_and_gen = {
            "All-In-One": ["HD 6000","HD 7000","HD 8000","Rx 200","Rx 300" ],
            "Arctic Islands": ["R5 400","R7 400","RX 400"],
            "Bristol Ridge (Rx 300)": [],
            "Carrizo (Rx 300 Mobile)": [],
            "Cezanne": ["Vega Mobile","Vega"], #issue: specific case here
            "Console GPU": ["Atari","Chuwi","Microsoft","Nintendo","Sony","Valve","Zhongshan Subor"],
            "Crystal System": ["R5 M200","R5 M300","R5 M400","R7 M200","R7 M300","R7 M400","R9 M200","R9 M300","R9 M400","Rx M200","Rx M300","Rx M400","Rx M500"],
            "Embedded": ["6000","8000","9000"],
            "Fire": ["FirePro","FirePro Mobile","FirePro Multi-View","FirePro Remote","FireStream"],
            "Great Horned Owl (Vega)": [],
            "Kabini": [],
            "Kaveri": [],
            "Lucienne": [],
            "Mining GPUs": [],
            "Mobility Radeon": ["M500","M500X","M600","Navi II","Navi","RX M400","RX M500","RX M500X","Vega"],
            "Mullins (Rx 200 Mobile)": [],
            "Navi": ["Navi (RX 5000)","Navi II","Navi III"],
            "Islands": ["Northern Islands","Pirate Islands","Sea Islands","Southern Islands","Volcanic Islands"],
            "Palm": [],
            "Picasso": [],
            "Polaris": [],
            "Radeon ": ["Radeon Instinct","Radeon Pro Mac","Radeon Pro Mobile","Radeon Pro","Radeon Sky"],
            "Raven Ridge": [],
            "Rembrandt": [],
            "Renoir": [],
            "Richland": [],
            "Solar System": [],
            "Stoney Ridge": [],
            "Sumo": [],
            "Temash": [],
            "Trinity": [],
            "Vancouver": [],
            "Vega": [],
            "Wrestler": [],
            }

    def series(self):
        amd_series = list(self.series_and_gen.keys())
        print("\n-----> AMD SERIES SELECT MENU <-----\n")
        for i, series in enumerate(amd_series):
            print(f"  [{i+1}] {series}")
        selected_series = int(input("\nSelected series: "))-1
        self.selected_series = amd_series[selected_series]
        self.df_with_filters = self.df[self.df.graphics_card_generation.str.contains(amd_series[selected_series])]

    def gen(self):        
        amd_gen = self.series_and_gen.get(self.selected_series)
        if amd_gen == []:
            self.df_with_filters = self.df[self.df.graphics_card_generation.str.contains(self.selected_series)]
        else:    
            print("\n-----> AMD GEN SELECT MENU <-----\n")
            for i, gen in enumerate(amd_gen):
                print(f"  [{i+1}] {gen}")
            selected_gen = int(input("\nSelected gen: "))-1 
            self.df_with_filters = self.df_with_filters[self.df_with_filters.graphics_card_generation.str.contains(self.series_and_gen.get(self.selected_series)[selected_gen])]
            
    def get_filtered_df(self):
        return self.df_with_filters

if __name__ == "__main__":
    b = Amd(df)
    b.series()
    b.gen()