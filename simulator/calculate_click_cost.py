import pandas as pd
import os
import glob
import json


with open('sim_conf') as json_file:
    data = json.load(json_file)
    cost = data["cost"]

list_of_costs = json.loads('{}')
os.chdir("D:/data/saved2")
for file in glob.glob("*.csv"):
    if file != "E3DDEB04F8AFF944B11943BB57D2F620.csv":
        print(file)
        df = pd.read_csv(file, sep=",", header=0, index_col=False)
        sales = df[df["Sale"] != 0].sum()["SalesAmountInEuro"]
        clicks = len(df)
        list_of_costs.update({file: ((cost/100)*sales)/clicks})

with open('costs.json', 'w') as out:
    json.dump(list_of_costs, out)
