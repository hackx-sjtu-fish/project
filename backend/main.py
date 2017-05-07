import sys, getopt,threading

from similarity import get_most_similar_keywords
from watson import get_class_words
from data_helper import get_data
from cognitive import get_face_keywords

def main():
	opts, args = getopt.getopt(sys.argv[1:], "", ['url=','data_dir='])
	url = "http://sjtudiudiu.org/media/lost/thumbnail_1bb7c09e-075f-4681-9eb9-5634e684edbd.png"
	data_dir = "data"
	for op, value in opts:
		if op == "--url":  
			url = value
		elif op == "--data_dir":
			data_dir = value

	# prepare data
	keywords, emoji_unicode, emoji_keywords_id = get_data(data_dir)
	# start parallel threads
	threading.Thread(target = get_watson, args = (url,keywords, emoji_unicode, emoji_keywords_id), name = 'Watson').start()
	threading.Thread(target = get_face, args = (url,keywords, emoji_unicode, emoji_keywords_id), name = 'Face').start()

def get_watson(url,keywords, emoji_unicode, emoji_keywords_id):
	# get labels with Watson
	class_words = get_class_words(url)
	# calculate most similar keywords among all keywords of emoji
	most_similar_keywords_id = get_most_similar_keywords(class_words, keywords)
	most_similar_keywords = {'adj':[],'noun':[]}
	for key,value in most_similar_keywords_id.items():
		most_similar_keywords[key].append([keywords[i] for i in value])
	print class_words
	print most_similar_keywords
	# different weights for noun and adj
	noun_weight = 1
	adj_weight = 0.2
	# calculate the score of every emoji
	best_mark = -1
	#emoji_keyords_scores = [ sum([1 if keyword_id in words_id else 0 for keyword_id in most_similar_keywords_id]) for words_id in emoji_keywords_id]
	emoji_keyords_scores = []
	for words_id in emoji_keywords_id:
		score = sum([noun_weight if keyword_id in words_id else 0 for keyword_id in most_similar_keywords_id['noun']]) + sum([adj_weight if keyword_id in words_id else 0 for keyword_id in most_similar_keywords_id['adj']])
		emoji_keyords_scores.append(score)

	for i in xrange(len(emoji_keyords_scores)):
	#	if emoji_keyords_scores[i] >= 1:
	#		print emoji_unicode[i],emoji_keyords_scores[i]
		if emoji_keyords_scores[i] > best_mark:
			best_mark = emoji_keyords_scores[i]
			best_index = i
	if best_mark > 1:
		print emoji_unicode[best_index]

def get_face(url,keywords, emoji_unicode, emoji_keywords_id):
	# get face info with Microsoft Cognitive Service
	face_words = get_face_keywords(url)
	#print face_words
	# calculate the score of every emoji
	for face_keywords in face_words:
		emoji_keyords_scores = [ sum([1 if keywords.index(face_keyword) in words_id else 0 for face_keyword in face_keywords]) for words_id in emoji_keywords_id]
		best_mark = -1
		for i in xrange(len(emoji_keyords_scores)):
			if emoji_keyords_scores[i] > best_mark:
				best_mark = emoji_keyords_scores[i]
				best_index = i
		print emoji_unicode[best_index]
if __name__ == "__main__":
	main()
