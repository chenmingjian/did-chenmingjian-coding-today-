import uiautomator2 as u2
import time
import os
os.system('adb connect 127.0.0.1:7555')
d = u2.connect() 

while True:
    d.click(926, 1760)
    print("click1")
    time.sleep(2)

    d.click(926, 1314)
    print("click2")
    time.sleep(13)

    d.press("back")
    print("back")
    time.sleep(2)
