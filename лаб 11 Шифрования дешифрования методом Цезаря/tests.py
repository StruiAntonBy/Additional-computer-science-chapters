import unittest
import main


class TestEncryption(unittest.TestCase):

    def test_encrypt(self):
        text = 'Съешь же ещё этих мягких французских булок, да выпей чаю.'
        self.assertEqual(main.encrypt(text, key=3), 'Фэзыя йз зьи ахлш пвёнлш чугрщцкфнлш дцосн, жг еютзм ъгб.')

    def test_decrypt(self):
        cipher = 'Фэзыя йз зьи ахлш пвёнлш чугрщцкфнлш дцосн, жг еютзм ъгб.'
        self.assertEqual(main.decrypt(cipher, key=3), 'Съешь же ещё этих мягких французских булок, да выпей чаю.')
