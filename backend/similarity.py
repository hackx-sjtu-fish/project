import numpy as np
from gensim.models import word2vec

model = word2vec.Word2Vec.load("data/text.model")

def get_similarities(word_a_set, word_b_set):
    words_similarities = {'adj':[],'noun':[]}
    stop_words = ['color']
    for key,value in word_a_set.items():
        for word_a in value:
            similarities = []
            if word_a not in stop_words:
                for word_b in word_b_set:
                    try:
                        similarity = model.similarity(word_a,word_b)
                    except:
                        similarity = 0
                    similarities.append(similarity)
                words_similarities[key].append(similarities)
    #print words_similarities
    return words_similarities

def get_most_similar_keywords(word_a_set, word_b_set):
    keyword_id = {'adj':[],'noun':[]}
    words_similarities = get_similarities(word_a_set, word_b_set)
    for key,value in words_similarities.items():
        for similarities in value:
            try:
                keyword_id[key].append(np.argmax(similarities))
            except:
                print 'No keywords!'
    return keyword_id

# def most_path_similar_words(word_a, word_b_set):
#     word_a = wn.synsets(word_a)[0]
#     similarities = [ word_a.path_similarity(wn.synsets(word_b)[0]) if len(wn.synsets(word_b))>0 else 0 for word_b in word_b_set ]
#     return similarities
    
# def most_lch_similar_words(word_a, word_b_set):
#     similarities = []
#     word_a = wn.synsets(word_a)[0]
#     for word_b in word_b_set:
#         try:
#             similarity = word_a.lch_similarity(wn.synsets(word_b)[0])
#         except:
#             similarity = 0
#         similarities.append(similarity)
#     return similarities

# def most_wup_similar_words(word_a, word_b_set):
#     similarities = []
#     word_a = wn.synsets(word_a)[0]
#     for word_b in word_b_set:
#         try:
#             similarity = word_a.wup_similarity(wn.synsets(word_b)[0])
#         except:
#             similarity = 0
#         similarities.append(similarity)
#     return similarities



# # from nltk.corpus import genesis
# # genesis_ic = wn.ic(genesis, False, 0.0)

# def most_res_similar_words(word_a, word_b_set):
#     similarities = []
#     word_a = wn.synsets(word_a)[0]
#     for word_b in word_b_set:
#         try:
#             similarity = word_a.res_similarity(wn.synsets(word_b)[0], brown_ic)
#         except:
#             similarity = 0
#         similarities.append(similarity)
#     return similarities

# def most_jcn_similar_words(word_a, word_b_set):
#     similarities = []
#     word_a = wn.synsets(word_a)[0]
#     for word_b in word_b_set:
#         try:
#             similarity = word_a.jcn_similarity(wn.synsets(word_b)[0], brown_ic)
#         except:
#             similarity = 0
#         similarities.append(similarity)
#     return similarities