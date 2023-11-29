import openai

# template = """Between >>> and <<< are the raw search result text from the website.
# Extract the answer to the question '{query}' or say "not found" if the information is not contained.
# Use the format
# Extracted:<answer or "not found">
# >>> {requests_result} <<<
# Extracted:"""
# template = """Between >>> and <<< are the raw search result text from the website.
# >>> {requests_result} <<<
# Extract the answer to the question '{query}' """

# PROMPT = PromptTemplate(
#     input_variables=["query", "requests_result"],
#     template=template,
# )


# chain = LLMRequestsChain(llm_chain=LLMChain(llm=OpenAI(temperature=0), prompt=PROMPT))
# question = "What is Zoom and what can it do?"
# inputs = {
#     "query": question,
#     "url": "https://uis.georgetown.edu/zoom/faq/#general",
# }
# response = chain(inputs)
# print(response['query'])
# print(response['output'])

def openai_chat(api_key, messages):
    openai.api_key = api_key

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can specify the model you want to use
            messages=messages
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"An error occurred: {e}"

# Usage example

def generate(query, context):
    api_key = "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"  
    messages = [
        {"role": "system", "content": "You are a helpful chatbot."},
        {"role": "user", "content": f"Please answer the question {query} base on this context: {context}. Please only use the knowledge from the context."}
    ]

    response = openai_chat('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', messages)
    print(response)
