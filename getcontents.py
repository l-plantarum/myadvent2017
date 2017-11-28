# coding=utf-8

import sys
import ssl
import os
import urllib.request
from bs4 import BeautifulSoup

# 第一引数がファイル名
keyword = sys.argv[1]

seq = 1

with open(keyword, 'r') as f:

	# 第一引数に.dirを付加した名前のディレクトリを掘る
	os.mkdir(keyword + '.dir')
	
	for it in f:
		# 改行コードを削除
		url = it.replace('\n', '').replace('\r','')
		
		# ここのドメインは外のサイトに飛ばされるのでカット
		if (url.find('https://ad.impress.co.jp/special/') == 0):
			continue
			
		print(seq)
		print(url)
			
		# URLの中身をディレクトリの下の連番のファイルに吐く
		f = open(keyword + '.dir/' + str(seq), 'w')
		resp = urllib.request.urlopen(url)
		src = resp.read()
		soup = BeautifulSoup(src, 'lxml')
		article =  soup.article
		if article == None:
			article = soup.find_all("div", id="article")
		else:
			contents = article.find_all('p')
		for c in contents:
			f.write(c.text)
		f.close()
		seq += 1
