import unittest
from src.utils import get_system_info
from src.validator import check_age
from src.calculator import add_numbers, calculate_area

class TestHealingAgent(unittest.TestCase):
    def test_syntax(self):
        self.assertTrue(check_age(20))

    def test_logic(self):
        # This will fail because the current logic returns circumference, not area
        import math
        self.assertAlmostEqual(calculate_area(2), 12.566, places=2)

    def test_type(self):
        with self.assertRaises(TypeError):
            add_numbers(5, "10") # Agent should fix this by casting