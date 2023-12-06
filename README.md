# DSAN5400FinalProject

This program is intended to serve as a retrieval based chatbot that answers a users question about Canvas, Zoom or Turnitin usage. The answers have been scraped from online FAQs from the following websites - 
Zoom: https://uis.georgetown.edu/zoom/faq/
Canvas: https://community.canvaslms.com/t5/Instructor-Guide/tkb-p/Instructor
Turnitin: https://www.turnitin.com/help_pages/instructor_faq.asp?

### This project can by run through the following steps:
1. Navigate to the bin of this project on your terminal.
2. Type:

        python main.py -q <query> -e <eval>

4. Query is the user question.
5. Eval is to print the test performance of the search engine.

### Chatbot design: 
1. Data is scraped from FAQ pages
to gain query/document pairs for questions about Canvas, Turnitin, and Zoom.
2. Search engine processes a user query, searches for relevant documents over a collection of documents using an inverted index, ranks relevant documents for relevance using TF-IDF scores, and returns the text of the most relevant document. 
3. Search engine output is passed into GPT-3.5's Chat Completions API, to summarize the content. 
4. Summarized content is output to the user. 

### Chatbot Architecture: 
![Architecture of the ChatBot](https://i.imgur.com/V30q1Ql.png)

### Evaluation of search engine performance: 
For a text dataset comprised of 20 queries, the search engine output is evaluated against the true document ID associated with each test query, using precision, recall, f-1, and MAP score metrics. Users can view these metrics using the evaluation argument tag -e.


