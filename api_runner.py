from api_caller import extract_pkmn
from backend.battle import pkmnBattle

from api_caller import MY_API, FRIEND_API


if __name__ == "__main__":
    my_pkmn = extract_pkmn(MY_API)
    friends_pkmn = extract_pkmn(FRIEND_API)

    pkmnBattle(my_pkmn, friends_pkmn)
