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

options.add_argument('--headless')

# ChromeのWebDriverオブジェクトを作成する。
driver = webdriver.Chrome(chrome_options=options)

# 検索クエリを発行
url = 'https://www.watch.impress.co.jp/extra/headline/search/?'

driver.get(url + urllib.parse.urlencode({'q': sys.argv[1]}))

f = open(sys.argv[1], 'w')

for page in range(2,12):
	time.sleep(5)
	wait = WebDriverWait(driver, 10)
	results = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.gsc-resultsbox-visible")))

	# 検索結果を表示する。
	lastUrl = ""
	for a in driver.find_elements_by_css_selector('a.gs-title'):
		currentUrl = a.get_attribute('href')
		if lastUrl != currentUrl and currentUrl != None:
			f.write(currentUrl + '\n')
		lastUrl = currentUrl
		# URLが二回出る→同じ内容が二回出ているから
	
	# 11ページはない
	if page == 11:
		break;
	for div in driver.find_elements_by_css_selector('div.gsc-cursor-page'):
		if int(div.text) == page:
			div.click()
			break

f.close()
driver.quit()  # ブラウザを終了する。
