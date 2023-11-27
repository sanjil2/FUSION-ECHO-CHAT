import nlp_model
import numpy as np
import random
import event_handler
import internet_search
from format_input import bag_of_words

document = nlp_model.document
doc = []
 
for item in document:
    doc.append(item)


def chat():
    print("Talk")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break
        result = nlp_model.model.predict([bag_of_words(inp, nlp_model.words)])
        result_index = np.argmax(result)
        tag = nlp_model.labels[result_index]

        responses = []

        for result_intent in doc:
            if result_intent['intent'] == tag:
                responses = result_intent['responses']

        reply = random.choice(responses)
        print(event_handler.event_handling(inp, tag, reply))

        if tag == "GoogleQuery":
            search_results = internet_search.search_google(inp)
            for search_result in search_results:
                print(search_result)

        if tag == "GoodBye" or tag == "CourtesyGoodBye":
            exit()
