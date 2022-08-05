import os
from tqdm import tqdm
from configparser import ConfigParser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


service = Service('/usr/local/bin/msedgedriver')
service.start()
dr = webdriver.Remote(service.service_url)
dr.implicitly_wait(10) # seconds


def rua_once(url):
    dr.get(url)
    for _ in range(10):
        dr.find_element(By.CLASS_NAME, "rt-checkbox").click()
        dr.find_element("xpath", "//button").click()


def read_config():
    conn = ConfigParser()
    file_path = os.path.join(os.path.abspath('.'),'config.ini')
    if not os.path.exists(file_path):
        raise FileNotFoundError("File 'config.ini' does not exist")
    conn.read(file_path)
    _url = conn.get('yzj','url')
    return {
        'url': _url,
        'repeat': int(conn.get('yzj', 'repeat')),
    }


if __name__ == '__main__':
    conf = read_config()
    for _ in tqdm(range(conf['repeat']), desc="Survey: "):
        rua_once(conf['url'])
    dr.quit()
