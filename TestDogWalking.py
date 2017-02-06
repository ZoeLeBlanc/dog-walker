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
        
        self.registrar.register_user(self.bob)
        self.assertTrue(self.registrar.user_is_registered(self.bob))

    def test_user_can_register_dog(self):
        self.registrar.register_dog(self.bob, self.pickles)
        self.assertIn(self.pickles, self.bob.get_dogs())

    def test_user_can_set_available_walking_time(self):
        self.scheduler.add_walk_time(self.pickles, "11:00a", "12:00p")

        available_times = self.pickles.get_walk_times()
        time_was_recorded = False

        for time in available_times:
            if time[1] == "11:00a" and time[2] == "12:00p":
                time_was_recorded = True

        self.assertTrue(time_was_recorded)

    def test_user_can_select_dog_to_walk(self):
        self.registrar.register_user(self.jane)
        available_times = self.pickles.get_walk_times()
        # [ (1, "11:00a", "12:00p", 1), (2, "4:00p", "6:00p", 1) ]

        self.scheduler.schedule_walk(self.jane, available_times[0][0])
        schedules = self.scheduler.get_user_schedule(self.jane)
        #    pk, user_id, time_id
        # [ (1,  2,       1) ]

        walk_is_scheduled = False
        for time in schedules:
            if time[2] == available_times[0][0]:
                walk_is_scheduled = True

        self.assertTrue(walk_is_scheduled)













