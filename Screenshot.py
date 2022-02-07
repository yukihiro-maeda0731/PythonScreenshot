import pyautogui as pag
from time import sleep

import matplotlib.pyplot as plt
import numpy as np
import tenserflow as tf
import tenserflow_datasets as tfds
from tenserflow import keras

builder = tfds.builder('rock_paper_scissors')
info = builder.info
ds_train = tfds.load(name="rock_paper_scissors", split="train")
ds_test = tfds.load(name="rock_paper_scissors", split="test")

fig = tfds.show_examples(info, ds_train)

# スクリーンショットの処理
# i = 1
# savepath = 'D:\portfolio\PythonScreenshot'

# try:
#     while True:
#         img = pag.screenshot(savepath + '/screenshot' + str(i) + '.png')
#         sleep(10)
#         i = i + 1
# except KeyboardInterrupt:
#     print('\n')