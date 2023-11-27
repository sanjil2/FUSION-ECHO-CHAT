from googlesearch import search


def search_google(user_input):
    search_results = []
    query = user_input
    for j in search(query, tld="co.in", num=5, stop=5, pause=2):
        search_results.append(j)

    return search_results
