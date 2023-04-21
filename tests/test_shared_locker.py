from  unittest import TestCase

from lockers import Shared

class TestSharedLocker(TestCase):
    def setUp(self) -> None:
        self.lock1 = Shared()
        self.lock2 = Shared()

    def test_1(self):
        """
        lock1 is will locker
        
        lock2 will unlock
        """
        self.assertEqual(self.lock1.lock(), True)
        self.assertEqual(self.lock2.unlock(), True)