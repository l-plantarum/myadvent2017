# -*- coding: utf-8 -*-

from gensim.models import word2vec
import sys

model = word2vec.Word2Vec.load("model")

print("strength")

strength = model.wv.most_similar(positive=[sys.argv[1]], negative=[sys.argv[2]])

print(strength)


print("weak")
weak = model.wv.most_similar(positive=[sys.argv[2]], negative=[sys.argv[1]])

print(weak)
