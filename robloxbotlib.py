def join_game(gameid,userdatadir,profile="Default"):
    
    from selenium import webdriver
    from selenium.webdriver import ActionChains
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.chrome.options import Options
    import time
    import os
    os.system("taskkill /f /im chrome.exe")
    os.system("taskkill /f /im RobloxPlayerBeta.exe")
    time.sleep(3)
    options = Options()
    options.add_argument(f"--user-data-dir={userdatadir}")
    options.add_argument(f"--profile-directory={profile}")
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()
    driver.get(f"https://www.roblox.com/games/{gameid}")
    
    
    driver.refresh()
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-common-play-game-lg.btn-primary-md.btn-full-width"))
    )

    # Click the button
    button.click()
    time.sleep(20)
    ##import win32gui
    #import win32con

    #hwnd = win32gui.GetForegroundWindow()
    #win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
    driver.close

def reset_player(waittime=5):
    import pyautogui
    import pydirectinput 
    import time
    pydirectinput.press('esc')
    time.sleep(2)
    pydirectinput.press('r')
    time.sleep(1)
    pydirectinput.press('enter')
    time.sleep(waittime)

def move_player(input,hold=1):
    import pyautogui
    import pydirectinput
    import time
    pydirectinput.keyDown(input)
    time.sleep(hold)
    pydirectinput.keyUp(input)

def leave_game():
    import pyautogui
    import pydirectinput
    import time
    import winsound
    import os
    pydirectinput.press('esc')
    time.sleep(2)
    pydirectinput.press('l')
    time.sleep(1)
    pydirectinput.press('enter')
    time.sleep(2)
    os.system("taskkill /f /im RobloxPlayerBeta.exe")
    winsound.Beep(frequency=300,duration=2000)

def player_chat(msg):
    import pyautogui
    import pydirectinput
    import time
    import winsound
    import os
    pydirectinput.press('/')
    time.sleep(2)
    pyautogui.write(msg)
    time.sleep(2)
    pydirectinput.press('enter')

def move_mouse_center():
    import pyautogui
    import pydirectinput
    # Get screen dimensions
    screen_width, screen_height = pyautogui.size()

    # Calculate center coordinates
    center_x = screen_width // 2
    center_y = screen_height // 2

    # Move the mouse to the center
    pyautogui.moveTo(center_x, center_y, duration=1.00)  # Optional duration for smooth movement

    print(f"Mouse moved to the center: ({center_x}, {center_y})")
    xedit = center_x - 1
    yedit = center_y - 1
    pydirectinput.moveTo(xedit,yedit)
    pydirectinput.click()

def check_game_state(state='Disconnected'):
    import pytesseract
    from pytesseract import Output
    import cv2
    import pyautogui
    import time
    text_to_find = state
    found = False
    screenshot_file = "screenshot.png"
    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    pyautogui.screenshot(screenshot_file)
    screenshot = cv2.imread(screenshot_file)
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    data = pytesseract.image_to_data(gray, output_type=Output.DICT, config='--psm 6')
    print(data)
    n_boxes = len(data['level'])
    for i in range(n_boxes):
        if data['text'][i].strip() == text_to_find:
            (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
            center_x = x + w // 2
            center_y = y + h // 2
            print(center_x,center_y)
            found = True
            break
    if found == True:
        return True
    else:
        return False
        