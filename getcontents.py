# coding=utf-8

import sys
import ssl
import os
import urllib.request
from bs4 import BeautifulSoup

# ���������t�@�C����
keyword = sys.argv[1]

seq = 1

with open(keyword, 'r') as f:

	# ��������.dir��t���������O�̃f�B���N�g�����@��
	os.mkdir(keyword + '.dir')
	
	for it in f:
		# ���s�R�[�h���폜
		url = it.replace('\n', '').replace('\r','')
		
		# �����̃h���C���͊O�̃T�C�g�ɔ�΂����̂ŃJ�b�g
		if (url.find('https://ad.impress.co.jp/special/') == 0):
			continue
			
		print(seq)
		print(url)
			
		# URL�̒��g���f�B���N�g���̉��̘A�Ԃ̃t�@�C���ɓf��
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
