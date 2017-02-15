# -*- coding: utf-8 -*-

def get_question(question):

	import pickle
	with open("clf","rb") as f1, open("tv","rb") as f2:
		clf = pickle.load(f1)
		tv = pickle.load(f2)	
	import jieba
	test = ' '.join(jieba.cut(question))
	tv_test = tv.transform([test])
	return clf.predict(tv_test)
