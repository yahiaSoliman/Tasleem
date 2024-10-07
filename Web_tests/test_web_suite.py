import unittest

from HTMLTestRunner import HTMLTestRunner

from Web_tests.test_web_login import WebLoginTest


suite_1 = unittest.TestSuite()
suite_1.addTest(unittest.TestLoader().loadTestsFromTestCase(WebLoginTest))

if __name__ == '__main__':
    runner = HTMLTestRunner(title='Tasleem WEB Tests', open_in_browser=True)
    runner.run(suite_1)
