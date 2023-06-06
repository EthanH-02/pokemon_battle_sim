import requests

from api_runner import MY_API, FRIEND_API
from pkmn import Pokemon
from debug.print_pkmn import printPkmn


def checkApi(api_url:str):
    rspn = requests.get(api_url)
    assert(rspn.status_code == 200)
    pkmn = Pokemon(rspn.json())
    printPkmn(pkmn)

def awaitPerm(prompt:str) -> bool:
    inp = input(prompt)
    if (inp.lower() == 'y'):
        return True
    elif (inp.lower() == 'n'):
        return False
    else:
        print('INVALID INPUT: please enter y or n')
        return awaitPerm(prompt)



if awaitPerm('Would you like to test your API? (y/n): '):
    print()
    checkApi(MY_API)
    print()

if awaitPerm('Would you like to test your friend\'s API? (y/n): '):
    print()
    checkApi(FRIEND_API)
    print()
