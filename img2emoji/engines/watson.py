#! /usr/env python2


import json

from watson_developer_cloud import VisualRecognitionV3


visual_recognition = VisualRecognitionV3('2016-05-20', api_key='b285038228bac310f5b055e873e56dcb0c83d313')


def get_classes(url):
    dump = json.dumps(visual_recognition.classify(images_url=url))
    dump = dump.replace('\n', '')
    classes = json.loads(dump)['images'][0]['classifiers'][0]['classes']
    return classes


def get_class_words(url):
    classes = get_classes(url)
    words = []
    for class_and_confidence in classes:
        for word in class_and_confidence['class'].split():
            words.append(word)
    words = list(set(words))
    return words
