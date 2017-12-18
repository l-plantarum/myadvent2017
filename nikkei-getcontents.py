import sys
import ssl
import os
import codecs
import urllib.request
import time
from bs4 import BeautifulSoup

# 第一引数がファイル名
urlfile = sys.argv[1]

seq = 1

with open(urlfile, 'r') as infile:

	# 結果を格納するディレクトリ
	os.mkdir("results")
	
	for it in infile:
		# 改行コードを削除
		url = it.replace('\n', '').replace('\r','')

		print(url)
	
		# URLの中身をディレクトリの下の連番のファイルに吐く
		f = codecs.open('results/' + str(seq), 'w', 'utf_8', 'ignore')
		page = 1
		print("page")
		print(page)
		resp = urllib.request.urlopen(url)
		src = resp.read()
		soup = BeautifulSoup(src, 'lxml')
		while True:
			# 有料記事
			article = soup.find("div", id="articleBody")
			# 日経ニューメディア
			if article == None:
				break
			induction = article.find("div", class_="induction")
			# 有料記事
			if induction != None:
				print("要有料登録")
				break
			paragraphs = article.find_all("p")
			for p in paragraphs:
				f.write(p.text)
			next = soup.find("li", class_="next")
			if (next == None):
				print("not found next")
				break;
			else:
				print("found next page")
			page += 1
			print("page")
			print(page)
			resp = urllib.request.urlopen(url + '?P='+str(page))
			src = resp.read()
			soup = BeautifulSoup(src, 'lxml')
		f.close()
		seq += 1
		print("***seq****, and sleep 5 second")
		print(seq)
		time.sleep(5)
		if (seq % 100) == 0:
			print("sleep 60 seconds.")
			time.sleep(60)
	infile.close()

