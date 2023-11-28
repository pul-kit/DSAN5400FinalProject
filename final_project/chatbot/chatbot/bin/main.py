
from chatbot.search_engine.tf_idf_searcher import SearchEngine




if __name__ == '__main__':
    query = 'how to use canvas?'
    searcher = SearchEngine()


    print(searcher.search(query))
