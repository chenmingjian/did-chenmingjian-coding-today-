import os
import numpy as np

ROOT_DIR = R"C:\Users\chen\Desktop\qt_project\build-landmark_i"
+"mprove_gui-Desktop_Qt_5_12_0_MSVC2017_64bit-Release\img_to_im"
+"prove\maybe_label"
SAVE_DIR = R"C:\Users\chen\Desktop\output"
ROOT_DIR, SAVE_DIR = SAVE_DIR, ROOT_DIR
for root, dirs, files in os.walk(ROOT_DIR):
    for f in files:
        path = os.path.join(root, f)

        location = np.loadtxt(path, delimiter=",")
        location = location[0:37]

        save_path = os.path.join(SAVE_DIR, f)
        np.savetxt(path, location, fmt="%d", delimiter=",", )
