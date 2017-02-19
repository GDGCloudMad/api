
import main
import unittest

class MainTest(unittest.TestCase):
    
    def setUp(self):
        self.app = main.app.test_client()

    def test_hello_world(self):
        rv = self.app.get('/get_author/ulysses')
        assert rv.data == 'James Joyce'

if __name__ == '__main__':
    unittest.main()

