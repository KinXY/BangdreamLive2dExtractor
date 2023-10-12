from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_motion_list(chara_id):
    html_source = f"https://bestdori.com/tool/explorer/asset/en/live2d/chara/{chara_id:03}_general"
    # get the html file of the url
    driver = webdriver.Chrome()
    driver.get(html_source)

    button = driver.find_element(By.CLASS_NAME, "delete")
    button.click()

    sleep(5)
    html = driver.page_source

    driver.stop_client()
    driver.quit()

    # Create a BeautifulSoup object
    soup = BeautifulSoup(html, "html.parser")

    # Find all <a> tags with href attribute
    links = soup.find_all("a", href=True)

    # Iterate through the links and extract the .mtn file names
    mtn_files = [link["href"] for link in links if link["href"].endswith(".mtn")]

    # turn the mtn_files into a list of strings
    mtn_files = ["https://bestdori.com/tool/explorer" + str(file) for file in mtn_files]

    return mtn_files
