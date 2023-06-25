import pyautogui
import cv2
import pyperclip
import time
import os

def intoWx():
    pyautogui.hotkey("win","d")
    if(os.path.exists('./desktop.png') == False):
        desktopimg = pyautogui.screenshot()
        desktopimg.save('./desktop.png')
    wxLogo = cv2.imread('./wxLogo.png')
    desktop = cv2.imread('./desktop.png')
    result = cv2.matchTemplate(wxLogo, desktop, cv2.TM_CCOEFF_NORMED)
    position = cv2.minMaxLoc(result)[3]
    x = position[0] + (wxLogo.shape[1] / 2)
    y = position[1] + (wxLogo.shape[0] / 2)
    pyautogui.doubleClick(x,y)

def clickSearch():
    if (os.path.exists('./wxScreen.png.png') == False):
        wxScreen = pyautogui.screenshot()
        wxScreen.save('./wxScreen.png')
    wxScreenImg = cv2.imread('./wxScreen.png')
    searchImg = cv2.imread('./search.png')
    result = cv2.matchTemplate(wxScreenImg, searchImg, cv2.TM_CCOEFF_NORMED)
    position = cv2.minMaxLoc(result)[3]
    x = position[0] + (searchImg.shape[1] / 2)
    y = position[1] + (searchImg.shape[0] / 2)
    pyautogui.click(x, y)

def searchFriend(name):
    pyperclip.copy(name)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)
    pyautogui.hotkey('enter')

def sendMessage(message):
    pyperclip.copy(message)
    pyautogui.hotkey('ctrl','v')
    time.sleep(0.5)
    pyautogui.hotkey('enter')

def clearImg():
    os.remove('./desktop.png')
    os.remove('./wxScreen.png')

if __name__ == '__main__':
    name = ""
    message = ""

    intoWx()
    clickSearch()
    searchFriend(name)
    sendMessage(message)
    # clearImg()
