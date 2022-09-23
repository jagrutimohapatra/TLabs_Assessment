import unittest
import main
class TestMain(unittest.TestCase):
  def test_main(self):
    grid = [[2, 1, 0, 2, 1, 2],
            [1, 1, 1, 1, 1, 1],
            [1, 0, 1, 2, 1, 1]]
    result = main.minTime(grid)
    self.assertEqual(result,'2')

    grid1 = [[2,1,0,2,1],[0,0,1,2,1],[1,0,0,2,1]]
    result1 = main.minTime(grid1)
    self.assertEqual(result1,'-1')

    grid2 = [[2,1,0,2,1],[1,1,1,1,1],[0,1,0,2,1]]
    result2 = main.minTime(grid2)
    self.assertEqual(result2,'3')

if __name__ == '__main__':
  unittest.main()