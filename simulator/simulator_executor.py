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
        for e in partners_to_involve_in_simulation:
            if e not in data["partners_to_read_data_from"]:
                partners_to_read_data_from.append(pdr(e))

    executor = sc(partners_to_involve_in_simulation, partners_to_read_data_from)
    for i in range(1, number_of_simulation_steps+1):
        print("Day : ", i)
        executor.next_day()
    results = {
        "Clicks of partners per day": executor.get_clicks_per_day(),
        "Sales of partners per day": executor.get_sales_per_day(),
        "Clicks sum": executor.get_clicks_sum(),
        "Sales sum": executor.get_sales_sum()
    }

    print("Clicks of partners per day\n", results.get("Clicks of partners per day"))
    print("Clicks of partners\n", results.get("Clicks sum"))
    print("Sales of partners per day\n", results.get("Sales of partners per day"))
    print("Sales of partners\n", results.get("Sales sum"))

    with open('simulation_results.json', 'w') as fp:
        json.dump(results, fp)
