import unittest
from unittest.mock import patch
import textrecognizer

class TestTextRecognizer(unittest.TestCase):
    def test_image1(self):
        with patch('builtins.print') as mocked_print:
            textrecognizer.recognize_text_from_file('./testpic.jpg')
            mocked_print.assert_called_with('SALON SEUDUN SANOMAT')

    def test_image2(self):
        with patch('builtins.print') as mocked_print:
            textrecognizer.recognize_text_from_file('./testpic2.jpg')
            mocked_print.assert_called_with('helo')

    def test_image3(self):
        with patch('builtins.print') as mocked_print:
            textrecognizer.recognize_text_from_file('./testpic3.jpg')
            mocked_print.assert_called_with('Surgery For My Legs Cause I Cant Stand You Hoes')

    def test_image4(self):
        with patch('builtins.print') as mocked_print:
            textrecognizer.recognize_text_from_file('./testpic4.jpg')
            mocked_print.assert_called_with('Waterbaby lookin ass.')

    def test_video1(self):
        with patch('builtins.print') as mocked_print:
            textrecognizer.recognize_text_from_file('./testvid.mp4')
            mocked_print.assert_called_with('Kulmia Groupin 15v juhlat')

    def test_video2(self):
        with patch('builtins.print') as mocked_print:
            textrecognizer.recognize_text_from_file('./testvid2.mp4')
            mocked_print.assert_called_with('GRIME DAILY')

    def test_video3(self):
        with patch('builtins.print') as mocked_print:
            textrecognizer.recognize_text_from_file('./testvid3.mp4')
            mocked_print.assert_called_with('Kohta mennään!')

if __name__ == '__main__':
    unittest.main()