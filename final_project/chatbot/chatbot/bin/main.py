import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from search_engine.tf_idf_searcher import SearchEngine

from eval.eval import get_test_ids, get_seach_engine_ids, evaluate




if __name__ == '__main__':
    query = 'how to use canvas?'
    searcher = SearchEngine()


    print(searcher.search(query))

    # evaluate search engine on test data
    test_ids = get_test_ids()
    search_engine_ids = get_seach_engine_ids() 

    prec, recall, f1, MAP = evaluate(test_ids, search_engine_ids) 
    print(f'\nEvaluation metrics:')
    print(f'Precision: {prec}')
    print(f'Recall: {recall}')
    print(f'F-1 score: {f1}')
    print(f'Mean Average Precision (MAP) score: {MAP}\n')

    print(f'True document ids for test queries: {test_ids}')
    print(f'Search engine predictions for doc_ids of test queries: {search_engine_ids}\n')
