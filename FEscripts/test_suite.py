import unittest
from FEscripts.create_order import TestCreateOrder
from FEscripts.update_store_settings import TestStoreSettings

suite_1 = unittest.TestSuite()
suite_1.addTest(unittest.TestLoader().loadTestsFromTestCase(TestCreateOrder))
suite_1.addTest(unittest.TestLoader().loadTestsFromTestCase(TestStoreSettings))

if __name__ == '__main__':
    runner = unittest.TextTestRunner()

    runner.run(suite_1)
    print("end of suite_1")
