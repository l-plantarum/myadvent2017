# coding=utf-8

import MeCab
import sys

#tagger = MeCab.Tagger('-F\s%f[6] -U\s%m -E\\n')
tagger = MeCab.Tagger('-F\s%f[6] -U\s%m -E\\n')
dir = sys.argv[1] + ".dir/"
out = sys.argv[1] + ".mecab"

fo = open(out, 'w')

for i in range(1, 100):
	fi = open(dir + str(i), 'r')
	line = fi.readline()
	while line:
		result = tagger.parse(line)
		fo.write(result[1:])
		line = fi.readline()
		
	fi.close();

fo.close()



