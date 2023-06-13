import unittest
from main import Sakinys


class UnitTests(unittest.TestCase):
    def setUp(self):
        self.sentence = Sakinys()
        self.sentence_two = Sakinys(tekstas="Mano tekstas yra toks")
        self.sentence_three = Sakinys(tekstas="Lorem ipsum dolor sit amet")
        self.empty = Sakinys("")

    def test_backwards(self):
        self.assertEqual(self.sentence.atbulai(), "nohtyP fo neZ")
        self.assertEqual(self.sentence_two.atbulai(), "skot ary satsket onaM")
        self.assertEqual(self.sentence_three.atbulai(), "tema tis rolod muspi meroL")
        self.assertEqual(self.empty.atbulai(), "")

    def test_text_to_upper(self):
        self.assertEqual(self.sentence.didziosiomis(), "ZEN OF PYTHON")
        self.assertEqual(self.sentence_two.didziosiomis(), "MANO TEKSTAS YRA TOKS")
        self.assertEqual(
            self.sentence_three.didziosiomis(), "LOREM IPSUM DOLOR SIT AMET"
        )
        self.assertEqual(self.empty.didziosiomis(), "")

    def test_text_to_lower(self):
        self.assertEqual(self.sentence.mazosiomis(), "zen of python")
        self.assertEqual(self.sentence_two.mazosiomis(), "mano tekstas yra toks")
        self.assertEqual(self.sentence_three.mazosiomis(), "lorem ipsum dolor sit amet")
        self.assertEqual(self.empty.mazosiomis(), "")

    def test_find_and_count(self):
        self.assertEqual(self.sentence.ieskoti("e"), 1)
        self.assertEqual(self.sentence_two.ieskoti("a"), 3)
        self.assertEqual(self.sentence_three.ieskoti("o"), 3)
        self.assertEqual(self.empty.ieskoti("a"), 0)

    def test_change_portion_of_string(self):
        self.assertEqual(self.sentence.pakeisti("Zen", "Ben"), "Ben of Python")
        self.assertEqual(
            self.sentence_two.pakeisti("Mano", "Savo"), "Savo tekstas yra toks"
        )
        self.assertEqual(
            self.sentence_three.pakeisti("Lorem", "Borem"), "Borem ipsum dolor sit amet"
        )
        self.assertEqual(self.empty.pakeisti("a", "b"), "")

    def test_get_desired_word(self):
        self.assertEqual(self.sentence.atspausdintiZodi(2), "Python")
        self.assertEqual(self.sentence_two.atspausdintiZodi(1), "tekstas")
        self.assertEqual(self.sentence_three.atspausdintiZodi(0), "Lorem")
        with self.assertRaises(IndexError):
            self.empty.atspausdintiZodi(0)

    def test_string_info(self):
        result_one = {
            "Žodžių kiekis": 3,
            "Skaičiai": 0,
            "Didžiosios": 2,
            "Mažosios": 9,
        }
        result_two = {
            "Žodžių kiekis": 4,
            "Skaičiai": 0,
            "Didžiosios": 1,
            "Mažosios": 17,
        }
        result_three = {
            "Žodžių kiekis": 5,
            "Skaičiai": 0,
            "Didžiosios": 1,
            "Mažosios": 21,
        }
        result_empty = {
            "Žodžių kiekis": 0,
            "Skaičiai": 0,
            "Didžiosios": 0,
            "Mažosios": 0,
        }

        self.assertEqual(self.sentence.info(), result_one)
        self.assertEqual(self.sentence_two.info(), result_two)
        self.assertEqual(self.sentence_three.info(), result_three)
        self.assertEqual(self.empty.info(), result_empty)
