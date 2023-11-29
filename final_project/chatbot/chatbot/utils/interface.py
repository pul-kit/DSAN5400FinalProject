import csv

def welcome_message():
    print("Hello! Welcome to an AI assistant designed for Canvas, Turnitin and Zoom!")
    print("Directly type your question and I will do my best to answer!")
    print("Type 'help' to learn more about me.")

def get_user_input():
    return input("You: ")

def display_bot_response(response):
    print("AI:", response)

def ask_for_rating():
    rating = input("Was I helpful? Let me know how I can be improved.")
    #TODO Replace File path with actual path
    with open("../rating.csv", 'a', newline='') as csv:
        csv.write(rating)
    print(f'Data appended to CSV file successfully.')    
