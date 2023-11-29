from langchain.chains import LLMChain, LLMRequestsChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# template = """Between >>> and <<< are the raw search result text from the website.
# Extract the answer to the question '{query}' or say "not found" if the information is not contained.
# Use the format
# Extracted:<answer or "not found">
# >>> {requests_result} <<<
# Extracted:"""
template = """Between >>> and <<< are the raw search result text from the website.
>>> {requests_result} <<<
Extract the answer to the question '{query}' """

PROMPT = PromptTemplate(
    input_variables=["query", "requests_result"],
    template=template,
)


chain = LLMRequestsChain(llm_chain=LLMChain(llm=OpenAI(temperature=0), prompt=PROMPT))
question = "What is Zoom and what can it do?"
inputs = {
    "query": question,
    "url": "https://uis.georgetown.edu/zoom/faq/#general",
}
response = chain(inputs)
print(response['query'])
print(response['output'])

