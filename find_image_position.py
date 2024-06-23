import cv2
import numpy as np
import pyautogui
from PIL import Image

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    return screenshot

def find_image_position(template_path, screenshot):
    # Read the template image
    template = cv2.imread(template_path, cv2.IMREAD_COLOR)
    
    # Perform template matching
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    
    # Get the best match position
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    # Get the size of the template
    h, w = template.shape[:2]
    
    # Define the bounding box
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    
    return top_left, bottom_right

def main():
    template_path = input("Enter the path of the template image: ")
    
    # Take a screenshot
    screenshot = take_screenshot()
    
    # Find the position of the template image in the screenshot
    top_left, bottom_right = find_image_position(template_path, screenshot)
    
    print(f"Top-left corner: {top_left}")
    print(f"Bottom-right corner: {bottom_right}")
    
    # Optionally, display the result
    cv2.rectangle(screenshot, top_left, bottom_right, (0, 255, 0), 2)
    cv2.imshow('Result', screenshot)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
