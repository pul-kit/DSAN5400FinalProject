import openai

def openai_chat(api_key, messages):
    """ 
    Initiates a chat conversation using the OpenAI GPT-3.5 Turbo model.
    :param api_key: (str) Your OpenAI API key for authentication.
    :param messages : (list) A list of message objects representing the conversation.
    :return : (str) OpenAI model's generated repsonse. 
    """
    openai.api_key = api_key

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can specify the model you want to use
            messages=messages
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"An error occurred: {e}"


def generate(query, context):
    """ 
    Generates a response to a user query based on a given context using the OpenAI GPT-3.5 Turbo model.
    :param query : (str) The user's question or query.
    :param context : (str) Context to base the response on.
    """
    api_key = "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"  
    messages = [
        {"role": "system", "content": "You are a helpful chatbot."},
        {"role": "user", "content": f"Please answer the question {query} base on this context: {context}. Please only use the knowledge from the context."}
    ]

    response = openai_chat('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', messages)
    print(response)
