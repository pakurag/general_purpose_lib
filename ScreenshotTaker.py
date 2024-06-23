import tkinter as tk
import pyautogui
import os
from datetime import datetime

class ScreenshotTaker:
    def __init__(self, root):
        self.root = root
        self.running = False
        
        self.create_widgets()
        
    def create_widgets(self):
        # Create a label for the directory path
        self.directory_label = tk.Label(root, text="Save Directory:")
        self.directory_label.pack(pady=5)

        # Create a text entry for the directory path
        self.directory_entry = tk.Entry(root, width=50)
        self.directory_entry.pack(pady=5)
        self.directory_entry.insert(0, "h:\\screenshot")  # Default directory

        # Create a label for the interval
        self.interval_label = tk.Label(root, text="Interval (seconds):")
        self.interval_label.pack(pady=5)

        # Create a text entry for the interval
        self.interval_entry = tk.Entry(root, width=10)
        self.interval_entry.pack(pady=5)
        self.interval_entry.insert(0, "3")  # Default interval

        # Create a button to take a screenshot
        self.screenshot_button = tk.Button(root, text="Take Screenshot", command=self.take_screenshot)
        self.screenshot_button.pack(pady=5)

        # Create a button to start taking screenshots every interval seconds
        self.start_button = tk.Button(root, text="Start", command=self.start_taking_screenshots)
        self.start_button.pack(pady=5)

        # Create a button to stop taking screenshots
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_taking_screenshots)
        self.stop_button.pack(pady=5)
        
    def take_screenshot(self):
        # Get the directory path from the text field
        directory = self.directory_entry.get()
        
        # Take a screenshot
        screenshot = pyautogui.screenshot()
        
        # Create the directory if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        # Generate filename with current date and time
        filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"
        filepath = os.path.join(directory, filename)
        
        # Save the screenshot
        screenshot.save(filepath)
        
    def start_taking_screenshots(self):
        try:
            self.screenshot_interval = int(self.interval_entry.get()) * 1000  # Convert seconds to milliseconds
        except ValueError:
            self.screenshot_interval = 3000  # Default to 3 seconds if invalid input
        self.running = True
        self.schedule_screenshot()
        
    def stop_taking_screenshots(self):
        self.running = False
        
    def schedule_screenshot(self):
        if self.running:
            self.take_screenshot()
            self.root.after(self.screenshot_interval, self.schedule_screenshot)

# Create the main window
root = tk.Tk()
root.title("Screenshot Taker")

# Create an instance of the ScreenshotTaker class
app = ScreenshotTaker(root)

# Run the application
root.mainloop()
