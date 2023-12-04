import pandas as pd

df = pd.read_csv("database\\techpowerup_gpus.csv")
df.set_index("id", inplace=True)

class Ati:
    def __init__(self, df):
        self.df = df
        
        self.df_with_filters = ""
        self.selected_series = ""
        
        # This doesn't include all of the generations of each series (and not all graphics cards series either)
        self.series_and_gen = {
            "All-In-Wonder": [],
            #ISSUE WITH CONSOLE GPUS ACROSS ALL CLASSES, if we tackle the issue would solve other issues with all clases aswell or maybe im dumb and its not realted at all to the others and this is already solved,,,
            "Console GPU": ["Microsoft","Nintendo"],
            "EGA": [],
            "Embedded": [],
            "Evergreen": [],
            "Fire": ["Fire GL","FireGL","FireMV Multi-View","FirePro Mobility","FirePro Multi-View","FirePro RG","FirePro"],
            "M": ["M1x","M2x","M5x","M6","M6x","M7","M7x","M8x","M9","M9x"],
            "Mach": ["Mach 32","Mach 64","Mach 8"],
            "Manhattan": [],
            "MDA/CGA": [],
            "Mobility FireGL": [],
            "Radeon": ["Radeon IGP","Radeon R100","Radeon R200","Radeon R300","Radeon R400 AGP","Radeon R400 PCIe","Radeon R500 AGP","Radeon R500 PCIe","Radeon R600","Radeon R700"],
            "Rage": ["Rage","Rage 2","Rage 3","Rage 4","Rage 6","Rage GL","Rage Mobility"],
            "VGA": [],
            }

    def series(self):
        ati_series = list(self.series_and_gen.keys())
        print("Select the series:")
        for i, series in enumerate(ati_series):
            print(f"  [{i+1}] {series}")

        selected_series = int(input("\nInput: "))-1
        self.selected_series = ati_series[selected_series]

    def gen(self):
        ati_gen = self.series_and_gen.get(self.selected_series)
        
        if ati_gen == []:
            self.df_with_filters = self.df[self.df.graphics_card_generation.str.contains(self.selected_series)]
            print(self.df_with_filters)
        else:
            print("\nSelect the generation:")
            for i, gen in enumerate(ati_gen):
                print(f"  [{i+1}] {gen}")
            selected_gen = int(input("\nInput: "))-1

            self.df_with_filters = self.df[self.df.graphics_card_generation.str.contains(self.series_and_gen.get(self.selected_series)[selected_gen])]
            print(self.df_with_filters)

a = Ati(df)
a.series()
a.gen()