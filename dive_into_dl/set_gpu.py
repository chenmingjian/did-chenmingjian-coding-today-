import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

gpus = tf.config.experimental.list_physical_devices(device_type='GPU')

cpus = tf.config.experimental.list_physical_devices(device_type='CPU')
print(gpus, cpus)
tf.config.experimental.set_visible_devices(devices=[gpus[3]], device_type="GPU")
tf.config.experimental.set_memory_growth(gpus[3], True)