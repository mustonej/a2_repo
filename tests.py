import unittest
from check_pwd import check_pwd

class TestCheckPwd(unittest.TestCase):
    def test_empty_string_fails(self):
        result = check_pwd("")
        self.assertFalse(result)
    
    def test_short_password_fails(self):
        result = check_pwd("Ab1!")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()