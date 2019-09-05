import uiautomator2 as u2

import os
import time

# os.system('adb connect 127.0.0.1:7555')
d = u2.connect()  # connect to device
print(d.info)

while True:
    d.click(0.5*576, 0.88*1024)
    print("ok")
    time.sleep(60)