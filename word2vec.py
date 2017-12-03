# -*- coding: utf-8 -*-

from gensim.models import word2vec
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences = word2vec.PathLineSentences("mecab")
model = word2vec.Word2Vec(sentences,
                          sg=1,
                          size=100,
                          min_count=1,
                          window=10,
                          hs=1,
                          negative=0)
model.save("model")
