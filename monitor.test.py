import unittest
from monitor import vitals_ok

class TestVitalsOk(unittest.TestCase):
    def test_temperature_high(self):
        self.assertFalse(vitals_ok(103, 80, 95))

    def test_temperature_low(self):
        self.assertFalse(vitals_ok(94, 80, 95))

    def test_pulse_low(self):
        self.assertFalse(vitals_ok(98, 59, 95))

    def test_pulse_high(self):
        self.assertFalse(vitals_ok(98, 101, 95))

    def test_spo2_low(self):
        self.assertFalse(vitals_ok(98, 80, 89))

    def test_all_ok(self):
        self.assertTrue(vitals_ok(98, 80, 95))

if __name__ == '__main__':
    unittest.main()