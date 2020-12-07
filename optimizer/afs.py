import pandas as pd
from datetime import datetime, timedelta
headers = ["Sale", "SalesAmountInEuro", "time_delay_for_conversion", "date", "nb_clicks_1week",
           "product_price", "product_age_group", "device_type", "audience_id", "product_gender", "product_brand",
           "product_category_1", "product_category_2", "product_category_3", "product_category_4", "product_category_5",
           "product_category_6", "product_category_7", "product_country", "product_id", "product_title", "partner_id",
           "user_id"]

print(len(['8887F115E0E142BB80201E753BE66E4D', '55CEAB2D9F1F7BFC027DAC0E928C0132', 'AD0107BADEE308615EB02357C5E2BE37', '94CA8CA7BECD657D4F9AF204B40C875A', 'ADFED19CCCF9A13E7A7E5A6D90761A02', '6843E5952E3A324E27D1F8E3C4830C87', '2CF5DE84915910C549B2576084A09870', '6E6AC8106BF22558CDDA130EB9F3D8DD', '014F17B51C77C0DC19CB9BB9206EBCB7', '6C6658A2C72EC82CC67871D93A1B9D52', '8BF4BDC098576687A0759723BBAA464E', '57191ADE04B714205761A70BA2024824']))
raw_dataset_df = pd.read_csv("D:/data/Criteo_Conversion_Search/CriteoSearchData.csv", sep="\t", header=0, nrows=100000)
raw_dataset_df.columns = headers
df_groups_for_partners = raw_dataset_df.groupby("partner_id")
partners_selected_for_test_parameter_for_Mr_Riegel_20201103 = ["C0F515F0A2D0A5D9F854008BA76EB537", "E3DDEB04F8AFF944B11943BB57D2F620", "E68029E9BCE099A60571AF757CBB6A08"]
for partner_id, df_group_for_partner in df_groups_for_partners:
    if partner_id in partners_selected_for_test_parameter_for_Mr_Riegel_20201103:
        test_parameter_for_Mr_Riegel_20201103 = df_group_for_partner.shape[0]
        print("test_parameter for partner_id " + partner_id + " : ", test_parameter_for_Mr_Riegel_20201103)