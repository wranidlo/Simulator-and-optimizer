from simulator.per_partner_simulator import per_partner_simulator as pps
from simulator.partner_data_reader import partner_data_reader as pdr
from datetime import timedelta


class simulator_core:
    def __init__(self, partners_list, partners_to_read_data_from):
        self.partners_list = partners_list
        self.partners_to_read_data_from = partners_to_read_data_from
        self.first_day = self.get_first_day()
        self.partner_simulator_list = []
        for e in self.partners_to_read_data_from:
            e.set_day(self.first_day-timedelta(1))
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
            e.next_day(partner_data_next_day.get(e.partner))


if __name__ == '__main__':
    pdr_a = pdr("0A2CEC84A65760AD90AA751C1C3DD861")
    pdr_b = pdr("1EFEC54BC5B5304BA8145CCC8037F98C")
    test = simulator_core(["1EFEC54BC5B5304BA8145CCC8037F98C"], [pdr_a, pdr_b])
    print(test.next_day())
    print(test.next_day())
