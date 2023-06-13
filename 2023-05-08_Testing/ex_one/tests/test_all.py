import unittest
import main


class UnitTests(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(56, main.skaiciu_suma(45, 5, 6))

    def test_sum_list(self):
        self.assertEqual(95, main.saraso_suma([4, 5, 78, 8]))

    def test_high_numb(self):
        self.assertEqual(789, main.didziausias_skaicius(5, 8, 789, 94, 78))

    def test_backw_str(self):
        self.assertEqual("salisA", main.stringas_atbulai("Asilas"))

    def test_str_info(self):
        string = "Laba diena laba diena lab 522"
        result = main.info_apie_sakini(string)
        self.assertEqual(result["zodziai"], 6)
        self.assertEqual(result["didziosios"], 1)
        self.assertEqual(result["mazosios"], 20)
        self.assertEqual(result["skaiciai"], 3)

    def test_unique_list(self):
        my_list = [4, 5, "Labas", 6, "Labas", True, 5, True, 10]
        result = main.unikalus_sarasas(my_list)
        expected = [4, 5, "Labas", 6, True, 10]
        self.assertCountEqual(result, expected)

    def test_prime_number(self):
        self.assertTrue(main.ar_pirminis(5))
        self.assertFalse(main.ar_pirminis(6))

    def test_backward_sentence(self):
        string = "Vienas du trys keturi"
        result = main.isrikiuoti_nuo_galo(string)
        expected = "keturi trys du Vienas"
        self.assertEqual(result, expected)

    def test_leap_year(self):
        self.assertTrue(main.ar_keliamieji(2020))
        self.assertFalse(main.ar_keliamieji(2100))
        self.assertTrue(main.ar_keliamieji(2000))

    def test_check_date(self):
        date_one = "2000-01-01 12:12:12"
        date_two = "1991-03-11 12:12:12"
        result_one = main.patikrinti_data(date_one)
        result_two = main.patikrinti_data(date_two)
        exp_one = 8529
        exp_two = 11747
        self.assertEqual(result_one, exp_one)
        self.assertEqual(result_two, exp_two)
