from optimizer.product_list_optimizer import product_list_optimizer as plo
import pandas


class per_partner_simulator:
    def __init__(self, partner):
        self.partner = partner
        self.partner_optimizer = plo(partner)
        self.excluded_items = []
        self.clicks_per_day = []
        self.sales_per_day = []
        self.gain_info = []

    def next_day(self, next_day_data, present_day):
        self.clicks_per_day.append(len(next_day_data.index))
        # self.clicks_per_day.append(len(next_day_data.loc[next_day_data['Sale'] == 0]))
        self.sales_per_day.append(next_day_data.loc[next_day_data['Sale'] == 1]['SalesAmountInEuro'].sum(axis=0))

        if next_day_data.shape[0] > 0:
            excluded_data = next_day_data[
                next_day_data["product_id"].apply(lambda x: x in self.excluded_items)]
            next_day_data = next_day_data[
                next_day_data["product_id"].apply(lambda x: x not in self.excluded_items)]
            # print("Excluded data: ", excluded_data["product_id"])
            if excluded_data.shape[0] > 0:
                sales = excluded_data.loc[excluded_data['Sale'] == 1]['SalesAmountInEuro'].sum(axis=0)
                clicks = len(excluded_data.index)
                gain = {
                    "clicks_savings": clicks,
                    "sale_losses": sales,
                    "profit_losses": (sales*10)/100,
                    "profit_gain": (sales*22)/100 - clicks
                }
                self.gain_info.append(gain)
            else:
                self.gain_info.append({
                    "clicks_savings": 0,
                    "sale_losses": 0,
                    "profit_losses": 0,
                    "profit_gain": 0
                })

        self.excluded_items = self.partner_optimizer.next_day(next_day_data, present_day)
        print("After this day list of excluded products", self.excluded_items)

    def get_clicks_per_day(self):
        return self.clicks_per_day

    def get_clicks_sum(self):
        return sum(self.clicks_per_day)

    def get_sales_per_day(self):
        return self.sales_per_day

    def get_sales_sum(self):
        return sum(self.sales_per_day)

    def get_gain_info(self):
        return self.gain_info
