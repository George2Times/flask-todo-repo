# Skrypt filtrujący użytkowników tylko z Polski

import random

# Moduł do generowania listy 10=(num_users) użytkowników 
def generate_users(num_users=10):
    names = ["Kamil", "John", "Anna", "Yeti", "Maria", "Steve", "Olga", "Andrzej", "Lucas", "Marta"]
    countries = ["Poland", "USA", "Germany", "France", "Poland", "Canada"]
    return [
        {"name": random.choice(names), "country": random.choice(countries)}
        for _ in range(num_users)
    ]

# Lista użytkowników# Lista użytkowników
users = generate_users()

# List Comprehension do filtrowania użytkowników z Polski
polish_users = [user for user in users if user.get("country") == "Poland"]

# Wyświetlenie wyników
print(polish_users)

# Testy
import unittest

class TestPolishUsersFilter(unittest.TestCase):
    def test_polish_users(self):
        users = [
            {"name": "Kamil", "country": "Poland"},
            {"name": "John", "country": "USA"},
            {"name": "Yeti"}  # Brak kraju
        ]
        result = [user for user in users if user.get("country") == "Poland"]
        expected_result = [{"name": "Kamil", "country": "Poland"}]
        self.assertEqual(result, expected_result)

    def test_no_polish_users(self):
        users_no_poland = [
            {"name": "John", "country": "USA"},
            {"name": "Anna", "country": "Germany"}
        ]
        result = [user for user in users_no_poland if user.get("country") == "Poland"]
        self.assertEqual(result, [])

    def test_empty_country(self):
        users_with_empty_country = [
            {"name": "Kamil", "country": "Poland"},
            {"name": "Yeti"}  # Brak kraju
        ]
        result = [user for user in users_with_empty_country if user.get("country") == "Poland"]
        expected_result = [{"name": "Kamil", "country": "Poland"}]
        self.assertEqual(result, expected_result)

    def test_generated_users(self):
        users = generate_users(100)
        polish_users = [user for user in users if user.get("country") == "Poland"]
        for user in polish_users:
            self.assertEqual(user.get("country"), "Poland")
        print('Done')

if __name__ == "__main__":
    unittest.main()
