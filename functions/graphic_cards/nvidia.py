import pandas as pd

df = pd.read_csv("database\\techpowerup_gpus.csv")
df.set_index("id", inplace=True)

class Nvidia:
    def __init__(self, df):
        self.df = df
        
        self.df_with_filters = ""
        self.selected_series = ""
        
        # This doesn't include all of the generations of each series (and not all graphics cards series either)
        self.series_and_gen = {
            "Console GPU": ["Microsoft","Nintendo","Sony" ],
            "Geforce": ["GeForce 1","GeForce 2","GeForce 3","GeForce 4","GeForce 5","GeForce 6","GeForce 7","GeForce 8","GeForce 9","GeForce FX","GeForce MX","GeForce Go","GeForce PCX", "GeForce2","GeForce4"],
            "GRID": ["GRID"],
            "ION": ["ION"],
            "Mining GPUs": ["Mining GPUs"],
            "NV1": ["NV1"],
            "NVS": ["NVS","NVS Mobile"],
            "Quadro": ["Quadro","Quadro CX","Quadro FX","Quadro Mobile","Quadro NVS","Quadro Plex","Quadro VX","Quadro2","Quadro4"],
            "Riva": ["Riva"],
            "Tegra": ["Tegra"],
            "Tesla": ["Tesla"],
            }

    def series(self):
        nvidia_series = list(self.series_and_gen.keys())
        print("Select the series:")
        for i, series in enumerate(nvidia_series):
            print(f"  [{i+1}] {series}")

        selected_series = int(input("\nInput: "))-1
        self.selected_series = nvidia_series[selected_series]

    def gen(self):
        print(self.series_and_gen.get(self.selected_series))
        
        nvidia_gen = self.series_and_gen.get(self.selected_series)
        print("Select the generation:")
        for i, gen in enumerate(nvidia_gen):
            print(f"  [{i+1}] {gen}")

        selected_gen = int(input("\nInput: "))-1
        
        self.df_with_filters = self.df[self.df.graphics_card_generation.str.contains(self.series_and_gen.get(self.selected_series)[selected_gen])]
        print(self.df_with_filters)

# THIS IS ONLY TO TEST. DELETE LATER!!!1!
if __name__ == "__main__":
    a = Nvidia(df)
    a.series()
    a.gen()