import pandas as pd
import os
import glob

os.chdir("D:/data/saved")
for file in glob.glob("*.csv"):
    print(file)
    df = pd.read_csv(file, sep=",", header=0, index_col=False)
    df = df.sort_values("date", ascending=True)
    df.to_csv(file)
