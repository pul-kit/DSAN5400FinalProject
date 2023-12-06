import os
import sys
import csv

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir) 

from eval import create_test_dataset

def store_data_in_csv(): 
    """ 
    Stores test data in a CSV file with columns for document ID and document content.
    """
    test, _ = create_test_dataset()

    csv_file_path = 'test_data.csv'

    headers = ['doc_id', 'doc']


    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=headers)
        csv_writer.writeheader()

        for key, value in test.items(): 
            row_data = {
                'doc_id': key,
                'doc': value,
            }
            csv_writer.writerow(row_data)

    print(f'Test data saved to {csv_file_path}')


def store_queries_in_txt(): 
    """ 
    Stores test queries in a text file.
    """
    txt_file_path = 'test_queries.txt'

    _, queries = create_test_dataset()
    with open(txt_file_path, 'w') as txt_file:
        for item in queries:
            txt_file.write(str(item) + '\n')

    print(f'Test queries saved to {txt_file_path}')


store_data_in_csv()
store_queries_in_txt()






