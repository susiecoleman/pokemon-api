

from unittest import TestCase
from search.pokemon import load_pokemon_json_list, search_pokemon

class TestSearch(TestCase):

    def test_match_for_name_and_type_does_not_cause_duplicate(self):
        pokemon = [
            {"name": "Grass", "type": "Grass"},
            {"name": "Scorbunny", "type": "Fire"}]
        filtered_pokemon = [
            {"name": "Grass", "type": "Grass"}]

        self.assertEqual(
            search_pokemon("grass", pokemon),
            filtered_pokemon,
            "Should return pokemon with name Grass only once"
        )

    def test_return_type_matches_first(self):
        pokemon = [
            {"name": "Grass", "type": "Fire"},
            {"name": "Grookey", "type": "Grass"}]
        filtered_pokemon = [
            {"name": "Grookey", "type": "Grass"},
            {"name": "Grass", "type": "Fire"}]

        self.assertEqual(
            search_pokemon("ss", pokemon),
            filtered_pokemon,
            "Should return pokemon with type grass then pokemon with name grass"
        )

    def test_search_finds_nothing_for_non_string_type_input(self):
        pokemon = [
            {"name": "Scorbunny", "type": "Fire"},
            {"name": "Grookey", "type": "Grass"}]
        filtered_pokemon = []

        self.assertEqual(
            search_pokemon(12, pokemon),
            filtered_pokemon,
            "Should empty list"
        )

    def test_search_finds_pokemon_with_matching_type(self):
        pokemon = [
            {"name": "Scorbunny", "type": "Fire"},
            {"name": "Grookey", "type": "Grass"}]
        filtered_pokemon = [{"name": "Grookey", "type": "Grass"}]

        self.assertEqual(
            search_pokemon("grass", pokemon),
            filtered_pokemon,
            "Should return one pokemon of type grass"
        )

    def test_search_finds_pokemon_with_matching_name(self):
        pokemon = [
            {"name": "Scorbunny", "type": "Fire"},
            {"name": "Grookey", "type": "Grass"}]
        filtered_pokemon = [{"name": "Grookey", "type": "Grass"}]

        self.assertEqual(
            search_pokemon("Grook", pokemon),
            filtered_pokemon,
            "Should return one pokemon with name Grookey"
        )

    def test_search_finds_pokemon_with_upper_lowercase_mismatch(self):
        pokemon = [
            {"name": "Scorbunny", "type": "Fire"},
            {"name": "Grookey", "type": "Grass"}]
        filtered_pokemon = [{"name": "Scorbunny", "type": "Fire"}]

        self.assertEqual(
            search_pokemon("sCOR", pokemon),
            filtered_pokemon,
            "Should return one pokemon with name Scorbunny"
        )

    def test_load_pokemon_json_list_parses_valid_json(self):
        self.assertEqual(
            load_pokemon_json_list("./json/valid_test_json.json"),
            [{"name": "name","type": "type"}],
            "Should be a list with one dictionary")

    def test_load_pokemon_json_list_invalid_file(self):
        self.assertEqual(
            load_pokemon_json_list('invalid_file_name'),
            [],
            "Should be an empty list if json file path is invalid")

    def test_load_pokemon_json_list_invalid_json_format(self):
        self.assertEqual(
            load_pokemon_json_list('broken_json.json'),
            [],
            "Should be an empty list if json is invalid")
