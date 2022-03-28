from sys import argv
import requests

def main():
    
    poke_name = argv[1]
    poke_info = get_pokemon_info(poke_name)
    if poke_info:
        pastebin_strings = get_pastebin_strings(poke_info)
        pass

def get_pastebin_strings(poke_dict):
    title = poke_dict + "'s Abilities:"
    body_text = "Abilities: ", poke_info["abilities"]
    return(body_text)

def get_pokemon_info(poke_name):
    print("Getting Pokemon information...", end="")
    response = requests.get('https://pokeapi.co/api/v2/pokemon/'+str(poke_name)+'/')

    if response.status_code == 200:
        print("success!")
        return response.json()
    else:
        print("failed. Response code",response.status_code)
        return

main()
