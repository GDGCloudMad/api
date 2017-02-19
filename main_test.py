
import main
import unittest

class MainTest(unittest.TestCase):
    
    def setUp(self):
        self.app = main.app.test_client()

    def test_hello_world(self):
        rv = self.app.get('/')
        assert rv.data == 'Hello world!'

if __name__ == '__main__':
    unittest.main()

