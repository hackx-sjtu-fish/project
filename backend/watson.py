import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

# Provide your key here
visual_recognition = VisualRecognitionV3('2016-05-20', api_key='')

def get_classes(url):
    dump = json.dumps(visual_recognition.classify(images_url=url))
    dump = dump.replace("\n","")
    #print dump
    classes = json.loads(dump)['images'][0]['classifiers'][0]['classes']
    return classes

def get_class_words(url):
    classes = get_classes(url)
    words = {'adj':[],'noun':[]}
    for class_and_confidence in classes:
        split_words = class_and_confidence['class'].split()
        if len(split_words) == 2:
            words['adj'].append(split_words[0])
            words['noun'].append(split_words[1])
        elif len(split_words) == 1:
            words['noun'].append(split_words[0])
    #print words
    for key in words:
        words[key] = list(set(words[key]))
    return words
