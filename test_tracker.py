import unittest
from datetime import datetime, timedelta
from tracker import week_start, get_csv_as_dict, create_bookings, booking_allowed, save_booking, update_today_booking

class TestMonitorTracker(unittest.TestCase):

    def test_monday_returns_same_monday(self):
        dt = datetime(2025, 4, 14, 10, 0)  # Monday
        result = week_start(dt)
        self.assertEqual(result, datetime(2025, 4, 14).date())

    def test_friday_before_6pm_returns_same_monday(self):
        dt = datetime(2025, 4, 18, 17, 59)  # Friday before 18:00
        result = week_start(dt)
        self.assertEqual(result, datetime(2025, 4, 14).date())

    def test_friday_after_6pm_returns_next_monday(self):
        dt = datetime(2025, 4, 18, 18, 1)  # Friday after 18:00
        result = week_start(dt)
        self.assertEqual(result, datetime(2025, 4, 21).date())

    def test_saturday_returns_previous_monday(self):
        dt = datetime(2025, 4, 19, 12, 0)  # Saturday
        result = week_start(dt)
        self.assertEqual(result, datetime(2025, 4, 14).date())

    def test_sunday_returns_previous_monday(self):
        dt = datetime(2025, 4, 20, 12, 0)  # Sunday
        result = week_start(dt)
        self.assertEqual(result, datetime(2025, 4, 14).date())

if __name__ == '__main__':
    unittest.main()