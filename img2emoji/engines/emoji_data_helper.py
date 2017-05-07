#! /usr/env python2


import os
import json


def get_emoji_data(emoji_data_dir):
    file_emoji_keywords_id = open(os.path.join(emoji_data_dir, 'emoji_keywords_id.json'), 'r')
    file_emoji_unicode = open(os.path.join(emoji_data_dir, 'emoji_unicode.json'), 'r')
    file_keywords = open(os.path.join(emoji_data_dir, 'keywords.json'), 'r')
    emoji_keywords_id = json.load(file_emoji_keywords_id)
    emoji_unicode = json.load(file_emoji_unicode)
    keywords = json.load(file_keywords)
    return keywords, emoji_unicode, emoji_keywords_id
