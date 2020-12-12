from simulator.simulator_core import simulator_core as sc
from simulator.partner_data_reader import partner_data_reader as pdr
import json
import matplotlib.pyplot as plt


if __name__ == '__main__':
    partners_to_involve_in_simulation = []
    partners_to_read_data_from = []
    number_of_simulation_steps = 0
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

    clicks, sale_losses, profit_losses, profit_gain = executor.get_gain_calculated()
    results = {
        "Clicks of partners per day": executor.get_clicks_per_day(),
        "Sales of partners per day": executor.get_sales_per_day(),
        "Clicks sum without exclusion": executor.get_clicks_sum(),
        "Sales sum without exclusion": executor.get_sales_sum(),
        "Gain info per partner per day": executor.get_gain_data_per_partner(),
        "Gain info summed": {
                    "clicks_savings": clicks,
                    "sale_losses": sale_losses,
                    "profit_losses": profit_losses,
                    "profit_gain": profit_gain
                }
    }

    print("Clicks of partners per day\n", results.get("Clicks of partners per day"))
    print("Clicks of partners\n", results.get("Clicks sum without exclusion"))
    print("Sales of partners per day\n", results.get("Sales of partners per day"))
    print("Sales of partners\n", results.get("Sales sum without exclusion"))
    print("Gain info per partner per day\n", results.get("Gain info per partner per day"))
    print("Gain info summed\n", results.get("Gain info summed"))
    with open('simulation_results.json', 'w') as fp:
        json.dump(results, fp, sort_keys=True, indent=4, separators=(',', ': '))
    ploted = executor.get_profit_gain_per_user_per_day()
    for e in ploted:
        plt.plot(range(1, number_of_simulation_steps+1), ploted.get(e))
        plt.ylabel('profit gain')
        plt.show()

    ploted = executor.get_profit_gain_per_user_per_day_accumulated()
    for e in ploted:
        plt.plot(range(1, number_of_simulation_steps + 1), ploted.get(e))
        plt.ylabel('profit gaina accumulated')
        plt.show()