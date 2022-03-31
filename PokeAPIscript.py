from sys import argv
import requests

def main():
    
    poke_name = argv[1]
    poke_info = get_pokemon_info(poke_name)

    if poke_info:
        pastebin_strings = get_pastebin_strings(poke_info)
        print(pastebin_strings[0], pastebin_strings[1])
        #pastebin_url = post_to_pastebin(pastebin_strings[], pastebin_strings[])
        #print(pastebin_url)

def get_pokemon_info(poke_name):
    print("Getting Pokemon information...", end="")
    URL = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(URL+str(poke_name)+'/')
    if response.status_code == 200:
        print("success!")
        return response.json()
    else:
        print("failed. Response code",response.status_code)
        return

def get_pastebin_strings(poke_dict):
    title = str(poke_dict) + "'s Abilities:"
    body_text = "Abilities: "
    for _ in poke_dict["abilities"]:
        body_text += ""
    return(title + body_text)

def post_to_pastebin(title, body_text):
    print("Posting to Pastebin...", end = '')

    pbin_params = {
        'api_dev_key': "f4R0OTFza_qTQ1NZJYLjoCeLqoHQux4X",
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title
    }
    URL = 'https://pastebin.com/api/api_post.php'
    response = requests.post(URL, params=pbin_params)

    if response.status_code == 200:
        print("success!")
        return response.json()
    else:
        print("failed. Response code",response.status_code)
        return

main()
