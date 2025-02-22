import pyautogui
import cv2
import numpy as np
import time
import pydirectinput
import os
import configparser
import robloxbotlib
import fumocamlib
import win32gui
import winsound
import subprocess
import pytesseract
from pytesseract import Output
config_file = configparser.ConfigParser()

def find_and_move_to_icon(icon_image_path, confidence=0.8, grayscale=True):
    import pyautogui
    import cv2
    import numpy as np
    import pydirectinput

    try:
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)  # Convert PIL Image to OpenCV BGR format

        
        icon = cv2.imread(icon_image_path)
        if icon is None:
            print(f"Error: Icon image not found at {icon_image_path}")
            return False

        
        if grayscale:
            screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
            icon_gray = cv2.cvtColor(icon, cv2.COLOR_BGR2GRAY)
            screenshot_for_matching = screenshot_gray
            icon_for_matching = icon_gray
        else:
            screenshot_for_matching = screenshot
            icon_for_matching = icon


        
        result = cv2.matchTemplate(screenshot_for_matching, icon_for_matching, cv2.TM_CCOEFF_NORMED)

        
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        
        if max_val >= confidence:
            top_left = max_loc
            bottom_right = (top_left[0] + icon.shape[1], top_left[1] + icon.shape[0])
            center_x = (top_left[0] + bottom_right[0]) // 2
            center_y = (top_left[1] + bottom_right[1]) // 2

            # 7. Move the mouse to the center of the icon
            pydirectinput.moveTo(center_x, center_y, duration=1.25) # Smooth movement
            print(f"Icon found and mouse moved to {center_x}, {center_y}")
            return True
        else:
            print(f"Icon not found. Best match confidence: {max_val}")
            return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def find_icon(icon_image_path, confidence=0.8, grayscale=True):
    import pyautogui
    import cv2
    import numpy as np

    try:
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)  # Convert PIL Image to OpenCV BGR format

        
        icon = cv2.imread(icon_image_path)
        if icon is None:
            print(f"Error: Icon image not found at {icon_image_path}")
            return False

        
        if grayscale:
            screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
            icon_gray = cv2.cvtColor(icon, cv2.COLOR_BGR2GRAY)
            screenshot_for_matching = screenshot_gray
            icon_for_matching = icon_gray
        else:
            screenshot_for_matching = screenshot
            icon_for_matching = icon


        
        result = cv2.matchTemplate(screenshot_for_matching, icon_for_matching, cv2.TM_CCOEFF_NORMED)

        
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        
        if max_val >= confidence:
            top_left = max_loc
            bottom_right = (top_left[0] + icon.shape[1], top_left[1] + icon.shape[0])
            center_x = (top_left[0] + bottom_right[0]) // 2
            center_y = (top_left[1] + bottom_right[1]) // 2

            print(f"Icon found at {center_x}, {center_y}")
            return True
        else:
            print(f"Icon not found. Best match confidence: {max_val}")
            return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    print("1")
    winsound.Beep(frequency=475,duration=1000)
    winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
    winsound.MessageBeep()
    winsound.MessageBeep()
    joinloop = 0
    username = subprocess.getoutput("echo %username%")
    while(joinloop < 1):
        winsound.Beep(frequency=475,duration=900)
        robloxbotlib.join_game(6238705697,f"C:/Users/{username}/AppData/Local/Google/Chrome/User Data")
        time.sleep(4)
        process_name = "RobloxPlayerBeta.exe"
        
        window_title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        if window_title == 'Roblox':
            winsound.Beep(frequency=600,duration=900)
            joinloop = 1
        else:
            winsound.Beep(frequency=200,duration=1000)
    try:
        # Get screen dimensions
        screen_width, screen_height = pyautogui.size()

        # Calculate center coordinates
        center_x = screen_width // 2
        center_y = screen_height // 2

        # Move the mouse to the center
        pyautogui.moveTo(center_x, center_y, duration=1.00)  # Optional duration for smooth movement

        print(f"Mouse moved to the center: ({center_x}, {center_y})")

    except Exception as e:
        print(f"An error occurred: {e}")
    time.sleep(2)
    pyautogui.leftClick()
    pyautogui.leftClick()
    time.sleep(10)
    if find_icon("resources\\Rules.PNG",0.3,False):
        print("Rules Opened")
        
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)  # Convert PIL Image to OpenCV BGR format
        confidence = 0.3
        
        icon = cv2.imread("resources\\CloseRules.PNG")

        

        screenshot_for_matching = screenshot
        icon_for_matching = icon

        result = cv2.matchTemplate(screenshot_for_matching, icon_for_matching, cv2.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_val >= confidence:
            top_left = max_loc
            bottom_right = (top_left[0] + icon.shape[1], top_left[1] + icon.shape[0])
            center_x = (top_left[0] + bottom_right[0]) // 2
            center_y = (top_left[1] + bottom_right[1]) // 2

        pydirectinput.moveTo(center_x,center_y,duration=1.00)
        xedit = center_x - 1
        yedit = center_y - 1
        pydirectinput.moveTo(xedit,yedit)
        pydirectinput.click()
        fumocamlib.anti_grief()
        fumocamlib.set_to_day()
        fumocamlib.set_fumo("Koishi")
        time.sleep(3)
        #fumocamlib.fumo_button()
        #settokoishiloop = 0
        #max_scrolls = 33
        #scrolls = 0
        #while(settokoishiloop < 1):
            #print(scrolls)
            #if find_and_move_to_icon("koishi.PNG",0.1,False) == True:
                #pydirectinput.click()
            #else:
                #scrolls = scrolls + 1
                #pyautogui.scroll(-200)  # Scroll down (negative value) Adjust 200 as needed
                #time.sleep(1)
            #if scrolls == max_scrolls:
                #scrolls = 0
                #for _ in range(max_scrolls):
                    #pyautogui.scroll(200)

                
        configChk = os.path.isfile("Config.ini")
        if configChk == False:
            print("No Config.ini File detected Creating File")
            msg = "Hello World"
            config_file.add_section("Hello")
            config_file.set("Hello", "test", f"{msg}")
            with open(r"Config.ini", 'w') as configfileObj:
                config_file.write(configfileObj)
                configfileObj.flush()
                configfileObj.close()
        endloop1 = 0
        while (endloop1 < 1):
            
            screenshot = pyautogui.screenshot()
            screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)  # Convert PIL Image to OpenCV BGR format
            confidence = 0.8
        
            icon = cv2.imread("resources\\spawn1_gamer.PNG")

        

            screenshot_for_matching = screenshot
            icon_for_matching = icon

            result = cv2.matchTemplate(screenshot_for_matching, icon_for_matching, cv2.TM_CCOEFF_NORMED)

            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            print(max_val)
            if max_val >= confidence:
                top_left = max_loc
                bottom_right = (top_left[0] + icon.shape[1], top_left[1] + icon.shape[0])
                center_x = (top_left[0] + bottom_right[0]) // 2
                center_y = (top_left[1] + bottom_right[1]) // 2
                endloop1 = 1
            else:
                robloxbotlib.reset_player()
        
        fumocamlib.nav_to_main()
        time.sleep(3)
        fumocamlib.sit()
        time.sleep(2)
        fumocamlib.resume_server_time()
        time.sleep(2)
        pydirectinput.press('tab')
        time.sleep(3)
        robloxbotlib.move_mouse_center()
        endloop2 = 0

        while (endloop2 < 1):
            time.sleep(30)
            if robloxbotlib.check_game_state('Disconnected') == True:
                import pathlib
                file_extension = pathlib.Path(__file__).suffix
                if file_extension == ".py":
                    os.system(f"start cmd.exe /c python {__file__}")
                    exit()
                else:
                    import sys
                    basefile = sys.executable
                    os.system(f"start cmd.exe /c {basefile}")
                    exit()
            pydirectinput.press('tab')
            time.sleep(5)
            pydirectinput.press('tab')




