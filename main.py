import os
import time
from tqdm import tqdm
from configparser import ConfigParser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# driver = webdriver.Chrome(options=options)
# service = Service('/usr/local/bin/msedgedriver')
service = Service('chromedriver.exe')
service.start()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
dr = webdriver.Remote(service.service_url, options=options)
dr.implicitly_wait(10) # seconds


def rua_once(conf):
    dr.get(conf['url'])
    dr.refresh()
    time.sleep(0.5)
    js = "document.getElementsByClassName('rt-button--large')[0].style.display=\'block\';"
    dr.execute_script(js)

    idx = 0
    finished = False
    while not finished:
        # 选择选项
        if not conf['useans']:
            dr.find_element(By.CLASS_NAME, "rt-checkbox").click()
        else:
            options = dr.find_elements(By.CLASS_NAME, "rt-checkbox")
            for ans in conf['answer'][idx]:
                ans = min(int(ans), len(options))
                options[ans - 1].click()

        finished = dr.find_element(By.CLASS_NAME, "rt-button--bottom__text").text == "提交"
        if finished:
            time.sleep(0.5)
        dr.find_element("xpath", "//button").click()
        idx += 1
        idx = min(idx, len(conf['answer']) - 1)


def read_config():
    conn = ConfigParser()
    file_path = os.path.join(os.path.abspath('.'),'config.ini')
    if not os.path.exists(file_path):
        raise FileNotFoundError("File 'config.ini' does not exist")
    conn.read(file_path)
    _answer = conn.get('yzj', 'answer').split(',')
    _answer = [_a.replace(' ', '') for _a in _answer]
    print(_answer)
    return {
        'url': conn.get('yzj','url'),
        'repeat': int(conn.get('yzj', 'repeat')),
        'useans': int(conn.get('yzj', 'useans')) == 1,
        'answer': _answer,
    }


if __name__ == '__main__':
    conf = read_config()
    for _ in tqdm(range(conf['repeat']), desc="Survey: "):
        rua_once(conf)
    dr.quit()
