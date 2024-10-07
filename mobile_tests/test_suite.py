import unittest

from HTMLTestRunner import HTMLTestRunner

from test_login import LoginTest


suite_1 = unittest.TestSuite()
suite_1.addTest(unittest.TestLoader().loadTestsFromTestCase(LoginTest))

if __name__ == '__main__':
    runner = HTMLTestRunner(title='Tasleem Mobile tests', open_in_browser=True)
    runner.run(suite_1)
