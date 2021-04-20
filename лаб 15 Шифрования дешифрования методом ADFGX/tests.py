import unittest
import main


class TestEncrypt(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(main.encrypt('attack at dawn', key='BATTLE'), 'FFFFFFFFGFDDXGDAXDXGGXGX')

    def test_decrypt(self):
        self.assertEqual(main.decrypt('FFFFFFFFGFDDXGDAXDXGGXGX', key='BATTLE'), 'ATTACKATDAWN')

    def test_encrypt1(self):
        self.assertEqual(main.encrypt('Hello world', key='HI'), 'AAXXDGDDXDFGXXGXGAXD')

    def test_decrypt1(self):
        self.assertEqual(main.decrypt('AAXXDGDDXDFGXXGXGAXD', key='HI'), 'HELLOWORLD')
