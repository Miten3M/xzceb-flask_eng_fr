import unittest
from translator import french_to_english,english_to_french

class TestEnglish_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'),'Bonjour')

class TestFrench_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'),'Hello')

unittest.main()