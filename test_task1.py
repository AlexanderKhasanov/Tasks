import unittest
from task1 import delete_copy

class TestDelCopy(unittest.TestCase):
    def setUp(self):
        self.delete = delete_copy

    def test_1(self):
        self.assertCountEqual( self.delete([1,2,3,4,5]), [1,2,3,4,5] )

    def test_2(self):
        self.assertCountEqual( self.delete([1,1,1,1,1]), [1] )

    def test_3(self):
        self.assertCountEqual( self.delete([]), [] )

    def test_4(self):
        self.assertCountEqual( self.delete([1,1,2,2,3,3,4,4,5,5]), [1,2,3,4,5] )

    def test_5(self):
        self.assertCountEqual( self.delete([1,2,3,4,5,1,2,3,4,5]), [1,2,3,4,5] )

    def test_6(self):
        self.assertCountEqual( self.delete([4,3,1,2,5,2,3,3,1,3]), [4, 3, 1, 2, 5] )

    def test_7(self):
        self.assertCountEqual( self.delete([4,3,1,2,5,2,3,3,1,3]), [4, 3, 1, 2, 5] )

if __name__ == "__main__":
    unittest.main()
