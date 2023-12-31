import os
import sys
import json 
import re
from sklearn import metrics

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir) 

from search_engine.tf_idf_searcher import SearchEngine
search_engine = SearchEngine()


def create_test_dataset(): 
    """
    Generates a test dataset from a JSON file containing query and document data.
    :return : A dictionary containing a subset of the original dataset, with only the first 20 entries.
    :return : A list of tuples, each containing a document ID and its corresponding query extracted from the dataset.
    """
    json_file_path = '../indexes/index.json'

    if os.path.exists(json_file_path):
        # Open the JSON file containing query and document data 
        with open(json_file_path, 'r') as file:
            # Load the JSON data
            long_dataset = json.load(file)

        # create a test dataset, containing only the first 30 querys/documents 
        dataset_items = list(long_dataset.items())
        test_dataset = dict(dataset_items[:20])

        # list of the 20 test queries, from the test dataset
        queries = []
        docid_list = list(test_dataset.keys())
        # iterate through each value in the dictionary
        for value in test_dataset.values():
            # split the text into sentences
            sentences = re.split(r'[.!?]', value)
            # isolate the first sentence (because the queries are in the first line of each value in the dataset)
            first_sentence = sentences[0].strip()
            queries.append(first_sentence)

        assert len(docid_list) == len(queries), 'Query list and doc_id list are not the same length'
        test_queries = list(zip(docid_list, queries))

        return(test_dataset, test_queries)
    
    else: 
        print(f"The file at {json_file_path} does not exist.")



def get_test_queries(): 
    """
    Retrieves a list of test queries generated from a test dataset.
    :return : A list of test queries.
    """
    _ , query_list = create_test_dataset() 
    querys = []

    for query in query_list: 
        querys.append(query[1])

    return querys


def get_test_ids(): 
    """ 
    Retrieves a list of test document IDs from the test dataset.
    :return : A list of document IDs.
    """
    test_dataset, _ = create_test_dataset()
    keys = list(test_dataset.keys())
    test_ids = [int(num) for num in keys]

    return test_ids


def get_seach_engine_ids(): 
    """ 
    Ouputs a list of predicted document IDs, by inputing the test queries into SearchEngine object.
    : return : A list of document IDs.
    """
    query_list = get_test_queries()

    doc_ids = []
    for query in query_list: 
        doc_id = search_engine.get_top_docid(query)
        doc_ids.append(doc_id)

    return doc_ids



def evaluate(true_ids, search_engine_ids): 
    """
    Takes gold label results and predicted search engine results to compute performance metrics. 
    :param true_ids: list of true doc_ids for query list 
    :param search_engine_ids: list of search engine generated doc_ids for query list 
    :return: precision, recall, f-1score, MAP score 
    """

    assert len(true_ids) == len(search_engine_ids), 'The lists of doc ids are not of equal length. Cannot compare.'

    true = set(true_ids)
    predicted = set(search_engine_ids)

    # calculate True Positives, False Positives, and False Negatives
    true_positives = len(true.intersection(predicted))
    false_positives = len(predicted - true)
    false_negatives = len(true - predicted)

    # calculate Precision, Recall, and F-1 Score
    precision = true_positives / (true_positives + false_positives)
    recall = true_positives / (true_positives + false_negatives)
    f1_score = 2 * (precision * recall) / (precision + recall)

    # calculate MAP score (Mean Average Precision: avg of the prec values obtained at different recall levels) 
    predictions = [] 
    for i in range(len(true_ids)):
        if true_ids[i] == search_engine_ids[i]:
            # output 1 when search engine matches true values at index i
            predictions.append(1)
        else: 
            # output 0 when search engine does not match true values at index i
            predictions.append(0)

    # list of binary true values 
    true_values = [1] * len(predictions)

    num_relevant_docs = sum(true_values)
    MAP = 0.0
    num_correct_predictions = 0

    for i, pred in enumerate(predictions):
        if pred == 1:
            num_correct_predictions += 1
            precision_at_k = num_correct_predictions / (i + 1)
            MAP += precision_at_k

    if num_relevant_docs > 0:
        MAP /= num_relevant_docs

    return precision, recall, round(f1_score, 2), round(MAP, 2) 



        









