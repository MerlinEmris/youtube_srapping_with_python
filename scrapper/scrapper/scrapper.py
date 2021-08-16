from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def youtube_video_data_scrapper(url: str, driver: str) -> dict:
    f"""
    youtube video data scrapper
    :param url: video url starting with https://
    :param driver:path to browser driver for selenium 
    :return: dict[str: str]
    """
    chrome_path = driver
    driver = webdriver.Chrome(chrome_path)
    driver.get(url)

    title = driver.find_element_by_xpath(
        '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/h1/yt-formatted-string').text
    description = driver.find_element_by_xpath(
        '//*[@id="description"]/yt-formatted-string').text
    owner = driver.find_element_by_xpath(
        '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[7]/div[2]/ytd-video-secondary-info-renderer/div/div/ytd-video-owner-renderer/div[1]/ytd-channel-name/div/div/yt-formatted-string/a').text
    views = driver.find_element_by_xpath(
        '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[1]/div[1]/ytd-video-view-count-renderer/span[1]').text.split('views')[0].strip().strip(',')
    date = driver.find_element_by_xpath(
        '//*[@id="info-strings"]/yt-formatted-string').text
    like = driver.find_element_by_xpath(
        '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/yt-formatted-string').text
    dislike = driver.find_element_by_xpath(
        '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[2]/a/yt-formatted-string').text

    data = {
        'title': title,
        "description": description,
        'owner': owner,
        'date': date,
        "views": views,
        'like': like,
        'dislike': dislike
    }
    print(data)
    driver.close()
    return data


