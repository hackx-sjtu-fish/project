import json
import os

def get_data(data_dir):
    file_emoji_keywords_id = file(os.path.join(data_dir,"emoji_keywords_id.json"),"rb")
    file_emoji_unicode = file(os.path.join(data_dir,"emoji_unicode.json"),"rb")
    file_keywords = file(os.path.join(data_dir,"keywords.json"),"rb")
    emoji_keywords_id = json.loads(file_emoji_keywords_id.read())
    emoji_unicode = json.loads(file_emoji_unicode.read())
    keywords = json.loads(file_keywords.read())
    return keywords, emoji_unicode, emoji_keywords_id

