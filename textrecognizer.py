from PIL import Image # pip install pillow
import cv2 # pip install opencv-python
import pytesseract # pip install pytesseract

def preprocess_image(image):
    # Muunna kuva harmaasävyiseksi
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Melun vähentämiseksi käytetään Gaussin sumennusta
    blur = cv2.GaussianBlur(gray, (5,5), 0)

    # Otsun kynnysarvo laskee automaattisesti parhaan kynnysarvon, joka erottaa etualan (tekstin) taustasta
    _, binary = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return binary

def recognize_text_from_image(image):
    # Muunna OpenCV-kuva (numpy-taulukko) PIL-kuvaan
    image = Image.fromarray(image)

    # Määritä Tesseractin asetukset
    # Tässä käytämme OCR Engine Mode 3 (oletusasetus) ja Page Segmentation Mode 6 (oletetaan yhtenäinen tekstilohko)
    config = '--oem 3 --psm 6'
    
    text = pytesseract.image_to_string(image)
    return text

def recognize_text_from_video(video_path, skip_frames=1):
    # Avaa video
    vidcap = cv2.VideoCapture(video_path)

    if not vidcap.isOpened():
        # Videon avaaminen epäonnistui
        print(f"Error opening video file: {video_path}")
        return

    frame_count = 0

    # Lue video ruutu kerrallaan
    while True:
        # Lue seuraava ruutu
        success, image = vidcap.read()
        if not success:
            break

        # Jos skip_frames on 1, käsitellään jokaista ruutua
        if frame_count % skip_frames == 0:
            image = preprocess_image(image)
            text = recognize_text_from_image(image)
            print(text)

        frame_count += 1

    # Sulje video
    vidcap.release()