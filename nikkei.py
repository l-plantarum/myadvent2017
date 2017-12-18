# coding=utf-8

import time
import urllib.parse
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = Options()

# ヘッドレスモードを有効にする

# options.add_argument('--headless')
options.add_argument('--unsafely-treat-insecure-origin-as-secure="http://itpro.nikkeibp.co.jp"' )

# ChromeのWebDriverオブジェクトを作成する。
driver = webdriver.Chrome(chrome_options=options)

# 検索クエリを発行
url = 'http://itpro.nikkeibp.co.jp/search/?'

driver.get(url + urllib.parse.urlencode({'q': sys.argv[1], 'rt': 'nocnt'}))

wait = WebDriverWait(driver, 30)

f = open(sys.argv[1], 'w')

for page in range(2,12):
	results = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.list_search")))
	print(results)
	# 検索結果を表示する。
	for h3 in results.find_elements_by_tag_name('h3'):
		a = h3.find_element_by_tag_name('a')
		currentUrl = a.get_attribute('href')
		print(currentUrl)
		f.write(currentUrl + '\n')
	
	# 11ページはない
	for div in driver.find_elements_by_css_selector('li.next'):
	    div.click()


f.close()
driver.quit()



