import pandas as pd
import os
from datetime import datetime


def calc_date(row):
    return datetime.fromtimestamp(int(row["date"]))


headers = ["Sale", "SalesAmountInEuro", "time_delay_for_conversion", "date", "nb_clicks_1week",
           "product_price", "product_age_group", "device_type", "audience_id", "product_gender", "product_brand",
           "product_category_1", "product_category_2", "product_category_3", "product_category_4", "product_category_5",
           "product_category_6", "product_category_7", "product_country", "product_id", "product_title", "partner_id",
           "user_id"]
i = 0

for chunk in pd.read_csv("D:/data/Criteo_Conversion_Search/CriteoSearchData.csv", sep="\t",
                         header=None, chunksize=1000000):

    chunk.columns = headers
    # chunk['date'] = chunk.apply(lambda row: calc_date(row), axis=1)
    partner_id_list = chunk["partner_id"].unique()
    chunk_sorted = chunk.sort_values("date", ascending=True)
    # chunk_sorted["date"] = pd.to_datetime(chunk_sorted["date"], format='%Y%b%d:%H:%M:%S.%f').dt.date
    chunk_sorted["date"] = [datetime.utcfromtimestamp(x).date() for x in chunk_sorted['date']]
    grouped_chunk = chunk_sorted.groupby("partner_id")
    for e in partner_id_list:
        if not os.path.isfile("D:/data/saved2/"+e+".csv"):
            grouped_chunk.get_group(e).to_csv("D:/data/saved2/" + e + ".csv")
        else:
            grouped_chunk.get_group(e).to_csv("D:/data/saved2/" + e + ".csv", mode='a', header=False)
    i = i+1
    print(i)
