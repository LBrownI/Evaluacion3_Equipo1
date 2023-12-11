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
            "All-In-Wonder": ["128","2006 Edition","7000","8500","9000","HD","X","X1"], #issue: specific case here
            "Console GPU": ["Microsoft","Nintendo"],
            "EGA": [],
            "Embedded": ["2000","4000"],
            "Evergreen": ["HD 5400","HD 5500","HD 5600","HD 5700","HD 5800","HD 5900"],
            "Fire": ["Fire GL","FireGL","FireMV Multi-View","FirePro Mobility","FirePro Multi-View","FirePro RG","FirePro"], #issue: specific case here
            "M": ["M1x","M2x","M5x","M6","M6x","M7","M7x","M8x","M9","M9x"],
            "Mach": ["Mach 32","Mach 64","Mach 8"],
            "Manhattan": [],
            "MDA/CGA": [],
            "Mobility FireGL": [],
            "Radeon": ["Radeon IGP","Radeon R100","Radeon R200","Radeon R300","Radeon R400 AGP","Radeon R400 PCIe","Radeon R500 AGP","Radeon R500 PCIe","Radeon R600","Radeon R700"],
            "Rage": ["Rage","Rage 2","Rage 3","Rage 4","Rage 6","Rage GL","Rage Mobility"], #issue: specific case here
            "VGA": [],
            }

    def series(self):
        ati_series = list(self.series_and_gen.keys())
        print("\n-----> ATI SERIES SELECT MENU <-----\n")
        for i, series in enumerate(ati_series):
            print(f"  [{i+1}] {series}")
        selected_series = int(input("\nSelected series: "))-1
        self.selected_series = ati_series[selected_series]
        self.df_with_filters = self.df[self.df.graphics_card_generation.str.contains(ati_series[selected_series])]

    def gen(self):
        ati_gen = self.series_and_gen.get(self.selected_series)
        if ati_gen == []:
            self.df_with_filters = self.df[self.df.graphics_card_generation.str.contains(self.selected_series)]
        else:
            print("\n-----> ATI GEN SELECT MENU <-----\n")
            for i, gen in enumerate(ati_gen):
                print(f"  [{i+1}] {gen}")
            selected_gen = int(input("\nSelected gen: "))-1
            self.df_with_filters = self.df[self.df.graphics_card_generation.str.contains(self.series_and_gen.get(self.selected_series)[selected_gen])]

    def get_filtered_df(self):
        return self.df_with_filters

if __name__ == "__main__":
    a = Ati(df)
    a.series()
    a.gen()