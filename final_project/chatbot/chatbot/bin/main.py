import sys
import os
import argparse

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from search_engine.tf_idf_searcher import SearchEngine
from utils.interface import display_bot_response, ask_for_rating
from eval.eval import get_test_ids, get_seach_engine_ids, evaluate
from utils.openai_API import generate



if __name__ == '__main__':
    """
    argparse to get user query and whether to evaluate
    """
    parser = argparse.ArgumentParser(
        description="Get user query and whether to evaluate or not."
    )
    parser.add_argument("-q", "--query", required=True, help="Enter your query. Type 'help' for instructions, 'data' for data sources, 'exit' to exit")
    parser.add_argument("-e", "--eval", help="Prints performance metrics of the search engine. Enter true or false.")
    args = parser.parse_args()
    
    user_input = args.query

    # Help user if input is help
    if user_input.lower() == 'help':
        display_bot_response("I am a bot that has been trained on FAQs about Canvas, Turnitin and Zoom. I don't have the capabliity to remember previous inputs.")
        
            
    # Exit if input is exit 
    elif user_input.lower() == 'exit':
        display_bot_response("Goodbye!")
        
        
    # Tell user data used if input is data
    elif user_input.lower() == 'data':
        display_bot_response("Here is a link to the data I have been trained on.")
        display_bot_response("Zoom: https://uis.georgetown.edu/zoom/faq/")
        display_bot_response("Canvas: https://community.canvaslms.com/t5/Instructor-Guide/tkb-p/Instructor")
        display_bot_response("Turnitin: https://www.turnitin.com/help_pages/instructor_faq.asp?")
        

    # Answer user's question
    else:
        searcher = SearchEngine()
        context = ','.join(searcher.search(user_input))
        context = context[0:4000]
        answer = generate(user_input, context)
        print(answer)
        ask_for_rating()
        
    
    
    #prints eval if user prompts    
    if args.eval.lower() == "true":
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
