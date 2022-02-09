import pyautogui as pag
from time import sleep
import smtplib, ssl
import os
from email.mime.application import MIMEApplication
import requests

# 画像認識の処理
# import matplotlib.pyplot as plt
# import numpy as np
# import tenserflow as tf
# import tenserflow_datasets as tfds
# from tenserflow import keras

# builder = tfds.builder('rock_paper_scissors')
# info = builder.info
# ds_train = tfds.load(name="rock_paper_scissors", split="train")
# ds_test = tfds.load(name="rock_paper_scissors", split="test")
# fig = tfds.show_examples(info, ds_train)



# メール送信の処理

def read_creds():
    user = passw = ""
    with open("credentials.txt", "r", encoding="utf-8") as f:
        file = f.readlines()
        user = file[0].strip()
        passw = file[1].strip()

    return user, passw

port = 465

sender, password = read_creds()

receiver = sender

message = """\
Subject: スクリーンショットを撮影しました
スクリーンショットを撮影しました
"""

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    # スクリーンショットの処理
    server.login(sender, password)
    i = 1
    savepath = 'D:\portfolio\PythonScreenshot'
    try:
        while True:
            
            img = pag.screenshot(savepath + '/screenshot' + str(i) + '.png')
            sleep(30)
            i = i + 1
            server.sendmail(sender, receiver, message)
            print("スクリーンショットを撮影しました"+ str(i) + '枚目')
    except KeyboardInterrupt:
        print('\n')    
    



