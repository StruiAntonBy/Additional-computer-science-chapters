import unittest
from main import encrypt, decrypt


class EncryptDecryptTest(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(encrypt('12'), '1 2')

    def test_decrypt(self):
        self.assertEqual(decrypt('1 2'), '12')

    def test1_encrypt(self):
        self.assertEqual(encrypt('Привет мир!'), 'пт рм ии вр е!')

    def test1_decrypt(self):
        self.assertEqual(decrypt('пт рм ии вр е!'), 'приветмир!')

    def test2_encrypt(self):
        self.assertEqual(encrypt('0123456789012345'), '0482 1593 2604 3715')

    def test2_decrypt(self):
        self.assertEqual(decrypt('0482 1593 2604 3715'), '0123456789012345')
