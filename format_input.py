import nltk
import nlp_model
import numpy as np


def bag_of_words(s, inp_sentence):
    inp_bag = [0 for _ in range(len(inp_sentence))]
    inp_words = nltk.word_tokenize(s)
    inp_words = [nlp_model.stemmer.stem(word.lower()) for word in inp_words]

    for inp_word in inp_words:
        for i, w in enumerate(nlp_model.words):
            if w == inp_word:
                inp_bag[i] = 1
    return np.array(inp_bag)
