import pandas as pd
from datetime import datetime, timedelta
headers = ["Sale", "SalesAmountInEuro", "time_delay_for_conversion", "date", "nb_clicks_1week",
           "product_price", "product_age_group", "device_type", "audience_id", "product_gender", "product_brand",
           "product_category_1", "product_category_2", "product_category_3", "product_category_4", "product_category_5",
           "product_category_6", "product_category_7", "product_country", "product_id", "product_title", "partner_id",
           "user_id"]
raw_dataset_df = pd.read_csv("D:/data/Criteo_Conversion_Search/CriteoSearchData.csv", sep="\t", header=0, nrows=100000)
raw_dataset_df.columns = headers
df_groups_for_partners = raw_dataset_df.groupby("partner_id")
partners_selected_for_test_parameter_for_Mr_Riegel_20201103 = ["C0F515F0A2D0A5D9F854008BA76EB537", "E3DDEB04F8AFF944B11943BB57D2F620", "E68029E9BCE099A60571AF757CBB6A08"]
for partner_id, df_group_for_partner in df_groups_for_partners:
    if partner_id in partners_selected_for_test_parameter_for_Mr_Riegel_20201103:
        test_parameter_for_Mr_Riegel_20201103 = df_group_for_partner.shape[0]
        print("test_parameter for partner_id " + partner_id + " : ", test_parameter_for_Mr_Riegel_20201103)