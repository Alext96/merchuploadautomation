import pyautogui

whatToDo = input("upload(u) or color(c) or saveshirts(s)")


# loop
def upload():
    for x in range(50):
        # pressUploadButton
        pyautogui.click(794, 1272, interval=1)
        # leftClickLatestPicture
        pyautogui.click(406, 254, interval=1)
        # deletePic
        pyautogui.press('delete', interval=1)
        pyautogui.click(406, 254, interval=1)
        # pressEnter
        pyautogui.press('enter', interval=15)
        # leftClickLatestPicture();
        # pyautogui.click(406, 254, interval=2)
        # pressopen
        # pyautogui.click(900, 785, interval=2)
        # clickNextTab();
        pyautogui.hotkey("ctrl", "tab", interval=0.5)
        x += 1
    else:
        print("done")


def saveshirts():
    for x in range(50):
        pyautogui.click(1466, 1368, interval=0.5)
        pyautogui.hotkey("ctrl", "tab", interval=0.5)
        x += 1
    else:
        print("done")


def color():
    for x in range(50):
        pyautogui.click(1819, 720, interval=0.5)
        pyautogui.click(1893, 717, interval=0.5)
        pyautogui.click(1973, 717, interval=0.5)
        pyautogui.click(2062, 703, interval=0.5)
        pyautogui.click(2139, 717, interval=0.5)
        pyautogui.click(2541, 1306, interval=0.5)
        pyautogui.click(1495, 863, interval=0.5)
        pyautogui.hotkey("ctrl", "tab", interval=0.5)
        x += 1
    else:
        print("done")


if whatToDo == "u":
    upload()

if whatToDo == "c":
    color()

if whatToDo == "s":
    saveshirts()
