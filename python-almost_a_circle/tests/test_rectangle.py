import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rect = Rectangle(5, 10, 15, 20, 25)
        self.test_cases = [
            {"params": (1, 2), "expected": (1, 2, 0, 0)},
            {"params": (1, 2, 3), "expected": (1, 2, 3, 0)},
            {"params": (1, 2, 3, 4), "expected": (1, 2, 3, 4)},
        ]

    def test_attributes(self):
        self.assertEqual(self.rect.width, 5)
        self.assertEqual(self.rect.height, 10)
        self.assertEqual(self.rect.x, 15)
        self.assertEqual(self.rect.y, 20)
        self.assertEqual(self.rect.id, 25)

    def test_area(self):
        self.assertEqual(self.rect.area(), 50)

    def test_to_dictionary(self):
        expected = {"x": 15, "y": 20, "id": 25, "height": 10, "width": 5}
        self.assertEqual(self.rect.to_dictionary(), expected)

    def test_update(self):
        self.rect.update(30, 35, 40, 45, 50)
        self.assertEqual(self.rect.width, 35)
        self.assertEqual(self.rect.height, 40)
        self.assertEqual(self.rect.x, 45)
        self.assertEqual(self.rect.y, 50)
        self.assertEqual(self.rect.id, 30)

    def test_invalid_width(self):
        with self.assertRaises(TypeError):
            self.rect.width = "invalid"

    def test_invalid_height(self):
        with self.assertRaises(TypeError):
            self.rect.height = "invalid"

    def test_invalid_x(self):
        with self.assertRaises(TypeError):
            self.rect.x = "invalid"

    def test_invalid_y(self):
        with self.assertRaises(TypeError):
            self.rect.y = "invalid"

    def test_rectangle_initialization(self):
        for test_case in self.test_cases:
            rect = Rectangle(*test_case["params"])
            self.assertEqual((rect.width, rect.height, rect.x, rect.y), test_case["expected"])

    def test_invalid_initialization(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(-1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)


if __name__ == '__main__':
    unittest.main()
