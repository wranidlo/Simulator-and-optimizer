from optimizer.product_list_optimizer import product_list_optimizer as plo
import pandas


class per_partner_simulator:
    def __init__(self, partner):
        self.partner = partner
        self.partner_optimizer = plo(partner)
        self.excluded_items = []

    def next_day(self, next_day_data):
        data_without_excluded = next_day_data[next_day_data["product_id"].apply(lambda x:x not in self.excluded_items)]
        self.excluded_items = self.partner_optimizer.next_day(data_without_excluded)
        print("After this day list of excluded products", self.excluded_items)
