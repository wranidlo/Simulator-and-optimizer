from simulator.simulator_core import simulator_core as sc
from simulator.partner_data_reader import partner_data_reader as pdr
import json


if __name__ == '__main__':
    partners_to_involve_in_simulation = []
    partners_to_read_data_from = []
    number_of_simulation_steps = 0
    nmp = 10
    with open('sim_conf') as json_file:
        data = json.load(json_file)
        number_of_simulation_steps = data["number_of_simulation_steps"]
        npm = data["npm"]
        for e in data["partners_to_involve_in_simulation"]:
            partners_to_involve_in_simulation.append(e)
        for e in data["partners_to_read_data_from"]:
            partners_to_read_data_from.append(pdr(e))

    executor = sc(partners_to_involve_in_simulation, partners_to_read_data_from)
    for _ in (0, number_of_simulation_steps):
        executor.next_day()
