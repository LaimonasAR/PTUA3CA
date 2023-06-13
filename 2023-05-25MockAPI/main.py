import requests
from typing import Dict, Optional
from random import randint
from pokemon import Pokemon, Statistics

POKEMON_ENDPOIT = "https://pokeapi.co/api/v2/pokemon/"


def get_random_pokemon() -> Dict[str, str]:
    pokeomn_id = randint(1, 1010)
    pokemon = requests.get(f"{POKEMON_ENDPOIT}{pokeomn_id}")
    return pokemon.json()


def convert_json_to_pokemon(api_response: Dict[str, str]) -> Pokemon:
    name = api_response["name"]
    response_stats = api_response["stats"]
    stats = []
    for response_stat in response_stats:
        stats.append(
            Statistics(response_stat["base_stat"], response_stat["stat"]["name"])
        )
    pokemon = Pokemon(name, stats)
    return pokemon


def get_all_stats_names() -> list[str]:
    stats_name = []
    stats = requests.get(f"https://pokeapi.co/api/v2/stat/")
    # print(stats)
    stats_json = stats.json()
    for x in stats_json["results"]:
        stats_name.append(x["name"])
    return stats_name


def choose_winner(pokemon1: Pokemon, pokemon2: Pokemon) -> Optional[Pokemon]:
    all_possible_stats = get_all_stats_names()
    p1_score = 0
    p2_score = 0
    for statistic in all_possible_stats:
        p1_stat_points = pokemon1.get_statistic_base_stat(statistic)
        p2_stat_points = pokemon2.get_statistic_base_stat(statistic)
        if p1_stat_points > p2_stat_points:
            p1_score += 1
        elif p2_stat_points > p1_stat_points:
            p2_score += 1
    if p1_score > p2_score:
        return pokemon1
    elif p2_score > p1_score:
        return pokemon2
    else:
        return None


if __name__ == "__main__":
    pokemon1 = convert_json_to_pokemon(get_random_pokemon())
    pokemon2 = convert_json_to_pokemon(get_random_pokemon())
    winner = choose_winner(pokemon1, pokemon2)
    print(f"first pokemon: {pokemon1}")
    print(f"second pokemon: {pokemon2}")
    if winner:
        print(f"The winner was {winner.name}")
    else:
        print("DRAW")

# def choose_winner(pokemon1: Pokemon, pokemon2: Pokemon) -> Pokemon:
#     print(f"Pokemon1 is {pokemon1.name}")
#     print(f"Pokemon2 is {pokemon2.name}")

#     pok_stat_count1 = len(pokemon1.stats)
#     pok_stat_count2 = len(pokemon2.stats)
#     print(pokemon1.stats)
#     print("******")
#     print(pokemon2.stats)
#     print(pok_stat_count1, pok_stat_count2)
#     if pok_stat_count1 > pok_stat_count2:
#         print(f"Winner - {pokemon1.name}, it has more stats")
#     elif pok_stat_count2 > pok_stat_count1:
#         print(f"Winner - {pokemon2.name}, it has more stats")
#     else:
#         pokemon1_stats_sum = 0
#         for stat in pokemon1.stats:
#             pokemon1_stats_sum += stat.base_stat

#         pokemon2_stats_sum = 0
#         for stat in pokemon2.stats:
#             pokemon2_stats_sum += stat.base_stat

#         if pokemon1_stats_sum > pokemon2_stats_sum:
#             print(
#                 f"Winner - {pokemon1.name}, with stats {pokemon1_stats_sum} against {pokemon2_stats_sum}"
#             )
#         elif pokemon1_stats_sum < pokemon2_stats_sum:
#             print(
#                 f"Winner - {pokemon2.name}, with stats {pokemon2_stats_sum} against {pokemon1_stats_sum}"
#             )
#         else:
#             print("it's a tie")


# api_response = get_random_pokemon()
# api_response2 = get_random_pokemon()
# pokemon1 = convert_json_to_pokemon(api_response=api_response)
# pokemon2 = convert_json_to_pokemon(api_response=api_response2)
# choose_winner(pokemon1, pokemon2)
