# Requirement
    python-2.7
    nltk
    nltk.wordnet
    nltk.wordnet_ic
    watson_developer_cloud
    cognitive_face

# Installation
    pip install nltk
    nltk.download("wordnet")    -- run in python
    nltk.download("wordnet_ic")    -- run in python
    pip install --upgrade watson-developer-cloud
    pip install cognitive_face

# Data
    keywords.json           --学弟爬的emoji的所有keywords, 转成Json，keywords的数组下标即id
    emoji_keywords_id.json  --每个emoji的所有keywords对应的id
    emoji_unicode.json      --每个emoji对应的unicode
    
# Quick Start
    chmod +x get_models.sh
    ./get_models.sh
    run main.py --url={url of the image}
    output is (should be) unicodes of the most similar emojies.
    Search emojies with unicodes here: http://www.unicode.org/emoji/charts/full-emoji-list.html

