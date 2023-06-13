import unittest
from unittest import mock
from main import get_random_pokemon, convert_json_to_pokemon, get_all_stats_names
import response

# class TestIntegration(unittest.TestCase):
#     def test_getting_and_converting_pokemon(self):
#         api_response = get_random_pokemon()
#         pokemon = convert_json_to_pokemon(api_response=api_response)


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == "https://pokeapi.co/api/v2/stat/":
        return MockResponse(
            {
                "results": [
                    {"name": "hp"},
                    {"name": "attack"},
                    {"name": "defense"},
                    {"name": "special-attack"},
                    {"name": "special-defense"},
                    {"name": "speed"},
                    {"name": "accuracy"},
                    {"name": "evasion"},
                ],
            },
            200,
        )
    if args[0] == "https://pokeapi.co/api/v2/pokemon/1":
        return MockResponse(
            response,
            200,
        )


class TestIntegration(unittest.TestCase):
    @mock.patch("requests.get", side_effect=mocked_requests_get)
    def test_getting_all_stat_names(self, mock_request):
        stat_names = get_all_stats_names()
        self.assertEqual(
            stat_names,
            [
                "hp",
                "attack",
                "defense",
                "special-attack",
                "special-defense",
                "speed",
                "accuracy",
                "evasion",
            ],
        )


class TestTwo(unittest.TestCase):
    @mock.patch("random.randint", side_effect=1)
    @mock.patch("requests.get", side_effect=mocked_requests_get())
    def test_integration(self, mock_randint, mock_request):
        pokemon_data = get_random_pokemon()
        pokemon = convert_json_to_pokemon(pokemon_data)
        self.assertEqual(pokemon.name, "bulbasaur")
