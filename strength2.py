#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gensim.models import word2vec
import sys
import codecs

model = word2vec.Word2Vec.load("model")

print("strength")

strength = model.wv.most_similar_cosmul(positive=[sys.argv[1], sys.argv[2]], negative=[sys.argv[3], sys.argv[4]])

print(strength)


print("weak")
weak = model.wv.most_similar_cosmul(positive=[sys.argv[3], sys.argv[4]], negative=[sys.argv[1], sys.argv[2]])

print(weak)
