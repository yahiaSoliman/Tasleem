import os

from appium.options.common import AppiumOptions


class Setup:
    # capabilities
    real_device_options = AppiumOptions()
    real_device_options.page_load_strategy = 'normal'
    real_device_options.platform_name = 'android'
    real_device_options.set_capability('appPackage', 'com.creativeadvtech.taza')
    real_device_options.set_capability('appActivity', 'com.creativeadvtech.taza.MainActivity')
    real_device_options.set_capability('deviceName', 'android')
    real_device_options.set_capability('platformName', 'android')
    real_device_options.set_capability('platformVersion', '12.0')
    real_device_options.set_capability('udid', 'R58RC0EZ4XH')
    real_device_options.set_capability('gpsLocation', '33.3118864,44.36437876755285')
    real_device_options.set_capability("autoGrantPermissions", "true")

    android_options = AppiumOptions()
    android_options.page_load_strategy = 'normal'
    android_options.platform_name = 'android'
    android_options.set_capability('app', os.environ["appurl"])  # 954
    android_options.set_capability('deviceName', 'Samsung Galaxy S22')
    android_options.set_capability('platformVersion', '12.0')
    android_options.set_capability('browserstack.appium_version', '2.0.1')  # latest accepted version by BS
    android_options.set_capability('gpsLocation', '33.3118864,44.36437876755285')

    ios_options = AppiumOptions()
    ios_options.page_load_strategy = 'normal'
    ios_options.platform_name = 'ios'
    ios_options.set_capability('app', 'bs://7ca543e98a237aef0631ad8432aff2efa94bcda3')  # 846
    ios_options.set_capability('deviceName', 'iPhone 13')
    ios_options.set_capability('platformVersion', '15')
    ios_options.set_capability('gpsLocation', '33.3118864,44.36437876755285')

    # urls
    local_url = "http://localhost:4723/wd/hub"
    keys = 'ysoliman_nx7XHD:PznNxwdkfBqNiygZ3jvR'
    browserstack_url = f'https://{keys}@hub-cloud.browserstack.com/wd/hub'
    REMOTE_URL_TUPLE = (browserstack_url, android_options)
