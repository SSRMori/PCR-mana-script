import os
import cv2
from gameOp import *
from image import *
from account import *
import psutil

android_home = os.getcwd() + "\\..\\"
os.environ['ANDROID_HOME'] = android_home


if __name__ == "__main__":
    accountList = getAccounts()
    os.system(".\\..\\platform-tools\\adb.exe kill-server")
    for account in accountList[:7]:
        g = game()
        g.login(account)
        g.taskbonus()
        g.mop(10)
        g.reconnect()
        g.Dungeon()
        g.taskbonus()
        g.gift()
        # print("Waiting")
        # input()
        g.backToTitle()
        del g
        os.system(".\\..\\platform-tools\\adb.exe kill-server")
        time.sleep(10)
        

