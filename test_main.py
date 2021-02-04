import unittest
import main


class TestCase(unittest.TestCase):
  
  def test_add(self):
    self.assertEqual(main.add(2,3), 5)
    self.assertEqual(main.add(2,0), 2)



  def test_subtract(self):
    self.assertEqual(main.subtract(10,2), 8)
    self.assertEqual(main.subtract(0,2), -2)


  def test_divide(self):
    self.assertEqual(main.divide(10,2),5)
    self.assertEqual(main.divide(10,0),0)

  def test_multiply(self):
    self.assertEqual(main.multiply(2,3),6)
    self.assertEqual(main.multiply(2,0),0)

if __name__ == '__main__':
  unittest.main(verbosity=2)