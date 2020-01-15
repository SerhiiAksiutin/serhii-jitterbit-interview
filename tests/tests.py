import unittest
import pdb

from selenium import webdriver


class SleneumTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        # pdb.set_trace()
        self.addCleanup(self.driver.quit)

if __name__ == '__main__':
    unittest.main(verbosity=2)
