import unittest
from .scrapper import youtube_video_data_scrapper
from mescrap.scrappy import scrapper


scrapper.youtube_video_data_scrapper


class TestScrapper(unittest.TestCase):
    def test_scrap(self):
        url = 'https://www.youtube.com/watch?v=rMO7APyBiMI'
        driver = r"C:\Users\ME\projects\for_github\chromedriver_win32\chromedriver.exe"
        self.assertAlmostEqual(
            youtube_video_data_scrapper(url=url, driver=driver), {})
