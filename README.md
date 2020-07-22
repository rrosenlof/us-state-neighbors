# About

Several .csv files working with US state data. Lower 48 states only. Primarily to create a database showing how many states are between any two states

### Contents:

##### Borders.csv

Each of the states, all the states that state directly borders, and the number of directly bordering states.

##### Neighbors.csv

A slightly different format of the `borders.csv` file. 1st column is a state and 2nd column is a directly bordering state.

##### Paths.csv

Each state and the shortest path to every other state. I only included one path, several states Column info:
Column Name | Description
--- | ---
**STATE_1** | Starting state
**STATE_1_ABBR** | Postal abbreviation
**STATE_2** | Ending state
**STATE_2_ABBR** | Postal abbreviation
**PATH** | One possible path, usually the shortest, between any two states. Using the postal codes in order, including starting and ending states
**INVERSE_PATH** | Same as path, but in opposite direction
**DISTANCE** | Number of states from starting state to ending state, ending state inclusive

##### All_paths.csv

Same as paths, but a row for each state to every other state

##### Main.py

Some scripts for trying to programatically create the `paths.csv` file. Conclusion: too complicated... I made `paths.csv` by hand mostly. More to come here maybe...

##### Linkedlistapi.py

For making linked lists, trying to create the paths

##### Words.py

Some testing functions

### Assumptions:

- Utah and New Mexico don't border
- Arizona and Colorado don't border
- Delaware and New Jersey border
- Michigan and Illinois don't border
- Michigan and Minnesota don't border