import os
from PIL import Image # pip install pillow
import cv2 # pip install opencv-python
import pytesseract # pip install pytesseract

def preprocess_image(image):
    '''Preprocess an image before text recognition'''
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use Gaussian blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5,5), 0)

    # Otsu's thresholding automatically calculates the best threshold value to separate the foreground (text) from the background
    _, binary = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return binary

def recognize_text_from_image(image):
    '''Recognize text from an image using Tesseract OCR'''
    
    # Convert OpenCV image (numpy array) to PIL image
    image = Image.fromarray(image)

    # Set Tesseract settings
    # Here we use OCR Engine Mode 3 (default setting) and Page Segmentation Mode 6 (assume a single block of text)
    config = '--oem 3 --psm 6'
    
    text = pytesseract.image_to_string(image)
    return text

def recognize_text_from_file(file_path, skip_frames=1):
    '''Recognize text from an image or video file'''
    
    # Check if the file exists
    _, ext = os.path.splitext(file_path)
    
    if ext.lower() in ['.jpg', '.png', '.jpeg', '.bmp']:
        
        # It's an image file
        image = cv2.imread(file_path)
        
        if image is None:
            print(f"Error opening image file: {file_path}")
            return
        image = preprocess_image(image)
        text = recognize_text_from_image(image)
        print(text)
        
    elif ext.lower() in ['.mp4', '.avi', '.mov', '.mkv']:
        
        # It's a video file
        vidcap = cv2.VideoCapture(file_path)
        
        if not vidcap.isOpened():
            print(f"Error opening video file: {file_path}")
            return
        
        frame_count = 0
        
        while True:
            success, image = vidcap.read()
            
            if not success:
                break
            
            if frame_count % skip_frames == 0:
                image = preprocess_image(image)
                text = recognize_text_from_image(image)
                print(text)
                
            frame_count += 1
            
        vidcap.release()
        
    else:
        print(f"Unsupported file format: {ext}")

if __name__ == "__main__":
    '''Main function to test the text recognition code'''
    # NOTE: For video, the program outputs the recognized text to the console for all frames!
    
    # There are photos and videos in the repository you can use for testing
    # ./testpic.jpg
    # ./testvid.mp4
    
    # To use your own test photo or video, replace the file path with the path to your image or video file with the slashes as forward slashes ("/") or double backslashes ("\\")
    
    file_path = "./testvid2.mp4"  
    recognize_text_from_file(file_path)