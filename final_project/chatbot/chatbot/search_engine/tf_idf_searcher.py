from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import os
import pickle
import json
from collections import defaultdict
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')


class SearchEngine:

    def __init__(self):
        pass


    def search(self, query):
        """ 
        Searches for relevant documents based on the input query using a TF-IDF-based search engine.
        :param query : (str) The input query for document search.
        :result : (str) The top ranked document(s) based on the TF-IDF scores.
        """
        with open('../vectorizer/tfidf_vectorizer.pkl', 'rb') as f:
            vectorizer = pickle.load(f)
        
        with open('../indexes/index.json', 'r') as f:
            index = json.load(f)
        
        with open('../indexes/inverted_index.json', 'r') as f:
            inverted_index = json.load(f)
        
        # Search the query using inverted index
        tokens = self.text_preprocessing(query)
        docs = []
        for token in tokens:
            docs.append(inverted_index[token])
        docs = set.intersection(*map(set, docs))

        # Rank the documents using TF-IDF
        if len(docs) == 0:
            return 'Sorry, I cannot find the answer to your question. Please try another question.'
        elif len(docs) == 1:
            return index[str(list(docs)[0])]
        else:
            query_vec = vectorizer.transform([query])
            scores = []
            for doc_id in docs:
                doc_vec = vectorizer.transform([index[str(doc_id)]])
                score = cosine_similarity(query_vec, doc_vec)
                scores.append((doc_id, score))
            scores = sorted(scores, key=lambda x: x[1], reverse=True)
            return index[str(scores[0][0])], index[str(scores[1][0])]

    
    def get_top_docid(self, query):
        """ 
        Retrieves the top-ranked document ID for a given query using a TF-IDF-based search engine.
        :param query : (str) The input query for document search.
        :return : (str) The document ID with the highest TF-IDF score.
        """
        with open('../vectorizer/tfidf_vectorizer.pkl', 'rb') as f:
            vectorizer = pickle.load(f)
        
        with open('../indexes/index.json', 'r') as f:
            index = json.load(f)
        
        with open('../indexes/inverted_index.json', 'r') as f:
            inverted_index = json.load(f)
        
        # Search the query using inverted index
        tokens = self.text_preprocessing(query)
        docs = []
        for token in tokens:
            docs.append(inverted_index[token])
        docs = set.intersection(*map(set, docs))

        # Rank the documents using TF-IDF
        if len(docs) == 0:
            return 'Sorry, I cannot find the answer to your question. Please try another question.'
        elif len(docs) == 1:  
            return list(docs)[0]
        else:
            query_vec = vectorizer.transform([query])
            scores = []
            for doc_id in docs:
                doc_vec = vectorizer.transform([index[str(doc_id)]])
                score = cosine_similarity(query_vec, doc_vec)
                scores.append((doc_id, score))
            scores = sorted(scores, key=lambda x: x[1], reverse=True)
       
            top_docid = scores[0][0]
            return top_docid


    def update(self):
        """ 
        Updates the search engine by adding new documents from CSV files in the specified data path.
        """
        data_path = '../data'
        documents = []
        id = 0
        index = {}
        for filename in os.listdir(data_path):
            if filename.endswith('.csv'):
                file_path = os.path.join(data_path, filename)
                df = pd.read_csv(file_path)
                # assuming the text is in a column named 'text'
                text = df['Question'] + ' ' + df['Answer']
                for t in text:
                    documents.append(t)
                    index[id] = t
                    id += 1
        
        
        vectorizer = TfidfVectorizer(stop_words='english')
        # fit and transform the corpus
        tfidf_matrix = vectorizer.fit_transform(documents)
        print(tfidf_matrix.toarray())
        with open('tfidf_vectorizer.pkl', 'wb') as f:
            pickle.dump(vectorizer, f)
        
        with open('../indexes/index.json', 'w') as f:
            json.dump(index, f)
        

        # Build an inverted index
        inverted_index = defaultdict(list)

        for doc_id, doc in index.items():
            tokens = self.text_preprocessing(doc)
            for token in tokens:
                inverted_index[token].append(doc_id)
        
        with open('../indexes/inverted_index.json', 'w') as f:
            json.dump(inverted_index, f)



    def text_preprocessing(self, text):
        """ 
        Performs text preprocessing on the input text, including tokenization, lowercase conversion, 
        removal of non-alphabetic tokens, and stemming.
        :param text : (str) The input text to be preprocessed.
        :return : (set) A set of processed tokens after text preprocessing.
        """
        stop_words = set(stopwords.words('english'))
        stemmer = PorterStemmer()
        tokens = word_tokenize(text)
        tokens = [token.lower() for token in tokens if token.isalpha()]
        tokens = [stemmer.stem(token) for token in tokens if token not in stop_words]
        return set(tokens)

