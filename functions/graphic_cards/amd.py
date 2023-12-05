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
            "All-In-One": ["(HD 6000)","All-In-One(HD 7000)","All-In-One(HD 8000)","All-In-One(Rx 200)","All-In-One(Rx 300)" ],
            "Arctic Islands": ["Arctic Islands(R5 400)","Arctic Islands(R7 400)","Arctic Islands(RX 400)"],
            "Bristol Ridge (Rx 300)": [],
            "Carrizo (Rx 300 Mobile)": [],
            "Cezanne": ["Cezanne(Vega Mobile)","Cezanne(Vega)"],
            "Console GPU": ["Atari","Chuwi","Microsoft","Nintendo","Sony","Valve","Zhongshan Subor"],
            "Embedded": [],
            "FirePro": [],
            "FireStream": [],
            "Great Horned Owl(Vega)": [],
            "Kabini": [],
            "Kaveri": [],
            "Lucienne": [],
            "Mining GPUs": [],
            "Mobility Radeon": [],
            "Mullins": [],
            "Navi": ["Navi(RX 5000)","Navi II","Navi III"],
            "Northern Islands": [],
            "Palm": [],
            "Picasso": [],
            "Pirate Islands": [],
            "Polaris": [],
            #Issue
            "Radeon": ["Radeon Instinct","Radeon Pro Mac","Radeon Pro Mobile","Radeon Pro","Radeon Sky"],
            "Raven Ridge": [],
            "Rembrandt": [],
            "Renoir": [],
            "Richland": [],
            "Sea Islands": [],
            "Solar System": [],
            "Southern Islands": [],
            "Stoney Ridge": [],
            "Sumo": [],
            "Temash": [],
            "Trinity": [],
            "Vancouver": [],
            "Vega": [],
            "Volcanic Islands": [],
            "Wrestler": [],
            }

    def series(self):
        amd_series = list(self.series_and_gen.keys())
        print("Select the series:")
        for i, series in enumerate(amd_series):
            print(f"  [{i+1}] {series}")

        selected_series = int(input("\nInput: "))-1
        self.selected_series = amd_series[selected_series]
        
        self.df_with_filters = self.df[self.df.graphics_card_generation.str.contains(amd_series[selected_series])]
        print(self.df_with_filters)


    def gen(self):        
        nvidia_gen = self.series_and_gen.get(self.selected_series)
        print("Select the generation:")
        for i, gen in enumerate(nvidia_gen):
            print(f"  [{i+1}] {gen}")

        selected_gen = int(input("\nInput: "))-1
        
        self.df_with_filters = self.df_with_filters[self.df_with_filters.graphics_card_generation.str.contains("Sumo")]
        print(self.df_with_filters)
            
            
    def get_filtered_df(self):
        return self.df_with_filters

if __name__ == "__main__":
    b = Amd(df)
    b.series()
    b.gen()

# asd
