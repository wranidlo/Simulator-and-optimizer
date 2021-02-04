# Simulator-and-optimizer

This project consists of two parts of a simulator and an optimizer.
## Simulator
Simulator consists of parts that allows:
- division of data from one file containing information about many companies into several files containing information about individual companies,
- running simulations for selected companies, during which the loaded data is divided into time windows equal to one day,
- starting optimization and excluding products indicated by the optimizer of the previous day,
- calculating the results (profits and losses) obtained as a result of the simulation (product exclusion) of a given producer.

##Optimizer
Optimizer collects the data received by the simulator and selecting products to exclude in the future time period (next day).
