import os
import nltk
import pickle
import tflearn
import numpy as np
import tensorflow as tf
from nltk.stem.lancaster import LancasterStemmer
from pymongo import MongoClient

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

stemmer = LancasterStemmer()

# Connect to MongoDB
client = MongoClient()
db = client['groot']
collection = db['groot_intents']

# Retrieve data from MongoDB
document = collection.find({})

try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for doc in document:
        if doc["intent"] not in labels:
            labels.append(doc["intent"])

        for text in doc['text']:
            sep_words = nltk.word_tokenize(text)
            words.extend(sep_words)
            docs_x.append(sep_words)
            docs_y.append(doc["intent"])

    words = sorted(set([stemmer.stem(w.lower()) for w in words if w != "?"]))

    out_empty = [0 for _ in range(len(labels))]
    training = []
    output = []

    for x, doc in enumerate(docs_x):
        bag = []
        doc_words = [stemmer.stem(w.lower()) for w in doc]
        for word in words:
            if word in doc_words:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = np.array(training)
    output = np.array(output)

with open("data.pickle", "wb") as f:
    pickle.dump((words, labels, training, output), f)

tf.compat.v1.reset_default_graph()
net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 64)
net = tflearn.fully_connected(net, 64)
net = tflearn.fully_connected(net, len(output[0]), activation='softmax')
net = tflearn.regression(net)

model = tflearn.DNN(net)

try:
    model.load("model.tflearn")
except:
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save('model.tflearn')
