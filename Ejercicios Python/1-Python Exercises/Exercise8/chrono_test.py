import unittest
import time
import chrono


class TestUM(unittest.TestCase):
    """Unit tests of exercise 8, chronometer"""

    def setUp(self):
        print("Executing test of exercise 8: chronometer")

    def test_chrono_start(self):
        """Init a chronometer and test the initial configuration"""
        c = chrono.ChronometerStarted()
        # The current time is stored as the chronometer's start time
        self.assertAlmostEqual(c._start, time.time(), 2)
        self.assertIs(c._stop, 0)

    def test_chrono_stop(self):
        """Stop an initiated chronometer and check its status"""
        c = chrono.ChronometerStarted()
        c.stop()
        # The stop time is stored as the chronometer's stop time
        self.assertAlmostEqual(c._stop, time.time(), 2)

    def test_chrono(self):
        """Test a chronometer running being stopped and initiated several times"""

        timer = chrono.ChronometerStarted()
        self.assertAlmostEqual(timer._start, time.time(), 2)
        time.sleep(1)
        self.assertAlmostEqual(timer.time(), 1, 2)
        time.sleep(2)
        timer.stop()
        time.sleep(1)
        timer.stop()
        timer.start()
        time.sleep(2)
        self.assertAlmostEqual(timer.time(), 2, 2)


if __name__ == "__main__":
    unittest.main()
