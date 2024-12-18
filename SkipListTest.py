from SkipList import SkipList
import unittest
from random import randint



class TestSkipList(unittest.TestCase):
    def setUp(self):
        self.skiplist = SkipList(max_levels=4)
        for i in range(0, 200, 5):
            self.skiplist.insert(i)


    def test_contains(self):
        self.assertTrue(self.skiplist.contains(5))
        self.assertTrue(self.skiplist.contains(195))
        self.assertFalse(self.skiplist.contains(200))
        self.assertFalse(self.skiplist.contains(98))
        self.assertTrue(self.skiplist.contains(0))

    def test_insert(self):
        self.assertTrue(self.skiplist.insert(1))
        self.assertTrue(self.skiplist.contains(1))
        self.assertTrue(self.skiplist.insert(-1))
        self.assertTrue(self.skiplist.contains(-1))
        self.assertTrue(self.skiplist.insert(1000000000))
        self.assertTrue(self.skiplist.contains(1000000000))
        self.assertFalse(self.skiplist.insert(1))

    def test_remove(self):
        self.assertTrue(self.skiplist.remove(5))
        self.assertFalse(self.skiplist.contains(5))

        self.assertFalse(self.skiplist.remove(-1))

        self.assertTrue(self.skiplist.remove(0))
        self.assertFalse(self.skiplist.contains(0))

if __name__ == "__main__":
    unittest.main()