import logging
from json import load, JSONDecodeError

pokemon = None

def load_pokemon_json_list(pokemon_list_file_name):
    try:
        with open(pokemon_list_file_name) as f:
            return load(f)
    except JSONDecodeError:
        logging.error(f'Pokemon List JSON file incorrectly formatted. Filename:{pokemon_list_file_name}')
        return []
    except IOError:
        logging.error(f'Pokemon List Json file not found. Filename:{pokemon_list_file_name}')
        return []

def get_pokemon():
    global pokemon
    if pokemon is None:
        pokemon = load_pokemon_json_list("./json/pokemon.json")
    return pokemon

def search_pokemon(query, pokemon=get_pokemon()):
    if isinstance(query,str):
        type_matches = []
        name_matches = []
        lowercase_query = query.lower()

        for p in pokemon:
            if lowercase_query in p["type"].lower():
                type_matches.append(p)
            elif lowercase_query in p["name"].lower():
                name_matches.append(p)
        
        return type_matches + name_matches
    else:
        return []


