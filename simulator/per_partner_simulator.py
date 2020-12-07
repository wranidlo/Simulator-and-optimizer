from optimizer.product_list_optimizer import product_list_optimizer as plo
import json


class per_partner_simulator:
    def __init__(self, partner):
        self.partner = partner
        self.partner_optimizer = plo(partner)
        self.excluded_items = []
        self.clicks_per_day = []
        self.sales_per_day = []
        self.gain_info = []
        with open('sim_conf') as json_file:
            data = json.load(json_file)
            self.npm = data["npm"]
            self.cost = data["cost"]
            self.click_cost = data["click_cost"]

    def next_day(self, next_day_data, present_day):
        unique_products = next_day_data["product_id"].unique().tolist()
        #print("Data z tego dnia: \n", next_day_data["date"])
        print("Wszystkie unikatowe produkty z danego dnia: ", len(unique_products))
        self.clicks_per_day.append(len(next_day_data.index))
        # self.clicks_per_day.append(len(next_day_data.loc[next_day_data['Sale'] == 0]))
        self.sales_per_day.append(next_day_data.loc[next_day_data['Sale'] == 1]['SalesAmountInEuro'].sum(axis=0))
        print("Liczba wszystkiech wierszy z danego dnia: ", next_day_data.shape[0])
        if next_day_data.shape[0] > 0:
            excluded_data = next_day_data[
                next_day_data["product_id"].apply(lambda x: x in self.excluded_items)]
            next_day_data = next_day_data[
                next_day_data["product_id"].apply(lambda x: x not in self.excluded_items)]
            unique_products = next_day_data["product_id"].unique().tolist()
            print("Wszystkie unikatowe produkty z danego dnia po usunięciu: ", len(unique_products))
            ex = excluded_data["product_id"].unique().tolist()
            print("Excluded products: ", ex)
            if excluded_data.shape[0] > 0:
                sales = excluded_data.loc[excluded_data['Sale'] == 1]['SalesAmountInEuro'].sum(axis=0)
                clicks = len(excluded_data.index)
                gain = {
                    "clicks_savings": (clicks*0.092),
                    "sale_losses": sales,
                    "profit_losses": (sales*self.npm)/100,
                    "profit_gain": (clicks*self.click_cost) - (sales*(self.npm+self.cost))/100
                }
                self.gain_info.append(gain)
            else:
                self.gain_info.append({
                    "clicks_savings": 0,
                    "sale_losses": 0,
                    "profit_losses": 0,
                    "profit_gain": 0
                })
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
