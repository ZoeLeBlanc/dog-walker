import unittest
from dogwalking import *

class TestDogWalking(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.bob = User("Bob", "Roberts", "po@po.com", "bobbytables")
        self.jane = User("Jane", "Jetson", "jane@jane.com", "janejetson")
        self.pickles = Dog("pickles", "Jack Russell")
        self.scheduler = Scheduler()
        self.registrar = Registrar()

    def test_user_can_register(self):
        self.assertIsInstance(self.bob, User)
        
        register_user(self.bob)
        self.assertTrue(user_is_registered(self.bob))

    def test_user_can_register_dog(self):
        self.bob.register_dog(self.pickles)
        self.assertIn(self.pickles, self.bob.get_dogs())

    def test_user_can_set_available_walking_time(self):
        self.scheduler.add_walk_time(self.pickles, "11:00a", "12:00p")

        self.assertIn({starttime:"11:00a", endtime:"12:00p"} , self.pickles.get_walk_times())

    def test_user_can_select_dog_to_walk(self):
        register_user(self.jane)
        available_times = self.pickles.get_walk_times()
        # [ (1, "11:00a", "12:00p", 1), (2, "4:00p", "6:00p", 1) ]

        self.scheduler.(self.jane, available_times[0])














