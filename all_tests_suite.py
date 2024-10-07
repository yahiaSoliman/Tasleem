import unittest

from HTMLTestRunner import HTMLTestRunner

from mobile_tests.test_login import LoginTest
from Api_tests.test_api_login import APILoginTest
from Web_tests.test_web_login import WebLoginTest


suite_1 = unittest.TestSuite()
suite_1.addTest(unittest.TestLoader().loadTestsFromTestCase(LoginTest))
suite_1.addTest(unittest.TestLoader().loadTestsFromTestCase(APILoginTest))
suite_1.addTest(unittest.TestLoader().loadTestsFromTestCase(WebLoginTest))

if __name__ == '__main__':
    runner = HTMLTestRunner(title='Tasleem All test cases', open_in_browser=True)
    runner.run(suite_1)
