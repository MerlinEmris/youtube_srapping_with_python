import scrapper

if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=rMO7APyBiMI'
    driver = r"C:\Users\ME\projects\for_github\chromedriver_win32\chromedriver.exe"
    print(youtube_video_data_scrapper(url, driver))
