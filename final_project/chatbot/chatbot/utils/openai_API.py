import openai

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


def generate(query, context):
    api_key = "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"  
    messages = [
        {"role": "system", "content": "You are a helpful chatbot."},
        {"role": "user", "content": f"Please answer the question {query} base on this context: {context}. Please only use the knowledge from the context."}
    ]

    response = openai_chat('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', messages)
    print(response)
