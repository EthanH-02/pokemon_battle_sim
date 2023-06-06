import requests
from pkmn import Pokemon

# Insert the URL to be utilised for your Pokemon API
MY_API = ''
FRIEND_API = ''

def extract_pkmn(api_url:str) -> Pokemon:

    # This code they will have to implement
    rspn = requests.get(api_url)
    assert(rspn.status_code == 200)
    pkmn = Pokemon(rspn.json())
    return pkmn
