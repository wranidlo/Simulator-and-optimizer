import random
import json


class product_list_optimizer:
    def __init__(self, partner):
        self.partner = partner
        self.seed = 12
        self.data = None
        with open('sim_conf') as json_file:
            data = json.load(json_file)
            self.seed = data["seed"]

    def next_day(self, data, present_day):
        print("Liczba wierszy po usunięciu produktów do wykluczenia: ", data.shape[0])
        if self.data is None:
            self.data = data
        else:
            self.data = self.data.append(data, ignore_index=True)
        print("Optimizing data for user: ", self.partner, " for day: ", present_day)
        # print(data[["SalesAmountInEuro", "date", "product_id"]].head(2))
        # unique_products = self.data["product_id"].unique().tolist()
        # print(unique_products)
        excluded_products = self.get_excluded_products_pseudorandomly(self.data)
        if excluded_products is None:
            return []
        else:
            return excluded_products

    def get_excluded_products_pseudorandomly(self, data):
        unique_products = data["product_id"].unique().tolist()
        print("Wszystkie unikatowe produkty w optimizerze: ", len(unique_products))
        unique_products.sort()
        how_many_products = round(len(unique_products) / 20)
        random.seed(self.seed)
        excluded_products = random.sample(unique_products, how_many_products)
        excluded_products.sort()
        print("Liczba produktów do wykluczenia w dniu następnym: ", len(excluded_products))
        return excluded_products
