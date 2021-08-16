import unittest
from scrappy.scrapper import youtube_video_data_scrapper


class TestScrapper(unittest.TestCase):
    def test_scrap(self):
        url = 'https://www.youtube.com/watch?v=TFMnICdHiyM'
        driver = r"C:\Users\ME\projects\for_github\chromedriver_win32\chromedriver.exe"
        self.assertAlmostEqual(
            youtube_video_data_scrapper(url=url, driver=driver)['title'], "Xiaomi Mi 11 Lite vs Samsung A52: SIMILAR BUT ONLY ONE WINNER! Let's Find Out!")


if __name__ == '__main__':
    unittest.main()
