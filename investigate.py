from datetime import datetime

import pytz

x = str(datetime.now(pytz.timezone('Asia/Baghdad')).time())[0:8]
print(x)
