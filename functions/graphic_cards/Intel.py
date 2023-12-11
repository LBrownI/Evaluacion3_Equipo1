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
            "Alchemist": ["Arc 3","Arc 5","Arc 7","Pro-Series"],
            "Extreme Graphics": ["Extreme Graphics (IGP)","Extreme Graphics 2"],
            "GMA Graphics": ["GMA 3000 IGP","GMA 3100 IGP","GMA 3500 IGP","GMA 4500 IGP","GMA 950 IGP"],
            "GMA Graphics-M":["GMA 3000 IGP","GMA 3100 IGP","GMA 3600 IGP","GMA 4500M IGP","GMA 4700M IGP","GMA 900 IGP","GMA 950 IGP"],
            "GMA Graphics-T":["GMA 500 IGP","GMA 600 IGP","GMA IGP"],
            "Graphics ": ["Graphics","Graphics (IGP)","Graphics-M"],
            "H3C Graphics": [],
            "HD Graphics": ["Alder Lake","Broadwell","Coffee Lake","Comet Lake","Haswell","Ivy Bridge","Kaby Lake","Rocket Lake","Sandy Bridge","Skylake","Westmere"],
            "HD Graphics-M": ["Alder Lake","Broadwell","Coffee Lake","Comet Lake","Haswell","Ice Lake","Ivy Bridge","Jasper Lake","Kaby Lake Refresh","Kaby Lake","Lakefield","Sandy Bridge","Tiger Lake","Westmere","Whiskey Lake"],
            "HD Graphics-T": ["Airmont","Amber Lake","Bay Trail","Goldmont Plus","Goldmont"], #issue: specific case here
            "HD Graphics-W": ["Broadwell","Coffee Lake","Comet Lake","Haswell","Ivy Bridge","Rocket Lake","Sandy Bridge","Skylake"],
            "HD Graphics-MW": [],
            "Knights Corner": [],
            "Knights Ferry": [],
            "Xe Graphics": [],
            }

    def series(self):
        intel_series = list(self.series_and_gen.keys())
        print("\n-----> INTEL SERIES SELECT MENU <-----\n")
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
            print("\n-----> INTEL GEN SELECT MENU <-----\n")
            for i, gen in enumerate(intel_gen):
                print(f"  [{i+1}] {gen}")
            selected_gen = int(input("\nSelected gen: "))-1
            if intel_gen[selected_gen] == "Goldmont":
                self.df_with_filters = self.df[self.df["graphics_card_generation"] == "Goldmont"]   
            if intel_gen[selected_gen] == "Graphics":
                self.df_with_filters = self.df[self.df["graphics_card_generation"] == "Graphics"]    
            else:
                self.df_with_filters = self.df[self.df.graphics_card_generation.str.contains(self.series_and_gen.get(self.selected_series)[selected_gen])]
    
    def get_filtered_df(self):
        return self.df_with_filters

if __name__ == "__main__":
    a = Intel(df)
    a.series()
    a.gen()