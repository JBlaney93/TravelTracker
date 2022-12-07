import unittest
from models.user import User
from models.country import Country
from models.memory import Memory 

class TestMemory(unittest.TestCase):
    def setUp(self):
        self.user = User('Jim')

        self.country = Country('Scotland', 'Glasgow', True)

        self.memory= Memory(self.user, self.country, 'Great city, heart of Scotland')

    
    def test_user_has_name(self):
        self.assertEqual('Jim', self.user.name)


    def test_country_has_name(self):
        self.assertEqual('Scotland', self.country.name)

    def test_country_has_cities(self):
        self.assertEqual('Glasgow', self.country.cities)

    def test_country_visted(self):
        self.assertEqual(True, self.country.visited)


    def test_memory_has_user(self):
        self.assertEqual(self.user, self.memory.user)

    def test_memory_has_country(self):
        self.assertEqual(self.country, self.memory.country)

    def test_memory_has_memory(self):
        self.assertEqual('Great city, heart of Scotland', self.memory.memory)

    