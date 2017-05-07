import numpy as np
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic

brown_ic = wordnet_ic.ic('ic-brown.dat')
semcor_ic = wordnet_ic.ic('ic-semcor.dat')


def get_similarities(word_a, word_b_set, sim_algorithm):
    similarities = []
    word_a = wn.synsets(word_a)[0]
    for word_b in word_b_set:
        try:
            if sim_algorithm == "path":
                similarity = word_a.path_similarity(wn.synsets(word_b)[0])
            elif sim_algorithm == "lch":
                similarity = word_a.lch_similarity(wn.synsets(word_b)[0])
            elif sim_algorithm == "wup":
                similarity == word_a.wup_similarity(wn.synsets(word_b)[0])
            elif sim_algorithm == "res":
                similarity = word_a.res_similarity(wn.synsets(word_b)[0], brown_ic)
            elif sim_algorithm == "jcn":
                similarity = word_a.jcn_similarity(wn.synsets(word_b)[0], brown_ic)
        except:
            similarity = 0
        similarities.append(similarity)
    return similarities


def get_most_similar_keywords(word_a, word_b_set, sim_algorithm):
    similarities = get_similarities(word_a, word_b_set, sim_algorithm)
    keyword_id = np.argmax(similarities)
    return keyword_id