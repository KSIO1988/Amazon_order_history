import configparser
import json
import os

from selenium import webdriver

conf = configparser.ConfigParser()
path = os.path.join(os.path.dirname(__file__), 'settings.ini')
conf.read(path, 'UTF-8')

# プロファイルパス
PROFILE_PATH = conf['driver']['PROFILE_PATH']
options = webdriver.chrome.options.Options()
options.add_argument('--user-data-dir=' + PROFILE_PATH)

# アマゾン
LogIn_ID = conf['Amazon']['LogIn_ID']
LogIn_PASS = conf['Amazon']['LogIn_PASS']
Amazon_ADDRESS = conf['Amazon']['Amazon_ADDRESS']

# デフォルトのダウンロード先
Default_PATH = conf['Download']['Default_PATH']

# pdf化のための初期設定
chrome_options = webdriver.ChromeOptions()
settings = {"recentDestinations": [{"id": "Save as PDF",
                                    "origin": "local",
                                    "account": ""}],
            "selectedDestinationId": "Save as PDF", 
            "version": 2}
prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings)}
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('--kiosk-printing')


