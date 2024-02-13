import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rect = Rectangle(5, 10, 15, 20, 25) 

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

        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_invalid_height(self):
        with self.assertRaises(TypeError):
            self.rect.height = "invalid"

    def test_invalid_x(self):
        with self.assertRaises(TypeError):
            self.rect.x = "invalid"

    def test_invalid_y(self):
        with self.assertRaises(TypeError):
            self.rect.y = "invalid"


if __name__ == '__main__':
    unittest.main()