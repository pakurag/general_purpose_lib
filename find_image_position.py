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

def click_image_position(template_path):
    # Take a screenshot
    screenshot = take_screenshot()
    
    # Find the position of the template image in the screenshot
    top_left, bottom_right = find_image_position(template_path, screenshot)
    
    # Calculate the center of the found image
    center_x = (top_left[0] + bottom_right[0]) // 2
    center_y = (top_left[1] + bottom_right[1]) // 2
    
    # Move the mouse to the center of the found image and click
    pyautogui.moveTo(center_x, center_y)
    pyautogui.click()
    
    print(f"Clicked on position: ({center_x}, {center_y})")

def main():
    template_path = input("Enter the path of the template image: ")
    
    # Click on the position of the image
    click_image_position(template_path)

if __name__ == "__main__":
    main()
    
