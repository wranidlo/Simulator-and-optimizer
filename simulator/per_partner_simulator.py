from optimizer.product_list_optimizer import product_list_optimizer as plo
import pandas


class per_partner_simulator:
    def __init__(self, partner):
        self.partner = partner
        self.partner_optimizer = plo(partner)
        self.excluded_items = []
        self.clicks_per_day = []
        self.sales_per_day = []

    def next_day(self, next_day_data, present_day):
        self.clicks_per_day.append(len(next_day_data.index))
        self.sales_per_day.append(next_day_data.loc[next_day_data['Sale'] == 1]['SalesAmountInEuro'].sum(axis=0))

        data_without_excluded = next_day_data[next_day_data["product_id"].apply(lambda x:x not in self.excluded_items)]
        self.excluded_items = self.partner_optimizer.next_day(data_without_excluded, present_day)
        print("After this day list of excluded products", self.excluded_items)

    def get_clicks_per_day(self):
        return self.clicks_per_day

    def get_clicks_sum(self):
        return sum(self.clicks_per_day)

    def get_sales_per_day(self):
        return self.sales_per_day

    def get_sales_sum(self):
        return sum(self.sales_per_day)