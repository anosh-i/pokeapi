import requests
import csv

# List of Pokémon to retrieve
pokemon_list = ["pikachu", "dhelmise", "charizard", "parasect", "terodictilio", "kingler"]

# Function to fetch Pokémon data
def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Could not retrieve data for {pokemon_name}")
        return None

# Function to fetch Pokémon species data
def fetch_pokemon_species_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Could not retrieve species data for {pokemon_name}")
        return None

# Function to derive gender from the gender_rate in species data
def derive_gender(gender_rate):
    if gender_rate == -1:
        return "Unknown or Not Found"
    elif gender_rate == 0:
        return "Genderless"
    elif gender_rate == 1:
        return "Mostly Male"
    elif gender_rate == 2:
        return "Mostly Female"
    else:
        return "Male/Female"

# Retrieve data for each Pokémon in the list
pokemon_data_list = []
for pokemon_name in pokemon_list:
    data = fetch_pokemon_data(pokemon_name)
    species_data = fetch_pokemon_species_data(pokemon_name)
    if data and species_data:
        # Derive gender based on gender_rate in species data
        gender_rate = species_data.get("gender_rate", -1)
        gender_info = derive_gender(gender_rate)

        # Extract growth rate, color, shape, types
        growth_rate = species_data.get("growth_rate", {}).get("name", "Unknown")
        color = species_data.get("color", {}).get("name", "Unknown")
        shape = species_data.get("shape", {}).get("name", "Unknown")
        types = [t["type"]["name"] for t in data.get("types", [])]

        # Extract habitat (with a safety check)
        habitat = species_data.get("habitat", {}).get("name", "Unknown") if species_data.get("habitat") else "Unknown"

        # Add to Pokémon data list
        pokemon_data_list.append({
            "id": data["id"],
            "name": data["name"].capitalize(),
            "types": ", ".join(types).capitalize(),
            "gender": gender_info,
            "habitat": habitat.capitalize(),
            "color": color.capitalize(),
            "shape": shape.capitalize(),
            "growth_rate": growth_rate.capitalize()
        })

# Save the data to a CSV file
with open("pokemon_full_data.csv", mode="w", newline="") as file:
    fieldnames = ["id", "name", "types", "gender", "habitat", "color", "shape", "growth_rate"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for pokemon in pokemon_data_list:
        writer.writerow(pokemon)

# Print a summary of the data fetched in the desired order
for pokemon_data in pokemon_data_list:
    print(
        f"ID: {pokemon_data['id']}, Name: {pokemon_data['name']}, Types: {pokemon_data['types']}, "
        f"Gender: {pokemon_data['gender']}, Habitat: {pokemon_data['habitat']}, Color: {pokemon_data['color']}, "
        f"Shape: {pokemon_data['shape']}, Growth Rate: {pokemon_data['growth_rate']}"
    )
