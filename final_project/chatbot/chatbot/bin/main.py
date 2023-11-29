import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from search_engine.tf_idf_searcher import SearchEngine


if __name__ == '__main__':
    query = 'how to use canvas?'
    searcher = SearchEngine()


    print(searcher.search(query))
