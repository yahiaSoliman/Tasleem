import string
import random
import time
from datetime import datetime, timedelta


class DataSets:

    driver_username = "aromaniiBE5"
    driver_password = "P@ssword12"

    @staticmethod
    def from_date():
        last_week_data = datetime.now() - timedelta(days=30)
        result = last_week_data.replace(microsecond=0).isoformat()
        return result


    @staticmethod
    def to_date():
        result = datetime.now().replace(microsecond=0).isoformat()
        return result

    """
    generate random name to use for updating account information
    """

    @staticmethod
    def generate_random_name():
        result = ''.join(random.choices(string.ascii_lowercase +
                                        string.digits, k=7))
        return result

    """
    generate random email to use for updating account information
    """

    @staticmethod
    def generate_random_email():
        result = ''.join(random.choices(string.ascii_lowercase +
                                        string.digits, k=7))
        return result + "@mail.com"

    """
    generate random phone number
    """

    @staticmethod
    def generate_random_phone_number():
        x = str(time.time())
        y = x[-5:]
        return "78973" + y
