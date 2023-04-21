from  unittest import TestCase

from lockers import Queue

class TestSharedLocker(TestCase):
    def setUp(self) -> None:
        self.qlock1 = Queue()
        self.qlock2 = Queue()

    def test_1(self):
        """
        qlock1 is will locker
        
        qlock1 will unlock
        """
        self.assertEqual(self.qlock1.lock(), True)
        self.assertEqual(self.qlock1.unlock(), True)
        

    def test_2(self):
        """
        qlock1 is will locker
        
        qlock2 will try to unlock
        """

        # locked here
        self.assertEqual(self.qlock1.lock(), True)
        
        self.assertEqual(self.qlock2.unlock(), False)

        # unlocked here
        self.assertEqual(self.qlock1.unlock(), True)
        
    def test_3(self):
        """
        qlock1 will lock, then qlock1 will again try to lock it.
        finally qlock1 will unlock it.
        """
        self.assertEqual(self.qlock1.lock(), True)
        self.assertEqual(self.qlock1.lock(), False)
        self.assertEqual(self.qlock1.unlock(), True)
        self.assertEqual(self.qlock1.unlock(), False)