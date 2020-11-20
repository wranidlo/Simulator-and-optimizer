import random
import json
import pandas


class product_list_optimizer:
    def __init__(self, partner):
        self.partner = partner
        self.seed = 10
        self.data = None
        with open('sim_conf') as json_file:
            data = json.load(json_file)
            self.seed = data["seed"]
        random.seed(self.seed)

    def next_day(self, data, present_day):
        if self.data is None:
            self.data = data
        else:
            self.data = self.data.append(data, ignore_index=True)
        print("Optimizing data for user: ", self.partner, " for day: ", present_day)
        # print(self.data)
        unique_products = self.data["product_id"].unique()
        # print(unique_products)
        excluded_products = []
        if len(unique_products) > 1:
            item_nr = random.randint(0, len(unique_products))
            item = unique_products[item_nr-1]
            excluded_products.append(item)
        return excluded_products
