import mss
import mss.tools
from PIL import Image
import pytesseract


def capture_screen():
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Capture the primary monitor
        sct_img = sct.grab(monitor)
        file_path = "screenshot.png"
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=file_path)
        return file_path


def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text


def screen_to_text():
    image_path = capture_screen()
    text = extract_text_from_image(image_path)
    return text
