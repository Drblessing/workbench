def personalized_greeting(name, hour):
    if not (0 <= hour <= 23):
        raise ValueError("Hour must be in 0-23 range")
    if 5 <= hour < 12:
        return f"Good morning, {name}!"
    elif 12 <= hour < 18:
        return f"Good afternoon, {name}!"
    else:
        return f"Good evening, {name}!"


import unittest


class TestPersonalizedGreeting(unittest.TestCase):
    def test_morning_greeting(self):
        self.assertEqual(personalized_greeting("Daniel", 9), "Good morning, Daniel!")

    def test_afternoon_greeting(self):
        self.assertEqual(personalized_greeting("Daniel", 13), "Good afternoon, Daniel!")

    def test_evening_greeting(self):
        self.assertEqual(personalized_greeting("Daniel", 19), "Good evening, Daniel!")

    def test_invalid_hour_low(self):
        with self.assertRaises(ValueError):
            personalized_greeting("Daniel", -1)

    def test_invalid_hour_high(self):
        with self.assertRaises(ValueError):
            personalized_greeting("Daniel", 24)


if __name__ == "__main__":
    unittest.main()
