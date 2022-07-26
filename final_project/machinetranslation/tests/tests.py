import unittest

from translator import frenchtoenglish, englishtofrench

class TestfrenchtoEnglish(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(frenchtoenglish("None"),'')
        self.assertNotEqual(englishtofrench("None"),'')
        result= frenchtoenglish("Bonjour")
        self.assertEqual(result,"Hello")

        result2= frenchtoenglish("Bonjour")
        self.assertEqual(result2,"Hello")

class TestenglishtoFrench(unittest.TestCase):
    def test1(self):
        result3= englishtofrench("Hello")
        self.assertEqual(result3,"Bonjour")

        result4= englishtofrench("Hello")
        self.assertEqual(result4,"Bonjour")

unittest.main()