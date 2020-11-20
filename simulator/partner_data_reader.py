import pandas as pd
from datetime import datetime, timedelta


class partner_data_reader:
    def __init__(self, partner_id):
        self.partner_id = partner_id
        self.df = pd.read_csv("D:/data/saved/"+partner_id+".csv", sep=",", header=0)
        self.df["date"] = pd.to_datetime(self.df["date"])
        self.first_day = self.df["date"][0].date()
        self.day = self.first_day

    def set_day(self, day):
        self.day = day

    def next_day(self):
        # temp_index = self.df[self.df["date"].dt.date > self.day].index[0]
        # self.day = self.df["date"][temp_index].date()
        self.day = self.day + timedelta(1)
        temp = self.df[self.df["date"].dt.date == self.day]
        # print("Next day data for "+self.partner_id+" from partner data reader\n", temp["date"])
        return temp


if __name__ == '__main__':
    test = partner_data_reader("0A2CEC84A65760AD90AA751C1C3DD861")
    test.next_day()
    test.next_day()
    test.next_day()
