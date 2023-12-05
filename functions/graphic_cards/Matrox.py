import pandas as pd

df = pd.read_csv("database\\techpowerup_gpus.csv")
df.set_index("id", inplace=True)

class Matrox:
    def __init__(self, df):
        self.df = df
        
        self.df_with_filters = ""
        self.selected_series = ""
        
        # This doesn't include all of the generations of each series (and not all graphics cards series either)
        self.series_and_gen = {
            "G Series": ["G1xx","G2xx","G3xx","G4xx","G5xx"],
            "Mxxx": [],
            "Parhelia": [],
            "QID": [],
            }

    def series(self):
        matrox_series = list(self.series_and_gen.keys())
        print("Select the series:")
        for i, series in enumerate(matrox_series):
            print(f"  [{i+1}] {series}")

        selected_series = int(input("\nInput: "))-1
        self.selected_series = matrox_series[selected_series]
        
        self.df_with_filters = self.df[self.df.graphics_card_generation.str.contains(matrox_series[selected_series])]

    def gen(self):
        matrox_gen = self.series_and_gen.get(self.selected_series)
        
        if matrox_gen == []:
            self.df_with_filters = self.df[self.df.graphics_card_generation.str.contains(self.selected_series)]
        else:
            print("\nSelect the generation:")
            for i, gen in enumerate(matrox_gen):
                print(f"  [{i+1}] {gen}")
            selected_gen = int(input("\nInput: "))-1

            self.df_with_filters = self.df[self.df.graphics_card_generation.str.contains(self.series_and_gen.get(self.selected_series)[selected_gen])]

    def get_filtered_df(self):
        return self.df_with_filters

if __name__ == "__main__":
    a = Matrox(df)
    a.series()
    a.gen()