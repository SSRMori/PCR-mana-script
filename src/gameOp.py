from image import *
import uiautomator as ua
import time
import psutil
import os

class game(object):
    d = None
    connected = False

    def __init__(self):
        self.d = ua.device
        print("Device connected")
        self.connected = True
        print(self.d.info)

    def cpuMonitor(self):
        percent = psutil.cpu_percent()
        time.sleep(0.1)
        percent += psutil.cpu_percent()
        time.sleep(0.1)
        percent += psutil.cpu_percent()
        time.sleep(0.1)
        percent += psutil.cpu_percent()
        percent /= 4
        print("CPU usage is " + str(percent))
        while percent > 80:
            print("CPU usage TOO HIGH. waiting")
            self.reconnect()
            # os.system(".\\..\\platform-tools\\adb.exe kill-server")
            # self.connected = False
            # self.d = None
            # time.sleep(30)
            # self.__init__()
            time.sleep(10)
            percent = psutil.cpu_percent()
            time.sleep(0.1)
            percent += psutil.cpu_percent()
            time.sleep(0.1)
            percent += psutil.cpu_percent()
            time.sleep(0.1)
            percent += psutil.cpu_percent()
            percent /= 4
            print("CPU usage is " + str(percent))
        print("Connected")
    
    def reconnect(self):
        print("Reconnecting")
        os.system(".\\..\\platform-tools\\adb.exe kill-server")
        self.connected = False
        self.d = None
        time.sleep(30)
        self.__init__()
        self.d.screenshot("screenshot.png")

    def enter(self, name):
        self.cpuMonitor()
        template = templateLoad(name + ".png")
        photo_name = "screenshot.png"#"[" + time.strftime("%H-%M-%S", time.localtime()) + "]screenshot.png" 
        self.d.screenshot(photo_name)
        src = imLoad(photo_name)
        x, y = match(src, template)
        self.d.click(x, y)
        time.sleep(2)
    
    def click(self, name):
        self.cpuMonitor()
        time.sleep(2)
        template = templateLoad(name + ".png")
        photo_name = "screenshot.png"#"[" + time.strftime("%H-%M-%S", time.localtime()) + "]screenshot.png" 
        # print(photo_name)
        self.d.screenshot(photo_name)
        src = imLoad(photo_name)
        x, y = match(src, template)
        self.d.click(x, y)
    
    def getLoc(self, name):
        time.sleep(0.5)
        template = templateLoad(name + ".png")
        self.d.screenshot("screenshot.png")
        src = imLoad("screenshot.png")
        x, y = match(src, template)
        return x, y
    
    def clickLoc(self, x, y):
        self.cpuMonitor()
        time.sleep(0.5)
        self.d.click(x, y)

    def mop(self, times):
        print("Start mop")
        self.enter("advanture")
        print("\tEnter advanture")
        self.enter("main")
        print("\tEnter main story")
        self.click("mission")
        print("\tEnter default mission")
        print("\tSetting mop tickets")
        for _ in range(times-1):
            self.click("mopTicketPlus")
        print("\tMop tickets set")
        self.click("mopStart")
        print("\tStart mop")
        self.click("blueOK")
        time.sleep(times*2+ 4)
        self.click("whiteOK")
        print("\tMop finished")
        self.click("whiteOK")
        self.click("cancel")
        self.click("cancel")
        self.enter("mainPage")
        print("\tBack to main page")
        time.sleep(5)
        print("Mop finished")

    def taskbonus(self):
        print("Start get task bonus")
        self.enter("task")
        print("\tEnter task page")
        self.click("getAll")
        print("\tGet bonus")
        self.click("textClose")
        print("\tBack to main page")
        self.enter("mainPage")
        print("Get task bonus finished")

    def finderExp(self):
        print("Start complete finder exp mission")
        self.enter("advanture")
        print("\tEnter advanture")
        self.enter("finder")
        print("\tEnter finder")
        self.enter("exp")
        print("\tSelect exp mission")

        #self.enter("exp5")
        self.d.click(900, 250)
        # self.d.click(950, 350)

        print("\tSelect mission")
        self.click("mopTicketPlus")
        print("\tMop tickets set")
        self.click("mopStart")
        print("\tStart mop")
        self.click("blueOK")
        time.sleep(8)
        print("\tMop finished")
        self.click("finderCancel")
        self.enter("mainPage")
        print("\tBack to main page")
        print("Finder finished")

    def finderMana(self):
        print("Start complete finder exp mission")
        self.enter("advanture")
        print("\tEnter advanture")
        self.enter("finder")
        print("\tEnter finder")
        self.enter("mana")
        print("\tSelect mana mission")

        #self.enter("exp5")
        self.d.click(900, 250)
        # self.d.click(950, 350)

        print("\tSelect mission")
        self.click("mopTicketPlus")
        print("\tMop tickets set")
        self.click("mopStart")
        print("\tStart mop")
        self.click("blueOK")
        time.sleep(8)
        print("\tMop finished")
        self.click("finderCancel")
        self.enter("mainPage")
        print("\tBack to main page")
        print("Finder finished")

    def Dungeon(self):
        print("Start dungeon")
        self.enter("advanture")
        print("\tEnter advanture")
        self.enter("dungeon")
        print("\tEnter dungeon")
        self.enter("dungeon1")
        print("\tEnter dungeon 1")
        self.click("blueOK")
        time.sleep(5)
        self.click("dungeonLevel1")
        print("\tSelect dungeon level 1")
        self.click("challenge")
        
        time.sleep(5)
        # self.clickLoc(150, 220)
        time.sleep(2)
        self.clickLoc(635, 120)
        print("\tSelect support")
        time.sleep(2)
        self.clickLoc(150, 220)

        self.click("battleStart")
        print("\tStartBattle")
        self.click("blueOK")

        time.sleep(20)

        # self.click("battleMenu")
        self.clickLoc(1206, 33)
        self.click("battleWhiteGiveup")
        self.click("battleBlueGiveup")
        print("\tGive up battle")
        # time.sleep(30)
        # self.click("backToDungeon")
        print("\tBack to dungeon")
        time.sleep(2)
        self.click("exitDungeon")
        self.click("blueOK")
        time.sleep(2)
        self.enter("mainPage")
        print("\tBack to main page")
        print("Dungeon finished")

    def backToTitle(self):
        print("Start back to title")
        self.enter("menu")
        print("\tEnter menu page")
        self.click("backToTitle")
        self.click("blueOK")
        time.sleep(20)
        print("Back to title")
    
    def login(self, account):
        self.cpuMonitor()
        print("Start login in")
        # input()
        self.d.click(100, 100)
        self.d.wait.update()
        time.sleep(1)
        self.d(text="切换账号").click()
        print("\tSwitching account")
        time.sleep(0.5)
        self.d(text="切换账号").click()
        self.d(resourceId="com.bilibili.priconne:id/bsgamesdk_edit_username_login").set_text(account["name"])
        self.d(resourceId="com.bilibili.priconne:id/bsgamesdk_edit_password_login").set_text(account["password"])
        self.d(text="登 录").click()
        # time.sleep(5)
        # self.d.click(100, 100)
        time.sleep(15)
        self.click("skip")
        time.sleep(5)
        self.click("close")
        print("Account {} login in finished".format(account["name"]))

    def gift(self):
        print("Start get gift")
        self.click("gift")
        print("\tEnter gift page")
        self.click("getAll")
        print("\tGet gift")
        self.click("blueOK")
        self.click("whiteOK")
        self.click("cancel")
        print("\tBack to main page")
        print("Get gift finished")
