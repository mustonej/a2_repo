import unittest
from check_pwd import check_pwd

class TestCheckPwd(unittest.TestCase):
    def test_empty_string_fails(self):
        result = check_pwd("")
        self.assertFalse(result)
    
    def test_short_password_fails(self):
        result = check_pwd("Ab1!")
        self.assertFalse(result)
    
    def test_long_password_passes(self):
        result = check_pwd("Passwordthatistoolong1234566")
        self.assertFalse(result)
    
    def test_no_lowercase_fails(self):
        result = check_pwd("KLEA7495!")
        self.assertFalse(result)

    def test_no_uppercase_fails(self):
        result = check_pwd("klea7495!")
        self.assertFalse(result)

    def test_no_digit_fails(self):
        result = check_pwd("KLEAsdflkhdf!")
        self.assertFalse(result)

    def test_no_symbol_fails(self):
        result = check_pwd("KLEA7495")
        self.assertFalse(result)

    def test_wrong_symbol_fails(self):
        result = check_pwd("KLEA7495{}")
        self.assertFalse(result)
    
    def test_valid_password_passes(self):
        result = check_pwd("KLEa7495!")
        self.assertTrue(result)

    def test_8_character_passes(self):
        result = check_pwd("KLEa7495")
        self.assertTrue(result)
    
    def test_20_character_passes(self):
        result = check_pwd("KLEa7495!KLEa7495!KL")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()