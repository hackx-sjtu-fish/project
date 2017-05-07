#! /usr/env python2


from base_engine import BaseEngine
from emoji_data_helper import get_emoji_data
from watson import get_class_words
from similarity import get_most_similar_keywords


class SimpleEngine(BaseEngine):
    def __init__(self, emoji_data_dir, img_host, img_port):
        self.img_host = img_host
        self.img_port = img_port

        self.similarity_algorithm = 'path'
        self.mode = 'things'
        self.keywords, self.emoji_unicode, self.emoji_keywords_id = get_emoji_data(emoji_data_dir)

    def __call__(self, img_uuid, suffix, url=None):
        if url is None:
            url = 'http://{host}:{port}/getImg?img_uuid={img_uuid}&suffix={suffix}'\
                .format(host=self.img_host, port=self.img_port, img_uuid=img_uuid, suffix=suffix)

        class_words = get_class_words(url)

        most_similar_keywords_id = [get_most_similar_keywords(word, self.keywords, self.similarity_algorithm)
                                    for word in class_words]
        most_similar_keywords = [self.keywords[i] for i in most_similar_keywords_id]

        emoji_keyords_scores = [sum([1 if keyword_id in words_id else 0 for keyword_id in most_similar_keywords_id])
                                for words_id in self.emoji_keywords_id]

        max_score_index = 0
        for i in xrange(len(emoji_keyords_scores)):
            if emoji_keyords_scores[i] > emoji_keyords_scores[max_score_index]:
                max_score_index = i
        result = unichr(int(self.emoji_unicode[i].split(' ')[0][2:], 16))

        return result
#        for i in xrange(len(emoji_keyords_scores)):
#            if emoji_keyords_scores[i] >= 1:
#                print self.emoji_unicode[i], emoji_keyords_scores[i], '\n'

    def __del__(self):
        pass
