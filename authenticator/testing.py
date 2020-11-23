import unittest
import encrypter
import decrypter

class Test_encrypt_and_decrypt(unittest.TestCase):

    def test_encypt_username(self):
        self.assertEqual(encrypter.encrypt_username("jkokot"), "optpty")
        self.assertEqual(encrypter.encrypt_username("mvan-sch"), "r{fs2xhm")


    def test_encrypt_password(self):
        self.assertEqual(encrypter.encrypt_password("Bubbles1206"), "Gzggqjx675;")
        self.assertEqual(encrypter.encrypt_password("man42069"), "rfs975;>")


    def test_decrypt_username(self):
        self.assertEqual(decrypter.decrypt_username("optpty"),"jkokot")
        self.assertEqual(decrypter.decrypt_username("r{fs2xhm"),"mvan-sch")

    def test_decrypt_password(self):
        self.assertEqual(decrypter.decrypt_password("Gzggqjx675;"),"Bubbles1206")
        self.assertEqual(decrypter.decrypt_password("rfs975;>"),"man42069")

        
if __name__ == "__main__":
   unittest.main()