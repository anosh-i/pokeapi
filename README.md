# Pokeapi

This project is to collect pokemon information for a list of pokemon from the [PokeAPI](https://pokeapi.co/) database.

## Installation and setup

1. Install git -  [GitHub installation guide](https://github.com/git-guides/install-git) 
2. ⁠Clone the repository - git clone ____ 
3. ⁠Create a virtual environment to install dependencies - `python -m venv myenv` 
4. ⁠Activate the virtual environment - `source myenv/bin/activate` 
5. ⁠Install dependencies - `pip install -r requirements.txt` 

## Run
`python3 main.py`

## Understanding output
This will generate a `pokemon_full_data.csv` file with the required columns for the specific static list of pokemon. An example output file has been included in repository.

## How to configure for other Pokemon
To add/remove pokemon from the list, add in the required pokemon name to the `pokemon_list` variable in `main.py`.
