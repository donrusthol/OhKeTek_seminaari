from PIL import Image
import unittest
import numpy as np # pip install numpy
import textrecognizer

class TestTextRecognizer(unittest.TestCase):
    def test_recognize_text_from_image(self):
        # Create a simple white image with PIL
        img = Image.new('RGB', (60, 30), color = (73, 109, 137))

        # Write some text on the image
        d = ImageDraw.Draw(img)
        d.text((10,10), "Hello", fill=(255, 255, 255))

        # Convert the PIL image to a numpy array
        img_array = np.array(img)

        # Call the function with the numpy array
        result = textrecognizer.recognize_text_from_image(img_array)

        # Check that the result is the expected text
        self.assertEqual(result, "Hello")

    def test_recognize_text_from_image_empty(self):
        # Create an empty white image with PIL
        img = Image.new('RGB', (60, 30), color = (73, 109, 137))

        # Convert the PIL image to a numpy array
        img_array = np.array(img)

        # Call the function with the numpy array
        result = textrecognizer.recognize_text_from_image(img_array)

        # Check that the result is an empty string
        self.assertEqual(result, "")

if __name__ == '__main__':
    unittest.main()