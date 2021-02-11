# Simulator-and-optimizer
This project consists of two parts of a simulator and an optimizer.
## Dataset
Datesed used in project available at https://ailab.criteo.com/criteo-sponsored-search-conversion-log-dataset/

## How to run
1. Run  partners_data_spliter.py to split dataset into single producer files (change localization of dataset)
2. Run sort_by_date.py to sort content of single producer files (enter the folder where the files are saved)
3. Run simulator_executor.py to start simulation, configuration settings are changed by editing the file sim_conf. 
Available setting are:
- partners_to_involve_in_simulation, 
- partners_to_read_data_from, 
- number_of_simulation_steps, 
- npm, 
- cost, 
- seed, 
- click_cost.

## Simulator
Simulator consists of parts that allows:
- division of data from one file containing information about many companies into several files containing information about individual companies,
- running simulations for selected companies, during which the loaded data is divided into time windows equal to one day,
- starting optimization and excluding products indicated by the optimizer of the previous day,
- calculating the results (profits and losses) obtained as a result of the simulation (product exclusion) of a given producer.

## Optimizer
Optimizer collects the data received by the simulator and selecting products to exclude in the future time period (next day).
