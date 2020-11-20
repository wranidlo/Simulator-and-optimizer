import random
import json
import pandas


class product_list_optimizer:
    def __init__(self, partner):
        self.partner = partner
        self.seed = 10
        with open('sim_conf') as json_file:
            data = json.load(json_file)
            self.seed = data["seed"]
        random.seed(self.seed)

    def next_day(self, data):
        print("Optimizing data for user: ", self.partner)
        print(data)
        unique_products = data["product_id"].unique()
        print(unique_products)
        excluded_products = []
        if len(unique_products) > 0:
            item_nr = random.randint(0, len(unique_products))
            item = unique_products[item_nr-1]
            excluded_products.append(item)
        return excluded_products
