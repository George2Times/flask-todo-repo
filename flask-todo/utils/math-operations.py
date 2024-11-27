# Skrypt do obliczania sumy oraz generowania potęg liczby 2

# Lista liczb
numbers = [1, 5, 2, 3, 1, 4, 1, 23, 12, 2, 3, 1, 2, 31, 23, 1, 2, 3, 1, 23, 1, 2, 3, 123]

# Obliczenie sumy pierwszych dziesięciu elementów, zaczynając od elementu 5
sum_of_elements = sum(numbers[4:14])

# Generowanie listy potęg liczby 2 dla n [1..20]
powers_of_2 = [2 ** n for n in range(1, 21)]

# Wyświetlenie wyników
print("Suma pierwszych dziesięciu elementów zaczynając od elementu 5:", sum_of_elements)
print("Lista potęg liczby 2 dla n od 1 do 20:", powers_of_2)

# Testy
import unittest

class TestSumAndPowers(unittest.TestCase):
    def test_sum_of_elements(self):
        numbers = [1, 5, 2, 3, 1, 4, 1, 23, 12, 2, 3, 1, 2, 31, 23, 1, 2, 3, 1, 23, 1, 2, 3, 123]
        result = sum(numbers[4:14])
        expected_result = 80  # 1 + 4 + 1 + 23 + 12 + 2 + 3 + 1 + 2 + 31 = 80
        self.assertEqual(result, expected_result)

    def test_powers_of_2(self):
        result = [2 ** n for n in range(1, 21)]
        expected_result = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
