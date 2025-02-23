def set_to_day():
    import cv2
    import pydirectinput
    import pyautogui
    import numpy as np
    import time
    import os
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)  # Convert PIL Image to OpenCV BGR format
    confidence = 0.3
        
    icon = cv2.imread("resources\\settingsicon.PNG")

        

    screenshot_for_matching = screenshot
    icon_for_matching = icon

    result = cv2.matchTemplate(screenshot_for_matching, icon_for_matching, cv2.TM_CCOEFF_NORMED)
    #print(max_val)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(max_val)
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
    time.sleep(3)
    # Look Day / Night Settings
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)  # Convert PIL Image to OpenCV BGR format
    confidence = 0.2
        
    icon = cv2.imread("resources\\daynightsettings.PNG")

        

    screenshot_for_matching = screenshot
    icon_for_matching = icon

    result = cv2.matchTemplate(screenshot_for_matching, icon_for_matching, cv2.TM_CCOEFF_NORMED)
    #print(max_val)
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
    time.sleep(3)
    # Click Day
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)  # Convert PIL Image to OpenCV BGR format
    confidence = 0.2
        
    icon = cv2.imread("resources\\day.PNG")

        

    screenshot_for_matching = screenshot
    icon_for_matching = icon

    result = cv2.matchTemplate(screenshot_for_matching, icon_for_matching, cv2.TM_CCOEFF_NORMED)
    #print(max_val)
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
    time.sleep(3)

def resume_server_time():
    import cv2
    import pydirectinput
    import pyautogui
    import numpy as np
    import time
    import os
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)  # Convert PIL Image to OpenCV BGR format
    confidence = 0.2
        
    icon = cv2.imread("resources\\settingsicon.PNG")

        

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
    time.sleep(3)
    # Look Day / Night Settings
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)  # Convert PIL Image to OpenCV BGR format
    confidence = 0.2
        
    icon = cv2.imread("resources\\daynightSettings.PNG")

        

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
    time.sleep(3)
    # Click Day / Night
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)  # Convert PIL Image to OpenCV BGR format
    confidence = 0.3
        
    icon = cv2.imread("resources\\daynight.PNG")

        

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
    time.sleep(3)

def set_fumo(fumo):
    import cv2
    import pydirectinput
    import pyautogui
    import numpy as np
    import time
    import os
    pydirectinput.press('tab')
    setfumoloop = 0
    while(setfumoloop < 1):
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)  # Convert PIL Image to OpenCV BGR format
        confidence = 0.5
        
        icon = cv2.imread("resources\\fumoicon.PNG")

        

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
            setfumoloop = 1
            fumo_button_x = center_x
            fumo_button_y = center_y
    
    pydirectinput.moveTo(center_x,center_y,duration=1.00)
    xedit = center_x - 1
    yedit = center_y - 1
    pydirectinput.moveTo(xedit,yedit)
    pydirectinput.click()
    time.sleep(3)
    
    # Get screen dimensions
    screen_width, screen_height = pyautogui.size()

    # Calculate center coordinates
    center_x = screen_width // 2
    center_y = screen_height // 2

    # Move the mouse to the center
    pyautogui.moveTo(center_x, center_y, duration=1.00)  # Optional duration for smooth movement
    pydirectinput.moveTo(center_x,center_y,duration=1.00)
    xedit = center_x - 1
    yedit = center_y - 1
    pydirectinput.moveTo(xedit,yedit)
    #pydirectinput.click()
    #pydirectinput.click()
    print(f"Mouse moved to the center: ({center_x}, {center_y})")
    print("OK")
    time.sleep(3)
    # look
    import pytesseract
    from pytesseract import Output
    import time
    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    screenshot_file = "screenshot.png"
    text_to_find = fumo

    found = False
    max_scrolls = 33  # Adjust as needed
    time.sleep(5)
    pyautogui.screenshot(screenshot_file)
    #for _ in range(max_scrolls):
        #pyautogui.scroll(200)
    endloop12 = 0
    times = 0
    while(endloop12 < 1):
        for _ in range(max_scrolls):
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
                    pydirectinput.moveTo(center_x,center_y,duration=1.00)
                    time.sleep(3)
                    found = True
                    break
            if found:
                pydirectinput.click()
                endloop12 = 1
                xedit = fumo_button_x - 1
                yedit = fumo_button_y - 1
                pydirectinput.moveTo(xedit,yedit)
                time.sleep(3)
                pydirectinput.click()
                pydirectinput.press('tab')
                break

            if not found:
                pyautogui.scroll(-200)  # Scroll down (negative value) Adjust 200 as needed
                time.sleep(1) # Small delay after scroll
                pyautogui.screenshot(screenshot_file) # Take new screenshot
                times = times + 1
                print(times)

        if not found:
            times = 0
            print(f"Text '{text_to_find}' not found after {max_scrolls} scrolls.")
            print("Will Try Again")
            for _ in range(max_scrolls):
                pyautogui.scroll(200)

