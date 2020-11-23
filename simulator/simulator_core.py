from simulator.per_partner_simulator import per_partner_simulator as pps
from simulator.partner_data_reader import partner_data_reader as pdr
from datetime import timedelta


class simulator_core:
    def __init__(self, partners_list, partners_to_read_data_from):
        self.partners_list = partners_list
        self.partners_to_read_data_from = partners_to_read_data_from
        self.first_day = self.get_first_day()
        self.present_day = self.first_day
        self.partner_simulator_list = []
        for e in self.partners_to_read_data_from:
            e.set_day(self.first_day - timedelta(1))
        for e in self.partners_to_read_data_from:
            if e.partner_id in self.partners_list:
                self.partner_simulator_list.append(pps(e.partner_id))

    def get_first_day(self):
        date_list = []
        for e in self.partners_to_read_data_from:
            if e.partner_id in self.partners_list:
                date_list.append(e.first_day)
        return min(date_list)

    def next_day(self):
        partner_data_next_day = {}
        for e in self.partners_to_read_data_from:
            partner_data_next_day[e.partner_id] = e.next_day()
        for e in self.partner_simulator_list:
            e.next_day(partner_data_next_day.get(e.partner), self.present_day)
        self.present_day = self.present_day + timedelta(1)

    def get_clicks_per_day(self):
        all_partners = {}
        for e in self.partner_simulator_list:
            all_partners[e.partner] = e.get_clicks_per_day()
        return all_partners

    def get_clicks_sum(self):
        all_partners = {}
        for e in self.partner_simulator_list:
            all_partners[e.partner] = e.get_clicks_sum()
        return all_partners

    def get_sales_per_day(self):
        all_partners = {}
        for e in self.partner_simulator_list:
            all_partners[e.partner] = e.get_sales_per_day()
        return all_partners

    def get_sales_sum(self):
        all_partners = {}
        for e in self.partner_simulator_list:
            all_partners[e.partner] = e.get_sales_sum()
        return all_partners

    def get_gain_data_per_partner(self):
        all_partners = {}
        for e in self.partner_simulator_list:
            all_partners[e.partner] = e.get_gain_info()
        return all_partners

    def get_gain_calculated(self):
        clicks = 0
        sale_losses = 0
        profit_losses = 0
        profit_gain = 0
        for e in self.partner_simulator_list:
            clicks += sum(item["clicks_savings"] for item in e.get_gain_info())
            sale_losses += sum(item["sale_losses"] for item in e.get_gain_info())
            profit_losses += sum(item["profit_losses"] for item in e.get_gain_info())
            profit_gain += sum(item["profit_gain"] for item in e.get_gain_info())
        return clicks, sale_losses, profit_losses, profit_gain

    def get_total_sales(self):
        total_sales = 0
        for e in self.partner_simulator_list:
            for f in e.sales_per_day:
                total_sales += f
        return total_sales

    def get_total_clicks(self):
        total_clicks = 0
        for e in self.partner_simulator_list:
            for f in e.clicks_per_day:
                total_clicks += f
        return total_clicks

    def get_profit_gain_per_user_per_day(self):
        out = {}
        for e in self.partner_simulator_list:
            out[e.partner] = []
            for day in e.get_gain_info():
                out[e.partner].append(day["profit_gain"])
        return out

    def get_profit_gain_per_user_per_day_accumulated(self):
        out = {}
        for e in self.partner_simulator_list:
            out[e.partner] = []
            for day in e.get_gain_info():
                if len(out[e.partner])>0:
                    last = len(out[e.partner])-1
                    out[e.partner].append(day["profit_gain"]+out[e.partner][last])
                else:
                    out[e.partner].append(day["profit_gain"])
        return out


if __name__ == '__main__':
    pdr_a = pdr("0A2CEC84A65760AD90AA751C1C3DD861")
    pdr_b = pdr("1EFEC54BC5B5304BA8145CCC8037F98C")
    test = simulator_core(["1EFEC54BC5B5304BA8145CCC8037F98C"], [pdr_a, pdr_b])
    print(test.next_day())
    print(test.next_day())