def fumo_button():
    import cv2
    import pydirectinput
    import pyautogui
    import numpy as np
    import time
    import os
    setfumoloop = 0
    while(setfumoloop < 1):
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)  # Convert PIL Image to OpenCV BGR format
        confidence = 0.4
        
        icon = cv2.imread("resources\\fumoicon.PNG")

        

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
            setfumoloop = 1
    
    pydirectinput.moveTo(center_x,center_y,duration=1.00)
    xedit = center_x - 1
    yedit = center_y - 1
    pydirectinput.moveTo(xedit,yedit)
    pydirectinput.click()
    time.sleep(3)
    
    # Get screen dimensions
    screen_width, screen_height = pyautogui.size()

    # Calculate center coordinates
    center_x = screen_width // 2
    center_y = screen_height // 2

    # Move the mouse to the center
    pyautogui.moveTo(center_x, center_y, duration=1.00)  # Optional duration for smooth movement
    pydirectinput.moveTo(center_x,center_y,duration=1.00)
    xedit = center_x - 1
    yedit = center_y - 1
    pydirectinput.moveTo(xedit,yedit)
    pydirectinput.click()
    #pydirectinput.click()
    print(f"Mouse moved to the center: ({center_x}, {center_y})")
    print("OK")
    time.sleep(3)

def anti_grief():
    import cv2
    import pydirectinput
    import pyautogui
    import pytesseract
    from pytesseract import Output
    import numpy as np
    import time
    import os
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)  # Convert PIL Image to OpenCV BGR format
    confidence = 0.3
        
    icon = cv2.imread("resources\\settingsicon.PNG")

        

    screenshot_for_matching = screenshot
    icon_for_matching = icon

    result = cv2.matchTemplate(screenshot_for_matching, icon_for_matching, cv2.TM_CCOEFF_NORMED)
    #print(max_val)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(max_val)
    if max_val >= confidence:
        top_left = max_loc
        bottom_right = (top_left[0] + icon.shape[1], top_left[1] + icon.shape[0])
        center_x = (top_left[0] + bottom_right[0]) // 2
        center_y = (top_left[1] + bottom_right[1]) // 2
        settingsicon_x = center_x
        settingsicon_y = center_y
        pydirectinput.moveTo(center_x,center_y,duration=1.00)
        xedit = center_x - 1
        yedit = center_y - 1
        pydirectinput.moveTo(xedit,yedit)
        pydirectinput.click()
        time.sleep(3)
    else:
        return False
    # Toggle Anti-Grief
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)  # Convert PIL Image to OpenCV BGR format
    confidence = 0.3
        
    icon = cv2.imread("resources\\antigriefoff.PNG")

        

    screenshot_for_matching = screenshot
    icon_for_matching = icon

    result = cv2.matchTemplate(screenshot_for_matching, icon_for_matching, cv2.TM_CCOEFF_NORMED)
    #print(max_val)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(max_val)
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
        time.sleep(2)
        pydirectinput.moveTo(settingsicon_x,settingsicon_y,duration=1.00)
        pydirectinput.click()
        time.sleep(3)
        return True
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)  # Convert PIL Image to OpenCV BGR format
    confidence = 0.3
       
    icon = cv2.imread("resources\\antigriefon.PNG")

        

    screenshot_for_matching = screenshot
    icon_for_matching = icon

    result = cv2.matchTemplate(screenshot_for_matching, icon_for_matching, cv2.TM_CCOEFF_NORMED)
    #print(max_val)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(max_val)
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
        time.sleep(2)
        pydirectinput.moveTo(settingsicon_x,settingsicon_y,duration=1.00)
        pydirectinput.click()
        time.sleep(3)
        return True
    else:
        return False
    
def nav_to_main():
    import robloxbotlib
    import time
    import pydirectinput
    time.sleep(5)
    robloxbotlib.move_player('w',3)
    time.sleep(2)
    robloxbotlib.move_player('d',1)
    time.sleep(2)
    robloxbotlib.move_player('w',1)
    time.sleep(2)
    robloxbotlib.move_player('d',2)
    time.sleep(2)
    robloxbotlib.move_player('w',1)
    time.sleep(2)
    robloxbotlib.move_player('d',1)
    time.sleep(2)
    pydirectinput.keyDown('left')
    time.sleep(0.7)
    pydirectinput.keyUp('left')

def sit():
    import cv2
    import pydirectinput
    import pyautogui
    import numpy as np
    import time
    import os
    sitfumoloop = 0
    while(sitfumoloop < 1):
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)  # Convert PIL Image to OpenCV BGR format
        confidence = 0.3
        
        icon = cv2.imread("resources\\fumo_sit.PNG")

        

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
            sitfumoloop = 1
    
    pydirectinput.moveTo(center_x,center_y,duration=1.00)
    xedit = center_x - 1
    yedit = center_y - 1
    pydirectinput.moveTo(xedit,yedit)
    pydirectinput.click()
    time.sleep(3)
